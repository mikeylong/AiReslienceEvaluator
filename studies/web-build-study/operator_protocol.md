# Web-Build Pilot Operator Protocol

Prepared April 14, 2026. This protocol was used for the recorded task runs in this repository and can also be reused for follow-on reruns.

## Operator Setup

- `operator_a`: Planned operator profile: design-forward frontend generalist who can use no-code tools comfortably.
- `operator_b`: Planned operator profile: frontend engineer comfortable with component systems, APIs, and handoff workflows.
- Operators should use the same machine class, browser, and network conditions where possible.
- Operators should not consult external tutorials mid-run.
- Tool order is pre-randomized in `task_metrics.csv`.

## Task 1: Net-new marketing page

- Timebox: `45` minutes
- Prompt: Create a responsive marketing page for Northstar Pediatrics, a subscription pediatric clinic. The page must include a hero, three benefit blocks, a pricing section, a testimonial, and a clear call to action for booking an intro call.

Acceptance criteria:
- Desktop and mobile layouts are usable.
- All five required sections exist.
- Brand tone feels healthcare-trustworthy rather than generic startup.
- The result is ready for stakeholder review without extra polishing outside the tool.

## Task 2: Governed revision and reuse

- Timebox: `60` minutes
- Prompt: Update the same project so the page supports three membership tiers, pulls testimonial and FAQ content from reusable structured content when available, adds a clinician profile section, and changes the primary CTA from booking to join waitlist.

Acceptance criteria:
- The update is applied without rebuilding the page from scratch.
- Reusable components, symbols, variables, or CMS content are used where the tool supports them.
- The design system stays visually consistent after the revision.
- The operator can identify a clear change history or reusable structure rather than only manual edits.

## Task 3: Publish or handoff

- Timebox: `60` minutes
- Prompt: Prepare the project for launch or developer handoff. Publish or generate the best available launch artifact, connect or simulate a custom domain or staging step if the product supports it, and document how a teammate or agent would safely make the next change.

Acceptance criteria:
- There is a clear publish, preview, export, or handoff artifact.
- The operator can point to versioning, roles, rollback, or approval behavior if the tool supports it.
- API, connector, repo, or agent hooks are exercised when available.
- A follow-up change path is documented well enough for another operator to continue safely.

## Metric Definitions

- `time_to_first_acceptable_output`: Minutes until the operator would show the artifact to a stakeholder without apology.
- `time_to_completion`: Minutes until the operator meets the task acceptance criteria or exhausts the timebox.
- `requirements_pass_rate`: Completed acceptance items divided by total acceptance items for that task.
- `manual_fix_count`: Count of noticeable manual repairs needed after the tool's initial generation or transformation.
- `structured_reuse`: `yes` if the operator used reusable components, variables, CMS, collections, or another structured abstraction; otherwise `no`.
- `publish_success`: `yes` if the operator produced a live preview, publish artifact, export, or handoff that another person could use immediately; otherwise `no`.
- `governance_support`: `0` to `3`, where `0` means no visible permissions, versioning, or rollback support and `3` means strong visible change controls.
- `agent_or_api_leverage`: `0` to `3`, where `0` means no meaningful agent, connector, API, or repo leverage and `3` means the operator used one of these to advance the task materially.

## Scoring Rule

Record measurements directly in `task_metrics.csv`. Do not backfill numbers from memory after the session. If a tool blocks on plan limits or authentication steps that the operator cannot complete, note the blocker in `notes` and mark the affected metric fields as blank.
