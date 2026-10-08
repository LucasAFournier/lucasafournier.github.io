#!/usr/bin/env python3
"""Dependency-free checks for an intentionally tiny public Quarto site.

This catches obvious mistakes; it cannot prove that research content is public.
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("index", "research", "publications")


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in (("href",) if tag == "a" else ("src",) if tag in ("img", "script") else ()):
            value = attrs.get(key)
            if value:
                self.links.append(value)


def preflight():
    profile = (ROOT / "profile.yml").read_text(encoding="utf-8")
    content = "\n".join((ROOT / (page + ".qmd")).read_text(encoding="utf-8") for page in PAGES)
    banned = {
        "Your Name": "Set the public name in profile.yml",
        "Your institution": "Set the public affiliation in profile.yml",
        "hello@example.org": "Set the public email in profile.yml",
        "your-username": "Set the public GitHub username in profile.yml",
        "[your ": "Replace bracketed content placeholders in QMD pages",
        "[your": "Replace bracketed content placeholders in QMD pages",
        "[First research theme]": "Complete research.qmd",
        "[Second research theme]": "Complete research.qmd",
        "[What interests you": "Complete research.qmd",
        "[Briefly describe": "Complete research.qmd",
    }
    problems = [message for token, message in banned.items() if token in (profile + content)]
    if problems:
        for message in sorted(set(problems)):
            print("ERROR:", message)
        raise SystemExit(1)
    print("PASS: obvious public profile/content placeholders cleared")


def rendered():
    site = ROOT / "_site"
    problems = []
    for page in PAGES:
        html_path = site / (page + ".html")
        if not html_path.is_file():
            problems.append("Missing rendered page: " + str(html_path))
            continue
        text = html_path.read_text(encoding="utf-8")
        if "<html" not in text.lower():
            problems.append("Invalid-looking HTML: " + html_path.name)
        if page == "index" and "about-trestles" not in text:
            # Quarto's HTML has an about container class when the template renders.
            problems.append("Home page does not appear to contain the Trestles about layout")
        parser = LocalLinks()
        parser.feed(text)
        for url in parser.links:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or url.startswith(("#", "/", "//")):
                continue
            local = (html_path.parent / unquote(parts.path)).resolve()
            if parts.path and not local.is_file() and not local.is_dir():
                problems.append(f"Broken local link in {html_path.name}: {url}")
    if problems:
        for problem in problems:
            print("ERROR:", problem)
        raise SystemExit(1)
    print("PASS: rendered pages exist, Trestles layout present, local links resolve")


if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    mode = argp.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--rendered", action="store_true")
    args = argp.parse_args()
    preflight() if args.preflight else rendered()
