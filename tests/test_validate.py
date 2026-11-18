# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

import pytest

from dalanda_registry.validate import (
    RegistryError,
    load_registry,
    normalise_url,
    url_problem,
    validate,
)


def entry(**overrides: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "id": "example-forum",
        "name": "Example Forum",
        "url": "https://forum.example.org/derja",
        "type": "website",
        "domains": ["forum"],
        "writing": ["arabic-script", "arabizi"],
        "description": "Public threads written in Derja.",
        "licence": "CC-BY-4.0",
        "provenance": "Published by the forum owners; public pages only.",
        "added": date(2026, 11, 18),
    }
    base.update(overrides)
    return base


def messages(entries: list[Any]) -> list[str]:
    return [str(p) for p in validate(entries)]


def test_valid_entry_has_no_problems() -> None:
    assert validate([entry(licence_url="https://example.org/licence", credit="Amira")]) == []


def test_empty_registry_is_valid() -> None:
    assert validate([]) == []


def test_missing_and_unknown_fields() -> None:
    bad = entry(email="x@example.org")
    del bad["licence"]
    out = messages([bad])
    assert any("missing ['licence']" in m for m in out)
    assert any("unknown fields ['email']" in m for m in out)


def test_entry_must_be_a_mapping() -> None:
    assert messages(["just a string"]) == ["sources[0]: each entry must be a mapping of fields"]


@pytest.mark.parametrize(
    ("overrides", "expected"),
    [
        ({"id": "Bad_ID"}, "'id' must be lowercase"),
        ({"name": "  "}, "'name' must be non-empty text"),
        ({"description": "x" * 501}, "over 500 characters"),
        ({"type": "podcast"}, "'type' must be one of"),
        ({"domains": []}, "'domains' must be a non-empty list"),
        ({"domains": ["forum", "sports"]}, "unknown values ['sports']"),
        ({"writing": ["arabizi", "arabizi"]}, "lists a value twice"),
        ({"added": "yesterday"}, "'added' must be a date"),
        ({"url": "ftp://example.org"}, "'url' must start with https://"),
        ({"licence_url": "https://u:p@example.org"}, "'licence_url' must not contain a user"),
        ({"credit": "amira@example.org"}, "display name, not an email"),
        ({"licence": "unknown"}, "'licence' must be checked"),
        ({"licence": " Not sure "}, "'licence' must be checked"),
        ({"url": "https://example.org/d?token=abc"}, "must not be a signed link"),
    ],
)
def test_field_rules(overrides: dict[str, Any], expected: str) -> None:
    out = messages([entry(**overrides)])
    assert any(expected in m for m in out), out


def test_duplicates_by_id_url_and_name() -> None:
    first = entry()
    same_url = entry(id="other", name="Other", url="http://www.FORUM.example.org/derja/")
    same_name = entry(id="third", name=" example forum ", url="https://b.example.org")
    same_id = entry(name="Fourth", url="https://c.example.org")
    out = messages([first, same_url, same_name, same_id])
    assert "sources[1] (other): same url as sources[0] (example-forum)" in out
    assert "sources[2] (third): same name as sources[0] (example-forum)" in out
    assert "sources[3] (example-forum): same id as sources[0] (example-forum)" in out


@pytest.mark.parametrize(
    ("url", "problem"),
    [
        ("https://example.org/a", None),
        ("https://example.org/a b", "must not contain spaces"),
        ("mailto:a@example.org", "must start with https:// or http://"),
        ("https://", "has no host name"),
        (
            "https://b.s3.amazonaws.com/f?X-Amz-Signature=ab&X-Amz-Expires=60",
            "must not be a signed link or contain an access token",
        ),
        ("https://example.org/f?sig=ab", "must not be a signed link or contain an access token"),
        ("https://example.org/search?q=token", None),
    ],
)
def test_url_problem(url: str, problem: str | None) -> None:
    assert url_problem(url) == problem


def test_normalise_url_keeps_query_and_port() -> None:
    assert (
        normalise_url("HTTP://www.Example.org:8080/a/?q=1#top") == "https://example.org:8080/a?q=1"
    )


def test_load_registry_reads_entries(tmp_path: Path) -> None:
    path = tmp_path / "sources.yaml"
    path.write_text("sources:\n  - id: a\n    added: 2026-11-18\n", encoding="utf-8")
    assert load_registry(path) == [{"id": "a", "added": date(2026, 11, 18)}]


@pytest.mark.parametrize("text", ["sources:\n", "sources: []\n"])
def test_load_registry_empty(tmp_path: Path, text: str) -> None:
    path = tmp_path / "sources.yaml"
    path.write_text(text, encoding="utf-8")
    assert load_registry(path) == []


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("sources:\n  - id: a\n    id: b\n", "duplicate key 'id'"),
        ("sources: [\n", "expected"),
        ("other: []\n", "exactly one top-level key"),
        ("sources: {}\n", "'sources' must be a list"),
    ],
)
def test_load_registry_rejects_bad_files(tmp_path: Path, text: str, expected: str) -> None:
    path = tmp_path / "sources.yaml"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(RegistryError, match=expected):
        load_registry(path)


def test_load_registry_missing_file(tmp_path: Path) -> None:
    with pytest.raises(RegistryError):
        load_registry(tmp_path / "nope.yaml")


def test_shipped_registry_is_valid() -> None:
    path = Path(__file__).resolve().parents[1] / "registry" / "sources.yaml"
    assert validate(load_registry(path)) == []
