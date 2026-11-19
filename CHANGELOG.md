# Changelog

All notable changes to this repository are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- README, roadmap and contributing guide for the data collection phase: contributors share links to Derja text on dalanda.ai.
- Data policy, privacy policy and terms of use.
- `registry/sources.md`: a readable table of accepted sources, generated from `sources.yaml` by `dalanda-registry render`. CI checks it is up to date.
- Privacy policy: Google sign-in, the `dalanda_lang` cookie, and AWS hosting in the United States. One contact address, dalanda@seneca.center, across the policy, terms and project docs.
- ADR 0002 accepted after review, with rules for private dataset access, model providers not training on chats, and the self-harm check.
- ADR 0001 (governance: who the maintainers are and how they decide) and ADR 0002 (privacy, retention and logging for the website).
- Public source registry (`registry/sources.yaml`) and the `dalanda-registry` checker for format, duplicates, dead links, unchecked licences and signed links. Entries can withhold their link when the contributor did not allow it to be shown.
- CI: lint, type check, tests, registry check, Gitleaks and a dependency audit on every pull request, plus CodeQL and dependency review once the repository is public. A branch ruleset and CODEOWNERS.
- Issue templates for suggesting a source and reporting a bug, and a pull request template.

### Changed

- Registry entries match the dalanda.ai contribute form: `domains` and `description` are optional, except that an entry with a withheld link needs a `description`. `licence` and `provenance` stay required and are recorded by the maintainer who accepts the source. The README, contributing guide, data policy and privacy policy describe the form's fields.
- The dalanda.ai contribute form also asks, optionally, what kind of text a source holds, its licence and where it comes from (picked from lists, so no free text), and whether the contributor wants to be credited by their display name. The maintainer still checks and confirms the licence and provenance.
