# Architecture

Today Dalanda has two parts: the dalanda.ai website, where people share sources, and this repository, which holds the public record. The model pipeline does not exist yet. Its phases are described in the [roadmap](../ROADMAP.md).

```text
Contributor
    │  shares a link (no files)
    ▼
dalanda.ai ──► maintainer review ──► accepted ──► registry/sources.yaml (this repo)
                     │                                   │
                     └─► rejected: not published         └─► CI: format, duplicates, links
```

## Components

### dalanda.ai

The website where contributors sign in with their email and submit a link with its details. It stores submissions while they wait for review. Its code is not in this repository. How it handles personal data is in the [privacy policy](privacy-policy.md).

### Maintainer review

A maintainer checks each submission against the [data policy](data-policy.md): language, licence, provenance and personal data. Accepted sources reach the registry through a pull request that the website's admin screen opens (its Sync button). A link the contributor did not allow to be shown is added with `link_withheld: true` and no `url`.

### Source registry

[registry/sources.yaml](../registry/sources.yaml) is the public list of accepted sources. Its fields are in [registry.md](registry.md). [registry/sources.md](../registry/sources.md) is generated from it as a readable table.

### Registry checker

`src/dalanda_registry` is a small Python package that validates the registry file, checks its links, and generates `sources.md`. CI runs it on every pull request and once a week.

| Module | Responsibility |
| --- | --- |
| `validate.py` | Loads the YAML, rejects repeated keys, checks fields and duplicates. |
| `links.py` | Checks that each link still resolves. |
| `cli.py` | The `dalanda-registry check` command. |

## Later

When processing, training and evaluation start, their code and docs will be added here with their own section in this file.
