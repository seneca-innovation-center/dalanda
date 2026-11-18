# SPDX-FileCopyrightText: 2026 Seneca Innovation Center
# SPDX-License-Identifier: Apache-2.0
"""Load the source registry and check every entry against the schema in docs/registry.md."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlsplit, urlunsplit

import yaml

TYPES = frozenset({"website", "archive", "dataset", "repository", "social-media", "other"})
DOMAINS = frozenset(
    {"forum", "news", "subtitle", "chat", "literary", "instruction", "transcript", "other"}
)
WRITING = frozenset({"arabic-script", "arabizi", "french-mixed"})

REQUIRED = (
    "id",
    "name",
    "type",
    "domains",
    "writing",
    "description",
    "licence",
    "provenance",
    "added",
)
OPTIONAL = ("url", "link_withheld", "licence_url", "credit")

ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EMAIL_PATTERN = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
MAX_DESCRIPTION = 500
# Licence values that mean nobody has checked it. The data policy rejects such sources.
UNCLEAR_LICENCES = frozenset({"unknown", "unclear", "not sure", "tbd", "todo", "n/a", "none", "?"})
# Query parameters that make a link private: signed URLs and access tokens.
SIGNED_LINK_PARAMS = frozenset(
    {
        "x-amz-signature",
        "x-amz-credential",
        "x-amz-security-token",
        "x-goog-signature",
        "x-goog-credential",
        "signature",
        "sig",
        "token",
        "access_token",
    }
)


class RegistryError(Exception):
    """The registry file cannot be read as a list of entries."""


@dataclass(frozen=True)
class Problem:
    where: str
    message: str

    def __str__(self) -> str:
        return f"{self.where}: {self.message}"


class _StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate keys instead of keeping the last one."""


def _construct_mapping(loader: _StrictLoader, node: yaml.MappingNode) -> dict[Any, Any]:
    seen: set[Any] = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        seen.add(key)
    return loader.construct_mapping(node)


_StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


def load_registry(path: Path) -> list[Any]:
    """Return the raw entries under `sources:`. Raise RegistryError if the file is malformed."""
    try:
        # _StrictLoader subclasses SafeLoader, so no arbitrary objects are built.
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=_StrictLoader)  # nosec B506
    except (OSError, yaml.YAMLError) as exc:
        raise RegistryError(f"{path}: {exc}") from exc
    if not isinstance(data, dict) or set(data) != {"sources"}:
        raise RegistryError(f"{path}: the file must have exactly one top-level key, 'sources'")
    sources = data["sources"]
    if sources is None:
        return []
    if not isinstance(sources, list):
        raise RegistryError(f"{path}: 'sources' must be a list")
    return sources


def url_problem(url: str) -> str | None:
    """Say why a URL is not acceptable, or return None."""
    if url != url.strip() or any(ch.isspace() for ch in url):
        return "must not contain spaces"
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https"):
        return "must start with https:// or http://"
    if not parts.hostname:
        return "has no host name"
    if parts.username or parts.password:
        return "must not contain a user name or password"
    params = {key.lower() for key, _ in parse_qsl(parts.query, keep_blank_values=True)}
    if params & SIGNED_LINK_PARAMS:
        return "must not be a signed link or contain an access token"
    return None


def normalise_url(url: str) -> str:
    """Reduce a URL to a form where trivially different spellings of one link compare equal."""
    parts = urlsplit(url.strip())
    host = (parts.hostname or "").lower().removeprefix("www.")
    if parts.port:
        host = f"{host}:{parts.port}"
    path = parts.path.rstrip("/")
    return urlunsplit(("https", host, path, parts.query, ""))


def _text(entry: dict[str, Any], key: str, where: str, problems: list[Problem]) -> str | None:
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        problems.append(Problem(where, f"'{key}' must be non-empty text"))
        return None
    return value


def _choices(
    entry: dict[str, Any], key: str, allowed: frozenset[str], where: str, problems: list[Problem]
) -> None:
    value = entry.get(key)
    if not isinstance(value, list) or not value:
        problems.append(Problem(where, f"'{key}' must be a non-empty list"))
        return
    unknown = [v for v in value if v not in allowed]
    if unknown:
        problems.append(
            Problem(where, f"'{key}' has unknown values {unknown}; use {sorted(allowed)}")
        )
    if len(set(map(str, value))) != len(value):
        problems.append(Problem(where, f"'{key}' lists a value twice"))


def _check_keys(entry: dict[str, Any], where: str, problems: list[Problem]) -> None:
    missing = [k for k in REQUIRED if k not in entry]
    if missing:
        problems.append(Problem(where, f"missing {missing}"))
    unknown = sorted(set(entry) - set(REQUIRED) - set(OPTIONAL))
    if unknown:
        problems.append(Problem(where, f"unknown fields {unknown}"))
    withheld = entry.get("link_withheld", False)
    if not isinstance(withheld, bool):
        problems.append(Problem(where, "'link_withheld' must be true or false"))
    elif withheld and "url" in entry:
        problems.append(Problem(where, "an entry with 'link_withheld: true' must not have a 'url'"))
    elif not withheld and "url" not in entry:
        problems.append(Problem(where, "missing ['url'] (or set 'link_withheld: true')"))


def _check_text_fields(entry: dict[str, Any], where: str, problems: list[Problem]) -> None:
    entry_id = _text(entry, "id", where, problems)
    if entry_id is not None and not ID_PATTERN.match(entry_id):
        problems.append(Problem(where, "'id' must be lowercase letters, digits and hyphens"))

    for key in ("name", "provenance"):
        _text(entry, key, where, problems)

    licence = _text(entry, "licence", where, problems)
    if licence is not None and licence.strip().lower() in UNCLEAR_LICENCES:
        problems.append(Problem(where, "'licence' must be checked before a source is accepted"))

    description = _text(entry, "description", where, problems)
    if description is not None and len(description) > MAX_DESCRIPTION:
        problems.append(Problem(where, f"'description' is over {MAX_DESCRIPTION} characters"))

    if "credit" in entry:
        credit = _text(entry, "credit", where, problems)
        if credit is not None and EMAIL_PATTERN.search(credit):
            problems.append(Problem(where, "'credit' must be a display name, not an email"))


def _check_urls(entry: dict[str, Any], where: str, problems: list[Problem]) -> None:
    for key in ("url", "licence_url"):
        if key not in entry:
            continue
        url = _text(entry, key, where, problems)
        reason = url_problem(url) if url is not None else None
        if reason:
            problems.append(Problem(where, f"'{key}' {reason}"))


def _check_categories(entry: dict[str, Any], where: str, problems: list[Problem]) -> None:
    if entry.get("type") not in TYPES:
        problems.append(Problem(where, f"'type' must be one of {sorted(TYPES)}"))
    _choices(entry, "domains", DOMAINS, where, problems)
    _choices(entry, "writing", WRITING, where, problems)
    if not isinstance(entry.get("added"), date):
        problems.append(Problem(where, "'added' must be a date like 2026-11-18"))


def _check_entry(entry: dict[str, Any], where: str) -> list[Problem]:
    problems: list[Problem] = []
    _check_keys(entry, where, problems)
    _check_text_fields(entry, where, problems)
    _check_urls(entry, where, problems)
    _check_categories(entry, where, problems)
    return problems


def validate(entries: list[Any]) -> list[Problem]:
    """Check every entry, then check that no id, URL or name appears twice."""
    problems: list[Problem] = []
    first_seen: dict[tuple[str, str], str] = {}

    for index, entry in enumerate(entries):
        where = f"sources[{index}]"
        if not isinstance(entry, dict):
            problems.append(Problem(where, "each entry must be a mapping of fields"))
            continue
        if isinstance(entry.get("id"), str):
            where = f"sources[{index}] ({entry['id']})"
        problems.extend(_check_entry(entry, where))

        keys = []
        if isinstance(entry.get("id"), str):
            keys.append(("id", entry["id"]))
        if isinstance(entry.get("url"), str):
            keys.append(("url", normalise_url(entry["url"])))
        if isinstance(entry.get("name"), str):
            keys.append(("name", entry["name"].strip().casefold()))
        for key in keys:
            if key in first_seen:
                problems.append(Problem(where, f"same {key[0]} as {first_seen[key]}"))
            else:
                first_seen[key] = where

    return problems
