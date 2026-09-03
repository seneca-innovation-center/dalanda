# Dalanda

Dalanda is a community-built foundational language model for Tunisian Arabic (Derja), in Arabic script and Arabizi, so people can talk to software the way they actually speak.

**Who it is for.** Contributors in Tunisia and the diaspora — linguists, developers, and anyone who can point to a public data source or improve the docs — plus stewards who set goals and review. You do not need a private call to start: the [roadmap](docs/roadmap.md) is the backlog.

**How to contribute.** Open a [Contribution](.github/ISSUE_TEMPLATE/contribution.yml), [Bug](.github/ISSUE_TEMPLATE/bug.yml), or [Data source](.github/ISSUE_TEMPLATE/data-source.yml) issue, then send a pull request with a DCO sign-off (`git commit -s`). Steward review is required; see [CONTRIBUTING.md](CONTRIBUTING.md) and [ADR 0001](docs/adr/0001-open-source-community-model.md). Do not upload training code dumps or datasets in this repo.

## Clone → install → CI green

```bash
git clone https://github.com/1devspace/dalanda.git
cd dalanda
python3 -m venv .venv   # Python 3.9 or newer
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
ruff check .
pytest -q
```

Those two commands (`ruff check .` and `pytest -q`) are what GitHub Actions runs on every pull request. If they pass locally, CI should be green.

## Licence

Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
