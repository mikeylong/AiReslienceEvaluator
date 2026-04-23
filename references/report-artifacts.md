# Report Artifact Requirements

Use these requirements when the `ai_resilience_evaluator` skill produces report artifacts.

## HTML Artifact

Default to a self-contained, paper-style report page with the 2x2 SVG as the first element, followed by the report title, metadata, abstract, score summary, section navigation, and full report body.

Tables must wrap text cleanly and avoid horizontal clipping where possible. The HTML must be shareable: use GitHub repository URLs or public source URLs instead of local filesystem paths, avoid `file://` links, and do not expose absolute user paths.

Add a footer with a generated timestamp and repository link in this format:

`Generated Apr 22, 2026 at 12:23 am &middot; GitHub repo`

Use the current local date/time for the timestamp and the repo remote or known public repository URL for the link. If no repository URL is available, omit the repo link rather than substituting a local path.

## Evidence Sources By Function

Add an `Evidence Sources By Function` appendix when the evaluation uses multiple source lanes. Use it to map source types to the claims they support, for example product facts and scope, workflow and integration claims, adoption and packaging signals, reliability and operational risk, trust and governance claims, qualitative reviewer context, controlled task evidence, and dated historical baselines.

For each row, include the source function, what it supports, representative sources, evidence weight, and how stale-context risk is handled. In the structured object, mirror this under `evidence_notes.sources_by_function` as objects with `function`, `supports`, `evidence_weight`, `stale_context_handling`, and `sources`.

## YouTube Review Transcript Evidence

For early entrants or sparse official evidence, use YouTube reviews only as third-party qualitative context. Prefer current videos with captions or transcripts, and capture title, publisher/channel, URL, publication date, transcript type, and how the evidence was used. Cross-check product facts against official sources. Do not treat YouTube transcript evidence as live task evidence or empirical parity with a controlled run unless the team actually performed the same task protocol.

When using YouTube transcript evidence, add a `YouTube Review Transcript Evidence` appendix after Evidence Notes. Use this shape:

- `Purpose`: why transcript evidence was used, usually early-product context or sparse official evidence.
- `Method`: search query/window, transcript source type, transcript pull date, and evidence weighting.
- `Sources`: a table with Target, Source, Publisher, Date, Transcript type, Evidence use, and URL.
- `Synthesis`: what the transcripts converged on, separating praise, friction, and reviewer uncertainty.
- `Scoring impact`: which factors gained confidence, which penalties were reinforced, and whether scores changed.
- `Limits`: state that transcripts are third-party qualitative evidence, not official claims or controlled empirical task evidence.

In the structured object, put transcript evidence under `evidence_notes.youtube_transcript_sources` as source objects with `target_name`, `title`, `publisher`, `published_date`, `url`, `transcript_type`, and `evidence_use`. Add `evidence_notes.youtube_transcript_method` and `evidence_notes.youtube_transcript_read`. Do not place local transcript file paths in the report object.

## SVG Artifact

Default to a plain black-and-white scalable SVG with no decorative effects, no fixed width or height, and a `viewBox` so the image scales cleanly.

Use the same quadrant labels and axis labels as the narrative. Add target markers with labels that always include the total score in `Name (xx/75)` form. Keep dashed divider lines neutral grey if you use them.

Keep quadrant labels visually subordinate and anchored on the frame edges or corners. Do not place descriptive quadrant subtitles inside the plotting area when they reduce marker readability. Place rotated y-axis labels in the gutter immediately adjacent to the axis line, not in the outer page margin, and center them vertically within their respective upper and lower halves of the axis.

If only one target is evaluated, plot that single point. If labels collide, do not stack text on top of markers. Move labels into left or right gutters, stack them with consistent spacing, and use simple leader lines or a compact legend so every label remains readable. If literal SVG generation is unavailable, return a compact plotting spec with axis labels, coordinates, and label text as the fourth artifact.
