# Contributing

The community builds. Stewards set goals and review. Read [ADR 0001](docs/adr/0001-open-source-community-model.md) and the [roadmap](docs/roadmap.md) before you open an issue.

## How to propose work

1. Open a scoped issue using **Contribution**, **Bug**, or **Data source**.
2. Wait for steward feedback if the change is large or adds text/data-source claims.
3. Fork, branch, and send a PR against `main`.
4. Sign off every commit (`git commit -s`) for the [DCO](https://developercertificate.org/).
5. If the PR adds text, fill in licence and provenance on the PR template.

Do not open a PR that uploads a training corpus, weights, or a scrape.

## Local check (same as CI)

```bash
python3 -m venv .venv   # Python 3.9 or newer
source .venv/bin/activate
pip install -e ".[dev]"
ruff check .
pytest -q
```

CI on each pull request runs that lint step and the placeholder test. Both must pass.
