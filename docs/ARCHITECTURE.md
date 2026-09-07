# Architecture

Dalanda’s product is a Tunisian Derja language model. This repository is not that model yet. It is the public layout the community will build into.

```text
dalanda/
  dalanda/          Python package (version only, for now)
  tests/            Placeholder tests so CI has something real to run
  configs/          Shared config later (not a dataset)
  docs/             Roadmap, ADRs, this file
  .github/          CI, issue and PR templates, branch ruleset
```

There is no API, no training loop, and nothing to self-host. When those land, they get their own docs and a new ADR.

Stewards set goals in [roadmap.md](roadmap.md). Review and licence rules are in [adr/0001-open-source-community-model.md](adr/0001-open-source-community-model.md).
