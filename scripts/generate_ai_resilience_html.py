#!/usr/bin/env python3
"""Generate the shareable HTML artifact for an AI resilience report set."""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_BASE = Path("reports/claude-design-figma-make-lovable-v0-ai-resilience-report")


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def normalize_base(path: Path) -> Path:
    if path.suffix in {".md", ".json", ".svg", ".html"}:
        return path.with_suffix("")
    return path


def read_text(path: Path, label: str) -> str:
    if not path.exists():
        fail(f"{label} not found: {path}")
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(read_text(path, "JSON report"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON report: {exc}")
    if not isinstance(data, dict):
        fail("JSON report root must be an object")
    return data


def current_timestamp() -> str:
    now = datetime.now()
    ampm = now.strftime("%p").lower()
    return f"{now.strftime('%b')} {now.day}, {now.year} at {now.strftime('%I').lstrip('0')}:{now.strftime('%M')} {ampm}"


def repo_url() -> str | None:
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

    raw = result.stdout.strip()
    if not raw:
        return None
    if raw.startswith("git@github.com:"):
        raw = "https://github.com/" + raw.removeprefix("git@github.com:")
    if raw.endswith(".git"):
        raw = raw[:-4]
    if raw.startswith("http://") or raw.startswith("https://"):
        return raw
    return None


def markdown_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)
    if not match:
        return fallback
    title = match.group(1).strip()
    return re.sub(r"\s+AI Resilience Report$", "", title)


def prepared_line(markdown: str) -> str | None:
    match = re.search(r"^Prepared:\s*(.+?)\s*$", markdown, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def body_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip() + "\n"


def slug(value: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", value.lower())
    cleaned = re.sub(r"\s+", "-", cleaned.strip())
    return cleaned or "section"


def section_nav(markdown: str) -> str:
    links: list[str] = []
    for match in re.finditer(r"^##\s+(.+?)\s*$", markdown, re.MULTILINE):
        title = match.group(1).strip()
        links.append(
            f'<a href="#{html.escape(slug(title), quote=True)}">{html.escape(title)}</a>'
        )
    return "\n".join(links)


def score_cards(report: dict[str, Any]) -> str:
    ranked = report.get("comparison", {}).get("ranked_targets", [])
    if not isinstance(ranked, list):
        ranked = []
    cards: list[str] = []
    for entry in ranked[:7]:
        if not isinstance(entry, dict):
            continue
        name = str(entry.get("target_name", "")).strip()
        total = entry.get("total")
        band = str(entry.get("band", "")).strip()
        if not name or not isinstance(total, int):
            continue
        label = f"{name} - {band}" if band else name
        cards.append(
            "<div class=\"score-card\">"
            f"<strong>{total}/75</strong>"
            f"<span>{html.escape(label)}</span>"
            "</div>"
        )
    return "\n".join(cards)


def marker_note(report: dict[str, Any]) -> str:
    quadrant = report.get("quadrant", {})
    marker_shapes = quadrant.get("marker_shapes") if isinstance(quadrant, dict) else None
    if not isinstance(marker_shapes, dict):
        return (
            "<strong>How to read the markers.</strong> Every marker is scored and "
            "ranked in the same 75-point cohort. Marker shape identifies the "
            "workflow entry point; it is not a scoring adjustment."
        )
    diamonds = sorted(
        name for name, shape in marker_shapes.items() if str(shape).lower() == "diamond"
    )
    circles = sorted(
        name for name, shape in marker_shapes.items() if str(shape).lower() == "circle"
    )
    parts = [
        "<strong>How to read the markers.</strong> Every marker is scored and ranked in the same 75-point cohort."
    ]
    if circles:
        parts.append(f"Circles mark visual/app-builder surfaces: {html.escape(', '.join(circles))}.")
    if diamonds:
        parts.append(f"Diamonds mark coding tools: {html.escape(', '.join(diamonds))}.")
    parts.append(
        "The shape is a caveat about workflow entry point and technical ergonomics, not an exclusion from the ranking."
    )
    return " ".join(parts)


def convert_markdown(markdown: str) -> str:
    try:
        result = subprocess.run(
            ["pandoc", "--from=gfm", "--to=html"],
            input=markdown,
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        fail("pandoc is required to regenerate HTML")
    except subprocess.CalledProcessError as exc:
        fail(f"pandoc failed: {exc.stderr.strip() or exc}")
    return result.stdout


def wrap_tables(fragment: str) -> str:
    return re.sub(
        r"(<table>.*?</table>)",
        r'<div class="table-wrap">\1</div>',
        fragment,
        flags=re.DOTALL,
    )


def css() -> str:
    return """
:root {
  --ink: #101010;
  --muted: #5f6368;
  --line: #d8d8d2;
  --soft: #f7f7f4;
  --soft-strong: #eeeeea;
  --max: 1180px;
  --measure: 900px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: #fff;
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  line-height: 1.5;
}
.page {
  width: min(var(--max), calc(100vw - 48px));
  margin: 0 auto;
  padding: 28px 0 72px;
}
.primary-figure { margin: 0; }
.primary-figure svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: min(78vh, 860px);
}
.chart-note,
.paper-header,
.nav,
.report-body,
.footer {
  max-width: var(--measure);
  margin-left: auto;
  margin-right: auto;
}
.chart-note {
  margin-top: 14px;
  color: #303236;
  font-family: Georgia, "Times New Roman", serif;
  font-size: 15px;
  line-height: 1.58;
}
.paper-header {
  margin-top: 36px;
  padding-top: 28px;
  border-top: 1px solid var(--line);
}
.eyebrow {
  margin: 0 0 10px;
  color: var(--muted);
  font-size: 12px;
  font-weight: 760;
  letter-spacing: 0;
  text-transform: uppercase;
}
.paper-header h1 {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(30px, 4vw, 46px);
  font-weight: 650;
  line-height: 1.12;
}
.meta {
  margin-top: 14px;
  color: var(--muted);
  font-size: 15px;
}
.abstract {
  margin-top: 18px;
  color: #2d2f32;
  font-family: Georgia, "Times New Roman", serif;
  font-size: 17px;
}
.score-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 8px;
  margin-top: 22px;
}
.score-card {
  border: 1px solid var(--line);
  background: var(--soft);
  padding: 12px 14px;
  min-height: 82px;
}
.score-card strong {
  display: block;
  font-size: 26px;
  line-height: 1;
}
.score-card span {
  display: block;
  margin-top: 6px;
  color: var(--muted);
  font-size: 13px;
}
.nav {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  gap: 10px;
  overflow-x: auto;
  padding: 12px 0;
  background: rgba(255, 255, 255, .95);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(8px);
}
.nav a {
  flex: 0 0 auto;
  padding: 7px 10px;
  border: 1px solid var(--line);
  background: #fff;
  color: #282828;
  font-size: 12px;
  font-weight: 680;
  text-decoration: none;
}
.report-body {
  display: grid;
  gap: 0;
  margin-top: 26px;
}
.report-body p,
.report-body ul,
.report-body .table-wrap {
  margin-top: 16px;
}
.report-body p {
  color: #2d2f32;
  font-size: 16px;
}
.report-body strong { color: #111; }
.report-body h2 {
  margin: 44px 0 0;
  padding-top: 36px;
  border-top: 1px solid var(--line);
  font-family: Georgia, "Times New Roman", serif;
  font-size: 30px;
  line-height: 1.08;
}
.report-body h3 {
  margin: 34px 0 0;
  font-size: 21px;
  line-height: 1.08;
}
.report-body ul {
  padding-left: 22px;
  color: #2d2f32;
}
.report-body li + li { margin-top: 8px; }
.table-wrap {
  width: 100%;
  overflow-x: auto;
  border: 1px solid var(--line);
  background: #fff;
}
table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  font-size: 13px;
}
th,
td {
  padding: 10px 12px;
  border-bottom: 1px solid var(--line);
  border-right: 1px solid var(--line);
  text-align: left;
  vertical-align: top;
  white-space: normal;
  overflow-wrap: anywhere;
  word-break: normal;
  hyphens: auto;
}
th:last-child,
td:last-child { border-right: 0; }
thead th {
  background: var(--soft-strong);
  font-size: 12px;
  font-weight: 760;
  text-transform: uppercase;
}
tbody tr:last-child td { border-bottom: 0; }
code {
  padding: 1px 5px;
  border: 1px solid var(--line);
  background: var(--soft);
  font-family: "Aptos Mono", "SFMono-Regular", Consolas, monospace;
  font-size: .92em;
}
a { color: #111; text-underline-offset: 2px; }
.footer {
  margin-top: 46px;
  padding-top: 22px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 13px;
}
@media (max-width: 760px) {
  .page { width: calc(100vw - 24px); }
  .chart-note,
  .paper-header,
  .nav,
  .report-body,
  .footer { max-width: none; }
}
""".strip()


def render_html(base: Path) -> str:
    markdown = read_text(base.with_suffix(".md"), "markdown report")
    svg = read_text(base.with_suffix(".svg"), "SVG")
    report = read_json(base.with_suffix(".json"))

    title = markdown_title(markdown, str(report.get("target_name", "AI Resilience Report")))
    prepared = prepared_line(markdown)
    metadata = "15-factor rubric - 75-point scale - same-cohort rerun"
    if prepared:
        metadata = f"Prepared {prepared} - {metadata}"

    body = wrap_tables(convert_markdown(body_markdown(markdown)))
    repo = repo_url()
    footer = f"Generated {html.escape(current_timestamp())}"
    if repo:
        footer += f' &middot; <a href="{html.escape(repo, quote=True)}">GitHub repo</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | AI Resilience Report</title>
<style>
{css()}
</style>
</head>
<body>
<main class="page paper">
<figure class="primary-figure" aria-label="AI resilience 2x2 chart">
{svg}
</figure>
<p class="chart-note">{marker_note(report)}</p>
<header class="paper-header">
<p class="eyebrow">Research report</p>
<h1>{html.escape(title)}</h1>
<p class="meta">{html.escape(metadata)}</p>
<p class="abstract"><strong>Abstract.</strong> {html.escape(str(report.get("summary", "")).strip())}</p>
<div class="score-grid">
{score_cards(report)}
</div>
</header>
<nav class="nav" aria-label="Report sections">
{section_nav(markdown)}
</nav>
<article class="report-body">
{body}
</article>
<p class="footer">{footer}</p>
</main>
</body>
</html>
"""


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "report_base",
        nargs="?",
        default=str(DEFAULT_BASE),
        help="Report basename or one artifact path. Defaults to the current cohort report.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    base = normalize_base(Path(args.report_base))
    html_path = base.with_suffix(".html")
    output = render_html(base)
    html_path.write_text(output, encoding="utf-8")
    print(f"wrote {html_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
