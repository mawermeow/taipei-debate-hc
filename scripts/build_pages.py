#!/usr/bin/env python3
"""Stage only public website files for GitHub Pages. No dependencies required."""

import json
import shutil
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "_site"
PUBLIC_FILES = (
    "index.html",
    "app.js",
    "style.css",
    "data.json",
    "provenance.json",
    ".nojekyll",
)


class CandidateOptions(HTMLParser):
    """Catch malformed option tags before publishing the candidate filter."""

    def __init__(self):
        super().__init__()
        self.in_candidates = False
        self.values = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "select":
            self.in_candidates = attrs.get("id") == "candidate-filter"
        elif tag == "option" and self.in_candidates:
            self.values.append(attrs.get("value"))

    def handle_endtag(self, tag):
        if tag == "select":
            self.in_candidates = False


def validate_candidate_filter(html):
    parser = CandidateOptions()
    parser.feed(html)
    if parser.values != ["all", "s", "j"]:
        raise ValueError("Candidate filter must contain all, s (沈伯洋), and j (蔣萬安) options")


def main():
    # Validate inputs before changing the previously generated artifact.
    for name in PUBLIC_FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(f"Missing website file: {name}")
    for name in ("data.json", "provenance.json"):
        json.loads((ROOT / name).read_text(encoding="utf-8"))

    validate_candidate_filter((ROOT / "index.html").read_text(encoding="utf-8"))

    if OUTPUT.is_symlink():
        raise RuntimeError("Refusing to write through an _site symlink")
    OUTPUT.mkdir(exist_ok=True)
    # Remove stale generated files so old content cannot remain published.
    for entry in OUTPUT.iterdir():
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry)
        else:
            entry.unlink()
    for name in PUBLIC_FILES:
        shutil.copy2(ROOT / name, OUTPUT / name)
    print(f"Staged {len(PUBLIC_FILES)} public files in {OUTPUT}")


if __name__ == "__main__":
    main()
