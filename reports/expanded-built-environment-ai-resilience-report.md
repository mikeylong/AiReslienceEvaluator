# Expanded Built-Environment AI Resilience Report

Prepared June 18, 2026 using the `ai_resilience_evaluator` rubric from `mikeylong/AiReslienceEvaluator`.

## Executive Summary

This rerun expands the original Accruent/Runwise comparison into an eight-company built-environment cohort spanning enterprise asset systems, IWMS/facilities platforms, smart-building controls, and energy optimization.

The highest-scoring target is **IBM Maximo (`71/75`)**, because it combines critical-asset workflow ownership, enterprise system-of-record depth, predictive-maintenance AI, and high switching costs. **BrainBox AI/Trane (`68/75`)** is the strongest pure AI-control story because its value is tied to autonomous HVAC control through Trane's building-management channel. **Runwise (`65/75`)** and **75F (`65/75`)** remain strong because they own physical control loops, sensors, and building-specific operating data.

The category effect matters. Software-only FM/IWMS systems can be highly resilient when they own governed records and recurring workflows, but physical control platforms get extra resilience when better models directly improve control decisions, comfort, energy savings, and alerting.

**Ranking**

1. IBM Maximo: `71/75` - strong resilience
2. BrainBox AI/Trane: `68/75` - strong resilience
3. 75F: `65/75` - strong resilience
4. Runwise: `65/75` - strong resilience
5. GridPoint: `63/75` - strong resilience
6. Accruent: `60/75` - strong resilience
7. Planon: `60/75` - strong resilience
8. Facilio: `59/75` - mixed but promising

## Comparison Block

Sorted by descending total score. Category effects describe how much the segment itself helps or hurts AI resilience; execution quality describes how well the company appears to be using that segment advantage.

| Rank | Target | Score | Category effects | Execution quality |
| --- | --- | --- | --- | --- |
| 1 | IBM Maximo | 71/75 | Critical-asset EAM gains the highest category tailwind because better AI acts on governed asset records, inspections, reliability data, and high-stakes work execution. | Execution quality is strongest on trust, APIs, enterprise distribution, and current Maximo Assistant evidence; agent-native delegation should be made clearer. |
| 2 | BrainBox AI/Trane | 68/75 | Autonomous HVAC control gets a strong category tailwind because model quality can directly improve comfort, energy, carbon, and operating actions. | Execution quality is strong on autonomous-control evidence and Trane channel leverage; open-agent and operator-governance detail is thinner. |
| 3 | 75F | 65/75 | Full-stack BAS hardware and interoperability create a category tailwind similar to controls incumbents, though at smaller public scale. | Execution quality is strong on hardware, APIs, BACnet/OpenADR posture, and security controls; public AI/adoption evidence is less current. |
| 4 | Runwise | 65/75 | Wireless control plus energy/comfort outcomes create category strength, but the lane is narrower than broad EAM or global controls platforms. | Execution quality is strong on building counts, savings, service accountability, and current AI-control narrative; formal trust evidence is the main gap. |
| 5 | GridPoint | 63/75 | Energy and demand-response control is category-favorable because savings are measurable and tied to grid economics. | Execution quality is strong on deployment footprint and savings proof; public SOC/API/current-AI evidence is weaker. |
| 6 | Accruent | 60/75 | Enterprise FM/CMMS/IWMS breadth is resilient through records and compliance, but category advantage varies by module. | Execution quality is strong on installed base, APIs, and security posture; visible AI is more embedded assistant/automation than autonomous agent execution. |
| 7 | Planon | 60/75 | IWMS source-of-truth and SAP adjacency support resilience, while weaker public AI-control evidence limits the category lift. | Execution quality is strong on trust, platform posture, SAP channel, and IWMS maturity; recent named AI products are less explicit. |
| 8 | Facilio | 59/75 | Agent-native FM workflows are strategically relevant, but the category is still proving whether agent orchestration becomes a durable moat. | Execution quality is strongest on Atom and MCP posture; long-term proof, certification clarity, and incumbent switching-cost depth are less mature. |

## 2x2 Placement

- X-axis: `Commodity Output -> Proprietary Advantage`
- Y-axis: `Nice-to-Have Utility -> Mission-Critical Workflow`
- Placement: `IBM Maximo and BrainBox AI/Trane lead the resilient quadrant; Runwise, 75F, GridPoint, Accruent, and Planon are also resilient; Facilio sits just below the strong-resilience threshold because its agentic layer is newer and more copyable, despite excellent agent readiness.`

**Rationale:** The chart separates companies that own physical/critical workflow execution from those with valuable but more software-layered workflow control. IBM Maximo wins on critical-asset system position. BrainBox AI/Trane, Runwise, 75F, and GridPoint score high on physical control or energy-control loops. Accruent and Planon score well through enterprise records, compliance, and workflow breadth. Facilio has the best explicit MCP/agent posture, but its current moat depends on proving that agentic execution becomes durable workflow ownership rather than a feature layer incumbents can copy.

## Full Score Table

| Target | Category | Factor | Score | Rationale |
| --- | --- | --- | --- | --- |
| IBM Maximo | Proprietary advantage | Context | 5/5 | Direct evidence. Maximo manages asset history, work data, maintenance workflows, inspections, sensor data, and reliability context across critical infrastructure. |
| IBM Maximo | Proprietary advantage | Trust | 5/5 | Direct evidence. IBM's enterprise cloud/security posture, Maximo security documentation, and critical-industry customer base support high trust. |
| IBM Maximo | Proprietary advantage | Distribution | 5/5 | Direct evidence. IBM sells Maximo across manufacturing, energy, utilities, transportation, government, healthcare, and other asset-intensive sectors. |
| IBM Maximo | Proprietary advantage | Judgment | 4/5 | Inference. Maximo embeds reliability, inspection, and maintenance logic, but final operational judgment remains with asset owners and technicians. |
| IBM Maximo | Proprietary advantage | Liability / Governance | 4/5 | Direct evidence. The suite supports compliance, safety, inspections, work control, and governed asset records, though customer operators retain final liability. |
| IBM Maximo | Workflow criticality | Frequency | 5/5 | Inference. Maintenance, inspection, reliability, and work-order processes are daily operating workflows in asset-intensive organizations. |
| IBM Maximo | Workflow criticality | Operational Dependence | 5/5 | Direct evidence. IBM positions Maximo around uptime, safety, compliance, outage reduction, and reliability for critical equipment and infrastructure. |
| IBM Maximo | Workflow criticality | System Position | 5/5 | Direct evidence. Maximo acts as a system of record and action for assets, work orders, maintenance processes, and reliability workflows. |
| IBM Maximo | Workflow criticality | Switching Cost | 5/5 | Inference. Historical asset data, integrations, work processes, training, and compliance records make migration materially costly. |
| IBM Maximo | Workflow criticality | Budget Durability | 5/5 | Inference. Critical-asset uptime, safety, inspections, and regulated maintenance are durable budget lines. |
| IBM Maximo | AI resilience tests | Model Improvement Test | 5/5 | Direct evidence. IBM describes AI and sensor-data use for issue detection, prioritization, forecasting, and predictive maintenance. |
| IBM Maximo | AI resilience tests | Wrapper Risk Test | 5/5 | Inference. The moat is enterprise asset data, workflows, integrations, and operational governance, not a thin AI interface. |
| IBM Maximo | AI resilience tests | Agent Readiness Test | 4/5 | Inference. IBM's platform and integration posture can support agentic workflows, but the public Maximo evidence is stronger for AI insights than explicit MCP-style delegation. |
| IBM Maximo | AI resilience tests | Accountability Test | 4/5 | Direct evidence. Maximo governs inspected and maintenance-controlled workflows, but accountability remains shared with operators. |
| IBM Maximo | AI resilience tests | Outcome Depth Test | 5/5 | Direct evidence. The product targets uptime, reliability, safety, asset life, production continuity, and field execution. |
| **IBM Maximo** | **Subtotal** | **Proprietary advantage** | **23/25** |  |
| **IBM Maximo** | **Subtotal** | **Workflow criticality** | **25/25** |  |
| **IBM Maximo** | **Subtotal** | **AI resilience tests** | **23/25** |  |
| **IBM Maximo** | **Total** |  | **71/75** | Strong resilience. |
| BrainBox AI/Trane | Proprietary advantage | Context | 4/5 | Direct evidence. The system uses building telemetry, weather, occupancy, energy use, HVAC behavior, and control data. |
| BrainBox AI/Trane | Proprietary advantage | Trust | 5/5 | Direct evidence. BrainBox cites SOC 2 Type II, encryption, RBAC/MFA, NIST alignment, and Trane's enterprise building-controls distribution. |
| BrainBox AI/Trane | Proprietary advantage | Distribution | 5/5 | Direct evidence. Trane acquired BrainBox AI and routes it through a global HVAC and building-management customer base. |
| BrainBox AI/Trane | Proprietary advantage | Judgment | 4/5 | Inference. Autonomous control and diagnostics encode domain-specific HVAC and energy judgment, though building operators still own final business constraints. |
| BrainBox AI/Trane | Proprietary advantage | Liability / Governance | 4/5 | Direct evidence. Trane/BrainBox operate in safety- and comfort-sensitive controls workflows with security controls, but public evidence still leaves customer operating responsibility in place. |
| BrainBox AI/Trane | Workflow criticality | Frequency | 5/5 | Direct evidence. HVAC optimization and control run continuously, not episodically. |
| BrainBox AI/Trane | Workflow criticality | Operational Dependence | 5/5 | Direct evidence. The product affects energy cost, comfort, emissions, maintenance prioritization, and building operations. |
| BrainBox AI/Trane | Workflow criticality | System Position | 4/5 | Direct evidence. It integrates with Trane controls and building systems, but may sit alongside existing BMS infrastructure rather than replace all control layers. |
| BrainBox AI/Trane | Workflow criticality | Switching Cost | 4/5 | Inference. Building integrations, tuned control models, and operational trust create switching friction. |
| BrainBox AI/Trane | Workflow criticality | Budget Durability | 5/5 | Direct evidence. Energy reduction, carbon goals, and HVAC performance are direct budget and compliance concerns. |
| BrainBox AI/Trane | AI resilience tests | Model Improvement Test | 5/5 | Direct evidence. The value proposition is model-driven autonomous HVAC prediction, optimization, and conversational building intelligence. |
| BrainBox AI/Trane | AI resilience tests | Wrapper Risk Test | 5/5 | Direct evidence. The moat is connected building control, telemetry, Trane distribution, and autonomous execution, not generic model output. |
| BrainBox AI/Trane | AI resilience tests | Agent Readiness Test | 4/5 | Direct evidence. ARIA and Trane AI-agent claims support conversational diagnosis and workflow assistance, but public evidence is less explicit on open delegated-agent APIs. |
| BrainBox AI/Trane | AI resilience tests | Accountability Test | 4/5 | Direct evidence. Trane's enterprise support and BrainBox security posture add accountability beyond recommendations. |
| BrainBox AI/Trane | AI resilience tests | Outcome Depth Test | 5/5 | Direct evidence. Claims center on energy-cost reduction, carbon reduction, comfort, and operational building performance. |
| **BrainBox AI/Trane** | **Subtotal** | **Proprietary advantage** | **22/25** |  |
| **BrainBox AI/Trane** | **Subtotal** | **Workflow criticality** | **23/25** |  |
| **BrainBox AI/Trane** | **Subtotal** | **AI resilience tests** | **23/25** |  |
| **BrainBox AI/Trane** | **Total** |  | **68/75** | Strong resilience. |
| 75F | Proprietary advantage | Context | 4/5 | Direct evidence. 75F owns building telemetry from sensors, controllers, thermostats, gateways, analytics, apps, and BAS workflows. |
| 75F | Proprietary advantage | Trust | 4/5 | Direct evidence. 75F publishes SOC 2 Type 1 evidence, security controls, encryption, audit logs, RBAC/MFA, and network/gateway security. |
| 75F | Proprietary advantage | Distribution | 4/5 | Credible third-party evidence. Public sources and company releases show meaningful installations and recognizable customer logos, though less scale than IBM, Trane, or GridPoint. |
| 75F | Proprietary advantage | Judgment | 4/5 | Inference. 75F embeds HVAC, IAQ, demand-response, and building-automation logic in hardware and software. |
| 75F | Proprietary advantage | Liability / Governance | 4/5 | Direct evidence. Security, audit logs, BACnet/OpenADR/Project Haystack posture, and building-control workflows support governance, though final operations remain customer-owned. |
| 75F | Workflow criticality | Frequency | 5/5 | Direct evidence. Building automation, comfort, IAQ, and HVAC controls operate continuously. |
| 75F | Workflow criticality | Operational Dependence | 5/5 | Direct evidence. The system affects comfort, HVAC energy use, IAQ, demand response, and building performance. |
| 75F | Workflow criticality | System Position | 4/5 | Direct evidence. 75F provides full-stack BAS functions but may coexist with other building systems and integrators. |
| 75F | Workflow criticality | Switching Cost | 4/5 | Inference. Installed hardware, control sequences, data integrations, and operator training create migration cost. |
| 75F | Workflow criticality | Budget Durability | 4/5 | Inference. Energy efficiency, comfort, IAQ, and controls budgets are durable, but buyer economics vary by building segment. |
| 75F | AI resilience tests | Model Improvement Test | 5/5 | Inference. Better models should improve control sequencing, diagnostics, IAQ optimization, and demand-response decisions over sensor/control data. |
| 75F | AI resilience tests | Wrapper Risk Test | 5/5 | Direct evidence. 75F is hardware, controls, APIs, apps, and automation, not a software-only model wrapper. |
| 75F | AI resilience tests | Agent Readiness Test | 4/5 | Direct evidence. Project Haystack open APIs and BACnet/OpenADR support system interoperability, though public evidence is not MCP-style agent governance. |
| 75F | AI resilience tests | Accountability Test | 4/5 | Direct evidence. Security, controls, SOC evidence, and building-automation responsibilities create accountability beyond recommendations. |
| 75F | AI resilience tests | Outcome Depth Test | 5/5 | Direct evidence. 75F targets HVAC savings, IAQ, comfort, demand response, and building automation outcomes. |
| **75F** | **Subtotal** | **Proprietary advantage** | **20/25** |  |
| **75F** | **Subtotal** | **Workflow criticality** | **22/25** |  |
| **75F** | **Subtotal** | **AI resilience tests** | **23/25** |  |
| **75F** | **Total** |  | **65/75** | Strong resilience. |
| Runwise | Proprietary advantage | Context | 4/5 | Direct evidence. Runwise uses wireless hardware, indoor sensors, weather forecasts, building-response history, usage data, and live operating state. |
| Runwise | Proprietary advantage | Trust | 4/5 | Direct evidence. Runwise claims 10,300+ powered buildings, 1,000+ customers, 24/7 support, utility relationships, and dedicated building experts. |
| Runwise | Proprietary advantage | Distribution | 4/5 | Direct evidence. Runwise has strong property-owner deployment in its core market, though narrower global reach than large incumbents. |
| Runwise | Proprietary advantage | Judgment | 4/5 | Inference. The system embeds building-control logic and field-service expertise rather than just surfacing dashboards. |
| Runwise | Proprietary advantage | Liability / Governance | 3/5 | Direct evidence. Runwise provides service accountability and savings claims, but public terms leave core safety and equipment responsibility with customers. |
| Runwise | Workflow criticality | Frequency | 5/5 | Direct evidence. Heating, cooling, water, and alerting systems are continuously monitored or controlled. |
| Runwise | Workflow criticality | Operational Dependence | 5/5 | Direct evidence. The product affects tenant comfort, energy cost, critical alerts, emissions/fines, and building operations. |
| Runwise | Workflow criticality | System Position | 4/5 | Direct evidence. Runwise sits in the monitoring and control layer, but does not replace every safety, equipment, or BMS function. |
| Runwise | Workflow criticality | Switching Cost | 4/5 | Inference. Installed devices, sensor data, integrations, service routines, and building-specific behavior models create switching friction. |
| Runwise | Workflow criticality | Budget Durability | 5/5 | Direct evidence. Runwise ties budget to energy savings, rebates, carbon fines, and operating profit. |
| Runwise | AI resilience tests | Model Improvement Test | 5/5 | Direct evidence. Runwise's current AI-control evidence describes decisions that skip or run heat cycles using indoor data, forecasts, seasonality, and prior response. |
| Runwise | AI resilience tests | Wrapper Risk Test | 5/5 | Direct evidence. The moat is installed controls, wireless sensors, operational data, service, and measured outcomes. |
| Runwise | AI resilience tests | Agent Readiness Test | 4/5 | Direct evidence. Runwise says it has open APIs and many integrations, but public evidence is thinner on autonomous third-party agent governance. |
| Runwise | AI resilience tests | Accountability Test | 4/5 | Direct evidence. No long-term contracts, 24/7 support, dedicated experts, technician service, and savings guarantees add commercial accountability. |
| Runwise | AI resilience tests | Outcome Depth Test | 5/5 | Direct evidence. The product directly targets energy savings, comfort, fines, leak/gas/heating alerts, and building operations. |
| **Runwise** | **Subtotal** | **Proprietary advantage** | **19/25** |  |
| **Runwise** | **Subtotal** | **Workflow criticality** | **23/25** |  |
| **Runwise** | **Subtotal** | **AI resilience tests** | **23/25** |  |
| **Runwise** | **Total** |  | **65/75** | Strong resilience. |
| GridPoint | Proprietary advantage | Context | 4/5 | Direct evidence. GridPoint uses equipment-level data, meters, sensors, controls, schedules, alerts, building assets, and historical energy data. |
| GridPoint | Proprietary advantage | Trust | 4/5 | Inference. Large deployed footprint and utility/commercial energy role support trust, but public SOC/ISO security evidence was not found in sampled sources. |
| GridPoint | Proprietary advantage | Distribution | 5/5 | Direct evidence. GridPoint says its platform is deployed across 20,000+ commercial buildings and is nearing $1.5B in customer savings. |
| GridPoint | Proprietary advantage | Judgment | 4/5 | Inference. Energy optimization, demand response, and asset-control algorithms encode operational energy judgment. |
| GridPoint | Proprietary advantage | Liability / Governance | 3/5 | Inference. Demand-response reporting and IPMVP-style savings evidence support governance, but formal safety/security/legal accountability is less public. |
| GridPoint | Workflow criticality | Frequency | 5/5 | Direct evidence. Energy monitoring, schedules, controls, and demand response are continuous or frequent operating workflows. |
| GridPoint | Workflow criticality | Operational Dependence | 4/5 | Direct evidence. GridPoint affects energy cost, HVAC performance, occupant comfort, food quality, compliance readiness, and maintenance costs. |
| GridPoint | Workflow criticality | System Position | 4/5 | Direct evidence. It controls and monitors building energy assets, but is more energy-focused than a full BAS or CMMS. |
| GridPoint | Workflow criticality | Switching Cost | 4/5 | Inference. Installed controllers, energy history, utility programs, schedules, and operational reporting create switching friction. |
| GridPoint | Workflow criticality | Budget Durability | 5/5 | Direct evidence. Energy savings, demand response, and grid-interactive building economics are durable operating budget drivers. |
| GridPoint | AI resilience tests | Model Improvement Test | 5/5 | Inference. Better models should improve forecasting, optimization, diagnostics, and curtailment strategy over GridPoint's building-energy data. |
| GridPoint | AI resilience tests | Wrapper Risk Test | 4/5 | Direct evidence. Controls, metering, demand response, utility programs, and building asset data make GridPoint deeper than a dashboard wrapper. |
| GridPoint | AI resilience tests | Agent Readiness Test | 3/5 | Inference. Public evidence supports automation and controls, but not explicit AI-agent interfaces or delegated-action governance. |
| GridPoint | AI resilience tests | Accountability Test | 4/5 | Direct evidence. Customer savings, demand-response performance, real-time monitoring, and remote diagnostics make outcomes inspectable. |
| GridPoint | AI resilience tests | Outcome Depth Test | 5/5 | Direct evidence. The product targets energy cost, carbon, HVAC performance, food quality, grid services, and maintenance reduction. |
| **GridPoint** | **Subtotal** | **Proprietary advantage** | **20/25** |  |
| **GridPoint** | **Subtotal** | **Workflow criticality** | **22/25** |  |
| **GridPoint** | **Subtotal** | **AI resilience tests** | **21/25** |  |
| **GridPoint** | **Total** |  | **63/75** | Strong resilience. |
| Accruent | Proprietary advantage | Context | 4/5 | Direct evidence. Accruent stores and connects work orders, asset records, engineering documents, IoT signals, audit records, space data, and facilities history. |
| Accruent | Proprietary advantage | Trust | 4/5 | Direct evidence. Accruent publishes ISO/IEC 27001, SOC 1, SOC 2, UK ICO alignment, and critical-infrastructure compliance commitments. |
| Accruent | Proprietary advantage | Distribution | 5/5 | Direct evidence. Accruent says it has helped more than 10,000 organizations in more than 150 countries. |
| Accruent | Proprietary advantage | Judgment | 3/5 | Inference. The products encode facilities, maintenance, engineering-document, and compliance workflows, while scarce judgment often remains with customers and technicians. |
| Accruent | Proprietary advantage | Liability / Governance | 4/5 | Direct evidence. Accruent emphasizes compliance, audit logs, role controls, configurable security, and regulated workflows. |
| Accruent | Workflow criticality | Frequency | 4/5 | Inference. Maintenance, asset, space, document, and monitoring workflows are recurrent, though frequency varies by product and user. |
| Accruent | Workflow criticality | Operational Dependence | 4/5 | Direct evidence. Accruent positions its products around downtime reduction, compliance readiness, predictive maintenance, and asset lifecycle optimization. |
| Accruent | Workflow criticality | System Position | 4/5 | Direct evidence. Products act as systems of record and action for facilities and asset workflows while coexisting with ERP, BMS, and field-service systems. |
| Accruent | Workflow criticality | Switching Cost | 4/5 | Inference. Configured workflows, history, integrations, training, audit records, and implementation work create migration cost. |
| Accruent | Workflow criticality | Budget Durability | 4/5 | Inference. Maintenance, compliance, asset uptime, and facilities-management spend are durable, but broad modules vary in budget priority. |
| Accruent | AI resilience tests | Model Improvement Test | 4/5 | Direct evidence. Crue AI, predictive maintenance, Observe, EDMS automation, and analytics should improve when grounded in proprietary workflow context. |
| Accruent | AI resilience tests | Wrapper Risk Test | 4/5 | Inference. Generic AI can copy assistant features, but cannot easily replace installed records, integrations, and governance. |
| Accruent | AI resilience tests | Agent Readiness Test | 3/5 | Direct evidence. Accruent has REST APIs and integrations, but public evidence is stronger for conventional integration than explicit delegated-agent control. |
| Accruent | AI resilience tests | Accountability Test | 4/5 | Direct evidence. Compliance, auditability, security controls, and services give Accruent an accountability layer beyond AI output. |
| Accruent | AI resilience tests | Outcome Depth Test | 5/5 | Direct evidence. The products target downtime, compliance, energy, asset life, operational continuity, and safety-adjacent work. |
| **Accruent** | **Subtotal** | **Proprietary advantage** | **20/25** |  |
| **Accruent** | **Subtotal** | **Workflow criticality** | **20/25** |  |
| **Accruent** | **Subtotal** | **AI resilience tests** | **20/25** |  |
| **Accruent** | **Total** |  | **60/75** | Strong resilience. |
| Planon | Proprietary advantage | Context | 4/5 | Direct evidence. Planon unifies real estate, facilities, workplace, asset, service, energy, sustainability, and IoT-enabled building data. |
| Planon | Proprietary advantage | Trust | 5/5 | Direct evidence. Planon's trust center cites independent audits, ISO 27001, ISAE 3402 Type II, SOC 2, and other assurance signals. |
| Planon | Proprietary advantage | Distribution | 4/5 | Direct evidence. Planon positions itself as a global smart sustainable building management provider with broad IWMS adoption. |
| Planon | Proprietary advantage | Judgment | 4/5 | Inference. Embedded AI and IWMS workflows encode facilities, space, asset, contract, and maintenance judgment, but operators keep final decisions. |
| Planon | Proprietary advantage | Liability / Governance | 4/5 | Direct evidence. Planon emphasizes validated unified data, GDPR compliance, certifications, and governed cloud services. |
| Planon | Workflow criticality | Frequency | 4/5 | Inference. Workplace, service, maintenance, and portfolio workflows are recurring, though not all modules are daily for all users. |
| Planon | Workflow criticality | Operational Dependence | 4/5 | Direct evidence. The platform supports real estate, facility management, asset maintenance, workplace services, and sustainability operations. |
| Planon | Workflow criticality | System Position | 4/5 | Direct evidence. Planon is an IWMS/source-of-truth layer with IoT and smart-building integration, but often coexists with controls, ERP, and service systems. |
| Planon | Workflow criticality | Switching Cost | 4/5 | Inference. Portfolio data, configured workflows, integrations, and service processes create migration cost. |
| Planon | Workflow criticality | Budget Durability | 4/5 | Inference. Real estate, facilities, maintenance, and sustainability management are durable but can be cyclical by module. |
| Planon | AI resilience tests | Model Improvement Test | 4/5 | Direct evidence. Planon describes embedded AI for ticket creation, contract summaries, adaptive maintenance, triage, and building intelligence. |
| Planon | AI resilience tests | Wrapper Risk Test | 4/5 | Inference. The moat is unified validated IWMS data and workflow integration, not standalone AI text generation. |
| Planon | AI resilience tests | Agent Readiness Test | 3/5 | Inference. Planon has platform and integration posture, but public evidence is less explicit on external agent/MCP-style execution. |
| Planon | AI resilience tests | Accountability Test | 4/5 | Direct evidence. Trust-center controls, validated data, GDPR compliance, and governed workflows support accountability. |
| Planon | AI resilience tests | Outcome Depth Test | 4/5 | Direct evidence. Planon targets cost, utilization, maintenance, energy, workplace services, and sustainability outcomes. |
| **Planon** | **Subtotal** | **Proprietary advantage** | **21/25** |  |
| **Planon** | **Subtotal** | **Workflow criticality** | **20/25** |  |
| **Planon** | **Subtotal** | **AI resilience tests** | **19/25** |  |
| **Planon** | **Total** |  | **60/75** | Strong resilience. |
| Facilio | Proprietary advantage | Context | 4/5 | Direct evidence. Facilio unifies assets, work orders, tenants, vendors, compliance, finance, energy, refrigeration, and portfolio operations. |
| Facilio | Proprietary advantage | Trust | 3/5 | Direct evidence. Facilio states SOC 2 compliance and security controls, but its public security page also says it is working toward SOC2 compliant standards, creating some evidence ambiguity. |
| Facilio | Proprietary advantage | Distribution | 4/5 | Direct evidence. Facilio has visible enterprise portfolio customers and multi-site positioning, but less established reach than IBM, Accruent, Planon, or Trane. |
| Facilio | Proprietary advantage | Judgment | 4/5 | Direct evidence. Atom agents are designed to execute service, finance, compliance, approval, reporting, and dispatch workflows, not just record them. |
| Facilio | Proprietary advantage | Liability / Governance | 3/5 | Direct evidence. MCP permissions, OAuth2, and audit trails are strong, but broader liability and compliance posture is less proven publicly than mature incumbents. |
| Facilio | Workflow criticality | Frequency | 4/5 | Direct evidence. Service requests, work orders, vendor coordination, compliance, and invoices are recurring operational workflows. |
| Facilio | Workflow criticality | Operational Dependence | 4/5 | Inference. For multi-site FM teams, Facilio can become operationally important, though it may layer on top of existing CMMS/ERP systems. |
| Facilio | Workflow criticality | System Position | 4/5 | Direct evidence. Facilio can be the connected CMMS/platform layer or an AI layer over existing CMMS, ERP, and finance systems. |
| Facilio | Workflow criticality | Switching Cost | 4/5 | Inference. Operational workflows, integrations, agent configurations, and portfolio data create friction once deployed. |
| Facilio | Workflow criticality | Budget Durability | 4/5 | Inference. Facilities uptime, vendor coordination, compliance, and back-office labor reduction have durable budget logic. |
| Facilio | AI resilience tests | Model Improvement Test | 5/5 | Direct evidence. Facilio's Atom and MCP posture should benefit directly from better models that can coordinate FM workflows and retrieve operational context. |
| Facilio | AI resilience tests | Wrapper Risk Test | 3/5 | Inference. Facilio is more than a wrapper, but its most visible differentiation is AI-agent orchestration that other platforms may copy. |
| Facilio | AI resilience tests | Agent Readiness Test | 5/5 | Direct evidence. Facilio MCP connects Claude, ChatGPT, Copilot, and Cursor to Facilio data with permissions, OAuth2, and audit logs. |
| Facilio | AI resilience tests | Accountability Test | 4/5 | Direct evidence. Audit trails, permissions, human oversight, and workflow execution controls support accountability. |
| Facilio | AI resilience tests | Outcome Depth Test | 4/5 | Direct evidence. The suite targets service intake, dispatch, compliance, invoice validation, reporting, maintenance, and asset lifecycle outcomes. |
| **Facilio** | **Subtotal** | **Proprietary advantage** | **18/25** |  |
| **Facilio** | **Subtotal** | **Workflow criticality** | **20/25** |  |
| **Facilio** | **Subtotal** | **AI resilience tests** | **21/25** |  |
| **Facilio** | **Total** |  | **59/75** | Mixed but promising. |

## Top Strengths

### IBM Maximo
- Deep critical-asset system-of-record and system-of-action position.
- Strong AI plus sensor-data posture for predictive maintenance and reliability.
- Large enterprise distribution and high switching costs.

### BrainBox AI/Trane
- Autonomous HVAC control is directly strengthened by better models.
- Trane distribution gives BrainBox a major deployment channel.
- Strong security and building-control evidence.

### 75F
- Full-stack building automation rather than pure analytics.
- Open API and interoperability posture are stronger than most challengers.
- Hardware/control surface makes AI harder to commoditize.

### Runwise
- Physical control loop plus service accountability.
- Building-specific data makes better models more valuable.
- Outcome claims are tied to energy savings and comfort, not just analytics.

### GridPoint
- Large deployment footprint and measurable savings claims.
- Energy-control economics are tightly tied to customer budget.
- Demand response and grid services add system-level value beyond dashboards.

### Accruent
- Broad enterprise installed base across built-environment categories.
- Deep records and compliance context across facilities, assets, documents, and IoT.
- Security and professional-services posture supports enterprise adoption.

### Planon
- Strong IWMS source-of-truth position.
- Good trust/compliance evidence.
- Embedded AI is tied to operational workflows rather than isolated chat.

### Facilio
- Best explicit agent/MCP posture in the cohort.
- AI is aimed at workflow execution, not just summarization.
- Can layer onto existing CMMS/ERP/finance systems without rip-and-replace.

## Main Vulnerabilities

### IBM Maximo
- Large-platform complexity can slow adoption and make user experience uneven.
- Explicit agent-native governance is less visible than AI insight and workflow automation.
- Some reporting, assistant, and planning features can be copied by generic AI layers.

### BrainBox AI/Trane
- Can be category-limited to HVAC and energy optimization rather than full facilities operations.
- Open API and third-party agent posture is less clear than the control/AI story.
- Customer liability and building safety constraints remain outside the AI system.

### 75F
- Some adoption and funding evidence is older than the default 12-month window.
- Distribution is meaningful but below the largest incumbents.
- AI claims are real but less recently documented than BrainBox/Trane or Runwise.

### Runwise
- Security/compliance evidence is less formal publicly than BrainBox, 75F, IBM, or Planon.
- Category strength is highest where Runwise's wireless building-control wedge fits.
- Legal accountability is bounded by terms that keep equipment and tenant safety duties with customers.

### GridPoint
- Explicit AI messaging is less current/public than BrainBox, Runwise, or Facilio.
- Security certification evidence is less visible publicly.
- Scope is energy and controls rather than full facilities management.

### Accruent
- Portfolio breadth makes resilience uneven by module.
- Generic AI can compress assistant, reporting, search, and recommendation layers.
- Agent-native execution controls are less visible publicly than conventional APIs.

### Planon
- Mission criticality varies by module and customer maturity.
- Agent-native execution posture is less clear than Facilio's.
- Physical control loop is less direct than Runwise, 75F, BrainBox/Trane, or GridPoint.

### Facilio
- Newer agent claims have less long-term proof than incumbent workflow systems.
- Security evidence is directionally positive but publicly inconsistent.
- Some differentiation may compress if incumbents add similar agent layers.

## Strategic Read

### Durable Layers

- IBM Maximo: Asset and work history, Reliability models, Enterprise integrations, Inspection and compliance workflows, IBM trust and distribution.
- BrainBox AI/Trane: HVAC telemetry, Autonomous control models, Trane installed channel, Security posture, Energy and carbon outcomes.
- 75F: Sensors and controls, Project Haystack APIs, BACnet/OpenADR interoperability, Security controls, Building automation data.
- Runwise: Installed controls, Wireless sensor network, Building response history, Service organization, Energy and compliance ROI.
- GridPoint: Energy asset data, Grid-interactive controls, Demand-response programs, 20,000+ building footprint, Savings history.
- Accruent: Asset and facility records, Engineering documents, Compliance artifacts, Security posture, Implementation history.
- Planon: Unified IWMS data, Trust center, Smart-building integration, Configured facility and real estate workflows.
- Facilio: Operational workflow graph, Agent permissions and audit trails, CMMS integrations, Portfolio operations data.

### Commoditizing Layers

- IBM Maximo: Generic dashboard narratives, Assistant UX, Basic maintenance summaries.
- BrainBox AI/Trane: Generic energy reports, Chat-based diagnostics, Standalone optimization advice without control access.
- 75F: Analytics UI, Generic IAQ or energy recommendations, Digital assistant copy.
- Runwise: Energy dashboards, Generic operating recommendations, AI explanations without control or service.
- GridPoint: Energy analytics dashboards, Generic recommendations, Basic anomaly descriptions.
- Accruent: Assistant UI, Summarization, Document Q&A, Dashboard narratives.
- Planon: Ticket intake chat, Contract summaries, Simple reporting.
- Facilio: Chat interface, Generic ticket summaries, AI copy around agents.

### Next Moves

- IBM Maximo: Expose clearer permissioned agent interfaces for work planning and execution.
- IBM Maximo: Keep AI tied to governed asset records, inspections, and maintenance actions.
- BrainBox AI/Trane: Make agent permissions and operator override controls visible.
- BrainBox AI/Trane: Expand from HVAC optimization into broader building operations while preserving control trust.
- 75F: Refresh public AI launch evidence and adoption metrics.
- 75F: Make permissioned automation and operator-override governance more explicit.
- Runwise: Publish clearer security and controls-governance evidence.
- Runwise: Keep extending from heating into broader building systems without losing installation speed.
- GridPoint: Clarify AI/model layer and agent-readiness claims.
- GridPoint: Publish stronger security and controls-governance evidence.
- Accruent: Make AI action-safe inside governed workflows.
- Accruent: Expose clearer agent-grade controls for maintenance, compliance, and asset work.
- Planon: Make AI execution permissions and audit trails more visible.
- Planon: Deepen integration between IWMS intelligence and building-control actions.
- Facilio: Publish clearer SOC/security attestations and live-agent case outcomes.
- Facilio: Tie agents to durable compliance and financial controls that competitors cannot copy quickly.

## Final Verdict

The resilient end of this market is not defined by who has the flashiest AI assistant. It is defined by who owns trusted operational context, control authority, recurring work, and accountable outcomes.

**IBM Maximo** is the strongest overall resilience candidate because critical-asset customers run maintenance, inspection, reliability, and compliance workflows through it. **BrainBox AI/Trane** is the clearest example of AI becoming more valuable as it gets better because autonomous HVAC control is the product, not an add-on. **Runwise**, **75F**, and **GridPoint** are also strong because they connect software intelligence to live building systems and measurable energy/comfort outcomes. **Accruent** and **Planon** are resilient enterprise workflow platforms, but their visible AI layers need to remain tied to governed actions and records. **Facilio** is strategically interesting because it is agent-native, but its score is held below the strong band until its agentic execution shows the same proof depth and switching cost as older systems of record or physical control platforms.

## Confidence Level

`Medium-high`. The research uses current official sources where available, and the strongest claims are anchored in product pages, trust pages, and 2025-2026 releases. Confidence is lower for private retention, live implementation quality, customer-level economics, and agent-governance details that are not public.

## Evidence Notes

Research used a shared current-source window through June 18, 2026. Official company materials were weighted first. Credible third-party or press-release evidence was used mainly for acquisition, funding, adoption, or analyst-category context. No YouTube transcript evidence was used.

### IBM Maximo Sources
- [www.ibm.com/products/maximo](https://www.ibm.com/products/maximo)
- [www.ibm.com/products/maximo/asset-performance-management](https://www.ibm.com/products/maximo/asset-performance-management)
- [newsroom.ibm.com/blog-enhanced-maximo-streamlines-workforce-efficiency%2C-investment-planning%2C-and-facilities-management-introduces-gen-ai-assistant](https://newsroom.ibm.com/blog-enhanced-maximo-streamlines-workforce-efficiency%2C-investment-planning%2C-and-facilities-management-introduces-gen-ai-assistant)
- [www.ibm.com/new/announcements/introducing-maximo-assistant-an-ai-resource-for-teams](https://www.ibm.com/new/announcements/introducing-maximo-assistant-an-ai-resource-for-teams)
- [developer.ibm.com/apis/catalog/maximo--maximo-manage-rest-api/](https://developer.ibm.com/apis/catalog/maximo--maximo-manage-rest-api/)
- [cloud.ibm.com/docs/mas-ms?topic=mas-ms-Security](https://cloud.ibm.com/docs/mas-ms?topic=mas-ms-Security)
- [www.ibm.com/new/announcements/maximo-application-suite-achieves-fedramp-authorization](https://www.ibm.com/new/announcements/maximo-application-suite-achieves-fedramp-authorization)

### BrainBox AI/Trane Sources
- [www.trane.com/commercial/north-america/us/en/products-systems/smart-building-technology/ai-solutions/trane-autonomous-control.html](https://www.trane.com/commercial/north-america/us/en/products-systems/smart-building-technology/ai-solutions/trane-autonomous-control.html)
- [investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2025/Trane-Technologies-Ignites-a-New-Era-for-Smart-Buildings-with-Game-Changing-AI-Controls-and-AI-Agent/default.aspx](https://investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2025/Trane-Technologies-Ignites-a-New-Era-for-Smart-Buildings-with-Game-Changing-AI-Controls-and-AI-Agent/default.aspx)
- [investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2025/Trane-Technologies-Launches-BrainBox-AI-Lab-to-Transform-Energy-Management-and-Sustainability-in-Buildings/default.aspx](https://investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2025/Trane-Technologies-Launches-BrainBox-AI-Lab-to-Transform-Energy-Management-and-Sustainability-in-Buildings/default.aspx)
- [investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2025/Trane-Technologies-Completes-Acquisition-of-BrainBox-AI/default.aspx](https://investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2025/Trane-Technologies-Completes-Acquisition-of-BrainBox-AI/default.aspx)
- [brainboxai.com/en/articles/bulletproofing-your-building-data-why-it-teams-love-brainbox-ai](https://brainboxai.com/en/articles/bulletproofing-your-building-data-why-it-teams-love-brainbox-ai)

### 75F Sources
- [www.75f.io/](https://www.75f.io/)
- [www.75f.io/software/saffron-ai/](https://www.75f.io/software/saffron-ai/)
- [www.75f.io/software/api/](https://www.75f.io/software/api/)
- [www.75f.io/software/security/](https://www.75f.io/software/security/)
- [www.75f.io/news/75f-earns-soc-2-compliance/](https://www.75f.io/news/75f-earns-soc-2-compliance/)
- [www.globenewswire.com/news-release/2025/02/06/3022482/0/en/75f-raises-additional-45m-series-b-to-increase-energy-savings-and-make-building-automation-easier.html](https://www.globenewswire.com/news-release/2025/02/06/3022482/0/en/75f-raises-additional-45m-series-b-to-increase-energy-savings-and-make-building-automation-easier.html)

### Runwise Sources
- [www.runwise.com/](https://www.runwise.com/)
- [www.runwise.com/faq](https://www.runwise.com/faq)
- [www.runwise.com/services/heating](https://www.runwise.com/services/heating)
- [www.runwise.com/learn/ai-is-transforming-buildings-across-the-u.s](https://www.runwise.com/learn/ai-is-transforming-buildings-across-the-u.s)
- [www.runwise.com/terms-of-service](https://www.runwise.com/terms-of-service)
- [www.prnewswire.com/news-releases/runwise-raises-55m-to-scale-the-smart-operating-system-for-buildings-302476505.html](https://www.prnewswire.com/news-releases/runwise-raises-55m-to-scale-the-smart-operating-system-for-buildings-302476505.html)

### GridPoint Sources
- [www.gridpoint.com/](https://www.gridpoint.com/)
- [www.gridpoint.com/platform/](https://www.gridpoint.com/platform/)
- [www.gridpoint.com/solutions/](https://www.gridpoint.com/solutions/)
- [www.gridpoint.com/solutions/demand-management/](https://www.gridpoint.com/solutions/demand-management/)
- [www.gridpoint.com/news/gridpoint-nears-1-5b-in-customer-energy-savings-as-electricity-prices-hit-record-highs/](https://www.gridpoint.com/news/gridpoint-nears-1-5b-in-customer-energy-savings-as-electricity-prices-hit-record-highs/)
- [www.prnewswire.com/news-releases/gridpoint-nears-1-5-billion-in-customer-energy-savings-as-electricity-prices-hit-record-highs-302703248.html](https://www.prnewswire.com/news-releases/gridpoint-nears-1-5-billion-in-customer-energy-savings-as-electricity-prices-hit-record-highs-302703248.html)

### Accruent Sources
- [www.accruent.com/solutions/facility-asset-management-software](https://www.accruent.com/solutions/facility-asset-management-software)
- [www.accruent.com/solutions/cmms-software](https://www.accruent.com/solutions/cmms-software)
- [www.accruent.com/products/maintenance-connection/comprehensive-integrations](https://www.accruent.com/products/maintenance-connection/comprehensive-integrations)
- [www.accruent.com/products/observe](https://www.accruent.com/products/observe)
- [www.accruent.com/resources/blog-posts/how-accruent-is-simplifying-organizational-complexity-with-ai](https://www.accruent.com/resources/blog-posts/how-accruent-is-simplifying-organizational-complexity-with-ai)
- [www.accruent.com/security-compliance-certifications](https://www.accruent.com/security-compliance-certifications)
- [www.accruent.com/about-us](https://www.accruent.com/about-us)

### Planon Sources
- [planonsoftware.com/us/](https://planonsoftware.com/us/)
- [planonsoftware.com/us/software/](https://planonsoftware.com/us/software/)
- [planonsoftware.com/us/software/iwms/](https://planonsoftware.com/us/software/iwms/)
- [planonsoftware.com/us/software/planon-platform/](https://planonsoftware.com/us/software/planon-platform/)
- [planonsoftware.com/us/software/iwms/sap/](https://planonsoftware.com/us/software/iwms/sap/)
- [planonsoftware.com/us/news/planon-sap-solution-extension/](https://planonsoftware.com/us/news/planon-sap-solution-extension/)
- [planonsoftware.com/us/resources/blogs/making-buildings-think-ai-in-planon-iwms/](https://planonsoftware.com/us/resources/blogs/making-buildings-think-ai-in-planon-iwms/)
- [planonsoftware.com/us/trustcenter/industry-standards-and-regulations/](https://planonsoftware.com/us/trustcenter/industry-standards-and-regulations/)
- [planonsoftware.com/us/about-us/](https://planonsoftware.com/us/about-us/)

### Facilio Sources
- [facilio.com/](https://facilio.com/)
- [facilio.com/product/cmms-software/](https://facilio.com/product/cmms-software/)
- [facilio.com/product/connected-buildings/](https://facilio.com/product/connected-buildings/)
- [facilio.com/ai-suite/](https://facilio.com/ai-suite/)
- [facilio.com/ai-suite/mcp/](https://facilio.com/ai-suite/mcp/)
- [facilio.com/newsroom/facilio-launches-autonomous-ai-for-facilities-management/](https://facilio.com/newsroom/facilio-launches-autonomous-ai-for-facilities-management/)
- [facilio.com/security/](https://facilio.com/security/)
- [facilio.com/privacy-policy/](https://facilio.com/privacy-policy/)
- [facilio.com/about/](https://facilio.com/about/)
- [facilio.com/newsroom/integrated-estate-management-facilio-press-release/](https://facilio.com/newsroom/integrated-estate-management-facilio-press-release/)
- [facilio.com/newsroom/hellofresh-facilio-press-release/](https://facilio.com/newsroom/hellofresh-facilio-press-release/)

### Near-Miss Companies

- **ServiceChannel:** Strong facilities-management and contractor-network platform with 2026 AI launch evidence; excluded to keep the focused cohort balanced and avoid over-weighting retail FM workflow platforms. Source: [servicechannel.com/press/servicechannel-launches-servicechannel-ai-for-facilities-management/](https://servicechannel.com/press/servicechannel-launches-servicechannel-ai-for-facilities-management/)
- **Brightly:** Direct CMMS/asset-management peer with Siemens backing, large public-sector footprint, SOC 2 Type II evidence, and 2026 data/AI positioning; excluded because the selected cohort already includes Accruent, IBM Maximo, Planon, and Facilio. Source: [www.brightlysoftware.com/resource/brightly-software-accelerates-asset-intelligence-with-new-data-ai-innovations](https://www.brightlysoftware.com/resource/brightly-software-accelerates-asset-intelligence-with-new-data-ai-innovations)
- **Siemens Building X:** Major smart-building incumbent with open APIs, cybersecurity certifications, and AI/ML apps; excluded from the scored set to avoid over-weighting mega building-automation incumbents. Source: [www.siemens.com/en-us/products/building-x/](https://www.siemens.com/en-us/products/building-x/)
- **Johnson Controls OpenBlue/FM:Systems:** Strong controls plus workplace/facilities footprint after Johnson Controls acquired FM:Systems; excluded for the same incumbent-weighting reason as Siemens. Source: [fmsystems.com/johnson-controls-openblue/](https://fmsystems.com/johnson-controls-openblue/)
- **Eptura:** Broad worktech/IWMS portfolio with Microsoft and Autodesk adjacency; excluded because product naming and acquisition complexity would require a separate normalization pass. Source: [eptura.com/news/eptura-worktech-platform/](https://eptura.com/news/eptura-worktech-platform/)
- **Spacewell:** Relevant IWMS, smart-building, occupancy, and AI energy-optimization platform; excluded because Planon covers the global IWMS/smart-building lane in the focused set. Source: [spacewell.com/ai-building-management/](https://spacewell.com/ai-building-management/)
- **eMaint by Fluke Reliability:** Strong CMMS with reliability, API, SCADA/PLC/BMS integration, and condition-monitoring adjacency; excluded because IBM Maximo covers the heavier industrial EAM/reliability lane. Source: [www.emaint.com/emaint-integrations-your-cmms-connected/](https://www.emaint.com/emaint-integrations-your-cmms-connected/)

## Evidence Sources By Function

| Source function | What it supports | Representative sources | Evidence weight | Stale-context handling |
| --- | --- | --- | --- | --- |
| Product facts and scope | Product category, buyer/user workflow, and core operational surface for each scored company. | IBM Maximo, Accruent product pages, Facilio, Planon, Runwise, BrainBox/Trane, 75F, GridPoint. | High | Official product pages were treated as current unless visibly stale; older pages were used only for stable product background. |
| Workflow and integration claims | APIs, integrations, system-of-record/action role, BMS/control-loop posture, and agent readiness. | Facilio MCP, 75F API, IBM Maximo, Accruent APIs, Runwise FAQ, GridPoint platform, Trane AI Control. | High | Explicit current integration claims were preferred; agent-readiness scores were conservative where public evidence showed automation but not delegated-agent governance. |
| Adoption and distribution signals | Customer footprint, installed building counts, global reach, acquisition/distribution channel, and funding/deployment context. | IBM, Accruent About, Runwise homepage/PR, GridPoint 2026 release, Trane/BrainBox releases, 75F funding release. | Medium-high | Latest official figures were preferred; older adoption claims were labeled as stale or used cautiously. |
| Trust, security, and governance claims | Certifications, auditability, RBAC, OAuth, encryption, SOC/ISO evidence, liability/accountability posture. | Accruent security, Planon Trust Center, BrainBox security, 75F security/SOC, Facilio security/privacy, IBM Cloud/Maximo security docs, Runwise terms. | High | Legal/security pages outweighed marketing copy; missing public SOC/ISO evidence reduced trust/governance scores. |
| AI and model-resilience claims | Whether better models strengthen the product or commoditize visible features. | IBM AI/APM pages, Facilio Atom/MCP, Planon AI-in-IWMS, Runwise AI article, Trane/BrainBox AI releases, 75F Saffron/API, GridPoint automation pages. | Medium-high | Dated 2025-2026 AI launches were weighted most; older or undated AI claims were treated as supporting context rather than decisive proof. |
