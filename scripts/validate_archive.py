#!/usr/bin/env python3
"""
Alignment Constraint Archive — local quality validator.

This script is intentionally READ-ONLY:
- It never edits repository files.
- It never makes network requests.
- It uses only the Python standard library.

Run from the repository root:
    python3 scripts/validate_archive.py

Exit codes:
    0 = PASS (GitHub Actions shows a green check)
    1 = FAIL (GitHub Actions shows a red X)
"""

from __future__ import annotations

import json
import os
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urljoin, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_HOSTS = {"alignmentconstraint.org", "www.alignmentconstraint.org"}

PUBLIC_DIRS = {
    "apply",
    "cite",
    "core",
    "empirical",
    "open-problems",
    "proof-program",
    "public",
    "series-1",
    "series-2",
    "series-3",
    "specialist-handoff",
    "toys",
    "zh",
}

SKIP_TOP_LEVEL_DIRS = {
    ".git",
    ".github",
    "_site",
    "node_modules",
    "scripts",
    "vendor",
}

SKIP_FILES = {
    "ARCHIVE_QC_README.md",
}

# DOI placeholders are intentionally NOT listed here. They are authorized
# pending Session 4 fields until the real DOI records exist.
FORBIDDEN_PLACEHOLDERS = (
    "YOUR-" + "DOMAIN",
    "YOUR-" + "GITHUB-USERNAME",
    "YOUR " + "NAME HERE",
    "FILENAME-" + "HERE",
    "ARTICLE " + "TITLE HERE",
    "FULL " + "MEDIUM URL",
)

OBSOLETE_PATHS = {
    "/series-1/" + "system-aware-attractor/":
        "use /series-1/aligned-intelligence-converges-toward/",
    "series-3/" + "series-3-technical-companion.md":
        "use series-3/technical-companion.md",
    "series-3-" + "technical-companion.md":
        "use series-3/technical-companion.md",
    "TC2_" + "final.md":
        "use the canonical Series 2 Technical Companion URL/path",
}

MAJOR_PROOF_STATUS_FILES = (
    "README.md",
    "index.md",
    "llms.txt",
    "llms-full.txt",
    "AGENTS.md",
    "agent-index.json",
    "open-problems.json",
    "claim-graph.json",
    "core/proof-status.md",
    "core/stability-assumption.md",
    "core/for-researchers.md",
    "public/op4d-counterexample-challenge.md",
    "open-problems/index.md",
    "specialist-handoff/index.md",
)

CAUTION_MARKERS = (
    "candidate",
    "not theorem closure",
    "without theorem closure",
    "not a theorem",
    "not proven",
    "not proved",
    "not proof",
    "unproven",
    "independent specialist verification",
    "independent specialist review",
    "does not certify closure",
    "not established",
    "formal verification required",
)

TEXT_SUFFIXES = {
    ".md", ".markdown", ".txt", ".json", ".xml", ".yml", ".yaml",
    ".cff", ".html", ".htm",
}

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(\s*([^)]+?)\s*\)")
MARKDOWN_BLANK_ALT_RE = re.compile(r"!\[\s*\]\(")
HTML_IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE | re.DOTALL)
ATX_H1_RE = re.compile(r"^\s*#(?!#)\s+(.+?)\s*$", re.MULTILINE)
STAGE4_RE = re.compile(r"\bstage\s*4\b", re.IGNORECASE)


ALLOWED_SCHEMA_TYPES = {
    "WebSite", "WebPage", "CreativeWorkSeries", "ScholarlyArticle",
    "TechArticle", "Article", "DefinedTermSet", "DefinedTerm", "Person",
}

CENTRAL_STRUCTURED_DATA_FILES = (
    "_data/page_metadata.json",
    "_includes/head.html",
    "_includes/structured-data.html",
    "_includes/highwire-meta.html",
)


@dataclass(frozen=True)
class Issue:
    check: str
    path: str
    message: str
    line: int | None = None


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def should_skip(path: Path) -> bool:
    try:
        parts = path.relative_to(REPO_ROOT).parts
    except ValueError:
        return True
    if not parts:
        return False
    if parts[0] in SKIP_TOP_LEVEL_DIRS:
        return True
    return path.name in SKIP_FILES


def iter_repo_files():
    for path in REPO_ROOT.rglob("*"):
        if path.is_file() and not should_skip(path):
            yield path


def iter_text_files():
    for path in iter_repo_files():
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def is_page_markdown(path: Path) -> bool:
    if path.suffix.lower() not in {".md", ".markdown"}:
        return False
    rp = path.relative_to(REPO_ROOT)
    if rp.as_posix() == "index.md":
        return True
    if path.name.lower() == "readme.md":
        return False
    return bool(rp.parts and rp.parts[0] in PUBLIC_DIRS)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def line_at(text: str, index: int) -> int:
    return text.count("\n", 0, max(0, index)) + 1


def strip_markdown_heading_markup(value: str) -> str:
    value = re.sub(r"\s+#+\s*$", "", value.strip())
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return re.sub(r"\s+", " ", value).strip().casefold()


def normalize_title(value: object) -> str:
    return strip_markdown_heading_markup(str(value or ""))


def normalize_permalink(value: str) -> str:
    parsed = urlparse(value.strip())
    path = parsed.path or "/"
    if not path.startswith("/"):
        path = "/" + path
    path = re.sub(r"/+", "/", path)
    # Treat /foo and /foo/ as the same page, but preserve file-like routes.
    last = path.rsplit("/", 1)[-1]
    if path != "/" and "." not in last and not path.endswith("/"):
        path += "/"
    return path


def strict_simple_yaml_check(front: str) -> list[str]:
    """
    Validate the conservative YAML subset used by this archive's front matter.

    This avoids a third-party dependency and therefore avoids package downloads
    during the push-time check. GitHub Pages/Jekyll remains the final YAML parser.

    Accepted:
    - root-level key: value pairs
    - quoted or plain scalar values
    - block scalars using | or >
    - indented continuation/nested lines
    - comments and blank lines
    """
    problems: list[str] = []
    lines = front.splitlines()
    root_key_seen = False
    block_indent: int | None = None

    for n, raw in enumerate(lines, start=1):
        if "\t" in raw:
            problems.append(f"front matter line {n} contains a tab; use spaces")
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(raw) - len(raw.lstrip(" "))

        if block_indent is not None:
            if indent >= block_indent:
                continue
            block_indent = None

        if indent > 0:
            # Indented YAML is allowed as continuation/nesting.
            continue

        m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", raw)
        if not m:
            problems.append(
                f"front matter line {n} is not a valid root 'key: value' line"
            )
            continue

        root_key_seen = True
        value = m.group(2).strip()

        if value in {"|", ">", "|-", "|+", ">-", ">+"}:
            block_indent = 1
            continue

        if value.startswith('"') and not re.search(r'(?<!\\)"\s*$', value):
            problems.append(f"front matter line {n} has an unclosed double quote")
        if value.startswith("'") and not value.endswith("'"):
            problems.append(f"front matter line {n} has an unclosed single quote")

        # Catch the most common accidental one-line collapse inside a scalar.
        if " --- " in value and re.search(r"\b(title|permalink|description)\s*:", value):
            problems.append(
                f"front matter line {n} appears to contain collapsed front-matter fields"
            )

    if front.strip() and not root_key_seen:
        problems.append("front matter has no root-level keys")
    return problems


def parse_simple_frontmatter_mapping(front: str) -> dict[str, str]:
    """Extract the root scalar fields needed by this validator."""
    result: dict[str, str] = {}
    for raw in front.splitlines():
        if not raw or raw[0].isspace() or raw.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", raw)
        if not m:
            continue
        key, value = m.groups()
        value = value.strip()
        if len(value) >= 2 and (
            (value.startswith('"') and value.endswith('"')) or
            (value.startswith("'") and value.endswith("'"))
        ):
            value = value[1:-1]
        result[key] = value
    return result


def parse_frontmatter(path: Path) -> tuple[dict[str, str] | None, str, int, list[Issue]]:
    text = read_text(path)
    issues: list[Issue] = []

    if not text:
        issues.append(Issue("front matter", rel(path), "file is empty", 1))
        return None, "", 1, issues

    first_line = text.splitlines()[0] if text.splitlines() else ""
    if first_line.startswith("---") and first_line != "---":
        issues.append(Issue(
            "collapsed front matter",
            rel(path),
            "front matter opening delimiter must be alone on its own line",
            1,
        ))
        return None, text, 1, issues

    if not text.startswith("---\n"):
        issues.append(Issue(
            "front matter",
            rel(path),
            "public Markdown page must begin with a YAML front-matter block",
            1,
        ))
        return None, text, 1, issues

    lines = text.splitlines(keepends=True)
    closing_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            closing_index = i
            break

    if closing_index is None:
        issues.append(Issue(
            "front matter",
            rel(path),
            "front matter has no closing '---' delimiter",
            1,
        ))
        return None, text, 1, issues

    front = "".join(lines[1:closing_index])
    for problem in strict_simple_yaml_check(front):
        issues.append(Issue(
            "front matter",
            rel(path),
            problem,
            2,
        ))

    mapping = parse_simple_frontmatter_mapping(front)
    body = "".join(lines[closing_index + 1:])
    body_start_line = closing_index + 2

    if not mapping.get("title", "").strip():
        issues.append(Issue(
            "front matter",
            rel(path),
            "public page is missing a non-empty 'title:' field",
            2,
        ))

    # Root index intentionally publishes at / without a permalink field.
    if rel(path) != "index.md" and not mapping.get("permalink", "").strip():
        issues.append(Issue(
            "front matter",
            rel(path),
            "public page is missing a non-empty 'permalink:' field",
            2,
        ))

    return mapping, body, body_start_line, issues


def inferred_route(path: Path) -> str:
    rp = path.relative_to(REPO_ROOT).as_posix()
    if rp == "index.md":
        return "/"
    if rp.endswith("/index.md"):
        return "/" + rp[:-len("index.md")]
    if rp.endswith(".md"):
        return "/" + rp[:-3] + "/"
    if rp.endswith(".markdown"):
        return "/" + rp[:-9] + "/"
    return "/" + rp


def collect_pages():
    issues: list[Issue] = []
    page_data: dict[Path, tuple[dict[str, str], str, int]] = {}
    permalinks: dict[str, Path] = {}

    for path in sorted(iter_repo_files()):
        if not is_page_markdown(path):
            continue

        mapping, body, body_start, page_issues = parse_frontmatter(path)
        issues.extend(page_issues)
        if mapping is None:
            continue

        page_data[path] = (mapping, body, body_start)

        raw_permalink = mapping.get("permalink", "").strip()
        route = "/" if rel(path) == "index.md" else (
            normalize_permalink(raw_permalink) if raw_permalink else inferred_route(path)
        )

        if route in permalinks:
            issues.append(Issue(
                "unique permalinks",
                rel(path),
                f"permalink {route!r} is already used by {rel(permalinks[route])}",
                2,
            ))
        else:
            permalinks[route] = path

    return page_data, permalinks, issues


def check_json_files() -> list[Issue]:
    issues: list[Issue] = []
    for path in sorted(iter_repo_files()):
        if path.suffix.lower() != ".json":
            continue
        try:
            json.loads(read_text(path))
        except Exception as exc:
            issues.append(Issue(
                "valid JSON",
                rel(path),
                f"invalid JSON: {exc}",
                None,
            ))
    return issues


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def canonical_path_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc.casefold() not in CANONICAL_HOSTS:
        return None
    path = unquote(parsed.path or "/")
    if not path.startswith("/"):
        path = "/" + path
    return normalize_permalink(path) if "." not in path.rsplit("/", 1)[-1] else path


def existing_static_routes() -> set[str]:
    routes = set()
    for path in iter_repo_files():
        rp = path.relative_to(REPO_ROOT).as_posix()
        routes.add("/" + rp)
    return routes


def route_exists(path: str, page_routes: set[str], static_routes: set[str]) -> bool:
    if not path:
        return True
    path = unquote(path)
    if not path.startswith("/"):
        path = "/" + path

    # File-like routes map directly to repository files.
    last = path.rsplit("/", 1)[-1]
    if "." in last:
        return path in static_routes

    normalized = normalize_permalink(path)
    return normalized in page_routes


def check_sitemaps(page_routes: set[str], static_routes: set[str]) -> list[Issue]:
    issues: list[Issue] = []
    xml_path = REPO_ROOT / "sitemap.xml"
    txt_path = REPO_ROOT / "sitemap.txt"

    xml_urls: list[str] = []
    txt_urls: list[str] = []

    if not xml_path.exists():
        issues.append(Issue("sitemap XML", "sitemap.xml", "file is missing", None))
    else:
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
            if local_name(root.tag) != "urlset":
                issues.append(Issue(
                    "sitemap XML",
                    "sitemap.xml",
                    "root element must be <urlset>",
                    1,
                ))
            for elem in root.iter():
                if local_name(elem.tag) == "loc" and elem.text:
                    xml_urls.append(elem.text.strip())
        except Exception as exc:
            issues.append(Issue(
                "sitemap XML",
                "sitemap.xml",
                f"invalid XML: {exc}",
                None,
            ))

    if txt_path.exists():
        txt_urls = [
            line.strip()
            for line in read_text(txt_path).splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]

    for label, urls, source in (
        ("sitemap XML", xml_urls, "sitemap.xml"),
        ("sitemap text", txt_urls, "sitemap.txt"),
    ):
        seen: set[str] = set()
        for url in urls:
            if url in seen:
                issues.append(Issue(
                    label,
                    source,
                    f"duplicate sitemap URL: {url}",
                    None,
                ))
            seen.add(url)

            parsed = urlparse(url)
            if parsed.scheme != "https" or parsed.netloc.casefold() not in CANONICAL_HOSTS:
                issues.append(Issue(
                    label,
                    source,
                    f"sitemap URL is not a canonical HTTPS alignmentconstraint.org URL: {url}",
                    None,
                ))
                continue

            candidate = canonical_path_from_url(url)
            if candidate and not route_exists(candidate, page_routes, static_routes):
                issues.append(Issue(
                    label,
                    source,
                    f"sitemap URL has no matching local page/file: {url}",
                    None,
                ))

    if xml_urls and txt_urls and set(xml_urls) != set(txt_urls):
        only_xml = sorted(set(xml_urls) - set(txt_urls))
        only_txt = sorted(set(txt_urls) - set(xml_urls))
        detail = []
        if only_xml:
            detail.append("only in XML: " + ", ".join(only_xml[:5]))
        if only_txt:
            detail.append("only in TXT: " + ", ".join(only_txt[:5]))
        issues.append(Issue(
            "sitemap consistency",
            "sitemap.xml",
            "sitemap.xml and sitemap.txt do not contain the same URL set"
            + (f" ({'; '.join(detail)})" if detail else ""),
            None,
        ))

    return issues


def split_markdown_destination(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        return raw[1:raw.index(">")].strip()

    # Markdown permits an optional quoted title after the URL.
    # Internal archive targets in this repository do not contain spaces.
    if " " in raw:
        first, rest = raw.split(None, 1)
        if rest.lstrip().startswith(('"', "'", "(")):
            return first
    return raw


def check_internal_links(
    page_routes: set[str],
    static_routes: set[str],
    route_by_page: dict[Path, str],
) -> list[Issue]:
    issues: list[Issue] = []

    for path in sorted(iter_repo_files()):
        if path.suffix.lower() not in {".md", ".markdown"}:
            continue

        text = read_text(path)
        source_route = route_by_page.get(path, inferred_route(path))
        base_url = "https://alignmentconstraint.org" + source_route

        for match in MARKDOWN_LINK_RE.finditer(text):
            dest = split_markdown_destination(match.group(1))
            if not dest or dest.startswith("#"):
                continue

            parsed = urlparse(dest)

            if parsed.scheme in {"mailto", "tel", "javascript", "data"}:
                continue

            # External web link: leave it alone. The push-time validator never
            # uses the network to check external sites.
            if parsed.scheme in {"http", "https"}:
                if parsed.netloc.casefold() not in CANONICAL_HOSTS:
                    continue
                target_path = parsed.path or "/"
                if not route_exists(target_path, page_routes, static_routes):
                    issues.append(Issue(
                        "internal Markdown targets",
                        rel(path),
                        f"canonical-site link has no matching local page/file: {dest}",
                        line_at(text, match.start()),
                    ))
                continue

            path_part = unquote(parsed.path)
            if not path_part:
                continue

            # Repository-relative Markdown/file links.
            if path_part.endswith((".md", ".markdown")) or "." in PurePosixPath(path_part).name:
                if path_part.startswith("/"):
                    target = REPO_ROOT / path_part.lstrip("/")
                else:
                    target = path.parent / path_part
                try:
                    target = target.resolve()
                    target.relative_to(REPO_ROOT.resolve())
                except Exception:
                    issues.append(Issue(
                        "internal Markdown targets",
                        rel(path),
                        f"internal file link escapes the repository: {dest}",
                        line_at(text, match.start()),
                    ))
                    continue
                if not target.exists():
                    issues.append(Issue(
                        "internal Markdown targets",
                        rel(path),
                        f"internal file target does not exist: {dest}",
                        line_at(text, match.start()),
                    ))
                continue

            # Clean root-relative or relative public URL.
            if path_part.startswith("/"):
                target_route = path_part
            else:
                target_route = urlparse(urljoin(base_url, dest)).path

            if not route_exists(target_route, page_routes, static_routes):
                issues.append(Issue(
                    "internal Markdown targets",
                    rel(path),
                    f"internal page target has no matching local page: {dest}",
                    line_at(text, match.start()),
                ))

    return issues


def check_placeholders_and_obsolete_paths() -> list[Issue]:
    issues: list[Issue] = []

    for path in sorted(iter_text_files()):
        text = read_text(path)

        for token in FORBIDDEN_PLACEHOLDERS:
            index = text.find(token)
            if index >= 0:
                issues.append(Issue(
                    "forbidden placeholders",
                    rel(path),
                    f"forbidden placeholder remains: {token}",
                    line_at(text, index),
                ))

        # Obsolete paths matter in public pages, routing files, and sitemaps.
        rp = path.relative_to(REPO_ROOT)
        scan_obsolete = (
            is_page_markdown(path)
            or rp.as_posix() in {
                "README.md", "AGENTS.md", "llms.txt", "llms-full.txt",
                "sitemap.xml", "sitemap.txt", "agent-index.json",
                "open-problems.json", "claim-graph.json",
                "research-questions.txt",
            }
        )
        if scan_obsolete:
            for old, replacement in OBSOLETE_PATHS.items():
                index = text.find(old)
                if index >= 0:
                    issues.append(Issue(
                        "obsolete paths",
                        rel(path),
                        f"obsolete path/reference {old!r}; {replacement}",
                        line_at(text, index),
                    ))

    return issues


def check_medium_artifacts(page_data) -> list[Issue]:
    issues: list[Issue] = []
    patterns = (
        ("source=post_page", "Medium tracking artifact 'source=post_page' remains"),
        (
            "Press enter or click to view image in full size",
            "Medium image-view instruction remains",
        ),
    )

    for path in sorted(page_data):
        text = read_text(path)
        for needle, message in patterns:
            index = text.find(needle)
            if index >= 0:
                issues.append(Issue(
                    "Medium export artifacts",
                    rel(path),
                    message,
                    line_at(text, index),
                ))

        # MarkDownload/Medium bylines often leave a standalone "10 min read"
        # near the top. Limit this check to the opening section to avoid
        # matching legitimate prose elsewhere.
        opening = "\n".join(text.splitlines()[:80])
        m = re.search(r"(?mi)^\s*\d+\s+min(?:ute)?s?\s+read\s*$", opening)
        if m:
            issues.append(Issue(
                "Medium export artifacts",
                rel(path),
                "standalone Medium-style reading-time line remains near the top",
                line_at(text, m.start()),
            ))

    return issues


def check_duplicate_title_h1(page_data) -> list[Issue]:
    issues: list[Issue] = []

    for path, (mapping, body, body_start) in page_data.items():
        title = normalize_title(mapping.get("title"))
        if not title:
            continue

        match = ATX_H1_RE.search(body)
        if not match:
            continue

        h1 = normalize_title(match.group(1))
        if h1 and h1 == title:
            issues.append(Issue(
                "duplicate title/H1",
                rel(path),
                "first body H1 duplicates the front-matter title and may render twice",
                body_start + body.count("\n", 0, match.start()),
            ))

    return issues


def check_image_alt_text(page_data) -> list[Issue]:
    issues: list[Issue] = []

    for path in sorted(page_data):
        text = read_text(path)

        for match in MARKDOWN_BLANK_ALT_RE.finditer(text):
            issues.append(Issue(
                "image alt text",
                rel(path),
                "Markdown image has blank alt text",
                line_at(text, match.start()),
            ))

        for match in HTML_IMG_RE.finditer(text):
            tag = match.group(0)
            alt_match = re.search(
                r"\balt\s*=\s*(['\"])(.*?)\1",
                tag,
                flags=re.IGNORECASE | re.DOTALL,
            )
            if alt_match is None:
                issues.append(Issue(
                    "image alt text",
                    rel(path),
                    "HTML <img> is missing an alt attribute",
                    line_at(text, match.start()),
                ))
            elif not alt_match.group(2).strip():
                issues.append(Issue(
                    "image alt text",
                    rel(path),
                    "HTML <img> has empty alt text",
                    line_at(text, match.start()),
                ))

    return issues


def check_proof_status() -> list[Issue]:
    issues: list[Issue] = []

    for rp in MAJOR_PROOF_STATUS_FILES:
        path = REPO_ROOT / rp
        if not path.exists():
            issues.append(Issue(
                "Stage 4 proof status",
                rp,
                "required major routing/calibration file is missing",
                None,
            ))
            continue

        text = read_text(path)
        folded = text.casefold()

        if not STAGE4_RE.search(text):
            issues.append(Issue(
                "Stage 4 proof status",
                rp,
                "major routing/calibration file does not mention Stage 4",
                None,
            ))
            continue

        if not any(marker in folded for marker in CAUTION_MARKERS):
            issues.append(Issue(
                "Stage 4 proof status",
                rp,
                "Stage 4 is mentioned without a nearby archive-level non-closure/candidate caution",
                None,
            ))

    return issues


def parse_yaml_scalar_tree(path: Path) -> dict[str, str]:
    """Parse the conservative scalar/nested mapping subset used by project YAML."""
    text = read_text(path)
    result: dict[str, str] = {}
    stack: list[tuple[int, str]] = []
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        m = re.match(r"^\s*([A-Za-z0-9_-]+)\s*:\s*(.*)$", raw)
        if not m:
            continue
        key, value = m.groups()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        prefix = ".".join(x[1] for x in stack)
        full = f"{prefix}.{key}" if prefix else key
        value = value.strip()
        if value:
            if len(value) >= 2 and (
                (value.startswith('"') and value.endswith('"')) or
                (value.startswith("'") and value.endswith("'"))
            ):
                value = value[1:-1]
            result[full] = value
        else:
            stack.append((indent, key))
    return result


def check_page_descriptions(page_data) -> list[Issue]:
    issues: list[Issue] = []
    seen: dict[str, Path] = {}
    for path, (mapping, _body, _body_start) in page_data.items():
        desc = mapping.get("description", "").strip()
        if not desc:
            issues.append(Issue(
                "page metadata",
                rel(path),
                "indexable page is missing a non-empty unique 'description:' field",
                2,
            ))
            continue
        folded = re.sub(r"\s+", " ", desc).strip().casefold()
        if folded in seen:
            issues.append(Issue(
                "page metadata",
                rel(path),
                f"description duplicates {rel(seen[folded])}",
                2,
            ))
        else:
            seen[folded] = path
    return issues


def check_centralized_structured_data(page_data, route_by_page) -> list[Issue]:
    issues: list[Issue] = []
    for rp in CENTRAL_STRUCTURED_DATA_FILES:
        if not (REPO_ROOT / rp).exists():
            issues.append(Issue("structured data", rp, "required centralized metadata file is missing", None))

    data_path = REPO_ROOT / "_data/page_metadata.json"
    metadata = None
    if data_path.exists():
        try:
            metadata = json.loads(read_text(data_path))
        except Exception as exc:
            issues.append(Issue("structured data", "_data/page_metadata.json", f"invalid JSON: {exc}", None))

    if isinstance(metadata, dict):
        expected_routes = set(route_by_page.values())
        actual_routes = set(metadata)
        for missing in sorted(expected_routes - actual_routes):
            p = next((p for p, r in route_by_page.items() if r == missing), None)
            issues.append(Issue(
                "structured data",
                rel(p) if p else "_data/page_metadata.json",
                f"no centralized page-metadata entry for canonical route {missing}",
                None,
            ))
        for extra in sorted(actual_routes - expected_routes):
            issues.append(Issue(
                "structured data",
                "_data/page_metadata.json",
                f"metadata entry has no matching rendered Markdown page: {extra}",
                None,
            ))
        for route, entry in metadata.items():
            if not isinstance(entry, dict):
                issues.append(Issue("structured data", "_data/page_metadata.json", f"entry {route} must be an object", None))
                continue
            schema = entry.get("schema_type")
            if schema not in ALLOWED_SCHEMA_TYPES:
                issues.append(Issue(
                    "structured data", "_data/page_metadata.json",
                    f"entry {route} has missing/unsupported schema_type {schema!r}", None,
                ))
            if not str(entry.get("document_role", "")).strip():
                issues.append(Issue(
                    "structured data", "_data/page_metadata.json",
                    f"entry {route} is missing document_role", None,
                ))

    # Article bodies must not carry independently maintained JSON-LD anymore.
    for path, (_mapping, body, body_start) in page_data.items():
        idx = body.find('application/ld+json')
        if idx >= 0:
            issues.append(Issue(
                "structured data",
                rel(path),
                "manual page-body JSON-LD remains; use the centralized structured-data layer instead",
                body_start + body.count("\n", 0, idx),
            ))

    head_path = REPO_ROOT / "_includes/head.html"
    if head_path.exists():
        head = read_text(head_path)
        for needle in ("{% seo", "include highwire-meta.html", "include structured-data.html"):
            if needle not in head:
                issues.append(Issue("structured data", "_includes/head.html", f"required head integration is missing: {needle}", None))

    # If a page ever declares a manual canonical_url, it must exactly match its route.
    cfg = parse_yaml_scalar_tree(REPO_ROOT / "_config.yml") if (REPO_ROOT / "_config.yml").exists() else {}
    site_url = cfg.get("url", "").rstrip("/")
    for path, (mapping, _body, _body_start) in page_data.items():
        manual = mapping.get("canonical_url", "").strip()
        if manual:
            expected = site_url + route_by_page[path]
            if manual.rstrip("/") != expected.rstrip("/"):
                issues.append(Issue(
                    "canonical metadata", rel(path),
                    f"canonical_url {manual!r} does not match permalink-derived canonical URL {expected!r}", 2,
                ))
    return issues


def check_identity_metadata_sync() -> list[Issue]:
    issues: list[Issue] = []
    fw_path = REPO_ROOT / "framework-metadata.yml"
    cfg_path = REPO_ROOT / "_config.yml"
    if not fw_path.exists() or not cfg_path.exists():
        return issues
    fw = parse_yaml_scalar_tree(fw_path)
    cfg = parse_yaml_scalar_tree(cfg_path)
    comparisons = (
        ("canonical_name", "title", "framework name"),
        ("canonical_url", "url", "canonical URL"),
        ("version", "framework_version", "framework version"),
        ("license", "framework_license", "license"),
        ("proof_status", "framework_proof_status", "proof status"),
        ("author.name", "author.name", "author name"),
        ("author.orcid", "author.url", "author ORCID/URL"),
    )
    for fw_key, cfg_key, label in comparisons:
        if fw.get(fw_key) != cfg.get(cfg_key):
            issues.append(Issue(
                "metadata synchronization", "_config.yml",
                f"{label} differs from framework-metadata.yml ({cfg.get(cfg_key)!r} != {fw.get(fw_key)!r})",
                None,
            ))
    return issues


def build_route_by_page(page_data) -> dict[Path, str]:
    result = {}
    for path, (mapping, _body, _body_start) in page_data.items():
        if rel(path) == "index.md":
            result[path] = "/"
        elif mapping.get("permalink", "").strip():
            result[path] = normalize_permalink(mapping["permalink"])
        else:
            result[path] = inferred_route(path)
    return result


def annotate(issue: Issue) -> None:
    location = issue.path
    if issue.line is not None:
        location += f":{issue.line}"
    print(f"ERROR [{issue.check}] {location} — {issue.message}")

    # GitHub Actions turns this into a clickable red annotation.
    if os.environ.get("GITHUB_ACTIONS") == "true":
        escaped = issue.message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        if issue.line is not None:
            print(f"::error file={issue.path},line={issue.line}::{issue.check}: {escaped}")
        else:
            print(f"::error file={issue.path}::{issue.check}: {escaped}")


def main() -> int:
    os.chdir(REPO_ROOT)

    print("=" * 72)
    print("Alignment Constraint Archive — automatic quality check")
    print("READ-ONLY: this validator does not edit files or access the internet.")
    print("=" * 72)

    page_data, permalink_map, issues = collect_pages()
    page_routes = set(permalink_map)
    page_routes.add("/")
    static_routes = existing_static_routes()
    route_by_page = build_route_by_page(page_data)

    issues.extend(check_json_files())
    issues.extend(check_sitemaps(page_routes, static_routes))
    issues.extend(check_internal_links(page_routes, static_routes, route_by_page))
    issues.extend(check_placeholders_and_obsolete_paths())
    issues.extend(check_medium_artifacts(page_data))
    issues.extend(check_duplicate_title_h1(page_data))
    issues.extend(check_image_alt_text(page_data))
    issues.extend(check_proof_status())
    issues.extend(check_page_descriptions(page_data))
    issues.extend(check_centralized_structured_data(page_data, route_by_page))
    issues.extend(check_identity_metadata_sync())

    # Stable output order makes failures easier to compare between commits.
    issues = sorted(
        set(issues),
        key=lambda x: (x.path, x.line or 0, x.check, x.message),
    )

    print()
    print(f"Public Markdown pages examined: {len(page_data)}")
    print(f"Unique public routes found:     {len(page_routes)}")
    print(f"JSON files examined:            {sum(1 for p in iter_repo_files() if p.suffix.lower() == '.json')}")
    print()

    if issues:
        print(f"RESULT: FAIL — {len(issues)} problem(s) need attention.")
        print("Nothing was changed. Fix the items below and push again.")
        print("-" * 72)
        for issue in issues:
            annotate(issue)
        print("-" * 72)
        print("After you fix the listed items, GitHub will run this check again automatically.")
        return 1

    print("RESULT: PASS")
    print("No requested archive-quality problems were found.")
    print("GitHub Actions should show a green check for 'Archive QC'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
