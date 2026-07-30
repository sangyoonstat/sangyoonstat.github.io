#!/usr/bin/env python3

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class ReferenceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for key in ("href", "src"):
            if key in attributes:
                self.references.append((key, attributes[key]))


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    expected_pages = {
        "index.html",
        "research.html",
        "teaching.html",
    }

    missing_pages = sorted(page for page in expected_pages if not (root / page).is_file())
    if missing_pages:
        raise SystemExit(f"Missing rendered pages: {', '.join(missing_pages)}")

    missing_targets = []
    forbidden_hits = []
    forbidden_text = ("Sangyoon_Yi_CV.pdf", "301-G", "74078-1056")

    for page in sorted(root.glob("*.html")):
        content = page.read_text(encoding="utf-8")
        for text in forbidden_text:
            if text in content:
                forbidden_hits.append(f"{page.name}: {text}")

        parser = ReferenceParser()
        parser.feed(content)
        for key, value in parser.references:
            parsed = urlparse(value)
            if parsed.scheme or value.startswith(("#", "//", "mailto:", "tel:", "data:")):
                continue

            relative_path = unquote(parsed.path)
            if not relative_path:
                continue

            target = page.parent / relative_path
            if relative_path.endswith("/"):
                target /= "index.html"
            if not target.exists():
                missing_targets.append(f"{page.name}: {key}={value}")

    if missing_targets:
        raise SystemExit("Missing local targets:\n" + "\n".join(missing_targets))
    if forbidden_hits:
        raise SystemExit("Restricted public content found:\n" + "\n".join(forbidden_hits))
    if list(root.rglob("*.pdf")):
        raise SystemExit("A PDF file is present in the rendered public site.")

    print(
        f"Validated {len(expected_pages)} pages: "
        "all local targets resolve and restricted content is absent."
    )


if __name__ == "__main__":
    main()
