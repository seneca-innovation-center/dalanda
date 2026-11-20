# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
"""Tests for the `dalanda-registry` command line."""

from __future__ import annotations

from pathlib import Path

import pytest

from dalanda_registry import cli

# editorconfig-checker-disable
GOOD = """\
sources:
  - id: example-forum
    name: Example Forum
    url: https://forum.example.org/derja
    type: website
    domains: [forum]
    writing: [arabizi]
    description: Public threads written in Derja.
    licence: CC-BY-4.0
    licence_url: https://example.org/licence
    provenance: Published by the forum owners.
    added: 2026-11-18
"""
# editorconfig-checker-enable


def write(tmp_path: Path, text: str) -> Path:
    """Write a registry file into tmp_path and return its path."""
    path = tmp_path / "sources.yaml"
    path.write_text(text, encoding="utf-8")
    return path


def test_check_ok(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.main(["check", str(write(tmp_path, GOOD))]) == 0
    assert "1 sources, format and duplicates OK" in capsys.readouterr().out


def test_check_reports_problems(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = write(tmp_path, GOOD.replace("type: website", "type: podcast"))
    assert cli.main(["check", str(path)]) == 1
    assert "'type' must be one of" in capsys.readouterr().err


def test_check_bad_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.main(["check", str(write(tmp_path, "nope: 1\n"))]) == 1
    assert "exactly one top-level key" in capsys.readouterr().err


def test_check_links_ok(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    seen: list[str] = []

    def fake_check_links(urls: list[str]) -> dict[str, str]:
        seen.extend(urls)
        return {}

    monkeypatch.setattr(cli, "check_links", fake_check_links)
    assert cli.main(["check", str(write(tmp_path, GOOD)), "--links"]) == 0
    assert seen == ["https://forum.example.org/derja", "https://example.org/licence"]
    assert "format, duplicates and links OK" in capsys.readouterr().out


def test_check_links_dead(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(cli, "check_links", lambda urls: {urls[0]: "HTTP 404"})
    assert cli.main(["check", str(write(tmp_path, GOOD)), "--links"]) == 1
    assert "https://forum.example.org/derja: HTTP 404" in capsys.readouterr().err


def test_render_writes_and_checks(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    path = write(tmp_path, GOOD)
    page = tmp_path / "sources.md"
    assert cli.main(["render", str(path), "--check"]) == 1
    assert "out of date" in capsys.readouterr().err
    assert cli.main(["render", str(path)]) == 0
    assert "[Example Forum](https://forum.example.org/derja)" in page.read_text(encoding="utf-8")
    assert cli.main(["render", str(path), "--check"]) == 0
    assert "up to date" in capsys.readouterr().out


def test_render_refuses_invalid_registry(tmp_path: Path) -> None:
    path = write(tmp_path, GOOD.replace("type: website", "type: podcast"))
    assert cli.main(["render", str(path)]) == 1
    assert not (tmp_path / "sources.md").exists()
