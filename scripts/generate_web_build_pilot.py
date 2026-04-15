#!/usr/bin/env python3

import csv
import json
import math
import statistics
from collections import Counter
from copy import deepcopy
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "studies" / "web-build-study"
EVIDENCE_DIR = OUT / "evidence-packets"
RATER_DIR = OUT / "rater-scorecards"
INDIVIDUAL_DIR = OUT / "individual-reports"


AXES = {
    "x": "Commodity Output -> Proprietary Advantage",
    "y": "Nice-to-Have Utility -> Mission-Critical Workflow",
}

FACTORS = [
    ("proprietary_advantage", "context", "Context"),
    ("proprietary_advantage", "trust", "Trust"),
    ("proprietary_advantage", "distribution", "Distribution"),
    ("proprietary_advantage", "judgment", "Judgment"),
    ("proprietary_advantage", "liability_governance", "Liability / Governance"),
    ("workflow_criticality", "frequency", "Frequency"),
    ("workflow_criticality", "operational_dependence", "Operational Dependence"),
    ("workflow_criticality", "system_position", "System Position"),
    ("workflow_criticality", "switching_cost", "Switching Cost"),
    ("workflow_criticality", "budget_durability", "Budget Durability"),
    ("ai_resilience_tests", "model_improvement_test", "Model Improvement Test"),
    ("ai_resilience_tests", "wrapper_risk_test", "Wrapper Risk Test"),
    ("ai_resilience_tests", "agent_readiness_test", "Agent Readiness Test"),
    ("ai_resilience_tests", "accountability_test", "Accountability Test"),
    ("ai_resilience_tests", "outcome_depth_test", "Outcome Depth Test"),
]

RATERS = {
    "desk_rater_alpha": {
        "label": "Desk Rater Alpha",
        "lens": "More conservative on governance, switching cost, and outcome ownership.",
    },
    "desk_rater_beta": {
        "label": "Desk Rater Beta",
        "lens": "Balanced baseline reading of the evidence packet.",
    },
    "desk_rater_gamma": {
        "label": "Desk Rater Gamma",
        "lens": "More positive on agent leverage and model-improvement upside.",
    },
}

TARGETS = [
    {
        "slug": "figma-sites",
        "name": "Figma Sites",
        "scope": "Scoped to Figma's website design and publishing product rather than the full Figma suite.",
        "summary": "Figma Sites still benefits from Figma's collaborative context and distribution, but the observed task phase showed weaker workflow fit than the desk read assumed. In this protocol it behaved more like an adjacent publishing surface than a durable prompt-first site operating tool.",
        "quadrant_placement": "Right of center on proprietary advantage, modestly above the workflow midpoint",
        "quadrant_rationale": "Figma Sites retains inherited platform strength from Figma, but the observed product path was template-first or code-component-first and the Starter plan blocked publish, which reduced confidence in day-two governed workflow ownership.",
        "plot": {"x": 68, "y": 61, "label_dx": 14, "label_dy": -10},
        "confidence": {
            "level": "medium",
            "reason": "Official materials plus direct task evidence now make the workflow-fit gap clearer: Sites inherits strong platform context, but the observed build and publish path did not validate a strong prompt-first operating role.",
        },
        "top_strengths": [
            "Shared components, variables, and file context carry directly into the website workflow.",
            "Figma's distribution into design and product teams makes Sites easier to adopt than a net-new site tool.",
            "The product sits close to Dev Mode and other handoff surfaces instead of being only a one-shot generator.",
        ],
        "main_vulnerabilities": [
            "Runtime ownership and business outcomes still happen outside the tool.",
            "Publishing and governance depth look lighter than Webflow or Wix Studio.",
            "AI-assisted generation inside Sites is easy for competitors to imitate.",
        ],
        "strategic_read": {
            "durable_layers": [
                "Shared files, components, and variable context",
                "Review and collaboration workflow",
                "Direct path from design artifact to published site",
                "Installed-base distribution across product teams",
            ],
            "commoditizing_layers": [
                "Template-like landing page generation",
                "Generic copy and image assistance",
                "Surface-level website drafting",
            ],
            "next_moves": [
                "Deepen CMS, publishing governance, and site operations so Sites is harder to route around.",
                "Make agent-assisted updates safe, reversible, and grounded in shared design-system rules.",
            ],
        },
        "final_verdict": "Figma Sites remains more resilient than a pure AI website wrapper because of Figma's broader context and distribution, but the empirical task phase lowered the workflow-depth read and moved it behind Figma Make in this cohort.",
        "evidence_notes": [
            {"title": "Figma Sites product page", "url": "https://www.figma.com/sites/"},
            {"title": "Figma Sites launch post", "url": "https://www.figma.com/blog/introducing-figma-sites/"},
            {"title": "Figma pricing", "url": "https://www.figma.com/pricing/"},
            {"title": "Figma security", "url": "https://www.figma.com/security/"},
        ],
        "evidence_packet": {
            "scope": "Website creation and publishing inside Figma, including collaborative design context and the publish surface exposed through Sites.",
            "buyer_user": "Primary buyers are design, brand, and product teams already paying for Figma. Primary users are designers working with developers and marketers on shared website artifacts.",
            "pricing_packaging": "Evidence indicates Sites is packaged alongside broader Figma plans rather than sold as a standalone operating platform, which helps distribution but limits how much the product itself controls budget durability.",
            "ai_features": "AI upside comes from adjacent Figma AI and Make workflows rather than a unique model moat inside Sites itself. The current durable layer is the shared file and design-system context around the site.",
            "apis_integrations": "Sites benefits from Figma's broader design-to-code ecosystem, including Dev Mode adjacency and the same account surface that exposes connectors and MCP-related features elsewhere in the pricing stack.",
            "governance": "Publishing sits inside Figma's team and organization permissions, but public evidence still shows lighter website-specific governance than Webflow or Wix Studio.",
            "trust_security": "Figma publishes a mature security posture and organization controls, which lifts trust relative to newer AI-native builders.",
            "publishing_workflow": "The product explicitly promises design, prototype, and publish in one surface. That is stronger than a draft-only tool, but the long-term moat depends on deeper site operations after the initial publish step.",
        },
        "desk_factors": {
            "context": {"score": 4, "label": "Direct evidence", "rationale": "Figma Sites reuses shared components, variables, and file context from the design workflow instead of starting from a blank website canvas."},
            "trust": {"score": 4, "label": "Direct evidence", "rationale": "Sites inherits Figma's organization-level security and account controls, which matter for teams already standardizing on the broader platform."},
            "distribution": {"score": 5, "label": "Direct evidence", "rationale": "Figma already sits inside many product and brand design teams, so Sites can piggyback on an existing collaboration footprint."},
            "judgment": {"score": 3, "label": "Inference", "rationale": "The tool preserves design intent well, but scarce website strategy and performance judgment still live largely with the team using it."},
            "liability_governance": {"score": 3, "label": "Direct evidence", "rationale": "Team and org controls exist, but public evidence still points to lighter publishing governance than the more operations-heavy web platforms."},
            "frequency": {"score": 4, "label": "Inference", "rationale": "Teams that already work in Figma can use Sites in recurring launch and update cycles, though not every Figma user publishes sites regularly."},
            "operational_dependence": {"score": 3, "label": "Inference", "rationale": "Sites can matter materially for launch velocity, but it is not yet the default operating system for public web programs in the way deeper incumbents can be."},
            "system_position": {"score": 4, "label": "Direct evidence", "rationale": "The product sits at the handoff point between design intent and publishable website output rather than only at ideation time."},
            "switching_cost": {"score": 3, "label": "Inference", "rationale": "Teams with established Figma systems gain reuse, but the published site layer remains portable enough that migration risk is still moderate."},
            "budget_durability": {"score": 4, "label": "Inference", "rationale": "Sites benefits from Figma's existing seat budget, which makes it more durable than a standalone experimental AI subscription."},
            "model_improvement_test": {"score": 4, "label": "Inference", "rationale": "Better models should improve iteration speed and content generation inside the same shared design context instead of bypassing it entirely."},
            "wrapper_risk_test": {"score": 3, "label": "Inference", "rationale": "Sites is deeper than a generator because it carries team context and design systems, but the web publishing surface is still young enough to face copycat pressure."},
            "agent_readiness_test": {"score": 4, "label": "Direct evidence", "rationale": "The broader Figma stack already exposes strong design-to-code and agent-facing surfaces, which helps Sites fit agent-assisted workflows."},
            "accountability_test": {"score": 2, "label": "Inference", "rationale": "The product influences what gets shipped, but it does not own uptime, conversion, or downstream business execution once the site is live."},
            "outcome_depth_test": {"score": 3, "label": "Inference", "rationale": "Sites can accelerate launches and improve consistency, but real business outcomes still depend on external content, traffic, and experimentation loops."},
        },
        "rater_overrides": {
            "desk_rater_alpha": {"liability_governance": -1, "operational_dependence": -1},
            "desk_rater_beta": {},
            "desk_rater_gamma": {"model_improvement_test": 1, "agent_readiness_test": 1},
        },
        "empirical_adjustments": {
            "liability_governance": {"delta": -1, "rationale": "Observed task evidence. The live product path exposed lighter publish control than the desk read assumed, and Starter-plan restrictions blocked a real publish outcome in both runs."},
            "operational_dependence": {"delta": -1, "rationale": "Observed task evidence. The task phase did not show Sites acting like a central operating layer for recurring website work; it behaved more like an adjacent surface."},
            "system_position": {"delta": -1, "rationale": "Observed task evidence. The blank-site path routed into code-component Make and the alternate path was template-first, which weakened the direct system-of-action read for this protocol."},
            "agent_readiness_test": {"delta": -1, "rationale": "Observed task evidence. Agent-adjacent potential remained theoretical in the task phase because the observed site workflow did not expose a strong brief-driven or change-driven agent path."},
            "accountability_test": {"delta": -1, "rationale": "Observed task evidence. The product influenced drafts but did not validate accountable publish or governed follow-up workflow under the observed plan and product path."},
            "outcome_depth_test": {"delta": -1, "rationale": "Observed task evidence. Because creation and publish both blocked on workflow fit or plan limits, the task phase did not support the stronger business-outcome read from the desk pass."},
        },
        "empirical_task_read": "Both observed runs hit the same product-path mismatch: blank-site creation routed toward Make code components while the alternate path was template-first, and Starter blocked publish. That evidence reduced the workflow-depth read despite Figma's broader platform strength.",
    },
    {
        "slug": "figma-make",
        "name": "Figma Make",
        "scope": "Scoped to Figma's prompt-to-app and prompt-to-interface builder rather than the broader collaborative design platform.",
        "summary": "Figma Make moved up materially after the task phase because it was the cleanest end-to-end performer in the cohort: it generated quickly, handled governed revision cleanly, and published versioned artifacts without breaking workflow continuity.",
        "quadrant_placement": "Right of center on proprietary advantage, near the workflow midpoint",
        "quadrant_rationale": "Make still is not a full web operating platform, but the observed runs validated more durable workflow ownership than the desk pass initially credited, especially around governed revision, versioning, and publishable artifacts.",
        "plot": {"x": 58, "y": 44, "label_dx": 12, "label_dy": 18},
        "confidence": {
            "level": "medium-high",
            "reason": "Current pricing and help materials are now reinforced by direct task evidence: Make completed all six observed rows cleanly, which materially reduced uncertainty about workflow depth relative to the original desk-only read.",
        },
        "top_strengths": [
            "Prompting can pull in Figma styling context, connectors, and MCP-friendly workflows.",
            "The observed task phase validated clean in-place revision, versioning, and publishable output rather than only first-draft speed.",
            "Distribution into existing Figma teams makes experimentation cheaper than adopting a new standalone builder.",
        ],
        "main_vulnerabilities": [
            "Workflow depth still looks closer to prototyping than to governed production operations.",
            "Accountability for shipped outcomes remains external.",
            "Prompt-to-app experiences are under intense model-driven commoditization pressure.",
        ],
        "strategic_read": {
            "durable_layers": [
                "Figma library and styling context",
                "Connector and documentation grounding",
                "Agent-friendly handoff to coding workflows",
            ],
            "commoditizing_layers": [
                "Prompt-to-app generation itself",
                "Standalone prototype drafting",
                "Generic UI scaffolding",
            ],
            "next_moves": [
                "Attach Make outputs to governed review, deployment, and change-management loops.",
                "Turn connectors and context grounding into durable workflow ownership rather than a faster demo surface.",
            ],
        },
        "final_verdict": "Figma Make is still not a full web operating platform, but the task phase showed it already behaves like a more durable creation-and-change surface than the desk pass assumed, lifting it above Figma Sites and Framer in the empirical-adjusted ranking.",
        "evidence_notes": [
            {"title": "Figma Make product page", "url": "https://www.figma.com/make/"},
            {"title": "Figma pricing", "url": "https://www.figma.com/pricing/"},
            {"title": "What is Figma?", "url": "https://help.figma.com/hc/en-us/articles/14563969806359-What-is-Figma"},
            {"title": "Figma security", "url": "https://www.figma.com/security/"},
        ],
        "evidence_packet": {
            "scope": "Prompt-to-code and prompt-to-interface creation inside Figma Make, including connectors, MCP support, and code-sharing hooks named on the pricing page.",
            "buyer_user": "Primary users are product designers, PMs, and engineers exploring ideas quickly. Buyers are usually existing Figma teams rather than a new budget owner.",
            "pricing_packaging": "Make appears inside the broader Figma pricing surface, where the packaging emphasizes connectors, file sharing, and agent support more than standalone production hosting economics.",
            "ai_features": "This is the most overtly AI-native offering in the Figma cohort slice. The key question is whether grounding in Figma context is enough to keep the product from collapsing into generic prompt-to-app generation.",
            "apis_integrations": "Official pricing materials explicitly call out MCP support, Make connectors, and the ability to share code with AI coding agents, which is unusually strong agent posture for this category.",
            "governance": "Governance inherits from the broader Figma account, but public evidence does not yet show deep production approvals, rollback, or publish controls as the main value proposition.",
            "trust_security": "Figma's general security posture helps trust, but Make still needs stronger evidence that teams rely on it for accountable production outcomes rather than exploratory generation.",
            "publishing_workflow": "Help and pricing materials position Make as a way to turn ideas and existing designs into functioning web apps and interfaces. That is useful, but the durable moat depends on what happens after generation.",
        },
        "desk_factors": {
            "context": {"score": 3, "label": "Direct evidence", "rationale": "Make can pull in library styling and existing Figma context, but the generated app itself is not yet a uniquely proprietary record layer."},
            "trust": {"score": 4, "label": "Direct evidence", "rationale": "The product benefits from Figma's broader enterprise posture and AI settings controls instead of asking teams to trust a brand-new builder in isolation."},
            "distribution": {"score": 4, "label": "Direct evidence", "rationale": "Figma's installed base gives Make privileged distribution into teams already living inside the platform."},
            "judgment": {"score": 2, "label": "Inference", "rationale": "The tool speeds up exploration, but scarce product, engineering, and business judgment still sits with the human team reviewing the output."},
            "liability_governance": {"score": 2, "label": "Inference", "rationale": "Public evidence emphasizes creation speed and connectors more than governed approvals, controls, or accountable production change management."},
            "frequency": {"score": 3, "label": "Inference", "rationale": "Make can become part of recurring prototyping loops, but it is not yet clearly a daily mission-critical workflow for most teams."},
            "operational_dependence": {"score": 2, "label": "Inference", "rationale": "Teams can route around Make with coding agents or other rapid builders if it is unavailable, which limits dependence today."},
            "system_position": {"score": 3, "label": "Direct evidence", "rationale": "The product sits in the idea-to-interface path and can hand work to coding agents, but it does not yet control the broader site or app operating stack."},
            "switching_cost": {"score": 2, "label": "Inference", "rationale": "Prompt histories and context matter, yet the underlying generation workflow remains portable to other tools and model-native environments."},
            "budget_durability": {"score": 3, "label": "Inference", "rationale": "Make benefits from existing Figma budgets, but the feature itself still competes with many adjacent AI build surfaces for attention and spend."},
            "model_improvement_test": {"score": 5, "label": "Direct evidence", "rationale": "The product should improve directly as underlying models and connectors get better because generation quality and speed are central to its proposition."},
            "wrapper_risk_test": {"score": 2, "label": "Inference", "rationale": "Make has useful grounding layers, but the visible user value is still close to a prompt-to-app experience that stronger commodity models can pressure quickly."},
            "agent_readiness_test": {"score": 5, "label": "Direct evidence", "rationale": "Pricing explicitly names MCP support, connectors, and sharing code with AI coding agents, which is unusually strong evidence of agent readiness."},
            "accountability_test": {"score": 1, "label": "Inference", "rationale": "Make does not own the final runtime, support burden, or business outcome when generated software fails after handoff."},
            "outcome_depth_test": {"score": 2, "label": "Inference", "rationale": "The product can shorten exploration and prototyping, but most durable commercial outcomes still depend on downstream engineering, launch, and operations."},
        },
        "rater_overrides": {
            "desk_rater_alpha": {"trust": -1, "switching_cost": -1, "accountability_test": -1},
            "desk_rater_beta": {},
            "desk_rater_gamma": {"model_improvement_test": 0, "outcome_depth_test": 1, "system_position": 1},
        },
        "empirical_adjustments": {
            "liability_governance": {"delta": 1, "rationale": "Observed task evidence. Both runs preserved versioned change flow and publish artifacts, which supports a stronger governed-change read than the desk pass gave it."},
            "operational_dependence": {"delta": 1, "rationale": "Observed task evidence. The tool supported the whole create-revise-publish loop in the study rather than only a disposable prototype step."},
            "system_position": {"delta": 1, "rationale": "Observed task evidence. Make held the center of the workflow across creation, revision, version history, and web or community publication."},
            "wrapper_risk_test": {"delta": 1, "rationale": "Observed task evidence. The live runs showed more durable value in structured change flow and context-preserving revision than a simple prompt-to-app wrapper read would imply."},
            "outcome_depth_test": {"delta": 1, "rationale": "Observed task evidence. The tool materially affected speed, completeness, and handoff quality across all three tasks instead of only improving ideation."},
        },
        "empirical_task_read": "Figma Make was the only offering to complete both governed-revision runs cleanly while also publishing versioned artifacts in both passes. That performance validated more workflow depth, governance, and wrapper resistance than the desk baseline assumed.",
    },
    {
        "slug": "lovable",
        "name": "Lovable",
        "scope": "Scoped to Lovable's AI app-building product and cloud deployment workflow rather than any future broader platform ambitions.",
        "summary": "Lovable remained one of the fastest tools in the cohort and the task phase validated stronger real workflow depth than the desk pass assumed. But free-credit and publish-permission friction kept the resilience read mixed rather than upgraded overall.",
        "quadrant_placement": "Near the center-right, below center on workflow criticality",
        "quadrant_rationale": "Lovable owns a useful prompt, repo, and deploy loop, yet the workflow still looks easier to substitute than the deeper governance, CMS, and multi-stakeholder operating layers in the cohort leaders.",
        "plot": {"x": 52, "y": 40, "label_dx": 14, "label_dy": -10},
        "confidence": {
            "level": "medium",
            "reason": "Lovable's public posture is still lighter than incumbent platforms, but the observed task runs confirmed that the tool can handle real create, revise, and handoff work. Confidence remains constrained by plan-credit and publish-permission blockers.",
        },
        "top_strengths": [
            "Fast prompt-to-app creation plus one-click deploy is directly aligned with stronger models.",
            "The product explicitly syncs with GitHub, which is more durable than a sandboxed demo builder.",
            "Docs show ongoing platform work around plans, roles, and branded emails instead of only a chat toy.",
        ],
        "main_vulnerabilities": [
            "Public governance and trust posture are much lighter than incumbent platforms.",
            "Free-credit ceilings and publish permissions created real packaging friction during the task phase.",
            "The visible customer value is close to commodity app generation, which raises wrapper risk.",
        ],
        "strategic_read": {
            "durable_layers": [
                "Repository sync and deploy loop",
                "Integrated cloud app workflow",
                "Growing workspace and collaboration surface",
            ],
            "commoditizing_layers": [
                "Prompt-driven UI and code generation",
                "Chat-centric assistant UX",
                "General-purpose scaffolding",
            ],
            "next_moves": [
                "Deepen governance, collaboration, and operations so Lovable owns more than generation speed.",
                "Turn deploy, auth, and integration loops into harder-to-replicate workflow depth.",
            ],
        },
        "final_verdict": "Lovable validated more real workflow depth than the desk pass initially credited, especially around prompt-first generation and in-place revision, but packaging and permission friction kept the overall resilience score mixed rather than improved.",
        "evidence_notes": [
            {"title": "Lovable pricing", "url": "https://lovable.dev/pricing"},
            {"title": "Lovable docs", "url": "https://docs.lovable.dev/"},
            {"title": "Lovable plans and credits", "url": "https://docs.lovable.dev/introduction/plans-and-credits"},
            {"title": "Lovable branded emails", "url": "https://docs.lovable.dev/features/custom-emails"},
            {"title": "Lovable pentesting blog post", "url": "https://lovable.dev/blog/announcing-pentesting"},
            {"title": "Lovable DPA", "url": "https://enterprise.lovable.dev/documents/Lovable_DPA_17Nov2025_Signed.pdf"},
        ],
        "evidence_packet": {
            "scope": "Prompt-to-web-app generation, GitHub sync, cloud deploy, and the surrounding workspace/account surface exposed in Lovable's public docs.",
            "buyer_user": "Primary users are founders, indie builders, and small product teams that want a faster path from prompt to working app. Buyers often overlap with users.",
            "pricing_packaging": "Public pricing and plan docs show a credit-metered model plus Pro, Business, and enterprise-style surfaces, which supports monetization but still looks more usage-tied than workflow-tied.",
            "ai_features": "Lovable is overtly agent-native: the product promise is to act like a superhuman full-stack engineer, which helps speed but also raises strong wrapper-risk questions.",
            "apis_integrations": "Official messaging highlights GitHub sync, deployment, and docs-driven product expansion. Public integration depth still looks narrower than Wix Studio, Webflow, or even Figma's connector story.",
            "governance": "Plans docs mention workspace roles and permissions, but public evidence remains thin on deep approvals, rollback governance, auditability, or large-team controls.",
            "trust_security": "Lovable now publishes pentesting messaging and an enterprise DPA, which is useful progress, but the trust surface is still lighter and newer than incumbent platform peers.",
            "publishing_workflow": "One-click deploy is a genuine system-of-action capability. The question is whether the deploy loop becomes a durable operating layer or remains interchangeable generation plus hosting convenience.",
        },
        "desk_factors": {
            "context": {"score": 3, "label": "Direct evidence", "rationale": "Lovable accumulates project context and repo-linked state, but the core app logic is often portable and not yet a proprietary data moat."},
            "trust": {"score": 2, "label": "Direct evidence", "rationale": "Pentesting and DPA materials help, yet public trust and governance depth still trail the more mature incumbents in the cohort."},
            "distribution": {"score": 3, "label": "Inference", "rationale": "Lovable has meaningful brand momentum in the AI builder space, but it does not yet control a pre-existing enterprise distribution channel."},
            "judgment": {"score": 2, "label": "Inference", "rationale": "The product accelerates implementation, but durable design, architecture, and business judgment remain external to the tool."},
            "liability_governance": {"score": 2, "label": "Inference", "rationale": "Current public evidence does not show Lovable owning deep approvals, auditability, or accountable governance for production web changes."},
            "frequency": {"score": 3, "label": "Inference", "rationale": "Builders can use Lovable intensively during creation sprints, but recurring day-two usage is less established than on heavier operating platforms."},
            "operational_dependence": {"score": 2, "label": "Inference", "rationale": "If Lovable disappeared, many teams could continue from GitHub or move to another coding agent stack, which limits dependence."},
            "system_position": {"score": 2, "label": "Direct evidence", "rationale": "Lovable is part of the create-and-deploy path, but it does not yet look like the central operating system for a broader website or app program."},
            "switching_cost": {"score": 2, "label": "Inference", "rationale": "Repository sync helps continuity, yet that same portability makes the workflow easier to substitute than a more closed operating layer."},
            "budget_durability": {"score": 3, "label": "Inference", "rationale": "The product can earn recurring spend from active builders, but the budget still competes with many adjacent AI coding and builder tools."},
            "model_improvement_test": {"score": 4, "label": "Direct evidence", "rationale": "Lovable benefits directly as model quality and agent reliability improve because generation speed and breadth sit at the core of the offering."},
            "wrapper_risk_test": {"score": 2, "label": "Inference", "rationale": "A lot of visible value is still close to the model layer and assistant UX, which creates meaningful wrapper pressure."},
            "agent_readiness_test": {"score": 4, "label": "Direct evidence", "rationale": "The product is explicitly agent-oriented and already bridges into deploy and repo workflows instead of stopping at text generation."},
            "accountability_test": {"score": 2, "label": "Inference", "rationale": "Lovable can help ship software, but final responsibility for correctness, security, and business impact still lands on the team using it."},
            "outcome_depth_test": {"score": 3, "label": "Inference", "rationale": "The tool can materially change shipping velocity, though durable commercial outcomes still depend on downstream maintenance, distribution, and operations."},
        },
        "rater_overrides": {
            "desk_rater_alpha": {"trust": -1, "distribution": -1, "switching_cost": -1},
            "desk_rater_beta": {},
            "desk_rater_gamma": {"model_improvement_test": 1, "agent_readiness_test": 1, "outcome_depth_test": 1},
        },
        "empirical_adjustments": {
            "system_position": {"delta": 1, "rationale": "Observed task evidence. Lovable handled real create, revise, and handoff work inside the same project more convincingly than the desk baseline implied."},
            "budget_durability": {"delta": -1, "rationale": "Observed task evidence. The daily free-credit ceiling materially constrained revision work in one live pass, which supports a weaker budget-durability read than the desk baseline."},
        },
        "empirical_task_read": "Lovable validated the prompt-first part of the thesis: it created strong first drafts quickly and completed one full governed revision cleanly. But a daily credit wall and publish permission blocker limited how much durable workflow ownership the study could credit.",
    },
    {
        "slug": "webflow",
        "name": "Webflow",
        "scope": "Scoped to Webflow's current website platform including CMS, hosting, APIs, and AI features.",
        "summary": "Webflow's empirical read mostly validated the desk score: it owns a real governed website operating stack with strong publish and review surfaces, while the observed failures were driven more by free-tier packaging and workspace state than by missing platform capability.",
        "quadrant_placement": "Upper-right, close to center",
        "quadrant_rationale": "Webflow controls meaningful workflow and platform surface area for web operations, but its visible AI layer is still partially commoditizable.",
        "plot": {"x": 72, "y": 66, "label_dx": 14, "label_dy": -8},
        "confidence": {
            "level": "medium-high",
            "reason": "Official evidence on platform breadth and governance is now reinforced by live publish observations. Remaining uncertainty is mostly about how much the free-tier blockers distorted the revision task, not about whether Webflow owns a real operating layer.",
        },
        "top_strengths": [
            "Real website operating layer with CMS, hosting, and publishing workflow",
            "Benefits from better models inside the platform",
            "Strong developer and agent-facing infrastructure",
        ],
        "main_vulnerabilities": [
            "AI generation features are easy to replicate",
            "Underlying content and structure are only moderately proprietary",
            "Lower-end site building is exposed to AI-native entrants",
        ],
        "strategic_read": {
            "durable_layers": [
                "CMS architecture",
                "Hosting and publishing",
                "Workflow governance",
                "Permissions",
                "Developer and agent surface",
            ],
            "commoditizing_layers": [
                "Generic AI generation",
                "Layout drafting",
                "Simple site creation",
            ],
            "next_moves": [
                "Push deeper into structured content and experimentation",
                "Make agent-safe publishing and website operations the core moat",
            ],
        },
        "final_verdict": "Webflow's empirical read mostly confirmed the desk score: it is defensible because of workflow ownership and platform breadth, even though AI-facing features remain exposed and the observed task blockers came from packaging rather than missing capability.",
        "evidence_notes": [
            {"title": "Webflow developer platform and APIs", "url": "https://developers.webflow.com/"},
            {"title": "Webflow Trust Center", "url": "https://trust.webflow.com/"},
            {"title": "Webflow AI", "url": "https://webflow.com/ai"},
            {"title": "Webflow pricing", "url": "https://webflow.com/pricing"},
        ],
        "evidence_packet": {
            "scope": "Website operations in Webflow, including CMS, hosting, publishing, APIs, and AI-assisted creation.",
            "buyer_user": "Primary buyers are marketing, web, and design-led growth teams. Primary users include marketers, designers, and developers working on the public website.",
            "pricing_packaging": "Webflow has explicit platform pricing and enterprise motion rather than only being bundled inside a broader design suite.",
            "ai_features": "Webflow markets AI directly, but the durable layer is still the governed site operating stack rather than the generative features themselves.",
            "apis_integrations": "The developer platform materially strengthens agent and system positioning by exposing APIs and developer workflows around the site layer.",
            "governance": "Publishing controls, permissions, and enterprise posture are core parts of the product story and help separate Webflow from a simple generator.",
            "trust_security": "The Trust Center and enterprise posture provide stronger public trust evidence than most AI-native builders in the cohort.",
            "publishing_workflow": "Webflow sits directly in structured content, publish, hosting, and iterative site operations, which is why it scores well on workflow depth.",
        },
        "desk_factors": {
            "context": {"score": 3, "label": "Direct evidence", "rationale": "Webflow stores site structure, CMS schemas, publishing state, and increasingly app and cloud deployment context, but much underlying content remains portable."},
            "trust": {"score": 4, "label": "Direct evidence", "rationale": "Enterprise customers can access deeper security documentation, and the platform emphasizes governance and security posture."},
            "distribution": {"score": 4, "label": "Direct evidence", "rationale": "Webflow has meaningful ecosystem reach across the website lifecycle and a large developer and app surface."},
            "judgment": {"score": 3, "label": "Inference", "rationale": "The platform improves execution quality and speed, but does not clearly own scarce domain judgment."},
            "liability_governance": {"score": 4, "label": "Direct evidence", "rationale": "Permissions, publishing controls, enterprise security posture, and workflow governance matter for public-facing web operations."},
            "frequency": {"score": 4, "label": "Inference", "rationale": "Web and marketing teams use the platform continuously or recurrently."},
            "operational_dependence": {"score": 4, "label": "Inference", "rationale": "The public website is commercially important for many businesses even if it is not always existential."},
            "system_position": {"score": 4, "label": "Direct evidence", "rationale": "Webflow sits directly in content creation, CMS, hosting, publishing, and now supports broader developer and cloud workflows."},
            "switching_cost": {"score": 3, "label": "Inference", "rationale": "Migration pain exists, but strong alternatives remain available."},
            "budget_durability": {"score": 4, "label": "Inference", "rationale": "Website platform spend is usually durable within modern go-to-market stacks."},
            "model_improvement_test": {"score": 4, "label": "Direct evidence", "rationale": "Better models should improve site operations, app generation, optimization, and content workflows inside Webflow."},
            "wrapper_risk_test": {"score": 3, "label": "Direct evidence", "rationale": "AI-facing features are exposed to commoditization, but the overall platform is deeper than an AI wrapper."},
            "agent_readiness_test": {"score": 5, "label": "Direct evidence", "rationale": "Webflow now exposes APIs across data, designer, and browser workflows, plus an MCP server and broader developer platform."},
            "accountability_test": {"score": 3, "label": "Inference", "rationale": "Webflow governs publishing and execution workflows, but does not fully own the business result."},
            "outcome_depth_test": {"score": 4, "label": "Inference", "rationale": "It can materially affect traffic, conversion, and operational web velocity, but broader GTM performance still depends on external strategy."},
        },
        "rater_overrides": {
            "desk_rater_alpha": {"switching_cost": -1, "accountability_test": -1},
            "desk_rater_beta": {},
            "desk_rater_gamma": {"model_improvement_test": 1},
        },
        "empirical_adjustments": {},
        "empirical_task_read": "Webflow published and shared handoff artifacts cleanly in both observed passes, which validated the platform-depth thesis. The task-2 failures were real, but they looked like free-plan or workspace-state blockers rather than evidence that the underlying workflow surface is thin.",
    },
    {
        "slug": "framer",
        "name": "Framer",
        "scope": "Scoped to Framer's website creation, CMS, publishing, AI, and plugin workflow rather than the broader design ecosystem around it.",
        "summary": "Framer's follow-on rerun validated its official AI site-generation path and same-project AI revisions, but that path was not surfaced cleanly in the first authenticated passes. Its empirical-adjusted score now sits in the middle because the core AI workflow is real while discoverability and launch reliability still look weaker than the strongest platforms.",
        "quadrant_placement": "Right of center, near the workflow midpoint",
        "quadrant_rationale": "Framer retains real CMS and publish ownership, and the follow-on Wireframer rerun showed a usable AI creation and revision path. The remaining weakness is not absence of AI, but inconsistent discoverability and a lighter publish-governance surface than Webflow or Wix Studio.",
        "plot": {"x": 64, "y": 56, "label_dx": 14, "label_dy": 18},
        "confidence": {
            "level": "medium",
            "reason": "Public documentation plus direct rerun evidence now verify that Framer's official AI, CMS, and publish story is real. Confidence is still capped because the path was easy to miss in the authenticated workspace and the public publish check looked less stable than the in-editor result.",
        },
        "top_strengths": [
            "Real CMS and publish workflow make Framer more than a one-shot AI site builder.",
            "Plugins, collaboration roles, and custom-domain publishing add operating depth.",
            "AI features benefit directly from stronger models without being the only story.",
        ],
        "main_vulnerabilities": [
            "The official AI path worked when entered through Wireframer, but it was not surfaced reliably from the first authenticated project routes.",
            "Governance and accountability still look lighter than Webflow or Wix Studio.",
            "Outcome ownership remains limited because Framer does not control the broader business stack.",
        ],
        "strategic_read": {
            "durable_layers": [
                "CMS collections and content workflow",
                "Publish plus custom-domain surface",
                "Plugin ecosystem and collaboration model",
            ],
            "commoditizing_layers": [
                "Generic AI site drafting",
                "Template-heavy landing page generation",
                "Surface-level copy and layout assistance",
            ],
            "next_moves": [
                "Deepen permissions, multi-site operations, and agent-aware change workflows.",
                "Keep moving from polished site creation toward more durable operating ownership.",
            ],
        },
        "final_verdict": "Framer remains in the cohort on the strength of a validated Wireframer flow, real in-project AI revision, and real publish mechanics. It still trails the strongest platforms because AI discoverability and launch reliability looked less consistent than the in-editor generation experience.",
        "evidence_notes": [
            {"title": "Framer pricing", "url": "https://www.framer.com/pricing/"},
            {"title": "Framer AI", "url": "https://www.framer.com/ai"},
            {"title": "Framer Developers: CMS", "url": "https://www.framer.com/developers/cms"},
            {"title": "Framer custom-domain SSL help", "url": "https://www.framer.com/help/articles/do-i-have-to-setup-ssl-when-adding-a-custom-domain-to-a-framer-project/"},
            {"title": "Framer roles and permissions", "url": "https://www.framer.com/help/articles/member-roles-and-permissions/"},
            {"title": "Framer security", "url": "https://www.framer.com/security"},
            {"title": "Framer Plugins 3.3", "url": "https://www.framer.com/updates/plugins-3-3"},
        ],
        "evidence_packet": {
            "scope": "Framer's website workflow including CMS, collaboration, AI site tooling, plugins, and publish/custom-domain support.",
            "buyer_user": "Primary buyers are designers, agencies, and marketing-led teams that want visually polished websites without a heavier developer-controlled stack.",
            "pricing_packaging": "Framer has explicit website pricing rather than only being a seat add-on, which supports budget durability if the site workflow is important to the team.",
            "ai_features": "Official AI messaging shows Framer investing in faster website creation, but the more durable layer is its combined CMS and publish flow rather than AI alone.",
            "apis_integrations": "Framer's CMS developer docs and plugin updates show real extensibility, though the ecosystem still looks narrower than Wix Studio or Webflow developer surfaces.",
            "governance": "Roles and permissions exist and the plugin system now respects them better, but public evidence still suggests a lighter governance model than the heavier operating platforms.",
            "trust_security": "Framer publishes security and custom-domain SSL documentation, which improves trust, but the enterprise control story is not as heavy as Wix Studio or Webflow.",
            "publishing_workflow": "Framer clearly owns publish, hosting, and custom domains, which is why it stays above simple generator tools on workflow criticality.",
        },
        "desk_factors": {
            "context": {"score": 3, "label": "Direct evidence", "rationale": "Framer stores site structure and CMS collections, but most underlying website content remains portable and not deeply proprietary."},
            "trust": {"score": 3, "label": "Direct evidence", "rationale": "Security and SSL documentation provide real trust evidence, though the public enterprise-control layer still looks lighter than incumbent leaders."},
            "distribution": {"score": 4, "label": "Inference", "rationale": "Framer has strong mindshare among designers and agencies building modern marketing sites, giving it better distribution than newer AI-native builders."},
            "judgment": {"score": 3, "label": "Inference", "rationale": "Framer can preserve polished design intent, but durable strategy and performance judgment still sits largely with the team using it."},
            "liability_governance": {"score": 3, "label": "Direct evidence", "rationale": "Roles, permissions, and publish controls exist, but public evidence still points to a lighter governance posture than Webflow or Wix Studio."},
            "frequency": {"score": 4, "label": "Inference", "rationale": "Teams running active websites can use Framer repeatedly for launches, edits, and CMS updates."},
            "operational_dependence": {"score": 3, "label": "Inference", "rationale": "Framer can become central for some teams, but it still looks more replaceable than the deeper operating stacks in the cohort."},
            "system_position": {"score": 4, "label": "Direct evidence", "rationale": "Framer owns content modeling, site editing, and publish-to-domain behavior rather than stopping at design files."},
            "switching_cost": {"score": 3, "label": "Inference", "rationale": "CMS and publish workflow create friction, but many of the assets and patterns remain movable enough that lock-in is moderate."},
            "budget_durability": {"score": 4, "label": "Inference", "rationale": "When Framer runs a public site, the budget can be durable because the website itself remains commercially important."},
            "model_improvement_test": {"score": 4, "label": "Direct evidence", "rationale": "AI tooling should improve directly as models get better, and those gains can compound inside an existing CMS and publish workflow."},
            "wrapper_risk_test": {"score": 3, "label": "Inference", "rationale": "Framer is not just a wrapper because it already owns publishing and CMS, but its most visible AI layers are still exposed to copycat pressure."},
            "agent_readiness_test": {"score": 3, "label": "Inference", "rationale": "Plugins and CMS developer surfaces help, but public evidence is lighter on explicit agent-facing posture than Figma Make, Webflow, or Wix Studio."},
            "accountability_test": {"score": 2, "label": "Inference", "rationale": "Framer controls what gets published, yet it does not own the broader business result or long-tail runtime accountability."},
            "outcome_depth_test": {"score": 3, "label": "Inference", "rationale": "The product can influence launch speed and website quality, but durable commercial results still rely on traffic, content, and experimentation outside Framer."},
        },
        "rater_overrides": {
            "desk_rater_alpha": {"trust": -1, "liability_governance": -1},
            "desk_rater_beta": {},
            "desk_rater_gamma": {"model_improvement_test": 1, "agent_readiness_test": 1},
        },
        "empirical_adjustments": {
            "accountability_test": {"delta": -1, "rationale": "Observed task evidence. Publish mechanics and View Changes were real, but the public launch spot check looked weaker than the in-editor canvas result, so accountable launch quality still reads lighter than the best platforms."},
            "outcome_depth_test": {"delta": -1, "rationale": "Observed task evidence. Framer generated and revised the site successfully, but the live launch artifact still looked less reliable than the in-editor workflow, which limits the business-outcome read."},
        },
        "empirical_task_read": "The follow-on rerun entered Framer through Wireframer and validated the official AI path that earlier authenticated passes missed. Framer generated a Northstar page quickly, then applied the governed revision prompt in the same project through Ask Framer. Publish and View Changes were real, but the public launch artifact looked less stable than the in-editor canvas result.",
    },
    {
        "slug": "wix-studio",
        "name": "Wix Studio",
        "scope": "Scoped to Wix Studio as the agency and enterprise web platform, including AI tooling, dev docs, security, and multi-site management surfaces.",
        "summary": "Wix Studio remains the strongest resilience candidate in this cohort because the task phase largely validated the desk thesis: its broad platform surface, publish flow, and enterprise positioning still outweigh the fragmentation seen in AI-assisted revision.",
        "quadrant_placement": "Upper-right, furthest right in the cohort",
        "quadrant_rationale": "Wix Studio owns a wider operating footprint than the other cohort members: AI tools, site editing, business solutions, developer docs, security, and multi-site management all push it closer to a durable web operating platform.",
        "plot": {"x": 76, "y": 70, "label_dx": 14, "label_dy": 18},
        "confidence": {
            "level": "medium-high",
            "reason": "Official platform evidence is now reinforced by observed publish behavior and real site-operation surface. Some uncertainty remains around how much the Aria revision fragmentation matters in higher-tier or more structured workflows.",
        },
        "top_strengths": [
            "Broad platform surface spanning agencies, enterprise, security, and developer workflows",
            "Explicit AI tooling lives inside a larger system of action rather than replacing it",
            "Developer docs and multi-site management support stronger long-term workflow depth",
        ],
        "main_vulnerabilities": [
            "Visible AI features are still reproducible by competitors",
            "Lower-end website creation remains exposed to commodity builders",
            "Some underlying content and site structure stay portable even when the platform surface is broad",
        ],
        "strategic_read": {
            "durable_layers": [
                "Agency and enterprise platform breadth",
                "Developer docs and API surface",
                "Security and reliability posture",
                "Multi-site management and business solutions",
            ],
            "commoditizing_layers": [
                "Generic AI drafting",
                "Simple visual site generation",
                "One-off brochure-site creation",
            ],
            "next_moves": [
                "Keep turning AI assistance into safer, more governed site operations instead of surface-level generation.",
                "Strengthen structured content, agent-safe edits, and multi-site controls to widen the moat.",
            ],
        },
        "final_verdict": "Wix Studio remains the strongest resilience candidate in this cohort because the empirical task phase still pointed to the broadest web operating footprint, even though its AI-assisted revision flow fragmented under the study protocol.",
        "evidence_notes": [
            {"title": "Wix Studio home", "url": "https://www.wix.com/studio"},
            {"title": "Wix Studio AI", "url": "https://www.wix.com/studio/ai"},
            {"title": "Wix Studio pricing", "url": "https://www.wix.com/studio/plans"},
            {"title": "Wix Studio security", "url": "https://www.wix.com/studio/infrastructure/security"},
            {"title": "Wix developer docs", "url": "https://dev.wix.com/"},
        ],
        "evidence_packet": {
            "scope": "Wix Studio's agency and enterprise web platform, including AI tools, developer docs, security posture, and operational infrastructure.",
            "buyer_user": "Primary buyers include agencies, larger web teams, and enterprises. Users span designers, developers, marketers, and operators managing multiple sites.",
            "pricing_packaging": "Wix Studio has explicit pricing and enterprise positioning, which supports budget durability and suggests the product is meant to be a real operating platform rather than a lightweight add-on.",
            "ai_features": "AI is present, but the more durable story is that AI sits inside a broad platform with business solutions, developer extensibility, and operational controls.",
            "apis_integrations": "Wix's developer docs point to a large API and app surface for building custom websites, apps, and headless experiences, which improves system position and agent relevance.",
            "governance": "The Studio site explicitly calls out enterprise security, performance, and multi-site management, which is stronger governance language than most peers in this category publish publicly.",
            "trust_security": "Security is a first-class public surface for Studio, which materially strengthens trust scores for a web platform comparison.",
            "publishing_workflow": "Studio is not just about design. The product is framed as a web platform for agencies and enterprises, which supports a stronger publish and operate thesis than more generation-centric peers.",
        },
        "desk_factors": {
            "context": {"score": 4, "label": "Direct evidence", "rationale": "Wix Studio owns site structure, business-solution connections, and broader platform context beyond a single design artifact."},
            "trust": {"score": 4, "label": "Direct evidence", "rationale": "Wix Studio publicly foregrounds security and enterprise-grade infrastructure, which strengthens trust relative to lighter AI-native builders."},
            "distribution": {"score": 5, "label": "Direct evidence", "rationale": "Wix has broad existing market reach and Studio is packaged for agencies and enterprises rather than needing to build distribution from scratch."},
            "judgment": {"score": 3, "label": "Inference", "rationale": "The platform can encode workflow and infrastructure choices, but scarce website strategy and creative judgment still remain largely external."},
            "liability_governance": {"score": 4, "label": "Direct evidence", "rationale": "Public messaging around security, reliability, and multi-site management supports a stronger governance story than most peers in this cohort."},
            "frequency": {"score": 4, "label": "Inference", "rationale": "Agencies and enterprise teams managing multiple sites can use Studio continuously, not only during initial build phases."},
            "operational_dependence": {"score": 4, "label": "Inference", "rationale": "Once Studio is running an important web program, teams are likely to depend on it for recurring operational work."},
            "system_position": {"score": 4, "label": "Direct evidence", "rationale": "The platform sits across building, publishing, business solutions, and developer extensions rather than only at the mockup layer."},
            "switching_cost": {"score": 4, "label": "Inference", "rationale": "Multi-site and enterprise use cases create more migration friction than lighter tools, even if underlying content is still somewhat portable."},
            "budget_durability": {"score": 4, "label": "Inference", "rationale": "Agency and enterprise site-platform spend is typically more durable than experimental AI tooling budgets."},
            "model_improvement_test": {"score": 4, "label": "Inference", "rationale": "Stronger models should improve Studio's AI surfaces, but the broader platform still matters because AI sits inside a larger system of action."},
            "wrapper_risk_test": {"score": 3, "label": "Inference", "rationale": "Wix Studio is clearly deeper than a wrapper, yet its visible AI layers are still subject to the same commoditization pressure affecting the category."},
            "agent_readiness_test": {"score": 4, "label": "Direct evidence", "rationale": "The developer docs and platform breadth suggest Studio can support agent-mediated workflows better than tools with only a narrow UI surface."},
            "accountability_test": {"score": 3, "label": "Inference", "rationale": "Studio controls meaningful site operations, but it still does not own the full business outcome after launch."},
            "outcome_depth_test": {"score": 4, "label": "Inference", "rationale": "Because the platform spans publishing, management, and business solutions, Studio can influence operational and commercial outcomes more deeply than lighter builders."},
        },
        "rater_overrides": {
            "desk_rater_alpha": {"switching_cost": -1, "accountability_test": -1},
            "desk_rater_beta": {},
            "desk_rater_gamma": {"model_improvement_test": 1, "agent_readiness_test": 1},
        },
        "empirical_adjustments": {},
        "empirical_task_read": "Wix Studio published cleanly in both passes and continued to look like a broad operating platform, which validated the desk ranking. The main empirical weakness was not lack of platform surface but AI-workflow fragmentation during task 2, where Aria suggested adjacent app actions instead of directly applying the governed revision.",
    },
]


TASKS = [
    {
        "id": "task_1",
        "name": "Net-new marketing page",
        "timebox_minutes": 45,
        "prompt": "Create a responsive marketing page for Northstar Pediatrics, a subscription pediatric clinic. The page must include a hero, three benefit blocks, a pricing section, a testimonial, and a clear call to action for booking an intro call.",
        "acceptance": [
            "Desktop and mobile layouts are usable.",
            "All five required sections exist.",
            "Brand tone feels healthcare-trustworthy rather than generic startup.",
            "The result is ready for stakeholder review without extra polishing outside the tool.",
        ],
    },
    {
        "id": "task_2",
        "name": "Governed revision and reuse",
        "timebox_minutes": 60,
        "prompt": "Update the same project so the page supports three membership tiers, pulls testimonial and FAQ content from reusable structured content when available, adds a clinician profile section, and changes the primary CTA from booking to join waitlist.",
        "acceptance": [
            "The update is applied without rebuilding the page from scratch.",
            "Reusable components, symbols, variables, or CMS content are used where the tool supports them.",
            "The design system stays visually consistent after the revision.",
            "The operator can identify a clear change history or reusable structure rather than only manual edits.",
        ],
    },
    {
        "id": "task_3",
        "name": "Publish or handoff",
        "timebox_minutes": 60,
        "prompt": "Prepare the project for launch or developer handoff. Publish or generate the best available launch artifact, connect or simulate a custom domain or staging step if the product supports it, and document how a teammate or agent would safely make the next change.",
        "acceptance": [
            "There is a clear publish, preview, export, or handoff artifact.",
            "The operator can point to versioning, roles, rollback, or approval behavior if the tool supports it.",
            "API, connector, repo, or agent hooks are exercised when available.",
            "A follow-up change path is documented well enough for another operator to continue safely.",
        ],
    },
]

TASK_ORDERS = {
    "operator_a": {
        "task_1": ["lovable", "framer", "webflow", "figma-make", "wix-studio", "figma-sites"],
        "task_2": ["webflow", "figma-sites", "wix-studio", "lovable", "framer", "figma-make"],
        "task_3": ["wix-studio", "webflow", "figma-sites", "framer", "figma-make", "lovable"],
    },
    "operator_b": {
        "task_1": ["wix-studio", "figma-sites", "lovable", "webflow", "framer", "figma-make"],
        "task_2": ["framer", "figma-make", "webflow", "wix-studio", "figma-sites", "lovable"],
        "task_3": ["figma-sites", "lovable", "framer", "wix-studio", "webflow", "figma-make"],
    },
}

OPERATOR_PROFILES = {
    "operator_a": "Planned operator profile: design-forward frontend generalist who can use no-code tools comfortably.",
    "operator_b": "Planned operator profile: frontend engineer comfortable with component systems, APIs, and handoff workflows.",
}


def ensure_dirs():
    for path in (OUT, EVIDENCE_DIR, RATER_DIR, INDIVIDUAL_DIR):
        path.mkdir(parents=True, exist_ok=True)


def clean_block(text):
    lines = dedent(text).splitlines()
    normalized = [line[8:] if line.startswith("        ") else line for line in lines]
    return "\n".join(normalized).strip() + "\n"


def score_shape(flat_scores):
    result = {
        "proprietary_advantage": {},
        "workflow_criticality": {},
        "ai_resilience_tests": {},
    }
    for category, factor, _label in FACTORS:
        result[category][factor] = flat_scores[factor]
    for category in ("proprietary_advantage", "workflow_criticality", "ai_resilience_tests"):
        result[category]["subtotal"] = sum(result[category][factor] for cat, factor, _ in FACTORS if cat == category)
    result["total"] = (
        result["proprietary_advantage"]["subtotal"]
        + result["workflow_criticality"]["subtotal"]
        + result["ai_resilience_tests"]["subtotal"]
    )
    return result


def factor_notes(target, mode="empirical"):
    notes = deepcopy(target["desk_factors"])
    if mode == "desk":
        return notes

    for factor, adjustment in target.get("empirical_adjustments", {}).items():
        notes[factor]["score"] = max(1, min(5, notes[factor]["score"] + adjustment["delta"]))
        notes[factor]["label"] = f"{notes[factor]['label']} + Observed task evidence"
        notes[factor]["rationale"] = f"{notes[factor]['rationale']} {adjustment['rationale']}"
    return notes


def flat_scores(target, mode="empirical"):
    notes = factor_notes(target, mode=mode)
    return {factor: notes[factor]["score"] for _category, factor, _label in FACTORS}


def target_scores(target, mode="empirical"):
    return score_shape(flat_scores(target, mode=mode))


def apply_overrides(base_scores, overrides):
    updated = deepcopy(base_scores)
    for factor, delta in overrides.items():
        updated[factor] = max(1, min(5, updated[factor] + delta))
    return updated


def target_report_json(target):
    scores = target_scores(target, mode="empirical")
    return {
        "target_name": target["name"],
        "summary": target["summary"],
        "quadrant": {
            "x_axis": AXES["x"],
            "y_axis": AXES["y"],
            "placement": target["quadrant_placement"],
            "rationale": target["quadrant_rationale"],
        },
        "scores": scores,
        "top_strengths": target["top_strengths"],
        "main_vulnerabilities": target["main_vulnerabilities"],
        "strategic_read": target["strategic_read"],
        "final_verdict": target["final_verdict"],
        "confidence": target["confidence"],
        "evidence_notes": [source["url"] for source in target["evidence_notes"]],
    }


def render_report_markdown(target):
    scores = target_scores(target, mode="empirical")
    notes = factor_notes(target, mode="empirical")
    rows = []
    for _category, factor, label in FACTORS:
        item = notes[factor]
        rows.append(f"| {label} | {item['score']}/5 | {item['label']}. {item['rationale']} |")

    evidence_lines = "\n".join(
        f"- {source['title']}: [{source['url']}]({source['url']})" for source in target["evidence_notes"]
    )
    strengths = "\n".join(f"- {item}" for item in target["top_strengths"])
    vulnerabilities = "\n".join(f"- {item}" for item in target["main_vulnerabilities"])
    durable = "\n".join(f"  - {item}" for item in target["strategic_read"]["durable_layers"])
    commoditizing = "\n".join(f"  - {item}" for item in target["strategic_read"]["commoditizing_layers"])
    next_moves = "\n".join(f"  - {item}" for item in target["strategic_read"]["next_moves"])

    return clean_block(
        f"""\
        # {target["name"]} AI Resilience Evaluation

        Prepared April 14, 2026 using the `ai_resilience_evaluator` rubric in this repository.

        ## Executive Summary

        {target["summary"]}

        ## 2x2 Placement

        - X-axis: `{AXES["x"]}`
        - Y-axis: `{AXES["y"]}`
        - Placement: `{target["quadrant_placement"]}`

        **Rationale:** {target["quadrant_rationale"]}

        ## Score Table

        | Factor | Score | Rationale |
        | --- | --- | --- |
        {chr(10).join(rows)}

        - Proprietary advantage subtotal: `{scores["proprietary_advantage"]["subtotal"]}/25`
        - Workflow criticality subtotal: `{scores["workflow_criticality"]["subtotal"]}/25`
        - AI resilience tests subtotal: `{scores["ai_resilience_tests"]["subtotal"]}/25`
        - Total: `{scores["total"]}/75`

        ## Top Strengths

        {strengths}

        ## Main Vulnerabilities

        {vulnerabilities}

        ## Strategic Read

        - Durable layers:
        {durable}
        - Commoditizing layers:
        {commoditizing}
        - Next moves:
        {next_moves}

        ## Empirical Task Read

        {target["empirical_task_read"]}

        ## Final Verdict

        {target["final_verdict"]}

        ## Confidence Level

        `{target["confidence"]["level"].capitalize()}`. {target["confidence"]["reason"]}

        ## Evidence Notes

        {evidence_lines}
        """
    )


def render_evidence_packet(target):
    sections = []
    for key, title in (
        ("scope", "Scope"),
        ("buyer_user", "Buyer And User"),
        ("pricing_packaging", "Pricing And Packaging"),
        ("ai_features", "AI Features"),
        ("apis_integrations", "APIs And Integrations"),
        ("governance", "Governance"),
        ("trust_security", "Trust And Security"),
        ("publishing_workflow", "Publishing Workflow"),
    ):
        sections.append(f"## {title}\n\n{target['evidence_packet'][key]}\n")

    sources = "\n".join(
        f"- {source['title']}: [{source['url']}]({source['url']})" for source in target["evidence_notes"]
    )
    return clean_block(
        f"""\
        # {target["name"]} Evidence Packet

        Prepared April 14, 2026 for the web-build empirical pilot. This packet uses a shared current-evidence window of the previous 12 months when change-sensitive materials are available, plus older durable product context where needed.

        ## Working Scope

        {target["scope"]}

        {chr(10).join(sections)}
        ## Source List

        {sources}
        """
    )


def rater_scorecard(target, rater_id):
    base = flat_scores(target, mode="desk")
    overrides = target["rater_overrides"][rater_id]
    adjusted = apply_overrides(base, overrides)
    shaped = score_shape(adjusted)
    return {
        "target_slug": target["slug"],
        "target_name": target["name"],
        "rater_id": rater_id,
        "rater_label": RATERS[rater_id]["label"],
        "rater_lens": RATERS[rater_id]["lens"],
        "scope": target["scope"],
        "scores": shaped,
        "factor_notes": {
            factor: {
                "score": adjusted[factor],
                "evidence_label": target["desk_factors"][factor]["label"],
                "rationale": target["desk_factors"][factor]["rationale"],
            }
            for _category, factor, _label in FACTORS
        },
        "limitations": "This is a structured desk-research rating pass from one shared evidence packet, not an independent blinded human rater.",
    }


def variance_bundle(scorecards):
    totals = [card["scores"]["total"] for card in scorecards]
    bundle = {
        "total_mean": round(sum(totals) / len(totals), 2),
        "total_min": min(totals),
        "total_max": max(totals),
        "total_stddev": round(statistics.pstdev(totals), 2),
    }
    by_category = {}
    for category in ("proprietary_advantage", "workflow_criticality", "ai_resilience_tests"):
        values = [card["scores"][category]["subtotal"] for card in scorecards]
        by_category[category] = {
            "mean": round(sum(values) / len(values), 2),
            "min": min(values),
            "max": max(values),
            "stddev": round(statistics.pstdev(values), 2),
        }
    max_disagreement = 0
    factor_disagreements = {}
    for _category, factor, _label in FACTORS:
        values = [card["factor_notes"][factor]["score"] for card in scorecards]
        spread = max(values) - min(values)
        factor_disagreements[factor] = spread
        max_disagreement = max(max_disagreement, spread)
    bundle["category_variance"] = by_category
    bundle["factor_spread"] = factor_disagreements
    bundle["max_factor_disagreement"] = max_disagreement
    return bundle


def factor_score_rows(target, scorecards):
    rows = []
    desk_notes = factor_notes(target, mode="desk")
    desk_scores = target_scores(target, mode="desk")
    empirical_notes = factor_notes(target, mode="empirical")
    empirical_scores = target_scores(target, mode="empirical")
    for _category, factor, _label in FACTORS:
        rows.append(
            {
                "target_slug": target["slug"],
                "target_name": target["name"],
                "score_set": "desk_consensus",
                "rater_id": "desk_consensus",
                "rater_lens": "Desk-only adjudicated consensus before empirical task adjustment",
                "category": _category,
                "factor": factor,
                "score": desk_notes[factor]["score"],
                "evidence_label": desk_notes[factor]["label"],
                "rationale": desk_notes[factor]["rationale"],
                "category_subtotal": desk_scores[_category]["subtotal"],
                "total_score": desk_scores["total"],
            }
        )
        rows.append(
            {
                "target_slug": target["slug"],
                "target_name": target["name"],
                "score_set": "empirical_consensus",
                "rater_id": "empirical_consensus",
                "rater_lens": "Empirical-adjusted consensus after live task evidence",
                "category": _category,
                "factor": factor,
                "score": empirical_notes[factor]["score"],
                "evidence_label": empirical_notes[factor]["label"],
                "rationale": empirical_notes[factor]["rationale"],
                "category_subtotal": empirical_scores[_category]["subtotal"],
                "total_score": empirical_scores["total"],
            }
        )
    for card in scorecards:
        for _category, factor, _label in FACTORS:
            note = card["factor_notes"][factor]
            rows.append(
                {
                    "target_slug": target["slug"],
                    "target_name": target["name"],
                    "score_set": "rater",
                    "rater_id": card["rater_id"],
                    "rater_lens": card["rater_lens"],
                    "category": _category,
                    "factor": factor,
                    "score": note["score"],
                    "evidence_label": note["evidence_label"],
                    "rationale": note["rationale"],
                    "category_subtotal": card["scores"][_category]["subtotal"],
                    "total_score": card["scores"]["total"],
                }
            )
    return rows


def task_metric_rows():
    rows = []
    task_lookup = {task["id"]: task for task in TASKS}
    for operator_id, task_order_map in TASK_ORDERS.items():
        for task_id, order in task_order_map.items():
            task = task_lookup[task_id]
            for run_order, slug in enumerate(order, start=1):
                target = next(item for item in TARGETS if item["slug"] == slug)
                rows.append(
                    {
                        "operator_id": operator_id,
                        "operator_profile": OPERATOR_PROFILES[operator_id],
                        "task_id": task_id,
                        "task_name": task["name"],
                        "offering_slug": slug,
                        "offering_name": target["name"],
                        "run_order": run_order,
                        "timebox_minutes": task["timebox_minutes"],
                        "status": "pending_execution",
                        "access_status": "requires_authenticated_product_access",
                        "time_to_first_acceptable_output_minutes": "",
                        "time_to_completion_minutes": "",
                        "requirements_pass_rate": "",
                        "manual_fix_count": "",
                        "structured_reuse": "",
                        "publish_success": "",
                        "governance_support": "",
                        "agent_or_api_leverage": "",
                        "notes": "",
                    }
                )
    return rows


def load_task_metric_rows(path):
    scaffold_rows = task_metric_rows()
    if not path.exists():
        return scaffold_rows

    with path.open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if not rows:
        return scaffold_rows

    fieldnames = list(scaffold_rows[0].keys())
    normalized = []
    for row in rows:
        normalized.append({field: row.get(field, "") for field in fieldnames})
    return normalized


def summarize_task_metrics(task_rows):
    status_counts = Counter((row.get("status") or "unknown") for row in task_rows)
    pending_runs = status_counts.get("pending_execution", 0)
    completed_runs = status_counts.get("completed_observed", 0)
    blocked_runs = sum(
        count
        for status, count in status_counts.items()
        if status not in {"pending_execution", "completed_observed"}
    )
    observed_runs = completed_runs + blocked_runs

    if observed_runs == 0:
        summary_status = "scheduled_not_executed"
        phase_status = "pending_authenticated_access"
        display_summary = f"{len(task_rows)} scheduled task rows are scaffolded but unfilled."
    elif pending_runs:
        summary_status = "partial_empirical_runs_recorded"
        phase_status = "partial_observed_task_evidence"
        display_summary = (
            f"{observed_runs} observed task rows are recorded and {pending_runs} rows remain pending."
        )
    else:
        summary_status = "empirical_runs_recorded"
        phase_status = "observed_task_evidence_recorded"
        display_summary = (
            f"{completed_runs} completed observations and {blocked_runs} blocker observations are recorded across "
            f"{len(task_rows)} task rows."
        )

    per_task = {}
    for task in TASKS:
        counts = Counter(row["status"] for row in task_rows if row["task_id"] == task["id"])
        per_task[task["id"]] = dict(sorted(counts.items()))

    return {
        "path": "task_metrics.csv",
        "row_count": len(task_rows),
        "status": summary_status,
        "phase_status": phase_status,
        "display_summary": display_summary,
        "completed_runs": completed_runs,
        "blocked_runs": blocked_runs,
        "pending_runs": pending_runs,
        "status_counts": dict(sorted(status_counts.items())),
        "task_status_counts": per_task,
        "method_note": (
            "operator_b is the primary live task pass. operator_a rows are a same-agent replication used to widen "
            "empirical coverage and stress-test the rubric, not to claim independent operator validity."
        ),
    }


def build_study_metadata(task_summary):
    notes = [
        "Per-offering narrative and JSON reports reuse the repository's existing single-target contract.",
        "The three rater passes are structured desk-rater simulations from a shared evidence packet, not blinded external humans.",
    ]

    if task_summary["status"] == "scheduled_not_executed":
        notes.append("Task metrics are scheduled but unfilled because this environment lacks product credentials for full empirical execution.")
    else:
        notes.extend(
            [
                f"Task metrics now include live observed runs: {task_summary['display_summary']}",
                task_summary["method_note"],
                "The primary ranking is now an empirical-adjusted consensus, while desk-only totals remain preserved for audit and comparison.",
                "Observed blockers are treated as empirical evidence about workflow fit, packaging, or governance rather than discarded as operator noise.",
            ]
        )

    return {
        "study_name": "Web-build empirical pilot for AI resilience",
        "prepared_on": "2026-04-14",
        "study_type": "pilot-validity",
        "unit_of_analysis": "product_offering",
        "evidence_window": "Most recent 12 months for change-sensitive official materials, plus older durable context when necessary",
        "cohort": [target["name"] for target in TARGETS],
        "phase_status": {
            "evidence_packets": "complete",
            "structured_desk_raters": "complete",
            "consensus_scoring": "complete",
            "operator_protocol": "complete",
            "operator_task_runs": task_summary["phase_status"],
        },
        "primary_hypothesis": "Higher resilience scores should align more strongly with governed revision, publishing, and handoff workflows than with raw first-draft speed.",
        "notes": notes,
    }


def build_validity_read(task_summary):
    validity = {
        "desk_phase_read": "The desk-research phase already ranks platform-like web operating tools above faster-but-thinner AI-native generators.",
        "task_phase_status": task_summary["phase_status"],
    }

    if task_summary["status"] == "scheduled_not_executed":
        validity.update(
            {
                "expected_outlier": "Lovable and Figma Make are expected to win on first-draft speed while trailing on governed revision and publish-or-handoff depth.",
                "next_required_step": "Run the 36 scheduled tool sessions in task_metrics.csv and record empirical measurements.",
            }
        )
        return validity

    validity.update(
        {
            "empirical_read": "The observed task data supports the rubric's central claim more than it refutes it: prompt-first speed and durable workflow ownership separate meaningfully once the study moves from generation into governed revision and publish-or-handoff steps.",
            "observed_findings": [
                "Figma Make was the cleanest end-to-end performer in the observed runs, completing all six rows with perfect requirement pass rates and visible versioning plus publish artifacts. That moved it above Figma Sites and Framer in the empirical-adjusted ranking.",
                "Lovable validated the desk-phase expectation that AI-native builders can win on first-draft speed and in-place revision, but it also surfaced plan-credit and publish-permission friction that kept governance shallower than the raw generation quality suggests.",
                "Webflow and Wix Studio validated the rubric's emphasis on publish workflow and operational surface. Both produced strong publish outcomes, while their main failures were packaging or revision-flow friction rather than inability to ship.",
                "Figma Sites underperformed because the live product path we exercised was plan-limited and code-component-first. Framer ended up more mixed: the first authenticated passes missed its AI path, but a follow-on Wireframer rerun validated real AI generation and same-project revision. That keeps Framer below the leaders, but no longer for 'no AI path' reasons.",
            ],
            "next_required_step": "Optional: add independent human reruns or higher-tier plan access if you want cleaner separation between product capability and plan-packaging blockers.",
        }
    )
    return validity


def desk_baseline_totals():
    return {
        target["slug"]: {
            "target_name": target["name"],
            "total": target_scores(target, mode="desk")["total"],
        }
        for target in TARGETS
    }


def empirical_adjustment_summary():
    summary = {}
    for target in TARGETS:
        desk_notes = factor_notes(target, mode="desk")
        empirical_notes = factor_notes(target, mode="empirical")
        changed = []
        for _category, factor, label in FACTORS:
            if factor in target.get("empirical_adjustments", {}):
                adjustment = target["empirical_adjustments"][factor]
                changed.append(
                    {
                        "factor": factor,
                        "label": label,
                        "delta": adjustment["delta"],
                        "desk_score": desk_notes[factor]["score"],
                        "empirical_score": empirical_notes[factor]["score"],
                        "rationale": adjustment["rationale"],
                    }
                )

        desk_total = target_scores(target, mode="desk")["total"]
        empirical_total = target_scores(target, mode="empirical")["total"]
        summary[target["slug"]] = {
            "target_name": target["name"],
            "desk_total": desk_total,
            "empirical_total": empirical_total,
            "total_delta": empirical_total - desk_total,
            "changed_factors": changed,
            "empirical_task_read": target["empirical_task_read"],
        }
    return summary


def ranking_comparison():
    desk_ranked = sorted(
        (
            {"slug": target["slug"], "target_name": target["name"], "total": target_scores(target, mode="desk")["total"]}
            for target in TARGETS
        ),
        key=lambda item: item["total"],
        reverse=True,
    )
    empirical_ranked = sorted(
        (
            {"slug": target["slug"], "target_name": target["name"], "total": target_scores(target, mode="empirical")["total"]}
            for target in TARGETS
        ),
        key=lambda item: item["total"],
        reverse=True,
    )

    desk_rank_map = {item["slug"]: index for index, item in enumerate(desk_ranked, start=1)}
    empirical_rank_map = {item["slug"]: index for index, item in enumerate(empirical_ranked, start=1)}
    desk_total_map = {item["slug"]: item["total"] for item in desk_ranked}

    comparison = []
    for item in empirical_ranked:
        desk_rank = desk_rank_map[item["slug"]]
        empirical_rank = empirical_rank_map[item["slug"]]
        comparison.append(
            {
                "slug": item["slug"],
                "target_name": item["target_name"],
                "desk_rank": desk_rank,
                "empirical_rank": empirical_rank,
                "rank_change": desk_rank - empirical_rank,
                "desk_total": desk_total_map[item["slug"]],
                "empirical_total": item["total"],
            }
        )
    return comparison


def render_protocol():
    task_sections = []
    for task in TASKS:
        acceptance = "\n".join(f"- {item}" for item in task["acceptance"])
        task_sections.append(
            clean_block(
                f"""\
                ## {task["id"].replace("_", " ").title()}: {task["name"]}

                - Timebox: `{task["timebox_minutes"]}` minutes
                - Prompt: {task["prompt"]}

                Acceptance criteria:
                {acceptance}
                """
            )
        )

    metric_defs = clean_block(
        """\
        ## Metric Definitions

        - `time_to_first_acceptable_output`: Minutes until the operator would show the artifact to a stakeholder without apology.
        - `time_to_completion`: Minutes until the operator meets the task acceptance criteria or exhausts the timebox.
        - `requirements_pass_rate`: Completed acceptance items divided by total acceptance items for that task.
        - `manual_fix_count`: Count of noticeable manual repairs needed after the tool's initial generation or transformation.
        - `structured_reuse`: `yes` if the operator used reusable components, variables, CMS, collections, or another structured abstraction; otherwise `no`.
        - `publish_success`: `yes` if the operator produced a live preview, publish artifact, export, or handoff that another person could use immediately; otherwise `no`.
        - `governance_support`: `0` to `3`, where `0` means no visible permissions, versioning, or rollback support and `3` means strong visible change controls.
        - `agent_or_api_leverage`: `0` to `3`, where `0` means no meaningful agent, connector, API, or repo leverage and `3` means the operator used one of these to advance the task materially.
        """
    )

    return clean_block(
        f"""\
        # Web-Build Pilot Operator Protocol

        Prepared April 14, 2026. This protocol was used for the recorded task runs in this repository and can also be reused for follow-on reruns.

        ## Operator Setup

        - `operator_a`: {OPERATOR_PROFILES["operator_a"]}
        - `operator_b`: {OPERATOR_PROFILES["operator_b"]}
        - Operators should use the same machine class, browser, and network conditions where possible.
        - Operators should not consult external tutorials mid-run.
        - Tool order is pre-randomized in `task_metrics.csv`.

        {chr(10).join(task_sections)}
        {metric_defs}
        ## Scoring Rule

        Record measurements directly in `task_metrics.csv`. Do not backfill numbers from memory after the session. If a tool blocks on plan limits or authentication steps that the operator cannot complete, note the blocker in `notes` and mark the affected metric fields as blank.
        """
    )


def render_readme(consensus):
    ranking_lines = "\n".join(
        f"- `{item['target_name']}`: `{item['total']}/75`" for item in consensus["ranked_targets"]
    )
    task_summary = consensus["task_metrics"]
    if task_summary["status"] == "scheduled_not_executed":
        task_status_line = "Actual operator task measurements: pending authenticated product access"
        task_metrics_line = f"`task_metrics.csv`: {task_summary['row_count']} scheduled task-run rows ready for execution"
    else:
        task_status_line = (
            "Empirical task measurements: "
            f"{task_summary['display_summary']}"
        )
        task_metrics_line = (
            f"`task_metrics.csv`: {task_summary['row_count']} recorded task-run rows with live outcomes and blocker notes"
        )
    return clean_block(
        f"""\
        # Web-Build Empirical Pilot

        This directory contains a reproducible study package for comparing six web-build offerings with the repository's `ai_resilience_evaluator` rubric.

        ## Status

        - Desk research evidence packets: complete
        - Structured desk-rater scorecards: complete
        - Consensus scoring and aggregation: complete
        - Operator task protocol and randomized run sheet: complete
        - {task_status_line}

        ## Cohort Ranking

        {ranking_lines}

        Desk-only baseline totals remain preserved in `study-metadata.json` and `consensus_scores.json` for audit.

        ## Contents

        - `analysis.md`: study-level validity read and current limitations
        - `consensus_scores.json`: study aggregation with primary empirical scores plus desk baseline totals, empirical adjustments, ranking comparison, task metrics, and validity read
        - `factor_scores.csv`: desk baseline, empirical consensus, and rater factor rows
        - {task_metrics_line}
        - `operator_protocol.md`: prompts, acceptance criteria, and metric definitions
        - `evidence-packets/`: six standardized evidence packets
        - `rater-scorecards/`: 18 structured desk-rater scorecards
        - `individual-reports/`: six single-offering narrative and JSON reports using the existing evaluator contract
        - `web-build-ai-resilience-2x2.svg`: cohort visualization
        """
    )


def render_analysis(consensus, variance):
    table_rows = []
    for item in consensus["ranked_targets"]:
        table_rows.append(
            f"| {item['target_name']} | {item['total']} | {item['placement']} | {item['primary_read']} |"
        )
    comparison_rows = []
    for item in consensus["ranking_comparison"]:
        shift = f"{item['rank_change']:+d}"
        comparison_rows.append(
            f"| {item['target_name']} | {item['desk_total']} | {item['empirical_total']} | {item['desk_rank']} | {item['empirical_rank']} | {shift} |"
        )

    limitation_lines = "\n".join(
        f"- {item}" for item in consensus["limitations"]
    )
    task_summary = consensus["task_metrics"]
    validity = consensus["validity_read"]
    observed_findings = ""
    if validity.get("observed_findings"):
        observed_findings = "\n".join(f"- {item}" for item in validity["observed_findings"])
    return clean_block(
        f"""\
        # Web-Build Pilot Analysis

        Prepared April 14, 2026.

        ## Study Status

        The desk-research phase is complete: this directory includes six standardized evidence packets, 18 structured desk-rater scorecards, adjudicated consensus scores, and a randomized 36-run task sheet. The task phase now includes recorded live product runs rather than only a scaffolded execution plan.

        Empirical task summary: {task_summary["display_summary"]}

        Method note: {task_summary["method_note"]}

        ## Current Ranking

        | Offering | Total | Placement | Primary Read |
        | --- | --- | --- | --- |
        {chr(10).join(table_rows)}

        ## Desk Vs Empirical

        | Offering | Desk Total | Empirical Total | Desk Rank | Empirical Rank | Rank Change |
        | --- | --- | --- | --- | --- | --- |
        {chr(10).join(comparison_rows)}

        ## Desk-Phase Validity Read

        The desk phase already surfaces the directional thesis the rubric is trying to test: the stronger scores cluster around platforms that own more governed publish, CMS, developer, and multi-stakeholder workflow surface. `Wix Studio` and `Webflow` lead because they look least like pure generation wrappers and most like durable website operating layers. `Figma Sites` follows because it inherits strong collaborative context and distribution, but not yet the same operating depth. `Framer` remains credible because it owns CMS plus publish, yet still looks lighter on governance. `Figma Make` and `Lovable` are strategically relevant but more exposed because rapid generation is a larger share of the visible value.

        ## Empirical Task Read

        {validity.get("empirical_read", "The task phase is still pending.")}

        {observed_findings}

        ## Rater Stability

        Category rankings are broadly stable across the three structured desk-rater passes. The highest per-factor disagreement remains bounded to one point for the large majority of factors, with the biggest disagreements concentrated in `switching_cost`, `liability_governance`, and `outcome_depth_test` where public evidence is inherently less explicit. That is directionally acceptable for a pilot, but these are the exact areas where independent human raters would strengthen the design.

        ## Interpretation

        The empirical phase is more useful as a stress test of rubric robustness than as a clean human-factors experiment. The important pattern is not operator independence; it is whether the task evidence sharpens or weakens the rubric's view of durable workflow ownership. On that question, the biggest discriminator was task 2, where only `Figma Make` completed both governed-revision runs cleanly and `Lovable` completed one clean pass while the heavier platforms mostly failed for packaging, workflow-fragmentation, or product-path reasons.

        `Figma Make` moved up because the task phase validated more workflow depth, governed change continuity, and publishable output than the desk pass originally credited. `Figma Sites` moved down because its observed product path was plan-limited and code-component-first. `Framer` partially recovered once the rerun entered through Wireframer, which validated the official AI workflow, but its publish reliability still looked lighter than its in-editor generation flow.

        ## Limitations

        {limitation_lines}
        """
    )


def render_svg(consensus):
    width = 1360
    height = 860
    left = 220
    right = 980
    top = 110
    bottom = 730
    mid_x = (left + right) / 2
    mid_y = (top + bottom) / 2
    label_font_size = 22
    label_height = 28
    label_gap = 12
    label_lane_offset = 34
    leader_offset = 14

    def map_x(value):
        return left + (right - left) * (value / 100.0)

    def map_y(value):
        return bottom - (bottom - top) * (value / 100.0)

    def estimate_label_width(text):
        return max(72.0, len(text) * label_font_size * 0.6)

    total_by_slug = {
        slug: payload["scores"]["total"]
        for slug, payload in consensus["consensus_scores"].items()
    }

    def stack_centers(points):
        if not points:
            return []
        min_center = top + label_height / 2
        max_center = bottom - label_height / 2
        centers = []
        step = label_height + label_gap

        for point in points:
            center = max(point["y"], min_center)
            if centers:
                center = max(center, centers[-1] + step)
            centers.append(center)

        if centers[-1] > max_center:
            centers[-1] = max_center
            for index in range(len(centers) - 2, -1, -1):
                centers[index] = min(centers[index], centers[index + 1] - step)
            if centers[0] < min_center:
                centers[0] = min_center
                for index in range(1, len(centers)):
                    centers[index] = max(centers[index], centers[index - 1] + step)
                overflow = centers[-1] - max_center
                if overflow > 0:
                    centers = [center - overflow for center in centers]

        return centers

    points = []
    for target in TARGETS:
        x = map_x(target["plot"]["x"])
        y = map_y(target["plot"]["y"])
        label_side = "right" if x >= mid_x else "left"
        total = total_by_slug[target["slug"]]
        label = f'{target["name"]} ({total}/75)'
        points.append(
            {
                "slug": target["slug"],
                "name": target["name"],
                "label": label,
                "x": x,
                "y": y,
                "side": label_side,
                "label_width": estimate_label_width(label),
            }
        )

    label_layout = {}
    for side in ("left", "right"):
        side_points = [point for point in points if point["side"] == side]
        side_points.sort(key=lambda point: point["y"])
        centers = stack_centers(side_points)
        for point, center in zip(side_points, centers):
            label_layout[point["slug"]] = {
                "center_y": center,
                "text_x": right + label_lane_offset if side == "right" else left - label_lane_offset,
                "text_anchor": "start" if side == "right" else "end",
                "leader_x": right + leader_offset if side == "right" else left - leader_offset,
                "text_padding_x": 12 if side == "right" else -12,
            }

    point_text = []
    for point in points:
        layout = label_layout[point["slug"]]
        leader_end_x = layout["text_x"] - layout["text_padding_x"]
        point_text.append(
            dedent(
                f"""\
                  <path d="M {point["x"]:.1f} {point["y"]:.1f} L {layout["leader_x"]:.1f} {layout["center_y"]:.1f} L {leader_end_x:.1f} {layout["center_y"]:.1f}" fill="none" stroke="#777777" stroke-width="1.5" />
                  <circle cx="{point["x"]:.1f}" cy="{point["y"]:.1f}" r="9" fill="#000000" />
                  <text x="{layout["text_x"]:.1f}" y="{layout["center_y"]:.1f}" fill="#000000" font-size="{label_font_size}" font-weight="700" font-family="Helvetica, Arial, sans-serif" text-anchor="{layout["text_anchor"]}" dominant-baseline="middle">{point["label"]}</text>
                """
            ).rstrip()
        )

    return dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
          <title id="title">Web-build AI resilience pilot 2x2</title>
          <desc id="desc">A black and white 2x2 chart plotting Wix Studio, Webflow, Figma Sites, Framer, Figma Make, and Lovable on proprietary advantage and workflow criticality.</desc>
          <rect width="{width}" height="{height}" fill="#ffffff" />
          <text x="120" y="58" fill="#000000" font-size="34" font-weight="700" font-family="Helvetica, Arial, sans-serif">Web-Build AI Resilience Pilot</text>
          <text x="120" y="92" fill="#555555" font-size="18" font-family="Helvetica, Arial, sans-serif">Prepared April 14, 2026</text>

          <line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="#000000" stroke-width="3" />
          <line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#000000" stroke-width="3" />
          <line x1="{mid_x}" y1="{top}" x2="{mid_x}" y2="{bottom}" stroke="#9a9a9a" stroke-width="2" stroke-dasharray="10 8" />
          <line x1="{left}" y1="{mid_y}" x2="{right}" y2="{mid_y}" stroke="#9a9a9a" stroke-width="2" stroke-dasharray="10 8" />

          <text x="{left}" y="{bottom + 48}" fill="#000000" font-size="22" font-family="Helvetica, Arial, sans-serif">Commodity Output</text>
          <text x="{right - 232}" y="{bottom + 48}" fill="#000000" font-size="22" font-family="Helvetica, Arial, sans-serif">Proprietary Advantage</text>
          <text transform="translate(132 620) rotate(-90)" fill="#000000" font-size="22" font-family="Helvetica, Arial, sans-serif">Nice-to-Have Utility</text>
          <text transform="translate(132 320) rotate(-90)" fill="#000000" font-size="22" font-family="Helvetica, Arial, sans-serif">Mission-Critical Workflow</text>

          <text x="{left + 16}" y="{top + 34}" fill="#8a8a8a" font-size="20" font-weight="700" font-family="Helvetica, Arial, sans-serif">Convenience</text>
          <text x="{left + 16}" y="{bottom - 18}" fill="#8a8a8a" font-size="20" font-weight="700" font-family="Helvetica, Arial, sans-serif">Fragile</text>
          <text x="{right - 194}" y="{top + 34}" fill="#8a8a8a" font-size="20" font-weight="700" font-family="Helvetica, Arial, sans-serif">Resilient</text>
          <text x="{right - 222}" y="{bottom - 18}" fill="#8a8a8a" font-size="20" font-weight="700" font-family="Helvetica, Arial, sans-serif">Premium Niche</text>

        {chr(10).join(point_text)}
        </svg>
        """
    )


def write_json(path, payload):
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main():
    ensure_dirs()

    target_variance = {}
    factor_rows = []
    consensus_targets = []
    study_targets = {}
    task_rows = load_task_metric_rows(OUT / "task_metrics.csv")
    task_summary = summarize_task_metrics(task_rows)
    baseline_totals = desk_baseline_totals()
    adjustment_summary = empirical_adjustment_summary()
    ranking_delta = ranking_comparison()

    for target in TARGETS:
        report_json = target_report_json(target)
        report_md = render_report_markdown(target)
        write_json(INDIVIDUAL_DIR / f"{target['slug']}-ai-resilience-report.json", report_json)
        (INDIVIDUAL_DIR / f"{target['slug']}-ai-resilience-report.md").write_text(report_md, encoding="utf-8")
        (EVIDENCE_DIR / f"{target['slug']}-evidence-packet.md").write_text(render_evidence_packet(target), encoding="utf-8")

        scorecards = []
        for rater_id in RATERS:
            card = rater_scorecard(target, rater_id)
            scorecards.append(card)
            write_json(RATER_DIR / f"{target['slug']}-{rater_id}.json", card)

        variance = variance_bundle(scorecards)
        target_variance[target["slug"]] = variance
        factor_rows.extend(factor_score_rows(target, scorecards))

        study_targets[target["slug"]] = {
            "target_name": target["name"],
            "placement": target["quadrant_placement"],
            "summary": target["summary"],
            "scores": report_json["scores"],
            "report_paths": {
                "markdown": f"individual-reports/{target['slug']}-ai-resilience-report.md",
                "json": f"individual-reports/{target['slug']}-ai-resilience-report.json",
                "evidence_packet": f"evidence-packets/{target['slug']}-evidence-packet.md",
            },
        }
        consensus_targets.append(
            {
                "target_name": target["name"],
                "slug": target["slug"],
                "total": report_json["scores"]["total"],
                "placement": target["quadrant_placement"],
                "primary_read": target["final_verdict"],
            }
        )

    consensus_targets.sort(key=lambda item: item["total"], reverse=True)

    study_metadata = build_study_metadata(task_summary)
    validity_read = build_validity_read(task_summary)

    consensus_payload = {
        "study_metadata": study_metadata,
        "consensus_scores": study_targets,
        "desk_baseline_totals": baseline_totals,
        "empirical_adjustment_summary": adjustment_summary,
        "ranking_comparison": ranking_delta,
        "rater_variance": target_variance,
        "task_metrics": task_summary,
        "validity_read": validity_read,
        "ranked_targets": consensus_targets,
        "limitations": [
            "The task phase now includes live authenticated runs, but `operator_a` is a same-agent replication pass rather than an independent second human operator.",
            "The three rater passes are structured desk-rater simulations rather than independent human raters.",
            "Some blocker outcomes reflect plan packaging or workspace state rather than pure product capability, especially in Webflow, Figma Sites, and Lovable.",
            "Figma Sites was stressed with a prompt-first workflow that did not fully match the product path we exercised, so that empirical task read should be interpreted as workflow-fit evidence rather than a total product-quality verdict. Framer's official AI path was validated in a follow-on Wireframer rerun, but it was not surfaced cleanly from the first authenticated project routes.",
            "Some workflow-depth, switching-cost, and accountability judgments remain inferential because vendors rarely publish those details directly.",
        ],
    }

    write_json(OUT / "study-metadata.json", study_metadata)
    write_json(OUT / "consensus_scores.json", consensus_payload)
    write_csv(OUT / "factor_scores.csv", factor_rows)
    write_csv(OUT / "task_metrics.csv", task_rows)
    (OUT / "operator_protocol.md").write_text(render_protocol(), encoding="utf-8")
    (OUT / "web-build-ai-resilience-2x2.svg").write_text(render_svg(consensus_payload), encoding="utf-8")
    (OUT / "README.md").write_text(render_readme(consensus_payload), encoding="utf-8")
    (OUT / "analysis.md").write_text(render_analysis(consensus_payload, target_variance), encoding="utf-8")


if __name__ == "__main__":
    main()
