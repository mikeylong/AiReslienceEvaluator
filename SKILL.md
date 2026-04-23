---
name: "ai_resilience_evaluator"
description: "Produce an AI resilience assessment with a markdown narrative, shareable HTML report, 2x2 placement, 15-factor score, moat audit, final verdict, structured object, and scalable 2x2 graphic when evaluating a company, comparing targets, stress-testing a memo, re-scoring after new evidence, or ranking candidates."
---

# AI Resilience Evaluator

Use this skill to assess whether a company, product, business unit, market category, or investment target owns durable value above commodity AI generation.

Default posture: produce a research-backed resilience assessment, not a generic company summary. Treat current facts as time-sensitive. When the analysis depends on recent launches, pricing, integrations, security posture, APIs, positioning, or leadership claims, verify them with current sources.

## Trigger Cases

Use this skill when the user asks to:

- evaluate a specific company or product for resilience to AI disruption
- compare multiple companies using the same rubric
- score a category or ranked candidate set
- stress-test a strategy or investment memo
- re-score a company after a launch, product shift, or new evidence

## Contract

Return four artifacts every time:

1. A readable markdown narrative with these sections: Executive summary, 2x2 placement, full score table, top strengths, main vulnerabilities, strategic read, final verdict, confidence level, evidence notes.
2. A shareable HTML report generated from the markdown narrative and SVG. Treat this as the primary user-facing output artifact after markdown.
3. A structured object with these base keys: `target_name`, `summary`, `quadrant`, `scores`, `top_strengths`, `main_vulnerabilities`, `strategic_read`, `final_verdict`, `confidence`, `evidence_notes`.
4. A scalable SVG 2x2 that plots the target or targets on the same axes used in the narrative. If literal SVG generation is unavailable, return a compact plotting spec with axis labels, coordinates, and label text as the fourth artifact.

Use this object shape consistently:
- `quadrant`: `x_axis`, `y_axis`, `placement`, `rationale`
- `scores`: `proprietary_advantage`, `workflow_criticality`, `ai_resilience_tests`, `total`
- each score category: named factors plus `subtotal`
- `strategic_read`: `durable_layers`, `commoditizing_layers`, `next_moves`
- `confidence`: `level`, `reason`

Add `comparison` only when multiple targets are supplied. When `comparison` is present, include `ranked_targets`, `relative_summary`, and `key_differences`. Sort `ranked_targets` by descending total score and explain when the spread is mostly category-driven rather than execution-driven.

If evidence is sparse, still return all four artifacts, but mark uncertain factor scores as `null`, label subtotals and totals as partial, lower confidence, and include `unknowns_that_would_change_the_score_most`.

Allowed assumptions:
- infer buyer, user, workflow, and category when evidence supports the inference
- use category-pattern inference only after exhausting company-specific evidence
- use user-provided artifacts without external browsing when the task is explicitly artifact-bound

Do not promise:
- certainty where evidence is weak
- private-market facts you cannot verify
- resilience based on UX quality, AI branding, or popularity alone

## Research Standard

Use this evidence order: official company materials, product documentation, pricing and packaging, integration and API docs, trust and security docs, credible third-party analysis, user artifacts, then category inference.
Use a shared evidence standard and a shared default time window across targets in comparison mode. Default to the most recent 12 months for change-sensitive evidence, and use older materials only for durable background context.
If the user did not explicitly limit the task to provided artifacts, prefer current-source research over stale prior knowledge for company facts that can change.
Do not use existing repo reports, prior score artifacts, README summaries, consensus files, or older study writeups as factual evidence for a fresh evaluation unless the user explicitly scopes that dated study in. Local repo files may still supply the rubric contract, validators, formatting examples, and edit targets.
Distinguish evidence from inference in every factor rationale with one of these labels: `Direct evidence`, `Credible third-party evidence`, `Inference`.

For early entrants or sparse official evidence, use YouTube reviews only as third-party qualitative context. Prefer current videos with available captions or transcripts, capture source metadata, cross-check product facts against official sources, and do not treat transcript evidence as controlled live-task evidence.

## Workflow

1. Normalize the target.
Build a short operational profile covering what is sold, who buys it, who uses it, what workflow it serves, where AI appears in the value chain, the relevant category, and any comparison targets or constraints. If the target spans multiple products or business units, scope the analysis to the named unit; if the prompt is ambiguous, state the scope you chose.

2. Gather evidence.
Start with official materials, then product docs, pricing, integrations, APIs, trust/security, and only then move to third-party analysis or category inference. If the user supplied a memo, notes, or transcript, treat that artifact as evidence to analyze, not as ground truth.

3. Identify moat layers.
Assess whether the company meaningfully owns context, trust, distribution, judgment, and liability or governance.

4. Assess workflow criticality.
Determine whether the product is optional, recurring but replaceable, embedded, or mission-critical.

5. Run AI pressure tests.
Stress-test the business against stronger models, cheaper entrants, faster software creation, agent-mediated discovery and execution, and the declining value of raw generation.

6. Score the rubric.
Assign a score from 1 to 5 for each factor with one concise rationale tied to evidence or explicit inference.

7. Place the target in the 2x2.
Use structural judgment, not arithmetic alone. Totals inform the placement, but do not fully determine it.

8. Generate the strategic read, HTML report, and visual.
State what is durable, what is commoditizing, what improves as models improve, and what must become true for the company to remain resilient. Create a shareable HTML report and a minimal 2x2 that use the same axes and placements as the written assessment.

## Scoring Model

Score 15 factors on a fixed 75-point rubric. Do not weight categories numerically in v1.

Score these categories and factors:

- `proprietary_advantage`: `context`, `trust`, `distribution`, `judgment`, `liability_governance`
- `workflow_criticality`: `frequency`, `operational_dependence`, `system_position`, `switching_cost`, `budget_durability`
- `ai_resilience_tests`: `model_improvement_test`, `wrapper_risk_test`, `agent_readiness_test`, `accountability_test`, `outcome_depth_test`

Important scoring rules:

- `wrapper_risk_test` is reversed: `5` means low wrapper risk and `1` means high wrapper risk.
- Do not give high scores for polish, interface familiarity, or feature novelty alone.
- Do not treat AI features as moat unless they are tied to trust, context, workflow control, governance, or accountability.
- If evidence is sparse, lower confidence before lowering the business-quality judgment. Only use `null` scores when the gap is too material to defend a number.
- Do not back-solve factor scores from the final verdict; assign factor scores first, then interpret the aggregate.

Use these interpretation bands: `60-75` strong resilience, `45-59` mixed but promising, `30-44` vulnerable middle, `<30` high disruption risk.

## Heuristics And Red Flags

Increase scores when evidence shows proprietary workflow context, recurring-work embed, system-of-record or system-of-action position, real domain judgment, approvals or auditability, stronger models increasing value, trusted distribution or routing power, accountability in high-stakes outcomes, support for both human and agent use, or payment for outcomes rather than drafts.

Decrease scores when evidence shows wrapper dependence on generic models, novelty without workflow depth, low switching cost, public or easily replicated context, weak distribution, output that must be verified elsewhere, no role when the AI is wrong, draft-only usage, polish mistaken for judgment, or interface familiarity mistaken for moat.

Call out these red flags explicitly when present:

- `Wrapper Illusion`, `Workflow Thinness`, `Trust Gap`, `Context Weakness`, `Agent Irrelevance`, `Accountability Vacuum`

## Category Interpretation

Apply category adjustments in the narrative, not in the scoring math.

- Regulated or high-stakes domains: emphasize trust, governance, accountability, auditability, and system position.
- Creative and media: emphasize taste, curation, community trust, and distribution; weak workflow embed is not automatically fatal.
- Developer tooling and infrastructure: emphasize system position, workflow embed, context depth, platform leverage, and whether better models strengthen or replace the tool.
- Marketplaces and platforms: emphasize trust, verification, routing power, transaction confidence, and network effects.

When differences between companies are driven by category structure rather than execution, say so explicitly.

## Output Guidance

The narrative should be concise, comparative when useful, direct about what is durable versus exposed, and explicit about uncertainty. Avoid hype language, generic strategy cliches, vague admiration, unsupported claims, and fake precision. For HTML, SVG, source-function, and YouTube transcript appendix details, follow [references/report-artifacts.md](references/report-artifacts.md).

The score table should show every factor with `score`, a one-sentence `rationale`, and an evidence label.

Compact rationale style:

- `Context: 4 — Direct evidence. The product stores governed workflow state and customer records used in daily operations.`
- `Wrapper risk test: 2 — Inference. Most customer-visible value appears reproducible with commodity models and ordinary UX.`

For comparison mode, score each target individually, rank by total score, add a `comparison` block with `ranked_targets`, `relative_summary`, and `key_differences`, and keep the same evidence standard and time window for all targets.

For re-score mode, identify what changed, note which factor scores moved and why, and distinguish changed evidence from unchanged prior assumptions. For memo stress-test mode, evaluate the memo's claims against external evidence when available, state where the memo overstates moat or misses risk, and do not treat the memo's framing as proof. For ranked-list mode, evaluate each target with the same rubric, then present the ranking as a compact portfolio screen rather than collapsing everything into one blended narrative.

## Edge Cases

- If the user provides only a target name, infer the rest from current research and state the inferred buyer, user, and workflow.
- If the user provides only a category, assess the category's typical resilience pattern, name the likely durable and exposed layers, and be explicit that the result is category-level rather than company-specific.
- If the user provides only artifacts, assess the thesis conservatively and identify which missing facts would most change the result.
- If public evidence is thin, return a tentative quadrant, partial scores where needed, low confidence, and the top unknowns.
- If comparison targets span different categories, normalize the scoring method and explain category effects separately from execution quality.
- If a company uses AI internally but sells durable non-AI value, do not penalize it for not branding itself as an AI company.
- If a company has strong taste, brand, or community but weak workflow embed, explain the premium-niche path explicitly instead of forcing a workflow-centric conclusion.
- If a recent launch is doing most of the narrative work, separate the resilience of the underlying business from the resilience of the new AI feature set.
- If no file format is specified for the chart artifact, default to SVG.
- If the visual would contain many targets, keep the chart readable first; shorten labels, move labels into external lanes, or return ranked labels outside the plot rather than cluttering the quadrant.

## Example Requests

- `Evaluate Datadog for resilience to AI disruption.`
- `Compare Clio, Notion, and Figma using the AI resilience rubric.`
- `Compare Clio, Notion, and Figma using the AI resilience rubric for slide-ready review.`
- `Score this investor memo and tell me whether the moat is real.`
- `Reassess this company after its new agent product launch.`
- `Rank these six startups by AI resilience.`
