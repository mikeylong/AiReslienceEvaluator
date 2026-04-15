Use the installed `ai_resilience_evaluator` skill and follow the contract in `/Users/mike/AiReslienceEvaluator/SKILL.md`.

Task:
Compare Figma, Clio, and Notion for AI resilience using the repository rubric.

Requirements:
- Use current official-source research. Prefer official company materials, product documentation, pricing, integrations, APIs, trust/security, and related official materials.
- Do not use existing repo analysis outputs, report files, README summaries, or prior scores as evidence or starting points. You may read `/Users/mike/AiReslienceEvaluator/SKILL.md` for the rubric, but do not rely on `/Users/mike/AiReslienceEvaluator/reports/*` or other local report artifacts for company facts or scores.
- Return the three standard skill artifacts:
  1. Human-readable narrative
  2. Structured object
  3. SVG artifact
- Package the result as a single JSON object that conforms to the provided response schema.
- Put the full human-readable writeup into `narrative_markdown`.
- Put the structured skill output into `structured_object`.
- Put the SVG or plotting-spec fallback into `svg_artifact`.
- Put run details into `run_metadata`, including any self-reported model identifier, timestamp, and constraints you encountered.
- In `run_metadata`, only use these keys: `timestamp`, `requested_model`, `resolved_model`, `cwd`, `notes`.
- Populate all five `run_metadata` keys even if some values are approximate or empty.
- If you cannot produce literal SVG, return a plotting-spec fallback in `svg_artifact`.
- Include current official source URLs in the structured object evidence notes.
- Do not modify any files.

Output requirements:
- Rank all three companies.
- Score each company across the full rubric.
- Include comparison output in `structured_object.comparison`.
- Use the exact company names `Figma`, `Clio`, and `Notion`.
- Return JSON only. Do not wrap it in Markdown fences.
