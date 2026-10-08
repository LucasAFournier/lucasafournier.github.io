# Website agent contract

This repository is an **approved-public-only**, minimal Quarto academic website.
Read this file before editing anything. Its rules apply to cloud and local agents.

## Sources and scope
- `profile.yml`: the authoritative public profile, homepage title, contact links and Trestles image.
- `index.qmd`, `research.qmd`, `publications.qmd`: public-facing text only.
- `publications.bib`: exclusively approved, publicly released items.
- `_quarto.yml` and `styles.scss`: configuration and restrained Morph customization.
- No private research, notes, PDFs, datasets, credentials or manuscript drafts may enter the repo, including its Git history, even temporarily.
- Do not read or copy from private Zotero collections, private research wikis or local directories unless the human explicitly supplies approved public extracts for this task.
- If publication status or accuracy is uncertain, stop and request a decision.

## Content preservation
- Preserve every existing approved fact, citation, URL, section and substantive claim unless the request explicitly authorizes changing it.
- Do not invent affiliations, degrees, publications, grants, collaborators, dates, project results, or biography details.
- Do not silently paraphrase, truncate, remove, or translate existing content.
- Keep changes small and task-scoped. Avoid additional frameworks, remote assets, analytics, plugins or build dependencies without approval.
- Prefer native Quarto/Markdown/SCSS and relative `.qmd` links.

## Verification before proposing a PR
1. Run `python scripts/check_site.py --preflight` after the human has filled placeholders.
2. Run `quarto render`, then `python scripts/check_site.py --rendered`.
3. Run `git diff --check` and inspect `git diff` (including new files) for correctness and privacy.
4. For visual/layout changes, examine mobile (~390px) and desktop (~1280px) views, links and keyboard navigation. Attach screenshots where browser tools are available; explicitly disclose checks that could not run.
5. Report changed files, preservation decisions, test results and remaining uncertainties in the PR description. Never claim to have run a check that did not run.

## Publication gate
- Work in a branch; present a pull request for human review.
- Never force-push to `main`, merge your own PR, modify branch protections, trigger deployment, or bypass checks.
- Only human-reviewed changes may be merged into protected `main`; GitHub Actions deploys that branch.
- These instructions are *not* a technical security boundary: repository rulesets and Pages environment protection must be configured in GitHub.
