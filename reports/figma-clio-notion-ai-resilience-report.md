# Figma, Clio, and Notion AI Resilience Comparison

Prepared April 14, 2026 using the `ai_resilience_evaluator` rubric in this repository.

## Executive Summary

Clio remains the clearest resilience winner of the three. Its advantage comes less from "having AI" than from owning a legal system of record with compliance, billing, client, and workflow accountability in a regulated operating environment.

Figma still looks resilient, but for a different reason: it sits in a durable design-to-development workflow with strong distribution, shared design-system context, and increasingly explicit agent-facing infrastructure through Dev Mode, Code Connect, and MCP support. Notion has improved materially with Enterprise Search, AI Connectors, custom agents, and MCP governance, but it is still a more general coordination layer than a hard system of record, so its workflow criticality is less consistent across customers.

## 2x2 Placement

- X-axis: `Commodity Output -> Proprietary Advantage`
- Y-axis: `Nice-to-Have Utility -> Mission-Critical Workflow`
- Clio: `Resilient`
- Figma: `Resilient`
- Notion: `Convenience`, close to the resilient boundary

**Rationale:** Category structure matters here. Clio benefits from the fact that legal operations are high-stakes, compliance-heavy, and deeply workflow-bound. Figma benefits from being the default collaboration and handoff layer around product design systems, but it still depends on downstream engineering and business execution. Notion's AI surface is improving quickly, yet many deployments still function as a flexible knowledge and coordination layer rather than the system that directly owns the business outcome.

## Comparison

- Ranked targets: `Clio (68)`, `Figma (58)`, `Notion (56)`
- Relative summary: Clio leads because it owns regulated operational context and accountability. Figma comes next because it controls shared design workflow and increasingly bridges directly into code. Notion is improving fast as an agent-ready workspace and enterprise knowledge layer, but its depth still varies by team and use case.
- Key differences:
  - Clio's moat is category-specific workflow ownership.
  - Figma's moat is collaborative design context plus strong developer handoff.
  - Notion's moat is broad workspace context, but its workflow embed is less uniformly mission-critical.

## Clio

**Summary:** Clio is highly resilient to AI disruption because it owns legal workflow context, trust, billing, records, and compliance in a category where accountability matters. Stronger models are more likely to amplify the platform than displace it.

**Quadrant:** `Resilient`

| Factor | Score | Rationale |
| --- | --- | --- |
| Context | 5/5 | Direct evidence. Clio manages matters, contacts, documents, billing, intake, and firm operations in a legal-specific workflow system. |
| Trust | 5/5 | Direct evidence. Clio emphasizes enterprise-grade encryption, SOC 2 Type 2, PCI DSS compliance, HIPAA options, and legal-data protection posture. |
| Distribution | 5/5 | Direct evidence. Clio is positioned as the central hub for law firms, connects 300+ tools, and benefits from strong category trust and installed-base advantages. |
| Judgment | 4/5 | Inference. The product encodes substantial legal-workflow judgment, though final legal judgment still sits with practitioners. |
| Liability / Governance | 5/5 | Direct evidence. Permissions, audits, security posture, and recordkeeping all matter materially in legal operations. |
| Frequency | 5/5 | Inference. Law firms use matter, billing, intake, and communication systems continuously. |
| Operational Dependence | 5/5 | Inference. Practice management software is operationally central to running a modern law firm. |
| System Position | 5/5 | Direct evidence. Clio explicitly positions itself as the central hub for the firm and exposes a robust API plus large integration surface. |
| Switching Cost | 4/5 | Inference. Migration of active matters, billing history, workflows, and staff habits creates real switching friction. |
| Budget Durability | 4/5 | Inference. This spend is tied to revenue collection, compliance, and daily operations, not discretionary experimentation. |
| Model Improvement Test | 4/5 | Inference. Better models improve summarization, drafting, search, and recommendations inside a strong workflow system. |
| Wrapper Risk Test | 4/5 | Direct evidence. Clio's value is not just an assistant layer; it sits on workflow, records, payments, and compliance infrastructure. |
| Agent Readiness Test | 4/5 | Direct evidence. Open API, OAuth-based integrations, and AI product direction make it compatible with automation and agentic workflows. |
| Accountability Test | 5/5 | Direct evidence. Legal operations demand auditability, permissions, privacy, and accountable system behavior. |
| Outcome Depth Test | 4/5 | Inference. Clio affects collection, workflow execution, client handling, and deadline management, even though legal outcome quality still depends on the lawyer. |

- Proprietary advantage subtotal: `24/25`
- Workflow criticality subtotal: `23/25`
- AI resilience tests subtotal: `21/25`
- Total: `68/75`

**Top strengths**

- Owns a high-trust legal operating layer rather than a thin AI surface.
- Benefits from category-specific compliance, workflow, and system-of-record depth.
- Should gain from stronger models because the platform already holds the operational context.

**Main vulnerabilities**

- `Agent Irrelevance`: if future legal agents route around practice-management interfaces, Clio must remain the action and record layer, not just the storage layer.
- `Outcome Dependence`: legal quality still depends on human professionals, so product automation has natural limits.
- `Platform Compression Risk`: some drafting and summarization features can still commoditize.

**Strategic read**

- Durable layers: matter records, billing and payments, intake, client workflow, compliance posture, ecosystem position.
- Commoditizing layers: generic drafting, summarization, and assistant-style UX.
- Next moves: deepen AI around workflow automation, intake conversion, billing acceleration, and legal-specific action loops that stay grounded in system data and permissions.

**Final verdict:** Clio is the strongest of the group because it owns regulated workflow, trusted data, and accountability in a high-stakes category.

**Confidence:** `Medium-high` because the platform posture, workflow role, and security/integration evidence are strong, though some scoring still relies on inference about actual switching depth across firms.

**Evidence notes**

- Clio homepage: [https://www.clio.com/](https://www.clio.com/)
- Security protocols and infrastructure guide: [https://www.clio.com/wp-content/uploads/2024/04/Brochure-Guide-Security-Protocols-and-Infrastructure-Guide.pdf](https://www.clio.com/wp-content/uploads/2024/04/Brochure-Guide-Security-Protocols-and-Infrastructure-Guide.pdf)

## Figma

**Summary:** Figma is resilient because it owns shared design workflow, team coordination, design-system context, and increasingly developer and agent handoff. Its moat is not raw generative design output; it is the collaborative operating layer between design intent and shipped product.

**Quadrant:** `Resilient`

| Factor | Score | Rationale |
| --- | --- | --- |
| Context | 4/5 | Direct evidence. Figma stores shared files, components, variables, design systems, and developer handoff context. |
| Trust | 4/5 | Direct evidence. Figma provides enterprise administration, security posture, and explicit controls for AI access and content training. |
| Distribution | 5/5 | Direct evidence. Figma remains the default collaboration layer for many digital product design teams and extends into development workflows. |
| Judgment | 3/5 | Inference. The product supports design judgment and consistency, but taste and decision quality still live mostly with people. |
| Liability / Governance | 3/5 | Direct evidence. Governance and AI controls matter, but the category carries less liability than regulated systems. |
| Frequency | 4/5 | Inference. Product teams use the platform continuously across design, review, and handoff cycles. |
| Operational Dependence | 4/5 | Inference. It is important to product-delivery workflows, though teams can still switch with enough effort. |
| System Position | 4/5 | Direct evidence. Dev Mode, Code Connect, and design-system workflow make Figma more than a drawing tool. |
| Switching Cost | 4/5 | Inference. Shared libraries, component systems, collaboration habits, and developer handoff create meaningful friction. |
| Budget Durability | 4/5 | Inference. Design tooling is durable operating spend, though less protected than core back-office systems. |
| Model Improvement Test | 4/5 | Direct evidence. Better models improve prompt-to-app and code-oriented workflows when grounded in Figma context. |
| Wrapper Risk Test | 4/5 | Direct evidence. Figma's value includes collaboration, versioning, components, and developer handoff, not just generation. |
| Agent Readiness Test | 5/5 | Direct evidence. Figma explicitly supports Dev Mode, MCP, Code Connect, VS Code integration, and AI product controls. |
| Accountability Test | 2/5 | Inference. Figma informs shipped quality, but it does not own runtime execution or most business outcomes. |
| Outcome Depth Test | 3/5 | Inference. It materially affects shipping speed and consistency, but downstream impact depends on engineering and product decisions. |

- Proprietary advantage subtotal: `19/25`
- Workflow criticality subtotal: `20/25`
- AI resilience tests subtotal: `18/25`
- Total: `58/75`

**Top strengths**

- Owns collaborative design-system and handoff context that gets more useful as models improve.
- Has unusually strong distribution into both design and development workflows.
- Shows explicit agent readiness through MCP, Dev Mode, and code-oriented tooling.

**Main vulnerabilities**

- `Wrapper Illusion`: prompt-to-UI and design generation features can commoditize quickly.
- `Outcome Dependence`: design workflow matters, but product and business outcomes happen outside the tool.
- `Judgment Gap`: AI can accelerate execution without creating distinctive taste or product judgment.

**Strategic read**

- Durable layers: shared design files, component systems, collaboration, review loops, developer handoff.
- Commoditizing layers: generic mockup generation, AI-assisted layout ideation, surface-level code generation.
- Next moves: keep tightening the design-to-code loop and make Figma context indispensable to both human developers and software agents.

**Final verdict:** Figma is resilient because it sits in a durable workflow transition point between design intent and implementation, but its generative features alone are not the moat.

**Confidence:** `Medium` because official evidence is strong on product direction and controls, while some scoring still depends on judgment about long-term switching costs and workflow centrality.

**Evidence notes**

- AI settings and content training controls: [https://help.figma.com/hc/en-us/articles/17725942479127-Manage-AI-settings-and-content-training-for-your-team-or-organization](https://help.figma.com/hc/en-us/articles/17725942479127-Manage-AI-settings-and-content-training-for-your-team-or-organization)
- Dev Mode / developer workflow materials: [https://www.figma.com/dev-mode/](https://www.figma.com/dev-mode/)
- Figma security and compliance documents: [https://www.figma.com/security/](https://www.figma.com/security/)

## Notion

**Summary:** Notion is stronger than a simple LLM wrapper because it combines workspace context, structured docs and databases, AI connectors, custom agents, and external tool governance. But it is still less resilient than Clio or Figma because many deployments remain helpful coordination layers rather than mission-critical systems of execution.

**Quadrant:** `Convenience`, near the resilient boundary

| Factor | Score | Rationale |
| --- | --- | --- |
| Context | 4/5 | Direct evidence. Notion owns internal knowledge, docs, databases, relations, and connected search context across multiple tools. |
| Trust | 4/5 | Direct evidence. Permissions, auditability, connector security practices, and admin controls create meaningful trust value. |
| Distribution | 4/5 | Direct evidence. Notion has broad horizontal adoption across functions, but less category-specific lock-in than vertical systems. |
| Judgment | 3/5 | Inference. It helps organize work and research, but domain judgment usually lives in users or connected systems. |
| Liability / Governance | 3/5 | Direct evidence. Enterprise Search and MCP governance improve control, but the product does not usually carry deep external liability. |
| Frequency | 5/5 | Inference. Teams often use Notion daily for docs, planning, and knowledge workflows. |
| Operational Dependence | 3/5 | Inference. It can be central, but many teams can substitute other tools or run partial workflows elsewhere. |
| System Position | 4/5 | Direct evidence. Notion is moving from note-taking toward an orchestration and knowledge layer through connectors, custom agents, and MCP. |
| Switching Cost | 3/5 | Inference. Migration of docs and databases is painful but generally feasible. |
| Budget Durability | 4/5 | Inference. Workspace and knowledge-management spend is sticky, though still easier to consolidate than regulated systems. |
| Model Improvement Test | 5/5 | Direct evidence. Better models directly improve search, synthesis, and custom-agent performance on top of workspace context. |
| Wrapper Risk Test | 3/5 | Direct evidence. Notion has real workflow and permissions depth, but some AI experiences can still be replicated by model-native products. |
| Agent Readiness Test | 5/5 | Direct evidence. Notion MCP, custom-agent support, Enterprise Search, AI Connectors, and admin governance are explicitly agent-oriented. |
| Accountability Test | 3/5 | Direct evidence. Logs, permissions, and governance matter, but many outcomes remain advisory or collaborative rather than fully owned. |
| Outcome Depth Test | 3/5 | Inference. Notion can improve coordination and execution quality, but final business outcomes typically occur in adjacent systems. |

- Proprietary advantage subtotal: `18/25`
- Workflow criticality subtotal: `19/25`
- AI resilience tests subtotal: `19/25`
- Total: `56/75`

**Top strengths**

- Owns broad workspace context and increasingly useful cross-tool retrieval.
- Gains directly from better models because synthesis and search improve with model quality.
- Has explicit enterprise controls for external AI and MCP connections.

**Main vulnerabilities**

- `Workflow Thinness`: some teams still treat Notion as a helpful layer rather than the system that directly governs execution.
- `Wrapper Illusion`: parts of the assistant and search experience are reproducible by model-native entrants.
- `Context Weakness`: valuable context exists, but much of it is portable or duplicated across other systems.

**Strategic read**

- Durable layers: workspace knowledge graph, structured docs/databases, permissions, cross-tool retrieval, admin governance.
- Commoditizing layers: generic writing help, simple Q&A, and assistant-style summarization.
- Next moves: make agents operationally useful enough that Notion becomes the trusted coordination and action layer rather than only the knowledge layer.

**Final verdict:** Notion is increasingly resilient, but it still depends on turning broad workspace context into deeper operational ownership before it can be considered truly hard to displace.

**Confidence:** `Medium` because the current product direction is visible and well documented, but workflow depth still varies a lot by customer.

**Evidence notes**

- Notion MCP help: [https://www.notion.com/help/notion-mcp](https://www.notion.com/help/notion-mcp)
- Enterprise Search security and privacy practices: [https://www.notion.com/help/enterprise-search-security-and-privacy-practices](https://www.notion.com/help/enterprise-search-security-and-privacy-practices)
- Custom agents and workspace AI materials: [https://www.notion.com/product/ai](https://www.notion.com/product/ai)
