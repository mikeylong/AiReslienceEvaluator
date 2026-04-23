#!/usr/bin/env python3
"""Validate an AI resilience report set.

Usage:
  python3 scripts/validate_ai_resilience_report.py reports/example-report
  python3 scripts/validate_ai_resilience_report.py reports/example-report --forbid Term
  python3 scripts/validate_ai_resilience_report.py reports/example-report --require-youtube-transcripts
  python3 scripts/validate_ai_resilience_report.py reports/example-report --require-sources-by-function

The positional path can be a basename without extension or any one of the
`.md`, `.json`, or `.svg` files in the set.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL_KEYS = {
    "target_name",
    "summary",
    "quadrant",
    "scores",
    "top_strengths",
    "main_vulnerabilities",
    "strategic_read",
    "final_verdict",
    "confidence",
    "evidence_notes",
}

REQUIRED_MARKDOWN_SECTIONS = [
    "Executive Summary",
    "2x2 Placement",
    "Full Score Table",
    "Top Strengths",
    "Main Vulnerabilities",
    "Strategic Read",
    "Final Verdict",
    "Confidence Level",
    "Evidence Notes",
]

CATEGORIES = {
    "proprietary_advantage": [
        "context",
        "trust",
        "distribution",
        "judgment",
        "liability_governance",
    ],
    "workflow_criticality": [
        "frequency",
        "operational_dependence",
        "system_position",
        "switching_cost",
        "budget_durability",
    ],
    "ai_resilience_tests": [
        "model_improvement_test",
        "wrapper_risk_test",
        "agent_readiness_test",
        "accountability_test",
        "outcome_depth_test",
    ],
}

ALLOWED_EVIDENCE_LABELS = {
    "Direct evidence",
    "Credible third-party evidence",
    "Inference",
}

YOUTUBE_URL_RE = re.compile(
    r"^https://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[A-Za-z0-9_-]{6,}"
)

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def normalize_report_base(path: Path) -> Path:
    if path.suffix in {".md", ".json", ".svg"}:
        return path.with_suffix("")
    return path


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError:
        fail(f"Missing JSON file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path}: {exc}")
    if not isinstance(value, dict):
        fail(f"JSON root must be an object: {path}")
    return value


def text_at(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"Missing {label}: {path}")


def require_keys(obj: dict[str, Any], keys: set[str], path: str) -> None:
    missing = sorted(keys - set(obj))
    if missing:
        fail(f"{path} missing required keys: {', '.join(missing)}")


def is_score_block(value: Any) -> bool:
    return isinstance(value, dict) and set(CATEGORIES).issubset(value.keys()) and "total" in value


def target_score_blocks(obj: dict[str, Any]) -> dict[str, dict[str, Any]]:
    scores = obj.get("scores")
    if not isinstance(scores, dict):
        fail("scores must be an object")
    if is_score_block(scores):
        return {str(obj.get("target_name", "target")): scores}
    blocks: dict[str, dict[str, Any]] = {}
    for name, block in scores.items():
        if not is_score_block(block):
            fail(f"scores.{name} must contain the three score categories and total")
        blocks[str(name)] = block
    if not blocks:
        fail("scores must contain at least one target")
    return blocks


def score_value(value: Any, path: str) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        fail(f"{path}.score must be an integer 1-5 or null")
    if value < 1 or value > 5:
        fail(f"{path}.score must be between 1 and 5")
    return value


def evidence_label(value: Any, path: str) -> None:
    if not isinstance(value, str):
        fail(f"{path}.evidence_label must be a string")
    if value not in ALLOWED_EVIDENCE_LABELS:
        fail(
            f"{path}.evidence_label must be one of "
            f"{', '.join(sorted(ALLOWED_EVIDENCE_LABELS))}; got {value!r}"
        )


def validate_scores(obj: dict[str, Any]) -> dict[str, int | None]:
    totals: dict[str, int | None] = {}
    blocks = target_score_blocks(obj)
    for target_name, target_scores in blocks.items():
        numeric_total = 0
        has_null = False
        for category, factors in CATEGORIES.items():
            category_block = target_scores.get(category)
            if not isinstance(category_block, dict):
                fail(f"scores.{target_name}.{category} must be an object")
            numeric_subtotal = 0
            category_has_null = False
            for factor in factors:
                item = category_block.get(factor)
                if not isinstance(item, dict):
                    fail(f"scores.{target_name}.{category}.{factor} must be an object")
                score = score_value(
                    item.get("score"),
                    f"scores.{target_name}.{category}.{factor}",
                )
                evidence_label(
                    item.get("evidence_label"),
                    f"scores.{target_name}.{category}.{factor}",
                )
                rationale = item.get("rationale")
                if not isinstance(rationale, str) or not rationale.strip():
                    fail(f"scores.{target_name}.{category}.{factor}.rationale is required")
                if score is None:
                    has_null = True
                    category_has_null = True
                else:
                    numeric_subtotal += score
            subtotal = category_block.get("subtotal")
            if category_has_null:
                if subtotal not in {None, numeric_subtotal}:
                    fail(
                        f"scores.{target_name}.{category}.subtotal must be null "
                        f"or equal scored-factor sum {numeric_subtotal}"
                    )
            elif subtotal != numeric_subtotal:
                fail(
                    f"scores.{target_name}.{category}.subtotal is {subtotal}, "
                    f"expected {numeric_subtotal}"
                )
            numeric_total += numeric_subtotal
        total = target_scores.get("total")
        if has_null:
            if total not in {None, numeric_total}:
                fail(f"scores.{target_name}.total must be null or equal scored-factor sum {numeric_total}")
            totals[target_name] = total if isinstance(total, int) else None
        else:
            if total != numeric_total:
                fail(f"scores.{target_name}.total is {total}, expected {numeric_total}")
            totals[target_name] = total
    return totals


def validate_comparison(obj: dict[str, Any], totals: dict[str, int | None]) -> None:
    comparison = obj.get("comparison")
    if comparison is None:
        return
    if not isinstance(comparison, dict):
        fail("comparison must be an object")
    for key in ["ranked_targets", "relative_summary", "key_differences"]:
        if key not in comparison:
            fail(f"comparison missing required key: {key}")
    ranked = comparison.get("ranked_targets")
    if not isinstance(ranked, list) or not ranked:
        fail("comparison.ranked_targets must be a non-empty array")
    ranked_totals: list[int] = []
    for index, entry in enumerate(ranked):
        if not isinstance(entry, dict):
            fail(f"comparison.ranked_targets[{index}] must be an object")
        name = entry.get("target_name")
        total = entry.get("total")
        if not isinstance(name, str) or not name:
            fail(f"comparison.ranked_targets[{index}].target_name is required")
        if not isinstance(total, int):
            fail(f"comparison.ranked_targets[{index}].total must be an integer")
        if name in totals and totals[name] is not None and totals[name] != total:
            fail(f"comparison total for {name} is {total}, expected {totals[name]}")
        ranked_totals.append(total)
    if ranked_totals != sorted(ranked_totals, reverse=True):
        fail("comparison.ranked_targets must be sorted by descending total")


def validate_markdown(path: Path, forbid: list[str]) -> str:
    markdown = text_at(path, "markdown report")
    for section in REQUIRED_MARKDOWN_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}\s*$", markdown, re.MULTILINE):
            fail(f"Markdown missing required section: {section}")
    validate_forbidden_terms(markdown, forbid, path)
    return markdown


def require_nonempty_string(obj: dict[str, Any], key: str, path: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(f"{path}.{key} must be a non-empty string")
    return value


def validate_youtube_transcripts(
    obj: dict[str, Any],
    markdown: str,
    require_transcripts: bool,
) -> None:
    evidence_notes = obj.get("evidence_notes")
    if not isinstance(evidence_notes, dict):
        fail("evidence_notes must be an object")

    sources = evidence_notes.get("youtube_transcript_sources")
    if sources is None:
        if require_transcripts:
            fail("evidence_notes.youtube_transcript_sources is required")
        return

    if not isinstance(sources, list) or not sources:
        fail("evidence_notes.youtube_transcript_sources must be a non-empty array")

    urls: list[str] = []
    for index, source in enumerate(sources):
        path = f"evidence_notes.youtube_transcript_sources[{index}]"
        if isinstance(source, str):
            url = source
        elif isinstance(source, dict):
            for key in [
                "target_name",
                "title",
                "publisher",
                "published_date",
                "url",
                "transcript_type",
                "evidence_use",
            ]:
                require_nonempty_string(source, key, path)
            published_date = source["published_date"]
            if not DATE_RE.match(published_date):
                fail(f"{path}.published_date must use YYYY-MM-DD format")
            url = source["url"]
        else:
            fail(f"{path} must be a YouTube URL string or source object")

        if not isinstance(url, str) or not YOUTUBE_URL_RE.match(url):
            fail(f"{path}.url must be a YouTube watch URL")
        urls.append(url)

    require_nonempty_string(evidence_notes, "youtube_transcript_read", "evidence_notes")
    method = evidence_notes.get("youtube_transcript_method")
    if method is not None and (not isinstance(method, str) or not method.strip()):
        fail("evidence_notes.youtube_transcript_method must be a non-empty string")

    if not re.search(r"^##\s+YouTube Review Transcript Evidence\s*$", markdown, re.MULTILINE):
        fail("Markdown missing YouTube Review Transcript Evidence appendix")
    for url in urls:
        if url not in markdown:
            fail(f"Markdown YouTube transcript appendix missing URL: {url}")


def validate_sources_by_function(
    obj: dict[str, Any],
    markdown: str,
    require_sources_by_function: bool,
) -> None:
    evidence_notes = obj.get("evidence_notes")
    if not isinstance(evidence_notes, dict):
        fail("evidence_notes must be an object")

    rows = evidence_notes.get("sources_by_function")
    if rows is None:
        if require_sources_by_function:
            fail("evidence_notes.sources_by_function is required")
        return

    if not isinstance(rows, list) or not rows:
        fail("evidence_notes.sources_by_function must be a non-empty array")
    if not re.search(r"^##\s+Evidence Sources By Function\s*$", markdown, re.MULTILINE):
        fail("Markdown missing Evidence Sources By Function appendix")

    for index, row in enumerate(rows):
        path = f"evidence_notes.sources_by_function[{index}]"
        if not isinstance(row, dict):
            fail(f"{path} must be an object")
        source_function = require_nonempty_string(row, "function", path)
        require_nonempty_string(row, "supports", path)
        require_nonempty_string(row, "evidence_weight", path)
        require_nonempty_string(row, "stale_context_handling", path)
        sources = row.get("sources")
        if not isinstance(sources, list) or not sources:
            fail(f"{path}.sources must be a non-empty array")
        for source_index, source in enumerate(sources):
            if not isinstance(source, str) or not source.strip():
                fail(f"{path}.sources[{source_index}] must be a non-empty string")
        if source_function not in markdown:
            fail(f"Markdown Evidence Sources By Function missing row: {source_function}")


def normalize_for_contains(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().lower()


def axis_terms(axis: Any) -> list[str]:
    if not isinstance(axis, str):
        return []
    return [part.strip() for part in re.split(r"\s*->\s*", axis) if part.strip()]


def validate_svg(path: Path, obj: dict[str, Any], totals: dict[str, int | None], forbid: list[str]) -> None:
    svg = text_at(path, "SVG")
    root = re.search(r"<svg\b([^>]*)>", svg, re.IGNORECASE)
    if not root:
        fail("SVG root element not found")
    root_attrs = root.group(1)
    if "viewBox=" not in root_attrs and "viewbox=" not in root_attrs.lower():
        fail("SVG root must include viewBox")
    if re.search(r"\s(width|height)\s*=", root_attrs, re.IGNORECASE):
        fail("SVG root must not include fixed width or height attributes")
    svg_normalized = normalize_for_contains(re.sub(r"<[^>]+>", " ", svg))
    quadrant = obj.get("quadrant", {})
    for axis in [quadrant.get("x_axis"), quadrant.get("y_axis")]:
        for term in axis_terms(axis):
            if normalize_for_contains(term) not in svg_normalized:
                fail(f"SVG missing axis term from structured object: {term}")
    for target_name, total in totals.items():
        if total is None:
            continue
        label = f"{target_name} ({total}/75)"
        if label not in svg:
            fail(f"SVG missing target label: {label}")
    validate_forbidden_terms(svg, forbid, path)


def validate_forbidden_terms(text: str, forbid: list[str], path: Path) -> None:
    for term in forbid:
        if not term:
            continue
        if re.search(re.escape(term), text, re.IGNORECASE):
            fail(f"Forbidden term {term!r} found in {path}")


def validate(
    base: Path,
    forbid: list[str],
    require_youtube_transcripts: bool = False,
    require_sources_by_function: bool = False,
) -> None:
    json_path = base.with_suffix(".json")
    markdown_path = base.with_suffix(".md")
    svg_path = base.with_suffix(".svg")
    obj = load_json(json_path)
    require_keys(obj, REQUIRED_TOP_LEVEL_KEYS, str(json_path))
    totals = validate_scores(obj)
    validate_comparison(obj, totals)
    markdown = validate_markdown(markdown_path, forbid)
    validate_youtube_transcripts(obj, markdown, require_youtube_transcripts)
    validate_sources_by_function(obj, markdown, require_sources_by_function)
    validate_svg(svg_path, obj, totals, forbid)
    validate_forbidden_terms(json.dumps(obj, ensure_ascii=False), forbid, json_path)
    print(f"ok: {base}")
    print(f"targets: {', '.join(f'{name}={score}/75' for name, score in totals.items())}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report_base", help="Report basename, .md, .json, or .svg path")
    parser.add_argument(
        "--forbid",
        action="append",
        default=[],
        help="Case-insensitive term that must not appear in the report set. May be repeated.",
    )
    parser.add_argument(
        "--require-youtube-transcripts",
        action="store_true",
        help=(
            "Require evidence_notes.youtube_transcript_sources plus a "
            "YouTube Review Transcript Evidence markdown appendix."
        ),
    )
    parser.add_argument(
        "--require-sources-by-function",
        action="store_true",
        help=(
            "Require evidence_notes.sources_by_function plus an Evidence "
            "Sources By Function markdown appendix."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        validate(
            normalize_report_base(Path(args.report_base)),
            args.forbid,
            args.require_youtube_transcripts,
            args.require_sources_by_function,
        )
    except ValidationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
