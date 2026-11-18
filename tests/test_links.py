# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import urllib.error
import urllib.request
from typing import Any

import pytest

from dalanda_registry.links import check_link, check_links


class FakeResponse:
    def __init__(self, status: int) -> None:
        self.status = status

    def __enter__(self) -> FakeResponse:
        return self

    def __exit__(self, *args: object) -> None:
        return None


def opener_for(answers: dict[tuple[str, str], int | Exception]) -> Any:
    """Build an opener that answers (method, url) with a status code or raises."""
    calls: list[tuple[str, str]] = []

    def opener(request: urllib.request.Request, timeout: float) -> FakeResponse:
        key = (request.get_method(), request.full_url)
        calls.append(key)
        answer = answers[key]
        if isinstance(answer, Exception):
            raise answer
        if answer >= 400:
            raise urllib.error.HTTPError(request.full_url, answer, "error", {}, None)  # type: ignore[arg-type]
        return FakeResponse(answer)

    opener.calls = calls  # type: ignore[attr-defined]
    return opener


URL = "https://example.org/data"


@pytest.mark.parametrize(
    ("answers", "expected"),
    [
        ({("HEAD", URL): 200}, None),
        ({("HEAD", URL): 404}, "HTTP 404"),
        ({("HEAD", URL): 405, ("GET", URL): 200}, None),
        ({("HEAD", URL): 405, ("GET", URL): 410}, "HTTP 410"),
        ({("HEAD", URL): 403, ("GET", URL): 403}, None),
        ({("HEAD", URL): 503}, "HTTP 503"),
        (
            {("HEAD", URL): urllib.error.URLError("no such host")},
            "could not connect (no such host)",
        ),
        ({("HEAD", URL): TimeoutError("timed out")}, "could not connect (timed out)"),
    ],
)
def test_check_link(answers: dict[tuple[str, str], int | Exception], expected: str | None) -> None:
    assert check_link(URL, opener=opener_for(answers)) == expected


def test_check_links_reports_only_dead_and_checks_each_url_once() -> None:
    good, dead = "https://good.example.org", "https://dead.example.org"
    opener = opener_for({("HEAD", good): 200, ("HEAD", dead): 404})
    assert check_links([good, dead, good], opener=opener) == {dead: "HTTP 404"}
    assert sorted(opener.calls) == [("HEAD", dead), ("HEAD", good)]
