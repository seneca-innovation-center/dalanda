# ADR 0001: Open-source community model

- Status: Accepted
- Date: 2026-09-03

## Context

Dalanda is meant to be found, cloned, and improved by people who were not in the room when it started. The repo is the product on day one. We need a clear split between who builds and who steers, before training code or datasets land.

## Decision

The community builds Dalanda. Anyone can propose data sources, docs, tooling, and later model work through issues and pull requests.

Stewards set goals and review. A small steward group publishes the roadmap, accepts or rejects contributions against those goals, and keeps licence, provenance, and safety bar.

This repo stays Apache-2.0. Contributions are made under the Developer Certificate of Origin (DCO). Text added to the project (docs, samples, prompts, dataset descriptions) must include licence and provenance.

## Consequences

- Work happens in public issues and PRs, not private threads.
- Stewards do not have to write every line; they do have to review and set direction.
- Training code and data dumps are out of scope until a later, reviewed change.
- Contributors should expect review against the published roadmap, not a private backlog.
