"""Dalanda project package. Scaffold only — no training code in this release."""

from __future__ import annotations

from importlib.metadata import metadata

__version__ = "0.0.1"


def package_identity() -> dict[str, str]:
    """Return installed package name, version, and summary from packaging metadata."""
    meta = metadata("dalanda")
    return {
        "name": meta["Name"],
        "version": meta["Version"],
        "summary": meta["Summary"],
    }
