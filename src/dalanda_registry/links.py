# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
"""Check that registry links still resolve."""

from __future__ import annotations

import urllib.error
import urllib.request
from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor
from typing import Any

USER_AGENT = "dalanda-registry-link-check (+https://github.com/seneca-innovation-center/dalanda)"

# The server answered, so the link is not dead. Many sites send these to automated clients.
REACHABLE_ERRORS = frozenset({401, 403, 429})
# The server may not support HEAD. Retry with GET before deciding.
RETRY_WITH_GET = frozenset({400, 403, 405, 501})

Opener = Callable[..., Any]


def _status(url: str, method: str, timeout: float, opener: Opener) -> int:
    request = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    try:
        with opener(request, timeout=timeout) as response:
            return int(response.status)
    except urllib.error.HTTPError as exc:
        return exc.code


def check_link(
    url: str, timeout: float = 20.0, opener: Opener = urllib.request.urlopen
) -> str | None:
    """Return None if the link resolves, or a short reason if it does not."""
    try:
        status = _status(url, "HEAD", timeout, opener)
        if status in RETRY_WITH_GET:
            status = _status(url, "GET", timeout, opener)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        reason = getattr(exc, "reason", exc)
        return f"could not connect ({reason})"
    if status < 400 or status in REACHABLE_ERRORS:
        return None
    return f"HTTP {status}"


def check_links(
    urls: Iterable[str],
    workers: int = 8,
    timeout: float = 20.0,
    opener: Opener = urllib.request.urlopen,
) -> dict[str, str]:
    """Check each URL once. Return {url: reason} for the ones that do not resolve."""
    unique = sorted(set(urls))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = pool.map(lambda u: check_link(u, timeout, opener), unique)
    return {url: reason for url, reason in zip(unique, results, strict=True) if reason is not None}
