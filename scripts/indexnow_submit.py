#!/usr/bin/env python3
"""Submit only changed canonical public URLs to IndexNow.

Designed for alignmentconstraint.org on GitHub Pages. The safety model is intentionally
conservative: a URL must be present in the current or previous sitemap.txt, must use the
canonical HTTPS host, and must not look like a draft/private/staging URL.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

SITE_ORIGIN = "https://alignmentconstraint.org"
SITE_HOST = "alignmentconstraint.org"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"

# These are infrastructure endpoints, not content URLs to notify via IndexNow.
INFRASTRUCTURE_PATHS = {
    "/robots.txt",
    "/sitemap.xml",
    "/sitemap.txt",
}

# A change here can alter rendered metadata/content across many public HTML pages.
SITEWIDE_FILES = {
    "_config.yml",
}
SITEWIDE_PREFIXES = (
    "_includes/",
    "_layouts/",
    "_data/",
)

# Cosmetic/static-asset-only edits do not need IndexNow notifications by themselves.
IGNORED_PREFIXES = (
    ".github/",
    "scripts/",
    "assets/",
)

NONPUBLIC_SEGMENTS = {
    "draft",
    "drafts",
    "_drafts",
    "private",
    "staging",
    "preview",
    "previews",
}

KEY_RE = re.compile(r"^[A-Za-z0-9-]{8,128}$")


def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout


def git_show(ref: str, path: str) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return proc.stdout if proc.returncode == 0 else None


def load_sitemap_text(text: str | None) -> set[str]:
    urls: set[str] = set()
    if not text:
        return urls
    for raw in text.splitlines():
        url = raw.strip()
        if url and is_safe_canonical_url(url):
            urls.add(url)
    return urls


def is_safe_canonical_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
    except ValueError:
        return False
    if parsed.scheme != "https" or parsed.netloc != SITE_HOST:
        return False
    if parsed.username or parsed.password or parsed.port:
        return False
    if parsed.query or parsed.fragment:
        return False
    path = parsed.path or "/"
    if path in INFRASTRUCTURE_PATHS:
        return False
    segments = {seg.lower() for seg in path.split("/") if seg}
    if segments & NONPUBLIC_SEGMENTS:
        return False
    return True


def is_html_page_url(url: str) -> bool:
    path = urlparse(url).path
    return path == "/" or path.endswith("/")


def parse_front_matter(text: str | None) -> dict[str, str]:
    if not text:
        return {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        out[key.strip()] = value
    return out


def markdown_url(path: str, content: str | None) -> str | None:
    if path == "index.md":
        return SITE_ORIGIN + "/"
    fm = parse_front_matter(content)
    if fm.get("published", "").lower() == "false":
        return None
    if fm.get("indexable", "").lower() == "false":
        return None
    permalink = fm.get("permalink")
    if not permalink or not permalink.startswith("/"):
        return None
    return SITE_ORIGIN + permalink


def changed_paths(base: str, head: str) -> list[tuple[str, list[str]]]:
    text = git("diff", "--name-status", "--find-renames", base, head, "--")
    changes: list[tuple[str, list[str]]] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        paths = parts[1:]
        changes.append((status, paths))
    return changes


def direct_file_url(path: str) -> str:
    return f"{SITE_ORIGIN}/{path}"


def add_if_allowlisted(target: set[str], url: str | None, allowlist: set[str]) -> None:
    if url and url in allowlist and is_safe_canonical_url(url):
        target.add(url)


def determine_urls(base: str, head: str) -> tuple[list[str], list[str]]:
    current_sitemap_text = git_show(head, "sitemap.txt")
    previous_sitemap_text = git_show(base, "sitemap.txt")
    current = load_sitemap_text(current_sitemap_text)
    previous = load_sitemap_text(previous_sitemap_text)

    if not current:
        raise RuntimeError("Current sitemap.txt is missing or contains no safe canonical URLs.")

    urls: set[str] = set()
    reasons: list[str] = []

    # New/removed sitemap entries are themselves meaningful discovery changes.
    for url in current - previous:
        urls.add(url)
        reasons.append(f"sitemap added: {url}")
    for url in previous - current:
        urls.add(url)
        reasons.append(f"sitemap removed: {url}")

    changes = changed_paths(base, head)

    sitewide = False
    for status, paths in changes:
        for path in paths:
            if path in SITEWIDE_FILES or path.startswith(SITEWIDE_PREFIXES):
                sitewide = True
                reasons.append(f"sitewide rendered metadata/content changed: {path}")

    if sitewide:
        # Submit rendered HTML pages only. Machine-readable files are handled when those
        # exact files change, rather than being resubmitted for a shared layout change.
        urls.update(url for url in current if is_html_page_url(url))

    for status, paths in changes:
        code = status[0]
        old_path = paths[0] if code in {"D", "R"} else None
        new_path = paths[-1] if code in {"A", "M", "R", "C"} else None

        # Skip changes that cannot independently alter indexable content.
        if all(p.startswith(IGNORED_PREFIXES) for p in paths):
            continue
        if any(p in SITEWIDE_FILES or p.startswith(SITEWIDE_PREFIXES) for p in paths):
            continue

        if new_path:
            new_content = git_show(head, new_path)
            if new_path.endswith(".md"):
                add_if_allowlisted(urls, markdown_url(new_path, new_content), current)
            else:
                add_if_allowlisted(urls, direct_file_url(new_path), current)

        if old_path:
            old_content = git_show(base, old_path)
            if old_path.endswith(".md"):
                add_if_allowlisted(urls, markdown_url(old_path, old_content), previous)
            else:
                add_if_allowlisted(urls, direct_file_url(old_path), previous)

    safe_urls = sorted(url for url in urls if is_safe_canonical_url(url))
    return safe_urls, reasons


def validate_key_file(key_file: Path) -> str:
    if not key_file.is_file():
        raise RuntimeError(f"IndexNow key file not found: {key_file}")
    key = key_file.read_text(encoding="utf-8").strip()
    if not KEY_RE.fullmatch(key):
        raise RuntimeError("IndexNow key must be 8-128 characters using only letters, numbers, or dashes.")
    if key_file.name != f"{key}.txt":
        raise RuntimeError("IndexNow root key filename must be exactly <key>.txt.")
    return key


def submit(urls: list[str], key: str, endpoint: str) -> int:
    payload = {
        "host": SITE_HOST,
        "key": key,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            code = response.getcode()
            body = response.read().decode("utf-8", errors="replace").strip()
    except urllib.error.HTTPError as exc:
        code = exc.code
        body = exc.read().decode("utf-8", errors="replace").strip()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"IndexNow network error: {exc}") from exc

    print(f"IndexNow response: HTTP {code}" + (f" — {body}" if body else ""))
    if code not in {200, 202}:
        raise RuntimeError(
            "IndexNow submission was not accepted. Common meanings: "
            "400 invalid format, 403 key verification failure, 422 host/key mismatch, 429 too many requests."
        )
    return code


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="Previous deployed commit/revision")
    parser.add_argument("--head", required=True, help="Successfully deployed commit/revision")
    parser.add_argument("--key-file", required=True, type=Path)
    parser.add_argument("--endpoint", default=INDEXNOW_ENDPOINT)
    parser.add_argument("--dry-run", action="store_true", help="Print URLs but do not submit")
    args = parser.parse_args()

    try:
        key = validate_key_file(args.key_file)
        # Verify the base exists before computing a diff. Fail closed rather than submitting the whole site.
        git("rev-parse", "--verify", args.base)
        git("rev-parse", "--verify", args.head)
        urls, reasons = determine_urls(args.base, args.head)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Deployed revision: {args.head}")
    print(f"Compared with: {args.base}")
    if reasons:
        print("Change signals:")
        for reason in reasons:
            print(f"  - {reason}")

    if not urls:
        print("No changed canonical public URLs qualify for IndexNow submission. Nothing to do.")
        return 0

    print(f"Qualified canonical URLs ({len(urls)}):")
    for url in urls:
        print(f"  {url}")

    if args.dry_run:
        print("Dry run only; no IndexNow request sent.")
        return 0

    try:
        submit(urls, key, args.endpoint)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
