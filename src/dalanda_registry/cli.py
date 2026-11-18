# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
"""Command line: `dalanda-registry check [PATH] [--links]`."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from dalanda_registry.links import check_links
from dalanda_registry.validate import RegistryError, load_registry, validate

DEFAULT_PATH = Path("registry/sources.yaml")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="dalanda-registry", description="Check the Dalanda source registry."
    )
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="validate the registry file")
    check.add_argument("path", nargs="?", type=Path, default=DEFAULT_PATH)
    check.add_argument("--links", action="store_true", help="also check that every link resolves")
    args = parser.parse_args(argv)

    try:
        entries = load_registry(args.path)
    except RegistryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    problems = validate(entries)
    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)
    if problems:
        return 1

    if args.links:
        urls = [entry["url"] for entry in entries]
        urls += [entry["licence_url"] for entry in entries if "licence_url" in entry]
        dead = check_links(urls)
        for url, reason in sorted(dead.items()):
            print(f"error: {url}: {reason}", file=sys.stderr)
        if dead:
            return 1

    checked = "format, duplicates and links" if args.links else "format and duplicates"
    print(f"{args.path}: {len(entries)} sources, {checked} OK")
    return 0
