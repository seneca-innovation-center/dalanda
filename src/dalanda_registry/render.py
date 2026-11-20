# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
"""Render the source registry as a Markdown page that people can read on GitHub."""

from __future__ import annotations

from typing import Any

HEADER = """\
<!-- Generated from sources.yaml by `uv run dalanda-registry render`. Do not edit by hand. -->

# Dalanda sources

Every source shared on [dalanda.ai](https://dalanda.ai) and accepted by a maintainer. \
The data is in [sources.yaml](sources.yaml); its fields are described in \
[docs/registry.md](../docs/registry.md). To ask for a source to be removed, see the \
[data policy](../docs/data-policy.md#ask-for-a-link-to-be-removed).
"""

COLUMNS = ("Source", "Type", "Written in", "Licence", "Description", "Credit", "Added")


def _cell(value: Any) -> str:
    """Make a value safe inside one Markdown table cell."""
    if value is None:
        return ""
    if isinstance(value, list):
        value = ", ".join(str(v) for v in value)
    text = " ".join(str(value).split())
    return text.replace("\\", "\\\\").replace("|", "\\|")


def _link(text: str, url: Any) -> str:
    if not isinstance(url, str):
        return text
    safe_url = url.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
    safe_text = text.replace("[", "\\[").replace("]", "\\]")
    return f"[{safe_text}]({safe_url})"


def _row(entry: dict[str, Any]) -> str:
    name = _cell(entry.get("name"))
    source = (
        f"{name} (link withheld)" if entry.get("link_withheld") else _link(name, entry.get("url"))
    )
    licence = _cell(entry.get("licence"))
    if licence:
        licence = _link(licence, entry.get("licence_url"))
    cells = (
        source,
        _cell(entry.get("type")),
        _cell(entry.get("writing")),
        licence,
        _cell(entry.get("description")),
        _cell(entry.get("credit")),
        _cell(entry.get("added")),
    )
    return "| " + " | ".join(cells) + " |"


def render(entries: list[dict[str, Any]]) -> str:
    """Return the Markdown page for a list of valid registry entries, oldest first."""
    lines = [HEADER]
    if not entries:
        lines.append("No sources have been accepted yet.\n")
        return "\n".join(lines)
    lines.append(f"{len(entries)} sources.\n")
    lines.append("| " + " | ".join(COLUMNS) + " |")
    lines.append("| " + " | ".join("---" for _ in COLUMNS) + " |")
    ordered = sorted(entries, key=lambda e: (str(e.get("added")), str(e.get("id"))))
    lines.extend(_row(entry) for entry in ordered)
    return "\n".join(lines) + "\n"
