"""Tests for the installed Dalanda package."""

from dalanda import __version__, package_identity


def test_package_identity_matches_install() -> None:
    ident = package_identity()
    assert ident["name"] == "dalanda"
    assert ident["version"] == __version__
    assert "Tunisian" in ident["summary"]
    assert "Derja" in ident["summary"]
