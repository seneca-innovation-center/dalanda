"""Placeholder test so CI has a passing suite before training code lands."""

from dalanda import __version__


def test_package_version_is_set() -> None:
    assert __version__ == "0.0.1"
