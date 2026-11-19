# Dalanda

Dalanda is an open-source, community-built project to make AI models that understand and speak Tunisian Derja: first a language model, then speech-to-text and text-to-speech.

[![CI](https://github.com/seneca-innovation-center/dalanda/actions/workflows/ci.yml/badge.svg)](https://github.com/seneca-innovation-center/dalanda/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

## Why

Most AI models handle Modern Standard Arabic and ignore the Arabic people in Tunisia actually use. Derja is written in Arabic script and in Arabizi (Latin letters and numbers, like `3aslema`), and it switches into French in the middle of a sentence. Dalanda builds models for Derja as people really write and speak it.

The end goal is an open model that anyone can use, study and build on.

## Status

| Phase | Status |
| --- | --- |
| Data collection | **Open now.** Share links to Derja text. |
| Processing | Coming soon |
| Training | Coming soon |
| Evaluation and release | Coming soon |

Each phase is described in the [roadmap](ROADMAP.md).

## Contribute today: share a source

Right now the project needs one thing: places where Derja is written. You share a **link**, not files.

1. Go to [dalanda.ai](https://dalanda.ai) and sign in with your email.
2. Open the Contribute page and paste the link: a website, an archive, a dataset you found or collected yourself, or a repository. Public and private datasets are both welcome, as long as you are allowed to share them.
3. Say what type of source it is (website, archive, dataset, repository, social media or other) and how it is written (Arabic script, Arabizi, mixed with French).
4. Optionally, give its name and a short description of what is in it. If you know its licence or where it comes from, say so in the description: it helps the maintainer check it.
5. Choose whether the link may be shown publicly, then submit. A maintainer reviews the source against the [data policy](docs/data-policy.md).
6. If it is accepted, it is added to the public [source registry](registry/sources.md) so anyone can see what has been collected. If you chose not to show the link, the entry is listed without it.

Not sure whether a source fits? [CONTRIBUTING.md](CONTRIBUTING.md) explains what makes a good source and lists the kinds of sources we are looking for. If you cannot use the website, open a [Suggest a source](https://github.com/seneca-innovation-center/dalanda/issues/new?template=suggest-source.yml) issue instead.

### Seneca Circle

Contributors are recognised and rewarded through [Seneca Circle](https://circle.seneca.center), the Seneca Innovation Center community.

## How issues will work

When processing, training and evaluation open, the work will be split into GitHub issues, labelled by phase (`phase: processing`, `phase: training`, `phase: evaluation`). Issues that are a good place to start will carry `good first issue`.

To pick one up, comment on the issue to say you are taking it. A maintainer assigns it to you, and you open a pull request that links the issue. One person works on an issue at a time, so check that it has no assignee first.

Until then, you can:

- share sources on [dalanda.ai](https://dalanda.ai);
- check the [source registry](registry/sources.md) and report dead links or wrong details;
- point us to related projects on Tunisian or Derja language work;
- report problems with this repository as a [bug](https://github.com/seneca-innovation-center/dalanda/issues/new?template=bug-report.yml).

## Getting started with this repository

There is no model code here yet. The repository holds the project docs, the source registry and the checker that CI runs on it. You need Python 3.11 or newer and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/seneca-innovation-center/dalanda.git
cd dalanda
uv sync --extra dev
```

## Usage

Check the registry the same way CI does:

```bash
uv run dalanda-registry check                # format and duplicates
uv run dalanda-registry check --links        # also checks that every link resolves
uv run dalanda-registry render               # rewrites registry/sources.md from sources.yaml
```

```text
registry/sources.yaml: 0 sources, format and duplicates OK
```

Run the tests and linters:

```bash
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy
```

## Documentation

- [ROADMAP.md](ROADMAP.md): the phases and their goals.
- [CONTRIBUTING.md](CONTRIBUTING.md): how to contribute and how review works.
- [docs/data-policy.md](docs/data-policy.md): what we collect, what we exclude, and how to ask for a link to be removed.
- [docs/registry.md](docs/registry.md): the fields in each registry entry.
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md): how a link gets from the website to the registry.
- [docs/adr/](docs/adr/): decision records. [ADR 0001](docs/adr/0001-open-source-community-model.md) says who the maintainers are and how they decide; [ADR 0002](docs/adr/0002-privacy-retention-and-logging.md) sets the website's privacy, retention and logging rules.
- [docs/privacy-policy.md](docs/privacy-policy.md) and [docs/terms.md](docs/terms.md): for the dalanda.ai website.
- [SUPPORT.md](SUPPORT.md), [SECURITY.md](SECURITY.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [CHANGELOG.md](CHANGELOG.md).

## License

The code in this repository is licensed under the [Apache License 2.0](LICENSE). Each source in the registry keeps its own licence. The licence for data that Dalanda publishes is still being decided and will be added here.
