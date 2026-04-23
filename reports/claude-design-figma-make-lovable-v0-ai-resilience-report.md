# Claude Design vs Figma Make vs Lovable vs Vercel v0 vs Codex vs Cursor vs Claude Code AI Resilience Report

Prepared: April 23, 2026

Scope: AI-assisted creation-to-published UI/product workflows used by designers, founders, PMs, and engineering-adjacent teams. Claude Design, Figma Make, Lovable, and Vercel v0 are visual/app-builder surfaces. Codex, Cursor, and Claude Code are codebase-native coding tools scored in the same cohort because designers can use them to generate and revise application UI, but they retain diamond markers in the 2x2 to flag the different entry point and the need for technical workflow comfort.

## Executive Summary

A current-source AI resilience comparison of seven AI-assisted creation-to-published UI/product workflows, now scored as one cohort. Cursor leads at 59/75 because it sits deepest in the editor, repository, terminal, and review loop. Claude Code and Codex follow at 58/75 and 57/75 because they are similarly close to production code, with slightly different distribution and workflow-continuity profiles. Vercel v0 leads the visual/app-builder products at 54/75 through Vercel deploy, GitHub, preview, and app-building linkage. Figma Make scores 50/75 from design-system context and Figma distribution. Lovable scores 46/75 as a credible full-stack app builder with cost and assurance caveats. Claude Design scores 44/75 because it has impressive visual breadth but launch-stage operational evidence.


Ranking:

| Rank | Target | Marker | Total | Band | Short read |
| --- | --- | --- | --- | --- | --- |
| 1 | Cursor | Diamond | 59/75 | Mixed But Promising | Best codebase-native operating surface; less designer-native than visual app builders. |
| 2 | Claude Code | Diamond | 58/75 | Mixed But Promising | Strong repo-native coding agent; excellent handoff partner but not a design workspace. |
| 3 | Codex | Diamond | 57/75 | Mixed But Promising | Powerful code agent and PR workflow; less visual/designer-native than v0 or Figma Make. |
| 4 | Vercel v0 | Circle | 54/75 | Mixed But Promising | Closest non-code-agent product to shipped software through Vercel, GitHub, PRs, and deploys. |
| 5 | Figma Make | Circle | 50/75 | Mixed But Promising | Best design-system context and stakeholder-prototype workflow; weaker as production control plane. |
| 6 | Lovable | Circle | 46/75 | Mixed But Promising | Strong prompt-to-app/deploy workflow, but trust, costs, and production assurance remain limiting. |
| 7 | Claude Design | Circle | 44/75 | Vulnerable Middle | Powerful visual artifact surface, but launch-stage evidence and production control are still thin. |

## 2x2 Placement

Axes used in the SVG:

- X-axis: Nice-to-Have Output -> Proprietary Workflow Context
- Y-axis: Prototype Surface -> Production Workflow Control

Marker convention: circles and diamonds are both scored in the same 75-point cohort. Circles mark visual/app-builder surfaces. Diamonds mark coding tools: Codex, Cursor, and Claude Code. The diamond is a caveat about workflow entry point, not a scoring discount or exclusion.


| Target | Marker | Placement | Rationale |
| --- | --- | --- | --- |
| Cursor | Diamond | Upper-right: strongest same-cohort workflow control, with designer-ergonomics caveat | Best codebase-native operating surface; less designer-native than visual app builders. |
| Claude Code | Diamond | Upper-right: terminal-native production control, with non-visual surface caveat | Strong repo-native coding agent; excellent handoff partner but not a design workspace. |
| Codex | Diamond | Upper-right: strong agentic coding command center, slightly lower continuity than editor-native Cursor | Powerful code agent and PR workflow; less visual/designer-native than v0 or Figma Make. |
| Vercel v0 | Circle | Upper-right: best visual app-builder link to deploy and production surfaces | Closest non-code-agent product to shipped software through Vercel, GitHub, PRs, and deploys. |
| Figma Make | Circle | Right of center: strongest design-context surface, below code-agent production control | Best design-system context and stakeholder-prototype workflow; weaker as production control plane. |
| Lovable | Circle | Near center-right: app-builder depth, below stronger incumbent/code-agent control | Strong prompt-to-app/deploy workflow, but trust, costs, and production assurance remain limiting. |
| Claude Design | Circle | Right of center on output breadth, below workflow midpoint | Powerful visual artifact surface, but launch-stage evidence and production control are still thin. |

## Full Score Table

### Cursor - 59/75

| Category | Factor | Score | Evidence label | Rationale |
| --- | --- | --- | --- | --- |
| Proprietary advantage | Context | 5 | Direct evidence | Cursor indexes codebases, uses editor state, rules, terminal context, and PR history, giving it the deepest local implementation context in this cohort. |
| Proprietary advantage | Trust | 4 | Direct evidence | Cursor publishes security, SOC 2 Type II, privacy-mode, and enterprise controls, while its own security page still cautions sensitive environments to assess risk. |
| Proprietary advantage | Distribution | 4 | Credible third-party evidence | The product benefits from AI-editor adoption and VS Code familiarity; recent reviewer transcripts also frame it as a default agentic coding workspace for many builders. |
| Proprietary advantage | Judgment | 2 | Inference | Cursor improves implementation throughput but does not own product judgment, brand taste, accessibility acceptance, or release decisions. |
| Proprietary advantage | Liability governance | 3 | Direct evidence | Review diffs, approval flows, security controls, privacy modes, and enterprise settings help governance, but customers remain accountable for shipped code. |
| Workflow criticality | Frequency | 4 | Credible third-party evidence | Reviewer transcripts show frequent agentic coding use; for designers specifically, frequency depends on comfort working in a code editor. |
| Workflow criticality | Operational dependence | 4 | Direct evidence | Cursor can sit inside the implementation loop through files, terminal commands, code review, agent tools, and codebase indexing. |
| Workflow criticality | System position | 5 | Direct evidence | It occupies the editor/agent layer where UI code is inspected, modified, run, reviewed, and committed. |
| Workflow criticality | Switching cost | 4 | Inference | Rules, indexed context, editor habits, and project setup create meaningful friction, though code remains portable. |
| Workflow criticality | Budget durability | 4 | Direct evidence | Paid team and enterprise packaging ties spend to daily software delivery rather than one-off prototype generation. |
| AI resilience tests | Model improvement test | 5 | Inference | Better models should increase value because Cursor attaches model output to repository context, terminal execution, and review loops. |
| AI resilience tests | Wrapper risk test | 4 | Inference | The codebase/editor position lowers wrapper risk, though Cursor still depends on access to frontier models and competing agentic editors. |
| AI resilience tests | Agent readiness test | 5 | Direct evidence | Cursor documents agent tools for search, edit, terminal execution, MCP, and codebase search. |
| AI resilience tests | Accountability test | 2 | Inference | It can surface diffs and run checks, but production correctness, security, accessibility, and user acceptance remain human-owned. |
| AI resilience tests | Outcome depth test | 4 | Credible third-party evidence | Transcripts show full-feature coding workflows and PR-oriented review, but not end-to-end responsibility for product outcomes. |

Subtotals: proprietary advantage 18/25, workflow criticality 21/25, ai resilience tests 20/25.

### Claude Code - 58/75

| Category | Factor | Score | Evidence label | Rationale |
| --- | --- | --- | --- | --- |
| Proprietary advantage | Context | 4 | Direct evidence | Claude Code reads project files, executes commands, uses memory/rules, connects via MCP, and can integrate external context such as Figma through tools. |
| Proprietary advantage | Trust | 4 | Direct evidence | Anthropic trust, enterprise packaging, and Claude distribution support buyer trust, though code-agent risk still requires customer controls. |
| Proprietary advantage | Distribution | 4 | Direct evidence | Claude Code inherits Claude/Anthropic distribution and has terminal, IDE, and GitHub workflow surfaces. |
| Proprietary advantage | Judgment | 2 | Inference | It can reason through code and edge cases, but product judgment, UX quality, and release approval remain user responsibilities. |
| Proprietary advantage | Liability governance | 3 | Direct evidence | GitHub Actions, MCP controls, permissions, and review workflows help governance but do not transfer accountability. |
| Workflow criticality | Frequency | 4 | Credible third-party evidence | Recent practitioner transcripts show recurring use for planning, coding, testing, and codebase exploration. |
| Workflow criticality | Operational dependence | 4 | Direct evidence | It can modify files, run commands, create commits, and operate in real repos, making it part of the implementation loop. |
| Workflow criticality | System position | 5 | Direct evidence | Claude Code sits directly in terminal/IDE/GitHub workflows where production code changes happen. |
| Workflow criticality | Switching cost | 4 | Inference | Project memories, commands, MCP setup, and workflow habits create friction, although source code remains portable. |
| Workflow criticality | Budget durability | 4 | Direct evidence | Claude paid plans and enterprise packaging make spend attach to software delivery, despite transcript-reported credit/cost management needs. |
| AI resilience tests | Model improvement test | 5 | Inference | Stronger reasoning and coding models should directly improve repo-level planning, edits, testing, and debugging. |
| AI resilience tests | Wrapper risk test | 4 | Inference | Terminal, GitHub, MCP, and workflow integration reduce wrapper risk, but competition among code agents remains intense. |
| AI resilience tests | Agent readiness test | 5 | Direct evidence | Claude Code is explicitly an agentic coding tool with MCP, IDE integrations, and GitHub workflows. |
| AI resilience tests | Accountability test | 2 | Inference | It can run checks and support reviews, but users still own correctness, security, accessibility, and production outcomes. |
| AI resilience tests | Outcome depth test | 4 | Credible third-party evidence | Transcripts show sophisticated codebase work and production-style review, but not durable ownership after deployment. |

Subtotals: proprietary advantage 17/25, workflow criticality 21/25, ai resilience tests 20/25.

### Codex - 57/75

| Category | Factor | Score | Evidence label | Rationale |
| --- | --- | --- | --- | --- |
| Proprietary advantage | Context | 4 | Direct evidence | Codex connects to repositories, cloud worktrees, IDE/terminal surfaces, skills, and PR review flows, but is less continuously editor-native than Cursor. |
| Proprietary advantage | Trust | 4 | Direct evidence | OpenAI security, enterprise data controls, and Codex product positioning support trust for teams. |
| Proprietary advantage | Distribution | 4 | Direct evidence | Codex benefits from ChatGPT/OpenAI distribution, app, IDE, and terminal surfaces. |
| Proprietary advantage | Judgment | 2 | Inference | It can reason through implementation, but product/design judgment and final release decisions remain external. |
| Proprietary advantage | Liability governance | 3 | Direct evidence | PR review, worktrees, comments, and business security controls support governance without assuming outcome liability. |
| Workflow criticality | Frequency | 4 | Credible third-party evidence | Official and reviewer transcripts position Codex for recurring engineering tasks, review, refactors, and multi-agent work. |
| Workflow criticality | Operational dependence | 4 | Direct evidence | Codex can modify repos, run work in cloud environments, support PRs, and integrate with local workflows. |
| Workflow criticality | System position | 5 | Direct evidence | It sits close to code, review, branch/worktree, terminal, and PR workflows. |
| Workflow criticality | Switching cost | 3 | Inference | Skills, automations, and OpenAI account workflows add friction, but code and repos remain portable. |
| Workflow criticality | Budget durability | 4 | Direct evidence | Team credits, ChatGPT/OpenAI packaging, and engineering workflow value make budget durability stronger than prototype-only tools. |
| AI resilience tests | Model improvement test | 5 | Inference | OpenAI coding-model improvements should directly increase Codex value across implementation, review, and multi-agent workflows. |
| AI resilience tests | Wrapper risk test | 4 | Inference | Repo, worktree, PR, skills, and automations reduce thin-wrapper risk, though the code-agent category is highly competitive. |
| AI resilience tests | Agent readiness test | 5 | Direct evidence | Codex is positioned as a multi-agent coding command center with cloud environments, skills, automations, IDE, and terminal surfaces. |
| AI resilience tests | Accountability test | 2 | Inference | Codex can run checks and support review, but customers own acceptance and production consequences. |
| AI resilience tests | Outcome depth test | 4 | Direct evidence | Official evidence shows feature, refactor, migration, review, and app-building workflows, but not customer outcome ownership. |

Subtotals: proprietary advantage 17/25, workflow criticality 20/25, ai resilience tests 20/25.

### Vercel v0 - 54/75

| Category | Factor | Score | Evidence label | Rationale |
| --- | --- | --- | --- | --- |
| Proprietary advantage | Context | 3 | Direct evidence | v0 can use repos, environment variables, Vercel configuration, design mode, databases, and APIs, but customer/product context often lives outside v0. |
| Proprietary advantage | Trust | 4 | Direct evidence | Vercel security, trust, deployment protections, and enterprise controls support buyer trust. |
| Proprietary advantage | Distribution | 4 | Direct evidence | v0 benefits from Vercel distribution, templates, one-click deploy, and developer-channel reach. |
| Proprietary advantage | Judgment | 2 | Inference | v0 can generate and revise apps, but product judgment, architecture, security, and release decisions still need human review. |
| Proprietary advantage | Liability governance | 4 | Direct evidence | GitHub, PRs, deploy protection, access controls, and Vercel platform defaults strengthen governance. |
| Workflow criticality | Frequency | 3 | Inference | App and website iteration can be recurring, but v0 may not be a daily operating surface for every team. |
| Workflow criticality | Operational dependence | 4 | Direct evidence | Repo import, deploy, preview, branch, and PR workflows can become part of shipping work. |
| Workflow criticality | System position | 4 | Direct evidence | v0 links AI generation to code, GitHub, Vercel deployment, and production preview workflows. |
| Workflow criticality | Switching cost | 3 | Inference | Git portability lowers lock-in while Vercel setup, deploy habits, and generated project context create some friction. |
| Workflow criticality | Budget durability | 4 | Direct evidence | Team/business packaging and production software use support budget durability. |
| AI resilience tests | Model improvement test | 5 | Inference | Better models should increase v0 value because outputs are tied to code, deploy, debugging, and platform workflows. |
| AI resilience tests | Wrapper risk test | 3 | Inference | Vercel linkage reduces wrapper risk, but visible prompt-to-app generation remains exposed to coding agents and model-native builders. |
| AI resilience tests | Agent readiness test | 5 | Direct evidence | v0 positions itself around agentic app/website building, planning, integrations, GitHub, and deployment. |
| AI resilience tests | Accountability test | 2 | Inference | v0 can route work through code and deployment controls, but users still own production correctness. |
| AI resilience tests | Outcome depth test | 4 | Direct evidence | v0 can create, publish, and deploy working applications, but durable operations still depend on customer process. |

Subtotals: proprietary advantage 17/25, workflow criticality 18/25, ai resilience tests 19/25.

### Figma Make - 50/75

| Category | Factor | Score | Evidence label | Rationale |
| --- | --- | --- | --- | --- |
| Proprietary advantage | Context | 4 | Direct evidence | Figma Make can attach Figma designs, components, library styling, images, and team templates to prompt-to-app workflows. |
| Proprietary advantage | Trust | 4 | Direct evidence | Figma paid plans, enterprise posture, collaboration, permissions, and security docs support buyer trust. |
| Proprietary advantage | Distribution | 4 | Direct evidence | Make benefits from Figma files, collaboration graph, paid seats, Community, and designer mindshare. |
| Proprietary advantage | Judgment | 2 | Inference | Make accelerates prototypes and web apps but does not own product judgment, usability validation, or production acceptance. |
| Proprietary advantage | Liability governance | 3 | Direct evidence | Figma sharing, plan controls, and governance help, but Figma docs still place content rights and publishing responsibility on users. |
| Workflow criticality | Frequency | 3 | Credible third-party evidence | Transcripts support repeated MVP/prototype use, but not daily production operation for most teams. |
| Workflow criticality | Operational dependence | 3 | Direct evidence | Make supports previews, collaboration, code editing, backends, and publishing, but teams can still move implementation elsewhere. |
| Workflow criticality | System position | 4 | Direct evidence | It sits inside Figma where design files, components, previews, and team collaboration already happen. |
| Workflow criticality | Switching cost | 2 | Inference | Generated artifacts are useful, but teams can recreate outputs elsewhere if Figma context is not central. |
| Workflow criticality | Budget durability | 3 | Direct evidence | Paid-seat and AI-credit packaging creates a budget path tied to existing Figma use. |
| AI resilience tests | Model improvement test | 5 | Inference | Better models should improve Make because Figma owns design context, components, and collaboration surfaces. |
| AI resilience tests | Wrapper risk test | 3 | Inference | Figma context reduces wrapper risk, but prompt-to-app generation is exposed to coding agents and app builders. |
| AI resilience tests | Agent readiness test | 5 | Direct evidence | Figma documents code, packages, publishing, and MCP/code-agent handoff for Make files. |
| AI resilience tests | Accountability test | 1 | Direct evidence | Make can publish and share, but it does not absorb responsibility for production correctness, rights, compliance, or app outcomes. |
| AI resilience tests | Outcome depth test | 4 | Credible third-party evidence | Transcripts and docs support strong interactive prototype/MVP outcomes, though not sustained production operation. |

Subtotals: proprietary advantage 17/25, workflow criticality 15/25, ai resilience tests 18/25.

### Lovable - 46/75

| Category | Factor | Score | Evidence label | Rationale |
| --- | --- | --- | --- | --- |
| Proprietary advantage | Context | 3 | Direct evidence | Lovable stores project code, chat context, GitHub sync, connectors, and app-building history, but deeper customer data usually lives elsewhere. |
| Proprietary advantage | Trust | 3 | Direct evidence | Security scans, SSO, audit logs, publishing controls, and enterprise features improve trust, but production assurance remains customer-owned. |
| Proprietary advantage | Distribution | 3 | Direct evidence | Lovable has direct app-builder distribution, templates, pricing tiers, connectors, and GitHub workflow without Figma/Vercel-scale incumbent channels. |
| Proprietary advantage | Judgment | 2 | Inference | Lovable can assemble apps quickly, but product, architecture, UX, and security judgment remain substantially user-owned. |
| Proprietary advantage | Liability governance | 3 | Direct evidence | Security and audit features help governance, but docs and transcript context reinforce that users must validate critical behavior. |
| Workflow criticality | Frequency | 3 | Credible third-party evidence | Transcripts support recurring prototype and app-building use, but not universal daily operational dependence. |
| Workflow criticality | Operational dependence | 3 | Direct evidence | Publishing, hosting, GitHub sync, cloud, and connectors make it operationally useful, though users can continue elsewhere. |
| Workflow criticality | System position | 4 | Direct evidence | Lovable spans generation, app code, publishing, GitHub, cloud/backend paths, and connectors. |
| Workflow criticality | Switching cost | 3 | Direct evidence | GitHub sync/export improves portability while project history, connectors, and cloud setup create moderate friction. |
| Workflow criticality | Budget durability | 2 | Credible third-party evidence | Docs and transcripts show credit/usage-cost sensitivity, making large sustained production budgets less certain. |
| AI resilience tests | Model improvement test | 4 | Inference | Better models should improve app assembly and debugging but also lower barriers for competing app builders. |
| AI resilience tests | Wrapper risk test | 3 | Inference | Lovable has more workflow depth than a thin wrapper, but prompt-to-app generation remains crowded and model-sensitive. |
| AI resilience tests | Agent readiness test | 4 | Direct evidence | Agent mode, browser testing, connectors, GitHub sync, and cloud integration make it meaningfully agent-ready. |
| AI resilience tests | Accountability test | 2 | Direct evidence | Security scans and controls help, but Lovable does not take responsibility for production correctness or app-specific assurance. |
| AI resilience tests | Outcome depth test | 4 | Credible third-party evidence | Transcripts and docs support live full-stack app outcomes, with review and reliability caveats. |

Subtotals: proprietary advantage 14/25, workflow criticality 15/25, ai resilience tests 17/25.

### Claude Design - 44/75

| Category | Factor | Score | Evidence label | Rationale |
| --- | --- | --- | --- | --- |
| Proprietary advantage | Context | 3 | Direct evidence | Claude Design can build design systems from codebases, design files, brand assets, and web capture, but production telemetry and customer state remain outside the product. |
| Proprietary advantage | Trust | 4 | Direct evidence | It inherits Claude/Anthropic trust and paid-plan distribution, though product-specific governance evidence is still sparse. |
| Proprietary advantage | Distribution | 4 | Direct evidence | Claude Design launches inside Claude for paid subscriber tiers and benefits from Claude distribution. |
| Proprietary advantage | Judgment | 2 | Inference | It expands visual exploration but does not own brand approval, design judgment, accessibility, or production acceptance. |
| Proprietary advantage | Liability governance | 2 | Direct evidence | Admin controls and org sharing exist, but launch-stage docs leave gaps around auditability, data residency, API maturity, and production governance. |
| Workflow criticality | Frequency | 3 | Credible third-party evidence | Transcripts support repeated artifact/prototype use, but frequency varies by role and launch-stage limits. |
| Workflow criticality | Operational dependence | 2 | Inference | Evidence supports ideation, refinement, export, and handoff rather than dependence as a system of record or production control plane. |
| Workflow criticality | System position | 3 | Direct evidence | Claude Design can hand off to Claude Code and read design/code context, but does not itself own Git, deploy, or release workflows. |
| Workflow criticality | Switching cost | 1 | Inference | Outputs can be exported or recreated, and durable lock-in beyond Claude preference is not yet proven. |
| Workflow criticality | Budget durability | 3 | Direct evidence | Paid-plan access and extra usage create a budget path, while transcript evidence flags limits and cost friction. |
| AI resilience tests | Model improvement test | 5 | Direct evidence | The product is model-native and powered by Anthropic multimodal capabilities, so model improvements should raise output breadth and quality. |
| AI resilience tests | Wrapper risk test | 2 | Inference | The launch surface is easy to imitate unless design-system, collaboration, handoff, and workflow controls deepen. |
| AI resilience tests | Agent readiness test | 4 | Direct evidence | Claude Design packages handoff bundles for Claude Code and supports code-powered prototypes, but external integration evidence is early. |
| AI resilience tests | Accountability test | 2 | Inference | Customers still own correctness, rights, approval, brand fit, accessibility, and production use. |
| AI resilience tests | Outcome depth test | 4 | Direct evidence | It spans prototypes, slides, decks, one-pagers, collateral, and interactive visual artifacts, though not production operation. |

Subtotals: proprietary advantage 15/25, workflow criticality 12/25, ai resilience tests 17/25.

## Top Strengths

| Target | Strengths |
| --- | --- |
| Cursor | Deep repo/editor context, codebase indexing, terminal/tool execution, reviewable diffs, enterprise security posture, and strong daily workflow fit. |
| Claude Code | Strong terminal/IDE/GitHub positioning, MCP extensibility, project memory, real-file edits, and credible practitioner workflow evidence. |
| Codex | OpenAI distribution, repository/worktree/PR workflows, skills and automations, multi-agent command-center positioning, and strong model-improvement leverage. |
| Vercel v0 | Best visual-builder bridge into code, GitHub, previews, Vercel deploys, and production sharing. |
| Figma Make | Design-file context, components, libraries, collaboration, stakeholder buy-in workflows, publishing, and agent handoff. |
| Lovable | Fast app generation, live publishing, GitHub sync, cloud/backend path, connectors, and increasingly explicit security tooling. |
| Claude Design | Chat-native visual creation, broad artifact range, design-system setup, inline refinement, export/handoff, and Claude distribution. |

## Main Vulnerabilities

| Target | Vulnerabilities |
| --- | --- |
| Cursor | Not a visual design surface; designers need code fluency or engineering partnership, and source-code privacy/security concerns remain material. |
| Claude Code | Requires technical workflow comfort, can consume credits quickly, and is not optimized as a visual design review surface. |
| Codex | Not a visual design tool; switching costs are moderate and production acceptance still needs human review. |
| Vercel v0 | Some moat belongs to Vercel rather than v0 alone; output quality, security, and architecture still require review. |
| Figma Make | Still more design/prototype surface than production operating system; accountability remains user-owned. |
| Lovable | Credit/usage costs, production assurance, and security review remain exposed; less incumbent distribution than Figma or Vercel. |
| Claude Design | Research-preview launch, sparse operational governance, low switching cost, and transcript-reported generic output/bug/limit concerns. |

Red flags observed:

- Cursor: Accountability Vacuum for production correctness; Trust Gap for highly sensitive code unless enterprise controls are validated.
- Claude Code: Accountability Vacuum; Workflow Thinness for nontechnical designers who need a visual operating surface.
- Codex: Accountability Vacuum; Workflow Thinness for purely visual ideation workflows.
- Vercel v0: Wrapper Illusion if generated apps are treated as production assurance; Accountability Vacuum for final release quality.
- Figma Make: Accountability Vacuum and partial Workflow Thinness outside design/prototype loops.
- Lovable: Trust Gap and Wrapper Risk if users assume generated full-stack apps are production-safe by default.
- Claude Design: Workflow Thinness and Context Weakness until team governance, integrations, and live production-handoff evidence mature.

## Strategic Read

Durable layers:

- Cursor: Codebase index, editor state, rules, terminal execution, PR/review loop, and daily developer workflow position.
- Claude Code: Terminal and GitHub workflow embed, MCP ecosystem, project memory, Anthropic distribution, and handoff compatibility with Claude Design.
- Codex: OpenAI account distribution, coding models, cloud worktrees, PR/review loop, skills, automations, and multi-surface access.
- Vercel v0: Vercel deployment surface, GitHub/PR path, preview links, enterprise security, and developer distribution.
- Figma Make: Figma design context, components/libraries, collaboration graph, existing paid-seat distribution, and design-to-prototype continuity.
- Lovable: Project/chat/code context, publish path, GitHub sync, cloud/backend workflows, connectors, and security scans.
- Claude Design: Claude multimodal model surface, Claude distribution, broad visual artifact range, design-system setup, and Claude Code handoff.

Commoditizing layers:

- Prompt-to-layout generation, one-off landing pages, generic app scaffolds, static prototypes, and basic code edits are increasingly exposed to stronger foundation models and competing agents.
- Visual polish without proprietary context, review loops, governance, or production linkage is not enough to sustain resilience.

Next moves that would raise resilience:

- Cursor: Run designer-led UI-generation tests, measure design-system adherence, and validate security/privacy settings for enterprise codebases.
- Claude Code: Score with a controlled designer-to-UI implementation run and test review discipline, rollback, accessibility, and security behavior.
- Codex: Run the same UI task protocol as visual builders and separate app-generation speed from reviewed production-readiness.
- Vercel v0: Run controlled live tasks across existing repos and measure bug rate, review quality, deployment handoff, and post-launch maintenance.
- Figma Make: Prove production handoff, lifecycle governance, and sustained usefulness after engineering takes over.
- Lovable: Reduce cost friction, prove sustained maintenance workflows, and make production security guarantees more operationally concrete.
- Claude Design: Publish clearer governance/API/integration docs and run side-by-side creation-to-publish tasks against the other cohort members.

## Comparison

When scored as one cohort, coding tools lead because the rubric rewards proximity to implementation context, versioned code, terminal/test loops, and production review. That is a category effect as much as an execution effect: Cursor, Claude Code, and Codex are not visual-first design products, so their diamond marker remains as a caveat. v0 is the strongest app-builder because it bridges AI generation to Vercel deploys and GitHub. Figma Make has the strongest design-context story. Lovable is a credible app-builder but weaker on trust and cost durability. Claude Design is high-upside but early and less operationally embedded.


`comparison.ranked_targets`: Cursor (59), Claude Code (58), Codex (57), Vercel v0 (54), Figma Make (50), Lovable (46), Claude Design (44).

## Final Verdict

The same-cohort rerun moves the coding tools from contextual diamonds into the ranked set. Cursor, Claude Code, and Codex lead because they operate closest to production code, test/build loops, and reviewable changes. That does not mean they are better design products; it means the AI resilience rubric rewards owned workflow context and production control. v0 is the strongest visual/app-builder product because Vercel gives it deploy and GitHub linkage. Figma Make remains the strongest design-context surface. Lovable is a credible full-stack app builder but must prove trust, cost durability, and sustained maintenance. Claude Design remains high-upside but launch-stage: broad artifact generation and Claude Code handoff are promising, but governance, integrations, and production-operation evidence are still thin.

## Confidence Level

Overall confidence: Medium. Official evidence is current and transcript evidence now covers every product, but no controlled live task run was performed for the seven-product cohort. The largest uncertainty is designer usability for code-native tools versus their clear production-control advantage.
- Cursor: Medium-high. Official security/docs evidence is strong and transcript evidence is recent, but UI-generation-for-designers needs controlled runs.
- Claude Code: Medium-high. Official Claude Code docs and current transcripts support the score; designer-specific usability remains less proven.
- Codex: Medium-high. OpenAI official evidence is strong and transcripts cover comparative use; design-specific UI runs are still missing.
- Vercel v0: Medium. Official evidence is strong and transcripts add context, but no controlled live task run was performed.
- Figma Make: Medium-high. Official docs and transcripts align on design-context strengths; production depth is still less proven.
- Lovable: Medium. Official docs and transcripts support a credible app-builder workflow, with cost/reliability caveats.
- Claude Design: Low-medium. Official launch docs and transcripts are current, but the product is new and operational evidence is sparse.

Unknowns that would change the score most:

- Side-by-side UI-generation runs for all seven tools using the same prompts, design-system inputs, accessibility requirements, Git/deploy requirements, and review rubric.
- Evidence of enterprise adoption, auditability, and production approval workflows for Claude Design and newer app-builder surfaces.
- Longitudinal maintenance data showing whether generated apps survive real bugs, feature changes, security review, and team handoff.
- Designer-specific evidence for Codex, Cursor, and Claude Code, especially for non-engineers working from visual requirements rather than existing code issues.

## Evidence Notes

Primary official evidence used:

- Anthropic, [Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/claude-design-anthropic-labs).
- Claude Help Center, [Claude Design admin guide](https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans).
- Claude Help Center, [Claude Design subscription usage and pricing](https://support.claude.com/en/articles/14667344-claude-design-subscription-usage-and-pricing).
- Claude Help Center, [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design).
- Claude Help Center, [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design).
- Figma Help Center, [Explore Figma Make](https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make).
- Figma Developer Docs, [Intro to Figma Make](https://developers.figma.com/docs/code/intro-to-figma-make/).
- Figma, [Plans & Pricing](https://www.figma.com/pricing/).
- Figma, [Security](https://www.figma.com/security/).
- Figma Help Center, [Governance+ for Figma Enterprise](https://help.figma.com/hc/en-us/articles/31825370509591-Governance-for-Figma-Enterprise).
- Lovable Docs, [Publish your Lovable project](https://docs.lovable.dev/features/publish).
- Lovable Docs, [Connect your project to GitHub](https://docs.lovable.dev/integrations/github).
- Lovable Docs, [Lovable Cloud](https://docs.lovable.dev/integrations/cloud).
- Lovable Docs, [Security overview](https://docs.lovable.dev/features/security).
- Lovable Docs, [Audit logs](https://docs.lovable.dev/features/audit-logs).
- Lovable, [Pricing](https://lovable.dev/pricing).
- Vercel, [Introducing the new v0](https://vercel.com/blog/introducing-the-new-v0).
- v0, [Product page](https://v0.app/).
- v0 Docs, [GitHub](https://v0.app/docs/github).
- v0, [Pricing](https://v0.app/pricing).
- Vercel, [Security](https://vercel.com/security).
- Vercel, [Trust Center](https://security.vercel.com/).
- OpenAI, [Codex](https://openai.com/codex).
- OpenAI Developers, [Codex cloud](https://platform.openai.com/docs/codex/overview).
- OpenAI, [Security and privacy](https://openai.com/security).
- Cursor, [Agent](https://cursor.com/product).
- Cursor Docs, [Agent overview](https://docs.cursor.com/chat/overview).
- Cursor Docs, [Codebase indexing](https://docs.cursor.com/chat/codebase).
- Cursor Docs, [Tools](https://docs.cursor.com/en/agent/tools).
- Cursor Docs, [Model Context Protocol](https://docs.cursor.com/en/context/mcp).
- Cursor, [Pricing](https://www.cursor.com/en/pricing).
- Cursor, [Security](https://www.cursor.com/security).
- Anthropic, [Claude Code product page](https://www.anthropic.com/claude-code).
- Anthropic Docs, [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview).
- Anthropic Docs, [Connect Claude Code to tools via MCP](https://docs.anthropic.com/en/docs/claude-code/mcp).
- Anthropic Docs, [Add Claude Code to your IDE](https://docs.anthropic.com/en/docs/claude-code/ide-integrations).
- Anthropic Docs, [Claude Code GitHub Actions](https://docs.anthropic.com/en/docs/claude-code/github-actions).
- Anthropic, [Trust Center](https://trust.anthropic.com/).
- Claude, [Status](https://anthropic.statuspage.io/).
- Figma, [Status](https://status.figma.com/).
- Lovable, [Status](https://status.lovable.dev/).
- Vercel, [Status](https://www.vercel-status.com/).
- v0, [Status](https://v0-status.com/).

## Evidence Sources By Function

| Source function | Supports | Evidence weight | Stale-context handling | Representative sources |
| --- | --- | --- | --- | --- |
| Product facts and scope | Defines the product surface, user, workflow, supported outputs, and scoped target boundary for each cohort member. | Highest: current official product pages, launch posts, help centers, docs, and pricing pages. | Use current official pages at report time; do not reuse older repo summaries for product facts. | https://www.anthropic.com/news/claude-design-anthropic-labs; https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make; https://docs.lovable.dev/features/publish; https://v0.app/; https://openai.com/codex; ... |
| Workflow and integration claims | Substantiates design-system context, code/Git handoff, publishing, deployment, repository sync, terminal/editor workflows, and MCP/tool integrations. | High: official developer docs, integration docs, and product docs; supplement with transcript evidence for user-visible workflow friction. | Prefer current docs and fresh transcript pulls; avoid dated repo task evidence for this rerun. | https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design; https://developers.figma.com/docs/code/intro-to-figma-make/; https://docs.lovable.dev/integrations/github; https://v0.app/docs/github; https://platform.openai.com/docs/codex/overview; ... |
| Adoption and packaging signals | Informs distribution, budget durability, paid-plan fit, usage-limit friction, and team/enterprise packaging. | Medium-high: official pricing and packaging pages plus recent transcript context for cost/friction patterns. | Use latest pricing pages and label transcript cost comments as qualitative, not official pricing facts. | https://support.claude.com/en/articles/14667344-claude-design-subscription-usage-and-pricing; https://www.figma.com/pricing/; https://lovable.dev/pricing; https://v0.app/pricing; https://openai.com/codex; ... |
| Reliability and operational risk | Checks incident history, service disruption evidence, and whether the product can be operationally depended on. | High for official status pages; medium for transcript-reported bugs/friction. | Use current status pages and current transcripts; do not treat old incidents as current unless repeated. | https://anthropic.statuspage.io/; https://status.figma.com/; https://status.lovable.dev/; https://www.vercel-status.com/; https://v0-status.com/ |
| Trust, security, and governance | Supports trust, liability governance, admin control, auditability, source-code privacy, data handling, and enterprise readiness. | Highest: official trust centers, security docs, admin guides, and governance docs. | Use current trust/security docs and mark missing or launch-stage controls as uncertainty. | https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans; https://www.figma.com/security/; https://docs.lovable.dev/features/security; https://vercel.com/security; https://openai.com/security; ... |
| Qualitative reviewer transcript context | Captures hands-on workflow friction, output quality, cost/credit sensitivity, designer/developer ergonomics, and reviewer uncertainty for every target. | Medium: third-party qualitative evidence; official demo transcripts are used only for workflow demonstration, not independent validation. | Use transcript pull date and video dates; cross-check product facts against official sources. | https://www.youtube.com/watch?v=IkspcJdeP3U; https://www.youtube.com/watch?v=IksDIJzfXg8; https://www.youtube.com/watch?v=Zrqpq-uQBM0; https://www.youtube.com/watch?v=EUPbdk972JI; https://www.youtube.com/watch?v=lhaGyrp1vfY; ... |
| Cohort normalization and coding-tool caveats | Explains why Codex, Cursor, and Claude Code are scored in the same cohort but retained as diamond markers: they are codebase-native UI-generation tools, not visual-first design surfaces. | Analytical normalization using the same rubric, official docs, and transcript context. | Treat marker shape as a caveat, not a scoring exemption; refresh with controlled live UI-generation runs. | https://openai.com/codex; https://www.cursor.com/security; https://docs.anthropic.com/en/docs/claude-code/overview |

## YouTube Review Transcript Evidence

Purpose: the rerun uses current transcript evidence for every product to capture hands-on friction, workflow positioning, cost sensitivity, and reviewer uncertainty that official sources do not fully expose.

Method: YouTube searches were run on April 23, 2026 for review, tutorial, demo, and comparison videos for each product. Captions were pulled with `yt-dlp` and treated as qualitative evidence. Product facts were cross-checked against official sources. Transcript evidence did not count as controlled live-task evidence.

Sources:

| Target | Source | Publisher | Date | Transcript type | Evidence use |
| --- | --- | --- | --- | --- | --- |
| Claude Design | [Claude Design is NOT what you think](https://www.youtube.com/watch?v=IkspcJdeP3U) | Malewicz | 2026-04-18 | captions pulled via yt-dlp | Product-position critique and Figma-replacement skepticism. |
| Claude Design | [I Tested Claude Design and Here's the Problem (Hands on review)](https://www.youtube.com/watch?v=IksDIJzfXg8) | Matt Thorne | 2026-04-19 | automatic captions | Hands-on output and workflow friction. |
| Figma Make | [Figma Make review: game-changer or all hype?](https://www.youtube.com/watch?v=Zrqpq-uQBM0) | No Code MBA | 2025-07-09 | provided captions | Third-party review of app/prototype generation, design-context fit, and limits. |
| Figma Make | [Designing Fast MVP's for Buy-in with Figma Make](https://www.youtube.com/watch?v=EUPbdk972JI) | Jesse Showalter | 2025-10-28 | automatic captions | MVP workflow and stakeholder buy-in use case. |
| Lovable | [Lovable vs MeDo, which AI app builder actually works?](https://www.youtube.com/watch?v=lhaGyrp1vfY) | Tech With Tim | 2026-01-14 | captions pulled via yt-dlp | Comparative app-builder workflow and reliability context. |
| Lovable | [Base44 vs Lovable: which AI app builder comes out on top?](https://www.youtube.com/watch?v=0UCWNYd3Heg) | Santrel Media | 2025-12-29 | automatic captions | Comparative app-builder workflow, speed, and output quality context. |
| Vercel v0 | [Replit vs. Lovable vs. v0 | Which is best for you? (Fall 2025 review)](https://www.youtube.com/watch?v=YCaCpONZdMw) | Olivia in the City | 2025-10-31 | automatic captions | Comparative app-builder positioning and workflow tradeoffs. |
| Vercel v0 | [v0 for AI Apps | Demo](https://www.youtube.com/watch?v=ey2XShILsx0) | Vercel | 2026-01-05 | provided captions | Official demo of AI app workflow and Vercel-oriented path. |
| Codex | [Codex vs Claude Code: which AI coding agent is better?](https://www.youtube.com/watch?v=qEs7UHZSfrg) | Steve (Builder.io) | 2025-09-28 | automatic captions | Comparative code-agent workflow, strengths, and limitations. |
| Codex | [Introducing the Codex app](https://www.youtube.com/watch?v=HFM3se4lNiw) | OpenAI | 2026-02-02 | provided captions | Official Codex app workflow and product positioning. |
| Cursor | [Cursor ditches VS Code, but not everyone is happy...](https://www.youtube.com/watch?v=JSuS-zXMVwE) | Fireship | 2026-04-06 | automatic captions | Recent Cursor positioning, workflow, and adoption friction context. |
| Cursor | [Cursor vs Conductor vs Superset — Which Agentic Code Editor Is The Best?](https://www.youtube.com/watch?v=EJX9Ckqt0YU) | Your Average Tech Bro | 2026-03-13 | automatic captions | Comparative agentic editor workflow and output context. |
| Claude Code | [The Ultimate Claude Code Guide | MCP, Skills & More](https://www.youtube.com/watch?v=uogzSxOw4LU) | Tech With Tim | 2026-04-13 | captions pulled via yt-dlp | Claude Code workflow, MCP, skills, and advanced usage context. |
| Claude Code | [How I use Claude Code (Senior Software Engineer Tips)](https://www.youtube.com/watch?v=MzhIr7BfpI0) | Maddy Zhang | 2026-04-05 | automatic captions | Practitioner workflow, review discipline, and production coding context. |

Synthesis: transcripts for the coding tools converge on strong repo, terminal, review, and multi-agent workflows, while also reinforcing caveats around cost, code fluency, review burden, and source-code risk. v0 transcripts support fast deploy-oriented app creation but still show template/aesthetic bias and need for review. Figma Make transcripts support MVP and stakeholder-prototype utility inside the Figma context. Lovable transcripts support fast full-stack app creation but repeatedly surface cost/credit and production-readiness concerns. Claude Design transcripts support broad visual output and design-system ingestion while reinforcing launch-stage concerns about generic output, limits, and product-position ambiguity.

Scoring impact:

- Cursor: transcript evidence increased confidence in workflow placement and reinforced the caveats in vulnerabilities; official sources still anchor product facts and factor scores.
- Claude Code: transcript evidence increased confidence in workflow placement and reinforced the caveats in vulnerabilities; official sources still anchor product facts and factor scores.
- Codex: transcript evidence increased confidence in workflow placement and reinforced the caveats in vulnerabilities; official sources still anchor product facts and factor scores.
- Vercel v0: transcript evidence increased confidence in workflow placement and reinforced the caveats in vulnerabilities; official sources still anchor product facts and factor scores.
- Figma Make: transcript evidence increased confidence in workflow placement and reinforced the caveats in vulnerabilities; official sources still anchor product facts and factor scores.
- Lovable: transcript evidence increased confidence in workflow placement and reinforced the caveats in vulnerabilities; official sources still anchor product facts and factor scores.
- Claude Design: transcript evidence increased confidence in workflow placement and reinforced the caveats in vulnerabilities; official sources still anchor product facts and factor scores.

Limits: transcripts are third-party qualitative evidence or official demo narration. They are useful for friction and positioning, but not a substitute for controlled task runs, official product claims, or production reliability data.
