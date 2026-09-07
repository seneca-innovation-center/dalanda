# Dalanda

Dalanda is a community project to build a language model that understands Tunisian Arabic (Derja), in Arabic script and Latin Arabizi, so people can talk to software the way they actually speak.

This repository is the public home of that work. It holds the licence, docs, issue templates, and CI. Training code and datasets are not in this tree yet; they will land only after review.

It is for contributors in Tunisia and the diaspora, and for stewards who set the [roadmap](docs/roadmap.md) and review changes. Start from an issue. You do not need a call.

[![CI](https://github.com/seneca-innovation-center/dalanda/actions/workflows/ci.yml/badge.svg)](https://github.com/seneca-innovation-center/dalanda/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/seneca-innovation-center/dalanda)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-3776AB)](pyproject.toml)

## Quick start

Needs Git and Python 3.9 or newer. From a clone, this should finish in under a minute:

```bash
git clone https://github.com/seneca-innovation-center/dalanda.git
cd dalanda
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest -q
```

GitHub Actions runs the same lint, format, and test commands on every pull request.

## How to contribute

Open a **Contribution**, **Bug**, or **Data source** issue, then send a pull request. Sign off your commits (`git commit -s`). If you add written material, fill in licence and provenance on the PR template. Do not upload corpora, weights, or scrapes.

See [CONTRIBUTING.md](CONTRIBUTING.md), the [code of conduct](CODE_OF_CONDUCT.md), and [ADR 0001](docs/adr/0001-open-source-community-model.md).

## Docs

- [Roadmap](docs/roadmap.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Security](SECURITY.md)
- [Changelog](CHANGELOG.md)

## Licence

Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
