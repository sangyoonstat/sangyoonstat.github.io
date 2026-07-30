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
