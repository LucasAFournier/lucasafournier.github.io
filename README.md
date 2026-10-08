# Minimal academic website · Trestles + Morph

A small Quarto site with a **Trestles** homepage, **Morph** theme, three public pages, BibTeX bibliography source, and GitHub Actions. It builds on GitHub: Windows is not part of the deployment process, and switching to Linux only requires cloning the repo.

## Before publishing (required)

1. Create a **public** GitHub repository named `<username>.github.io` (or use another repo name for a project site).
2. Upload the **contents** of this repository, preserving `.github/workflows/site.yml` and hidden files.
3. Replace the placeholder **name, affiliation, email and GitHub URL** in `profile.yml` with information you approve for publication. `profile.yml` also supplies the homepage title, Trestles layout, illustration and profile links.
4. Replace **all bracketed text** in `index.qmd` and `research.qmd` with your own approved public descriptions. The CI deliberately fails while obvious placeholders remain. No publication or personal fact has been invented for you.
5. Review `assets/profile-abstract.svg`; it is a generic graphic, not a photograph. To use your own photo, add `assets/portrait.jpg` and change the `about.image` field in `profile.yml` plus `image-alt` text.
6. Go to **Settings → Pages → Build and deployment → Source → GitHub Actions**.
7. Commit the completed files to `main`; the workflow will validate and deploy the site. Verify the first site at `https://<username>.github.io/` (for a user site).
8. **Protect `main` immediately after the initial push**: in Settings → Rules → Rulesets, require PRs and the `Build and validate` check. Ensure your own merge is possible but direct pushes are blocked. Also restrict the `github-pages` environment to `main` where available. Repository rules, not `AGENTS.md`, enforce approval.

> A public GitHub repository exposes its entire tracked history, not just the rendered website. Never commit private materials, even temporarily.

## Everyday use

- Edit page content in `.qmd`; edit homepage identity and profile links in `profile.yml`.
- Change site navigation or theme in `_quarto.yml` and typography in `styles.scss`.
- If you have Quarto installed locally, run `quarto preview` to view changes and `quarto render` to build.
- The `Build and validate` job renders each pull request without deployment. Only pushes to `main` can deploy; protect that branch before allowing agents to make changes.
- Coding agents should obey `AGENTS.md`, use branches, and create PRs you review before merging.

## Publications / Zotero

`publications.bib` is intentionally empty. Once approved public BibTeX entries are present, uncomment `nocite: |` and `@*` in `publications.qmd` and replace the waiting message. Later use Better BibTeX to auto-export **only a curated public collection** into this file on your local machine; that file change is not automatically merged or deployed.

## Optional: Linux transition

```bash
git clone https://github.com/USERNAME/USERNAME.github.io.git
cd USERNAME.github.io
quarto preview
```

Install Git, Quarto and (optionally) Codex CLI on your Linux laptop. No platform-specific scripts or automatic synchronizations need to be transferred from Windows.

## Files

```text
_quarto.yml                   # Site navigation, Morph theme, static build
profile.yml                   # Approved public homepage metadata
index.qmd                     # Native Trestles About homepage
research.qmd                  # Research interests
publications.qmd / .bib       # Curated publications
styles.scss                   # Small typography tweaks
assets/profile-abstract.svg   # Generic replaceable artwork
AGENTS.md                     # Agent editing, preservation & privacy rules
scripts/check_site.py         # CI placeholder, page & link checks
.github/workflows/site.yml    # PR check / main deploy
.gitignore                    # Never commit site output
```

## References

- [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
