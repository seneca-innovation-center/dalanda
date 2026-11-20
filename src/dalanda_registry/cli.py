# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
"""Command line: `dalanda-registry check [PATH] [--links]` and `render [PATH] [--check]`."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from dalanda_registry.links import check_links
from dalanda_registry.render import render
from dalanda_registry.validate import RegistryError, load_registry, validate

DEFAULT_PATH = Path("registry/sources.yaml")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dalanda-registry", description="Check the Dalanda source registry."
    )
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="validate the registry file")
    check.add_argument("path", nargs="?", type=Path, default=DEFAULT_PATH)
    check.add_argument("--links", action="store_true", help="also check that every link resolves")
    page = commands.add_parser("render", help="write sources.md next to the registry file")
    page.add_argument("path", nargs="?", type=Path, default=DEFAULT_PATH)
    page.add_argument(
        "--check", action="store_true", help="fail if sources.md is missing or out of date"
    )
    return parser


def _load_valid(path: Path) -> list[Any] | None:
    try:
        entries = load_registry(path)
    except RegistryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return None
    problems = validate(entries)
    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)
    return None if problems else entries


def _check(path: Path, links: bool) -> int:
    entries = _load_valid(path)
    if entries is None:
        return 1
    if links:
        urls = [entry["url"] for entry in entries if "url" in entry]
        urls += [entry["licence_url"] for entry in entries if "licence_url" in entry]
        dead = check_links(urls)
        for url, reason in sorted(dead.items()):
            print(f"error: {url}: {reason}", file=sys.stderr)
        if dead:
            return 1
    checked = "format, duplicates and links" if links else "format and duplicates"
    print(f"{path}: {len(entries)} sources, {checked} OK")
    return 0


def _render(path: Path, check_only: bool) -> int:
    entries = _load_valid(path)
    if entries is None:
        return 1
    page = path.with_suffix(".md")
    text = render(entries)
    if check_only:
        current = page.read_text(encoding="utf-8") if page.exists() else None
        if current != text:
            print(
                f"error: {page} is out of date; run `uv run dalanda-registry render` and commit it",
                file=sys.stderr,
            )
            return 1
        print(f"{page}: up to date")
        return 0
    page.write_text(text, encoding="utf-8")
    print(f"{page}: written, {len(entries)} sources")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command line and return the process exit code."""
    args = _parser().parse_args(argv)
    if args.command == "render":
        return _render(args.path, args.check)
    return _check(args.path, args.links)
