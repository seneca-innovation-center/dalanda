# ADR 0001: Open-source community model

- Status: Accepted
- Date: 2026-09-03 (updated 2026-11-18)
- Deciders: Raed Brahem, Amel Omri, Dalanda maintainers

## Context

Dalanda is meant to be found, cloned, and improved by people who were not in the room when it started. The repo is the product on day one. We need a clear split between who builds and who steers, before training code or datasets land.

## Decision

### Who builds

The community builds Dalanda. Anyone can propose data sources, docs, tooling, and later model work through issues, pull requests, and the dalanda.ai website.

### Who steers

Maintainers set goals and review. They publish the roadmap, accept or reject contributions against it, and uphold the licence, provenance and safety bar.

- **Who they are.** The maintainers are the members of the [`@seneca-innovation-center/dev`](https://github.com/orgs/seneca-innovation-center/teams/dev) GitHub team. It is the code owner for the whole repo (see [CODEOWNERS](../../.github/CODEOWNERS)).
- **How they are chosen.** Seneca Innovation Center appoints the first maintainers. After that, any maintainer can nominate a contributor who has made and reviewed good contributions over time. The nominee joins if no maintainer objects within 7 days. A maintainer who steps down or is inactive for 6 months is removed from the team.
- **How they decide.**
  - Pull requests and source submissions need **one approval** from a maintainer who is not the author.
  - ADRs, the roadmap, the [data policy](../data-policy.md), the [privacy policy](../privacy-policy.md) and the [terms](../terms.md) need **consensus**: the change is open for at least 3 working days and no maintainer has an unresolved objection.
  - If maintainers cannot agree, the Dalanda project lead at Seneca Innovation Center decides and records the reason in the pull request.

### Licence and sign-off

This repo stays Apache-2.0. Pull requests are made under the Developer Certificate of Origin (DCO). Submissions made through the website are covered by the site [terms](../terms.md) instead of the DCO. Text added to the project (docs, registry entries, dataset descriptions) must include licence and provenance.

### Data

Contributors share **links** to data, not the data itself. Downloading and processing a linked dataset is allowed only after a maintainer accepts the source, and only as its licence allows. Raw dumps and dataset copies are never committed to this repo. Processing and training code arrives with the phases in the [roadmap](../../ROADMAP.md), each through a reviewed change.

## Consequences

- Work happens in public issues and PRs, not private threads.
- Maintainers do not have to write every line; they do have to review and set direction.
- Contributors should expect review against the published roadmap, not a private backlog.
- [ADR 0002](0002-privacy-retention-and-logging.md) builds on this ADR for how the website handles personal data.
