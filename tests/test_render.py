# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from datetime import date
from pathlib import Path

from dalanda_registry.render import render
from dalanda_registry.validate import load_registry


def test_empty_registry() -> None:
    assert "No sources have been accepted yet." in render([])


def test_rows_are_sorted_escaped_and_linked() -> None:
    page = render(
        [
            {
                "id": "b-later",
                "name": "Later | Forum",
                "url": "https://example.org/b",
                "type": "website",
                "writing": ["arabizi", "french-mixed"],
                "licence": "CC-BY-4.0",
                "licence_url": "https://creativecommons.org/licenses/by/4.0/",
                "description": "Two\nlines",
                "added": date(2026, 11, 19),
            },
            {
                "id": "a-private",
                "name": "Private dataset [x]",
                "link_withheld": True,
                "type": "dataset",
                "credit": "Amira",
                "added": date(2026, 11, 18),
            },
        ]
    )
    rows = [line for line in page.splitlines() if line.startswith("| ") and "---" not in line]
    assert rows[1].startswith("| Private dataset [x] (link withheld) | dataset |")
    assert "Amira" in rows[1]
    assert "[Later \\| Forum](https://example.org/b)" in rows[2]
    assert "arabizi, french-mixed" in rows[2]
    assert "[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)" in rows[2]
    assert "Two lines" in rows[2]
    assert "2 sources." in page


def test_shipped_page_is_up_to_date() -> None:
    registry = Path(__file__).resolve().parents[1] / "registry"
    entries = load_registry(registry / "sources.yaml")
    assert (registry / "sources.md").read_text(encoding="utf-8") == render(entries)
