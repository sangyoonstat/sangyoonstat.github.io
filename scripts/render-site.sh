#!/usr/bin/env bash

set -euo pipefail

quarto render

cp _site/*.html .
cp _site/robots.txt _site/search.json _site/sitemap.xml .
mkdir -p site_libs assets/site
rsync -a --delete _site/site_libs/ site_libs/
rsync -a _site/assets/site/ assets/site/
