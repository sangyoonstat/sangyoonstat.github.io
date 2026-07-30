# Sangyoon Yi - Academic Website

This repository contains the source for [sangyoonstat.github.io](https://sangyoonstat.github.io), built with [Quarto](https://quarto.org/).

## Updating the site

The main pages are ordinary Quarto Markdown files:

- `index.qmd` - homepage
- `research.qmd` - research interests, publications, and preprints
- `teaching.qmd` - courses

Site-wide navigation is in `_quarto.yml`, and visual styling is in `styles.css`.

To preview locally, install Quarto and run:

```bash
quarto preview
```

Before committing an update, render the site and refresh the static files served by GitHub Pages:

```bash
bash scripts/render-site.sh
```

Commit both the edited `.qmd` source and the generated `.html`/`site_libs` files.
Pushing to `master` publishes the pre-rendered files through the repository's existing GitHub Pages configuration.

### Editing on GitHub.com

The recommended browser-only workflow is:

1. Open the `.qmd` source file on GitHub and click the pencil icon.
2. Make the change and choose **Create a new branch for this commit and start a pull request**.
3. Open the pull request and wait for the **Render Quarto website** check to pass.
4. Merge the pull request into `master`.
5. The workflow renders the site, validates it, and commits any refreshed static files automatically.

For a new preprint, edit `research.qmd` and add an item under **Publications and Preprints**:

```markdown
1. **[Paper title](https://arxiv.org/abs/ARXIV-ID)** With A. Author and B. Author.
```

Use `1.` for every publication entry. Markdown creates the displayed numbering automatically, so existing entries do not need to be renumbered.
