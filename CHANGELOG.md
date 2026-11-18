# Changelog

All notable changes to this repository are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- README, roadmap and contributing guide for the data collection phase: contributors share links to Derja text on dalanda.ai.
- Data policy, privacy policy and terms of use.
- ADR 0001 (governance: who the maintainers are and how they decide) and ADR 0002 (privacy, retention and logging for the website).
- Public source registry (`registry/sources.yaml`) and the `dalanda-registry` checker for format, duplicates, dead links, unchecked licences and signed links.
- CI: lint, type check, tests, registry check, Gitleaks and a dependency audit on every pull request, plus CodeQL and dependency review once the repository is public. A branch ruleset and CODEOWNERS.
- Issue templates for suggesting a source and reporting a bug, and a pull request template.
