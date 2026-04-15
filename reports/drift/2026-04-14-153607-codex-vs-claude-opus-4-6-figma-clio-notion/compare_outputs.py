#!/usr/bin/env python3

import json
import math
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


RUN_DIR = Path(__file__).resolve().parent
CONFIG = json.loads((RUN_DIR / "run-config.json").read_text())
SCHEMA = json.loads((RUN_DIR / "response-schema.json").read_text())
COMPANIES = ["Clio", "Figma", "Notion"]
CATEGORIES = [
    "proprietary_advantage",
    "workflow_criticality",
    "ai_resilience_tests",
]
URLISH_RE = re.compile(r"\b((?:https?://)?(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?:/[^\s—–,;)]*)?)")


def read_json(path: Path):
    return json.loads(path.read_text())


def command_output(args):
    return subprocess.check_output(args, text=True).strip()


def extract_ranked_targets(value):
    ranked = []
    for item in value or []:
        if isinstance(item, str):
            text = item
        elif isinstance(item, dict):
            text = item.get("target") or item.get("target_name") or item.get("name") or item.get("company") or json.dumps(item)
        else:
            text = str(item)
        for company in COMPANIES:
            if re.search(rf"\b{re.escape(company)}\b", text):
                if company not in ranked:
                    ranked.append(company)
                break
    return ranked


def extract_urls(value):
    urls = set()

    def canonicalize(url):
        parsed = urlsplit(url)
        host = parsed.netloc.lower()
        if host.startswith("www."):
            host = host[4:]
        path = parsed.path.rstrip("/") or "/"
        return urlunsplit(("https", host, path, "", ""))

    def walk(node):
        if isinstance(node, dict):
            for child in node.values():
                walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)
        elif isinstance(node, str):
            for match in re.findall(r"https?://[^\s\])>\"]+", node):
                urls.add(canonicalize(match.rstrip(".,;")))

    walk(value)
    return sorted(urls)


def quadrant_from_subtotals(x_value, y_value):
    right = x_value >= 13
    top = y_value >= 13
    if right and top:
        return "Resilient"
    if right and not top:
        return "Convenience"
    if not right and top:
        return "Premium Niche"
    return "Fragile"


def extract_theme_strings(items):
    if isinstance(items, list):
        return [str(item).strip() for item in items if str(item).strip()]
    if isinstance(items, str):
        return [items.strip()] if items.strip() else []
    return []


def normalize_urlish_source(item):
    if not isinstance(item, str):
        return item
    match = URLISH_RE.search(item)
    if not match:
        return item.strip()
    url = match.group(1).rstrip(".,;)")
    if not url.startswith("http://") and not url.startswith("https://"):
        url = f"https://{url}"
    return url


def flatten_company_scores(target):
    flattened = {}
    for category in CATEGORIES:
        category_scores = {}
        for factor, payload in (target.get("scores", {}).get(category) or {}).items():
            if factor == "subtotal":
                category_scores[factor] = payload
            elif isinstance(payload, dict) and "score" in payload:
                category_scores[factor] = payload["score"]
            else:
                category_scores[factor] = payload
        flattened[category] = category_scores
    flattened["total"] = target.get("scores", {}).get("total")
    return flattened


def normalize_claude_structured_object(structured_object):
    if "targets" not in structured_object:
        return structured_object

    targets = {
        item["target_name"]: item
        for item in structured_object.get("targets", [])
        if item.get("target_name") in COMPANIES
    }
    comparison = structured_object.get("comparison") or {}

    ranked_targets = []
    for item in comparison.get("ranked_targets", []):
        name = item.get("target") or item.get("target_name") or item.get("name")
        total = item.get("total")
        if name in COMPANIES and isinstance(total, int):
            ranked_targets.append({"target": name, "total": total})
    if not ranked_targets:
        ranked_targets = [
            {"target": company, "total": targets[company]["scores"]["total"]}
            for company in sorted(
                targets,
                key=lambda company: (-targets[company]["scores"]["total"], company),
            )
        ]

    placement_parts = []
    for company in extract_ranked_targets(ranked_targets):
        company_placement = ((targets.get(company) or {}).get("quadrant") or {}).get("placement")
        if company_placement:
            placement_parts.append(f"{company}: {company_placement}")

    confidence_levels = []
    confidence_reasons = []
    for company in COMPANIES:
        payload = (targets.get(company) or {}).get("confidence") or {}
        level = payload.get("level")
        reason = payload.get("reason")
        if level:
            confidence_levels.append(f"{company} {level}")
        if reason:
            confidence_reasons.append(f"{company}: {reason}")

    normalized = {
        "target_name": "Figma vs Clio vs Notion",
        "summary": comparison.get("relative_summary") or structured_object.get("summary") or "",
        "quadrant": {
            "x_axis": "Proprietary Advantage",
            "y_axis": "Workflow Criticality + AI Resilience Under Stronger Models",
            "placement": "; ".join(placement_parts) or "Clio strongest, Figma second, Notion third",
            "rationale": comparison.get("relative_summary") or "",
        },
        "scores": {
            "proprietary_advantage": {
                company: flatten_company_scores(targets[company])["proprietary_advantage"]
                for company in COMPANIES
            },
            "workflow_criticality": {
                company: flatten_company_scores(targets[company])["workflow_criticality"]
                for company in COMPANIES
            },
            "ai_resilience_tests": {
                company: flatten_company_scores(targets[company])["ai_resilience_tests"]
                for company in COMPANIES
            },
            "total": {
                company: flatten_company_scores(targets[company])["total"]
                for company in COMPANIES
            },
        },
        "top_strengths": {
            company: (targets.get(company) or {}).get("top_strengths") or []
            for company in COMPANIES
        },
        "main_vulnerabilities": {
            company: (targets.get(company) or {}).get("main_vulnerabilities") or []
            for company in COMPANIES
        },
        "strategic_read": {
            "durable_layers": {
                company: ((targets.get(company) or {}).get("strategic_read") or {}).get("durable_layers") or []
                for company in COMPANIES
            },
            "commoditizing_layers": {
                company: ((targets.get(company) or {}).get("strategic_read") or {}).get("commoditizing_layers") or []
                for company in COMPANIES
            },
            "next_moves": {
                company: ((targets.get(company) or {}).get("strategic_read") or {}).get("next_moves") or []
                for company in COMPANIES
            },
        },
        "final_verdict": comparison.get("relative_summary") or "",
        "confidence": {
            "level": ", ".join(confidence_levels) or "unspecified",
            "reason": " | ".join(confidence_reasons) or "No confidence rationale supplied.",
        },
        "evidence_notes": [
            {
                "company": company,
                "sources": [
                    normalize_urlish_source(source)
                    for source in ((targets.get(company) or {}).get("evidence_notes") or [])
                ],
            }
            for company in COMPANIES
        ],
        "comparison": {
            "ranked_targets": ranked_targets,
            "relative_summary": comparison.get("relative_summary") or "",
            "key_differences": comparison.get("key_differences") or [],
        },
    }
    return normalized


def normalize_response(kind, requested_model, cli_version, command_template, raw_payload, wrapper=None):
    response = raw_payload
    if kind == "claude" and isinstance(wrapper, dict):
        if "structured_output" in wrapper:
            response = wrapper["structured_output"]
        else:
            result_text = wrapper.get("result") or ""
            json_start = result_text.find("{")
            if json_start >= 0:
                response = json.loads(result_text[json_start:])
        if isinstance(response, dict) and isinstance(response.get("structured_object"), dict):
            response["structured_object"] = normalize_claude_structured_object(response["structured_object"])

    metadata = dict(response.get("run_metadata") or {})
    metadata["timestamp"] = CONFIG["timestamp"]
    metadata["cli"] = kind
    metadata["cli_version"] = cli_version
    metadata["command_template"] = command_template
    metadata["requested_model"] = requested_model
    metadata["cwd"] = CONFIG["cwd"]

    notes = list(metadata.get("notes") or [])
    if kind == "codex":
        metadata.setdefault("resolved_model", requested_model)
        metadata["live_research_enabled"] = "--search" in command_template
    elif kind == "claude":
        model_usage = (wrapper or {}).get("modelUsage") or {}
        metadata["resolved_model"] = requested_model if requested_model in model_usage else next(iter(model_usage), requested_model)
        metadata["live_research_enabled"] = "WebSearch" in command_template
        permission_denials = (wrapper or {}).get("permission_denials") or []
        if permission_denials:
            notes.append(f"Permission denials encountered: {len(permission_denials)}")

    metadata["notes"] = notes
    response["run_metadata"] = metadata
    return response


def json_type_ok(value, schema_type):
    if schema_type == "object":
        return isinstance(value, dict)
    if schema_type == "array":
        return isinstance(value, list)
    if schema_type == "string":
        return isinstance(value, str)
    if schema_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if schema_type == "null":
        return value is None
    if schema_type == "number":
        return (isinstance(value, int) or isinstance(value, float)) and not isinstance(value, bool)
    if schema_type == "boolean":
        return isinstance(value, bool)
    return False


def validate_against_schema(value, schema, path="$"):
    if "anyOf" in schema:
        errors = []
        for option in schema["anyOf"]:
            try:
                validate_against_schema(value, option, path)
                return
            except RuntimeError as exc:
                errors.append(str(exc))
        raise RuntimeError(f"{path}: no anyOf branch matched")

    if "oneOf" in schema:
        matches = 0
        for option in schema["oneOf"]:
            try:
                validate_against_schema(value, option, path)
                matches += 1
            except RuntimeError:
                pass
        if matches != 1:
            raise RuntimeError(f"{path}: expected exactly one oneOf branch to match")
        return

    expected_type = schema.get("type")
    if expected_type is not None:
        allowed = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(json_type_ok(value, item) for item in allowed):
            raise RuntimeError(f"{path}: expected type {allowed}, got {type(value).__name__}")

    if value is None:
        return

    if "enum" in schema and value not in schema["enum"]:
        raise RuntimeError(f"{path}: value {value!r} not in enum")

    if isinstance(value, str):
        min_length = schema.get("minLength")
        if min_length is not None and len(value) < min_length:
            raise RuntimeError(f"{path}: string shorter than minLength {min_length}")

    if isinstance(value, list):
        min_items = schema.get("minItems")
        if min_items is not None and len(value) < min_items:
            raise RuntimeError(f"{path}: array shorter than minItems {min_items}")
        item_schema = schema.get("items")
        if item_schema is not None:
            for index, item in enumerate(value):
                validate_against_schema(item, item_schema, f"{path}[{index}]")

    if isinstance(value, dict):
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                raise RuntimeError(f"{path}: missing required key {key}")
        if schema.get("additionalProperties") is False:
            extras = set(value) - set(properties)
            if extras:
                raise RuntimeError(f"{path}: unexpected keys {sorted(extras)}")
        for key, child_schema in properties.items():
            if key in value:
                validate_against_schema(value[key], child_schema, f"{path}.{key}")


def validate_response(response, label):
    try:
        import jsonschema
    except ImportError:
        validate_against_schema(response, SCHEMA)
        return {"label": label, "validated": True, "validator": "custom"}

    jsonschema.validate(response, SCHEMA)
    return {"label": label, "validated": True, "validator": "jsonschema"}


def get_scores(response):
    return response["structured_object"]["scores"]


def get_total(scores, company):
    return scores["total"][company]


def get_subtotal(scores, category, company):
    return scores[category][company]["subtotal"]


def get_factor_map(scores, category, company):
    return {
        key: value
        for key, value in scores[category][company].items()
        if key != "subtotal"
    }


def get_confidence_level(response):
    confidence = response["structured_object"].get("confidence")
    if isinstance(confidence, dict):
        return confidence.get("level")
    if isinstance(confidence, str):
        return confidence
    return None


def get_company_quadrants(response):
    scores = get_scores(response)
    quadrants = {}
    for company in COMPANIES:
        x_value = get_subtotal(scores, "proprietary_advantage", company)
        y_value = get_subtotal(scores, "workflow_criticality", company)
        quadrants[company] = quadrant_from_subtotals(x_value, y_value)
    return quadrants


def get_rank_order(response):
    ranked = extract_ranked_targets(response["structured_object"]["comparison"].get("ranked_targets"))
    if ranked:
        return ranked
    totals = {
        company: get_total(get_scores(response), company)
        for company in COMPANIES
    }
    return sorted(COMPANIES, key=lambda company: (-totals[company], company))


def compute_theme_overlap(codex_response, claude_response):
    per_company = {}
    material_difference = False
    for company in COMPANIES:
        codex_strengths = extract_theme_strings(codex_response["structured_object"]["top_strengths"].get(company))
        claude_strengths = extract_theme_strings(claude_response["structured_object"]["top_strengths"].get(company))
        codex_vulns = extract_theme_strings(codex_response["structured_object"]["main_vulnerabilities"].get(company))
        claude_vulns = extract_theme_strings(claude_response["structured_object"]["main_vulnerabilities"].get(company))

        combined_a = {item.lower() for item in codex_strengths + codex_vulns}
        combined_b = {item.lower() for item in claude_strengths + claude_vulns}
        union = combined_a | combined_b
        intersection = combined_a & combined_b
        similarity = (len(intersection) / len(union)) if union else 1.0
        if similarity < 0.3:
            material_difference = True

        per_company[company] = {
            "codex_strengths": codex_strengths,
            "claude_strengths": claude_strengths,
            "codex_vulnerabilities": codex_vulns,
            "claude_vulnerabilities": claude_vulns,
            "jaccard_similarity": round(similarity, 3),
        }
    return per_company, material_difference


def compute_interpretation(score_deltas, url_overlap_ratio, material_theme_difference):
    max_delta = max(abs(delta) for delta in score_deltas.values()) if score_deltas else 0
    if url_overlap_ratio < 0.35 and max_delta >= 3:
        return "source-selection drift"
    if max_delta >= 3:
        return "scoring drift"
    if material_theme_difference:
        return "narrative-emphasis drift"
    return "minimal drift"


def main():
    codex_version = command_output(["codex", "--version"])
    claude_version = command_output(["claude", "--version"])

    codex_raw = read_json(RUN_DIR / "codex-response.raw.json")
    claude_wrapper = read_json(RUN_DIR / "claude-response.raw.json")

    codex_response = normalize_response(
        kind="codex",
        requested_model=CONFIG["models"]["codex"],
        cli_version=codex_version,
        command_template=CONFIG["command_templates"]["codex"],
        raw_payload=codex_raw,
    )
    claude_response = normalize_response(
        kind="claude",
        requested_model=CONFIG["models"]["claude"],
        cli_version=claude_version,
        command_template=CONFIG["command_templates"]["claude"],
        raw_payload=claude_wrapper.get("structured_output", {}),
        wrapper=claude_wrapper,
    )

    validate_response(codex_response, "codex")
    validate_response(claude_response, "claude")

    (RUN_DIR / "codex-response.json").write_text(json.dumps(codex_response, indent=2) + "\n")
    (RUN_DIR / "claude-response.json").write_text(json.dumps(claude_response, indent=2) + "\n")

    codex_rank = get_rank_order(codex_response)
    claude_rank = get_rank_order(claude_response)
    codex_quadrants = get_company_quadrants(codex_response)
    claude_quadrants = get_company_quadrants(claude_response)

    total_deltas = {}
    category_deltas = defaultdict(dict)
    factor_deltas = defaultdict(lambda: defaultdict(dict))
    any_quadrant_change = False

    codex_scores = get_scores(codex_response)
    claude_scores = get_scores(claude_response)

    for company in COMPANIES:
        codex_total = get_total(codex_scores, company)
        claude_total = get_total(claude_scores, company)
        total_deltas[company] = claude_total - codex_total
        if codex_quadrants[company] != claude_quadrants[company]:
            any_quadrant_change = True

        for category in CATEGORIES:
            codex_subtotal = get_subtotal(codex_scores, category, company)
            claude_subtotal = get_subtotal(claude_scores, category, company)
            category_deltas[company][category] = claude_subtotal - codex_subtotal

            codex_factors = get_factor_map(codex_scores, category, company)
            claude_factors = get_factor_map(claude_scores, category, company)
            for factor in sorted(set(codex_factors) | set(claude_factors)):
                codex_value = codex_factors.get(factor)
                claude_value = claude_factors.get(factor)
                if codex_value is None or claude_value is None:
                    continue
                delta = claude_value - codex_value
                if abs(delta) > 1:
                    factor_deltas[company][category][factor] = {
                        "codex": codex_value,
                        "claude": claude_value,
                        "delta": delta,
                    }

    theme_overlap, material_theme_difference = compute_theme_overlap(codex_response, claude_response)

    codex_urls = set(extract_urls(codex_response["structured_object"].get("evidence_notes")))
    claude_urls = set(extract_urls(claude_response["structured_object"].get("evidence_notes")))
    url_union = codex_urls | claude_urls
    url_intersection = codex_urls & claude_urls
    url_overlap_ratio = (len(url_intersection) / len(url_union)) if url_union else 1.0

    rank_changed = codex_rank != claude_rank
    top_changed = codex_rank[:1] != claude_rank[:1]
    max_total_delta = max(abs(value) for value in total_deltas.values())

    if rank_changed or top_changed or any_quadrant_change or max_total_delta >= 6:
        severity = "high"
    elif not rank_changed and not top_changed and (3 <= max_total_delta <= 5 or material_theme_difference):
        severity = "moderate"
    else:
        severity = "none"

    interpretation = compute_interpretation(total_deltas, url_overlap_ratio, material_theme_difference)

    verdicts = {
        "codex": codex_response["structured_object"].get("final_verdict"),
        "claude": claude_response["structured_object"].get("final_verdict"),
    }
    confidence = {
        "codex": get_confidence_level(codex_response),
        "claude": get_confidence_level(claude_response),
    }

    metrics = {
        "run_dir": str(RUN_DIR),
        "prompt_path": CONFIG["prompt_path"],
        "models": CONFIG["models"],
        "cli_versions": {
            "codex": codex_version,
            "claude": claude_version,
        },
        "severity": severity,
        "interpretation": interpretation,
        "rankings": {
            "codex": codex_rank,
            "claude": claude_rank,
        },
        "quadrants": {
            "codex": codex_quadrants,
            "claude": claude_quadrants,
        },
        "total_deltas": {
            company: {
                "codex": get_total(codex_scores, company),
                "claude": get_total(claude_scores, company),
                "delta": total_deltas[company],
            }
            for company in COMPANIES
        },
        "category_subtotal_deltas": category_deltas,
        "factor_deltas_gt_1": factor_deltas,
        "final_verdicts": verdicts,
        "confidence_levels": confidence,
        "theme_overlap": theme_overlap,
        "source_url_overlap": {
            "codex_count": len(codex_urls),
            "claude_count": len(claude_urls),
            "intersection_count": len(url_intersection),
            "union_count": len(url_union),
            "overlap_ratio": round(url_overlap_ratio, 3),
            "shared_urls": sorted(url_intersection),
            "codex_only_urls": sorted(codex_urls - claude_urls),
            "claude_only_urls": sorted(claude_urls - codex_urls),
        },
    }

    (RUN_DIR / "drift-metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")

    lines = [
        "# Codex vs Claude Drift Summary",
        "",
        f"- Date: {CONFIG['timestamp']}",
        f"- Prompt: `{CONFIG['prompt_path']}`",
        f"- Codex: `{CONFIG['models']['codex']}` via `{codex_version}`",
        f"- Claude: `{CONFIG['models']['claude']}` via `{claude_version}`",
        f"- Severity: `{severity}`",
        f"- Interpretation: {interpretation}",
        "",
        "## Rankings",
        "",
        f"- Codex: {' > '.join(codex_rank)}",
        f"- Claude: {' > '.join(claude_rank)}",
        "",
        "## Per-Company Totals",
        "",
    ]

    for company in COMPANIES:
        lines.append(
            f"- {company}: Codex {get_total(codex_scores, company)}, Claude {get_total(claude_scores, company)}, delta {total_deltas[company]:+d}"
        )

    lines.extend([
        "",
        "## Quadrants",
        "",
    ])
    for company in COMPANIES:
        lines.append(
            f"- {company}: Codex `{codex_quadrants[company]}`, Claude `{claude_quadrants[company]}`"
        )

    lines.extend([
        "",
        "## Factor Deltas Greater Than 1",
        "",
    ])

    wrote_factor = False
    for company in COMPANIES:
        for category in CATEGORIES:
            for factor, payload in factor_deltas[company][category].items():
                wrote_factor = True
                lines.append(
                    f"- {company} {category}.{factor}: Codex {payload['codex']}, Claude {payload['claude']}, delta {payload['delta']:+d}"
                )
    if not wrote_factor:
        lines.append("- None")

    lines.extend([
        "",
        "## Verdict and Confidence",
        "",
        f"- Final verdicts differ: {'yes' if verdicts['codex'] != verdicts['claude'] else 'no'}",
        f"- Codex confidence: `{confidence['codex']}`",
        f"- Claude confidence: `{confidence['claude']}`",
        "",
        "## Source URL Overlap",
        "",
        f"- Shared URLs: {len(url_intersection)} of {len(url_union)} total unique URLs, overlap ratio {url_overlap_ratio:.3f}",
    ])

    if url_intersection:
        lines.append(f"- Shared set: {', '.join(sorted(url_intersection))}")
    if codex_urls - claude_urls:
        lines.append(f"- Codex-only: {', '.join(sorted(codex_urls - claude_urls))}")
    if claude_urls - codex_urls:
        lines.append(f"- Claude-only: {', '.join(sorted(claude_urls - codex_urls))}")

    lines.extend([
        "",
        "## Notes",
        "",
        f"- Theme emphasis materially differs: {'yes' if material_theme_difference else 'no'}",
        f"- Ranking changed: {'yes' if rank_changed else 'no'}",
        f"- Any quadrant changed: {'yes' if any_quadrant_change else 'no'}",
    ])

    (RUN_DIR / "drift-summary.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"compare_outputs.py failed: {exc}", file=sys.stderr)
        raise
