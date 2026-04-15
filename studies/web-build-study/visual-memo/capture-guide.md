# Visual Memo Capture Guide

This folder holds the screenshot inputs for the `web-build-study` visual memo. The HTML artifact is generated from the study data plus the local screenshots listed in [screenshot-manifest.json](/Users/mike/AiReslienceEvaluator/studies/web-build-study/visual-memo/screenshot-manifest.json).

The current memo renders one designated hero shot per offering. Keep the `hero` flag accurate in the manifest when recapturing.

## Rules

- Capture at desktop width.
- Use the live study artifacts, not marketing pages.
- Keep the screenshot count fixed at 12 total, 2 per offering.
- If an authenticated session expires, refresh auth before rebuilding the memo.
- If any required screenshot is missing, the generator should fail instead of silently degrading.

## Public captures

- `wix-studio-outcome`: `https://aistudy7.wixsite.com/professional-service`
- `webflow-outcome`: `https://northstar-pediatrics.webflow.io/`
- `figma-make-outcome`: `https://terra-low-46188087.figma.site/`
- `lovable-outcome`: `https://092ce542-4269-450c-9f47-b0d7206d618b.lovableproject.com/`

## Authenticated captures

- `wix-studio-blocker`: Wix Harmony editor with the Aria recommendation to add `Wix Pricing Plans`
- `webflow-blocker`: the failed `design/undefined` result from the AI-builder path
- `figma-make-workflow`: Figma Make publish or governed workflow dialog
- `lovable-blocker`: Lovable `Daily limit reached` dialog
- `figma-sites-mismatch`: Figma Sites code-oriented blank-site path
- `figma-sites-publish-blocker`: Figma Sites `You can’t publish on the Starter plan` dialog
- `framer-outcome`: Framer Wireframer desktop canvas showing the generated Northstar page
- `framer-blocker`: Framer editor showing the manual or template-first project path from the earlier pass

## Rebuild

After the screenshots are in place:

```bash
python3 /Users/mike/AiReslienceEvaluator/scripts/generate_web_build_visual_memo.py
```

The generated artifact will be written to [index.html](/Users/mike/AiReslienceEvaluator/studies/web-build-study/visual-memo/index.html).
