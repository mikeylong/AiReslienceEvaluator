#!/usr/bin/env python3

import csv
import json
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STUDY_DIR = ROOT / "studies" / "web-build-study"
VISUAL_DIR = STUDY_DIR / "visual-memo"
MANIFEST_PATH = VISUAL_DIR / "screenshot-manifest.json"
CONSENSUS_PATH = STUDY_DIR / "consensus_scores.json"
TASK_METRICS_PATH = STUDY_DIR / "task_metrics.csv"
SVG_PATH = STUDY_DIR / "web-build-ai-resilience-2x2.svg"
OUTPUT_PATH = VISUAL_DIR / "index.html"

EXPECTED_RANKING = [
    ("wix-studio", 58),
    ("webflow", 56),
    ("figma-make", 48),
    ("figma-sites", 47),
    ("framer", 47),
    ("lovable", 39),
]

RUBRIC_GROUPS = [
    (
        "Proprietary Advantage",
        "proprietary_advantage",
        [
            ("context", "Context"),
            ("trust", "Trust"),
            ("distribution", "Distribution"),
            ("judgment", "Judgment"),
            ("liability_governance", "Liability / Governance"),
        ],
        "/25",
    ),
    (
        "Workflow Criticality",
        "workflow_criticality",
        [
            ("frequency", "Frequency"),
            ("operational_dependence", "Operational Dependence"),
            ("system_position", "System Position"),
            ("switching_cost", "Switching Cost"),
            ("budget_durability", "Budget Durability"),
        ],
        "/25",
    ),
    (
        "AI Resilience Tests",
        "ai_resilience_tests",
        [
            ("model_improvement_test", "Model Improvement Test"),
            ("wrapper_risk_test", "Wrapper Risk Test"),
            ("agent_readiness_test", "Agent Readiness Test"),
            ("accountability_test", "Accountability Test"),
            ("outcome_depth_test", "Outcome Depth Test"),
        ],
        "/25",
    ),
]

TASKS_EXERCISED = [
    {
        "label": "Task 1",
        "name": "Net-new marketing page",
        "timebox": "45 min",
        "prompt": "Create a responsive marketing page for Northstar Pediatrics with a hero, three benefit blocks, a pricing section, a testimonial, and a clear call to action for booking an intro call.",
        "checks": "Usable on desktop and mobile, all five required sections present, healthcare-trustworthy tone, and ready for stakeholder review without extra polishing outside the tool.",
    },
    {
        "label": "Task 2",
        "name": "Governed revision and reuse",
        "timebox": "60 min",
        "prompt": "Update the same project so the page supports three membership tiers, reusable testimonial and FAQ content where available, a clinician profile section, and a primary CTA change from booking to join waitlist.",
        "checks": "Applied on the same project, uses structured reuse where the tool supports it, preserves a consistent design system, and exposes a clear history or reusable structure rather than manual-only edits.",
    },
    {
        "label": "Task 3",
        "name": "Publish or handoff",
        "timebox": "60 min",
        "prompt": "Prepare the project for launch or developer handoff, publish the best available artifact, and document how a teammate or agent would make the next safe change.",
        "checks": "Produces a usable launch or handoff artifact, surfaces versioning or approval behavior where supported, and exercises connector, API, repo, or agent hooks when available.",
    },
]

METRICS_CAPTURED = [
    "time_to_first_acceptable_output",
    "time_to_completion",
    "requirements_pass_rate",
    "manual_fix_count",
    "structured_reuse",
    "publish_success",
    "governance_support",
    "agent_or_api_leverage",
]


def read_json(path: Path):
    return json.loads(path.read_text())


def read_task_metrics(path: Path):
    rows = list(csv.DictReader(path.read_text().splitlines()))
    completed = 0
    blocked = 0
    pending = 0
    for row in rows:
        status = row["status"]
        if status == "completed_observed":
            completed += 1
        elif status.startswith("blocked_"):
            blocked += 1
        elif "pending" in status:
            pending += 1
    return {
        "rows": rows,
        "total": len(rows),
        "completed": completed,
        "blocked": blocked,
        "pending": pending,
    }


def load_manifest(path: Path):
    manifest = read_json(path)
    screenshots = manifest.get("screenshots", [])
    if len(screenshots) != 12:
        raise SystemExit(f"Expected 12 screenshots in manifest, found {len(screenshots)}.")

    counts = {}
    for shot in screenshots:
        slug = shot["offering_slug"]
        counts[slug] = counts.get(slug, 0) + 1

    expected_slugs = {slug for slug, _ in EXPECTED_RANKING}
    manifest_slugs = set(counts)
    if manifest_slugs != expected_slugs:
        raise SystemExit(
            f"Manifest offering slugs mismatch. Expected {sorted(expected_slugs)}, found {sorted(manifest_slugs)}."
        )

    missing_counts = {slug: count for slug, count in counts.items() if count != 2}
    if missing_counts:
        raise SystemExit(f"Each offering must have exactly 2 screenshots. Found {missing_counts}.")

    hero_counts = {}
    for shot in screenshots:
        if shot.get("hero", False):
            slug = shot["offering_slug"]
            hero_counts[slug] = hero_counts.get(slug, 0) + 1
    missing_heroes = sorted(slug for slug in expected_slugs if hero_counts.get(slug) != 1)
    if missing_heroes:
        raise SystemExit(f"Each offering must have exactly 1 hero screenshot. Problem slugs: {missing_heroes}.")

    missing_files = []
    for shot in screenshots:
        image_path = VISUAL_DIR / shot["output_path"]
        if shot.get("required", False) and not image_path.exists():
            missing_files.append(str(image_path))
    if missing_files:
        joined = "\n".join(f"- {item}" for item in missing_files)
        raise SystemExit(f"Missing required screenshots:\n{joined}")

    return manifest


def format_delta(value: int) -> str:
    if value > 0:
        return f"+{value}"
    return str(value)


def build_ranking(consensus_data):
    ranked_targets = consensus_data["ranked_targets"]
    current = [(item["slug"], item["total"]) for item in ranked_targets]
    if current != EXPECTED_RANKING:
        raise SystemExit(f"Ranking mismatch. Expected {EXPECTED_RANKING}, found {current}.")
    return ranked_targets


def get_hero_shots(manifest):
    hero_by_slug = {}
    for shot in manifest["screenshots"]:
        if shot.get("hero", False):
            hero_by_slug[shot["offering_slug"]] = shot
    return hero_by_slug


def load_report_details(consensus_data):
    details = {}
    for slug, entry in consensus_data["consensus_scores"].items():
        report_path = STUDY_DIR / entry["report_paths"]["json"]
        details[slug] = read_json(report_path)
    return details


def render_image_card(shot):
    src = html.escape(shot["output_path"])
    alt = html.escape(shot["alt"])
    caption = html.escape(shot["caption"])
    return f"""
      <figure class="shot">
        <img src="{src}" alt="{alt}" loading="lazy">
        <figcaption>{caption}</figcaption>
      </figure>
    """


def render_placement_analysis(ranking, report_details):
    rows = []
    for item in ranking:
        slug = item["slug"]
        report = report_details[slug]
        strength_text = "; ".join(report["top_strengths"][:2])
        vulnerability_text = "; ".join(report["main_vulnerabilities"][:2])
        rows.append(
            f"""
        <tr>
          <th>{html.escape(report['target_name'])} <span>{item['total']}/75</span></th>
          <td>{html.escape(report['quadrant']['placement'])}</td>
          <td>{html.escape(report['quadrant']['rationale'])}</td>
          <td>{html.escape(strength_text)}</td>
          <td>{html.escape(vulnerability_text)}</td>
          <td>{html.escape(report['final_verdict'])}</td>
        </tr>
        """
        )
    body_rows = "\n".join(rows)
    return f"""
    <section class="placement">
      <h2>2x2 Placement Rationale</h2>
      <p>The x-axis measures proprietary advantage from commodity output to defensible ownership. The y-axis measures workflow criticality from nice-to-have utility to mission-critical operating depth. Placement uses structural judgment informed by the 15-factor scores, not arithmetic alone.</p>
      <div class="table-wrap">
        <table class="placement-table">
          <thead>
            <tr>
              <th>Offering</th>
              <th>Placement</th>
              <th>Why It Lands There</th>
              <th>Strengths Pulling It Up/Right</th>
              <th>Vulnerabilities Pulling It Down/Left</th>
              <th>AI Resilience Read</th>
            </tr>
          </thead>
          <tbody>
            {body_rows}
          </tbody>
        </table>
      </div>
    </section>
    """


def render_section(rank, item, empirical_summary, hero_shots, report_details):
    slug = item["slug"]
    summary = empirical_summary[slug]
    report = report_details[slug]
    delta = summary["total_delta"]
    delta_text = (
        f"Desk {summary['desk_total']} to empirical {summary['empirical_total']} ({'unchanged' if delta == 0 else format_delta(delta)})"
    )
    strengths = "\n".join(
        f"<li>{html.escape(point)}</li>"
        for point in report["top_strengths"][:2]
    )
    vulnerabilities = "\n".join(
        f"<li>{html.escape(point)}</li>"
        for point in report["main_vulnerabilities"][:2]
    )
    image = render_image_card(hero_shots[slug])
    return f"""
    <section class="offering" id="{html.escape(slug)}">
      <div class="offering-head">
        <h2>{html.escape(item['target_name'])}</h2>
        <div class="scoreline">Rank {rank} · Score {item['total']} · {html.escape(delta_text)}</div>
      </div>
      <p class="read">{html.escape(summary['empirical_task_read'])}</p>
      <p class="placement-line"><strong>2x2 placement:</strong> {html.escape(report['quadrant']['placement'])}. {html.escape(report['quadrant']['rationale'])}</p>
      <div class="analysis-grid">
        <div>
          <h3>What Carries The Score</h3>
          <ul>
            {strengths}
          </ul>
        </div>
        <div>
          <h3>What Limits The Score</h3>
          <ul>
            {vulnerabilities}
          </ul>
        </div>
      </div>
      <p class="verdict"><strong>Final verdict:</strong> {html.escape(report['final_verdict'])}</p>
      <div class="hero-shot">
{image}
      </div>
    </section>
    """


def render_rubric_matrix(consensus_data, ranking):
    offerings = [consensus_data["consensus_scores"][item["slug"]] for item in ranking]
    header_cells = "\n".join(
        f"<th>{html.escape(item['target_name'])}<span>{item['total']}/75</span></th>"
        for item in ranking
    )
    rows = []
    for group_label, group_key, factors, subtotal_suffix in RUBRIC_GROUPS:
        rows.append(
            f'<tr class="group-row"><th colspan="{len(ranking) + 1}">{html.escape(group_label)}</th></tr>'
        )
        for factor_key, factor_label in factors:
            score_cells = "\n".join(
                f"<td>{offering['scores'][group_key][factor_key]}/5</td>"
                for offering in offerings
            )
            rows.append(f"<tr><th>{html.escape(factor_label)}</th>{score_cells}</tr>")
        subtotal_cells = "\n".join(
            f"<td>{offering['scores'][group_key]['subtotal']}{subtotal_suffix}</td>"
            for offering in offerings
        )
        rows.append(f'<tr class="subtotal-row"><th>Subtotal</th>{subtotal_cells}</tr>')

    total_cells = "\n".join(
        f"<td>{offering['scores']['total']}/75</td>"
        for offering in offerings
    )
    rows.append(f'<tr class="total-row"><th>Total</th>{total_cells}</tr>')
    body_rows = "\n".join(rows)
    return f"""
    <section class="rubric">
      <h2>15-Factor Rubric Score Matrix</h2>
      <p>This is the actual empirical-adjusted cohort score table, using the same 15-factor, 75-point rubric used in the individual reports. Each cell is the consensus score for that factor after the task evidence was folded back into the study.</p>
      <div class="table-wrap">
        <table class="matrix">
          <thead>
            <tr>
              <th>Factor</th>
              {header_cells}
            </tr>
          </thead>
          <tbody>
            {body_rows}
          </tbody>
        </table>
      </div>
    </section>
    """


def render_tasks_section():
    task_rows = "\n".join(
        f"""
        <tr>
          <th>{html.escape(task['label'])}</th>
          <td>{html.escape(task['name'])}</td>
          <td>{html.escape(task['timebox'])}</td>
          <td>{html.escape(task['prompt'])}</td>
          <td>{html.escape(task['checks'])}</td>
        </tr>
        """
        for task in TASKS_EXERCISED
    )
    metrics = ", ".join(f"`{item}`" for item in METRICS_CAPTURED)
    return f"""
    <section class="tasks">
      <h2>Tasks Exercised</h2>
      <p>The empirical phase pushed every offering through the same three-task protocol. This is the part that turns the study into a stress test of workflow durability rather than a docs-only ranking.</p>
      <div class="table-wrap">
        <table class="tasks-table">
          <thead>
            <tr>
              <th>Task</th>
              <th>What Was Tested</th>
              <th>Timebox</th>
              <th>Prompt</th>
              <th>Acceptance Checks</th>
            </tr>
          </thead>
          <tbody>
            {task_rows}
          </tbody>
        </table>
      </div>
      <p class="small">Metrics captured: {metrics}.</p>
    </section>
    """


def build_html(consensus_data, task_metrics, manifest):
    ranking = build_ranking(consensus_data)
    empirical_summary = consensus_data["empirical_adjustment_summary"]
    hero_shots = get_hero_shots(manifest)
    report_details = load_report_details(consensus_data)
    study_metadata = consensus_data["study_metadata"]
    validity_read = consensus_data["validity_read"]
    prepared_on = study_metadata["prepared_on"]
    cohort = ", ".join(study_metadata["cohort"])
    findings = "\n".join(
        f"<li>{html.escape(item)}</li>"
        for item in validity_read["observed_findings"]
    )
    tasks_section = render_tasks_section()
    rubric_matrix = render_rubric_matrix(consensus_data, ranking)
    placement_analysis = render_placement_analysis(ranking, report_details)
    ranking_items = "\n".join(
        f"<li><strong>{html.escape(item['target_name'])}</strong> {item['total']}</li>"
        for item in ranking
    )
    sections = "\n".join(
        render_section(index, item, empirical_summary, hero_shots, report_details)
        for index, item in enumerate(ranking, start=1)
    )
    svg_rel = "../web-build-ai-resilience-2x2.svg"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Web-Build Study Visual Memo</title>
  <style>
    :root {{
      --text: #111;
      --muted: #555;
      --line: #d6d6d6;
      --bg: #fff;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      line-height: 1.45;
    }}
    main {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 36px 24px 56px;
    }}
    h1, h2 {{
      margin: 0;
      line-height: 1.15;
      font-weight: 600;
    }}
    h1 {{
      font-size: 28px;
      margin-bottom: 8px;
    }}
    h2 {{
      font-size: 22px;
      margin-bottom: 8px;
    }}
    p {{
      margin: 0 0 12px;
    }}
    .meta,
    .small,
    .scoreline,
    figcaption,
    footer {{
      color: var(--muted);
    }}
    .intro,
    .study,
    .tasks,
    .rubric,
    .evidence,
    .findings,
    .placement,
    .ranking,
    .why,
    .offering,
    footer {{
      border-top: 1px solid var(--line);
      padding-top: 18px;
      margin-top: 18px;
    }}
    .chart img {{
      display: block;
      width: 100%;
      height: auto;
      border: 1px solid var(--line);
    }}
    .ranking ol {{
      margin: 10px 0 0 20px;
      padding: 0;
    }}
    .ranking li {{
      margin: 0 0 6px;
    }}
    .fact-grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-top: 14px;
    }}
    .fact {{
      border: 1px solid var(--line);
      padding: 12px;
    }}
    .fact strong {{
      display: block;
      font-size: 22px;
      line-height: 1.1;
      margin-bottom: 4px;
    }}
    .study ul,
    .findings ul {{
      margin: 10px 0 0 20px;
      padding: 0;
    }}
    .study li,
    .findings li {{
      margin: 0 0 8px;
    }}
    .table-wrap {{
      overflow-x: auto;
      margin-top: 12px;
    }}
    table {{
      width: 100%;
      min-width: 900px;
      border-collapse: collapse;
    }}
    th,
    td {{
      border: 1px solid var(--line);
      padding: 8px 10px;
      text-align: left;
      vertical-align: top;
      font-size: 14px;
    }}
    thead th {{
      background: #fafafa;
      font-weight: 600;
    }}
    .matrix thead th span {{
      display: block;
      color: var(--muted);
      font-weight: 400;
      margin-top: 2px;
    }}
    .group-row th {{
      background: #f6f6f6;
      font-weight: 600;
    }}
    .subtotal-row th,
    .subtotal-row td,
    .total-row th,
    .total-row td {{
      font-weight: 600;
    }}
    .offering-head {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      align-items: baseline;
      flex-wrap: wrap;
      margin-bottom: 8px;
    }}
    .read {{
      max-width: 900px;
    }}
    .placement-table th span {{
      display: block;
      color: var(--muted);
      font-weight: 400;
      margin-top: 2px;
    }}
    .placement-line,
    .verdict {{
      max-width: 920px;
    }}
    .analysis-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
      margin-top: 12px;
      max-width: 920px;
    }}
    .analysis-grid h3 {{
      margin: 0 0 8px;
      font-size: 16px;
    }}
    .analysis-grid ul {{
      margin: 0 0 0 18px;
      padding: 0;
    }}
    .analysis-grid li {{
      margin: 0 0 8px;
    }}
    .hero-shot {{
      margin-top: 12px;
    }}
    .shot {{
      margin: 0;
      max-width: 920px;
    }}
    .shot img {{
      display: block;
      width: 100%;
      height: auto;
      border: 1px solid var(--line);
    }}
    figcaption {{
      font-size: 14px;
      margin-top: 8px;
    }}
    .links {{
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      margin-top: 10px;
    }}
    .links a {{
      color: inherit;
    }}
    @media (max-width: 820px) {{
      main {{
        padding: 24px 16px 40px;
      }}
      .fact-grid {{
        grid-template-columns: 1fr 1fr;
      }}
      .analysis-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    @media (max-width: 560px) {{
      .fact-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Web-Build Study Visual Memo</h1>
      <p class="meta">Prepared {html.escape(prepared_on)}. Empirical-adjusted ranking for the web-build resilience study.</p>
    </header>

    <section class="intro">
      <p>This memo is a visual summary of the web-build pilot, not just a gallery of tool outputs. It combines desk-phase scoring with live task evidence so the ranking reflects what actually held up in create, revise, and publish workflows.</p>
    </section>

    <section class="study">
      <h2>Study Design</h2>
      <p>The unit of analysis is the product offering, not the parent company. The cohort is {html.escape(cohort)}. The study uses the repository's 15-factor resilience rubric, shared evidence packets, structured desk-rater passes, and empirical task reruns.</p>
      <ul>
        <li>Evidence window: {html.escape(study_metadata['evidence_window'])}.</li>
        <li>Desk phase: 6 standardized evidence packets and 18 structured desk-rater scorecards feed the baseline and consensus totals.</li>
        <li>Task phase: 3 tasks per tool test net-new creation, governed revision, and publish or handoff.</li>
        <li>Method note: `operator_b` is the primary live pass. `operator_a` rows are same-agent replications used to widen empirical coverage and stress-test the rubric, not to claim independent human-operator validity.</li>
      </ul>
      <div class="fact-grid">
        <div class="fact"><strong>6</strong><span>offerings in cohort</span></div>
        <div class="fact"><strong>18</strong><span>desk scorecards</span></div>
        <div class="fact"><strong>{task_metrics['total']}</strong><span>task rows recorded</span></div>
        <div class="fact"><strong>{task_metrics['completed']}/{task_metrics['blocked']}</strong><span>completed vs blocker observations</span></div>
      </div>
    </section>

    {tasks_section}

    {rubric_matrix}

    <section class="evidence">
      <h2>Empirical Basis</h2>
      <p>{html.escape(validity_read['empirical_read'])}</p>
      <p class="small">Current consensus totals incorporate both the desk baseline and the observed task evidence. Blockers are treated as evidence about workflow fit, packaging, or governance rather than ignored as noise.</p>
    </section>

    <section class="findings">
      <h2>Observed Findings</h2>
      <ul>
        {findings}
      </ul>
    </section>

    <section class="chart">
      <img src="{svg_rel}" alt="2x2 AI resilience chart for the web-build study">
    </section>

    {placement_analysis}

    <section class="ranking">
      <h2>Empirical Ranking</h2>
      <ol>
        {ranking_items}
      </ol>
    </section>

    <section class="why">
      <h2>Why This Is More Empirical Than A Report</h2>
      <p>A one-off report tells you what the rubric thinks from desk evidence. This memo also shows how those claims held up once the tools were forced through the same create, revise, and publish sequence. The hero shots below are tied to that empirical read, not to vendor marketing imagery.</p>
    </section>

    {sections}

    <footer>
      <p>Sources: <a href="../analysis.md">analysis.md</a>, <a href="../consensus_scores.json">consensus_scores.json</a>, <a href="../task_metrics.csv">task_metrics.csv</a>, <a href="screenshot-manifest.json">screenshot-manifest.json</a>.</p>
    </footer>
  </main>
</body>
</html>
"""


def main():
    consensus_data = read_json(CONSENSUS_PATH)
    manifest = load_manifest(MANIFEST_PATH)
    task_metrics = read_task_metrics(TASK_METRICS_PATH)

    html_doc = build_html(consensus_data, task_metrics, manifest)
    OUTPUT_PATH.write_text(html_doc)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
