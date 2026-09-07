# Contributing

The community builds. Stewards set goals and review. Read [ADR 0001](docs/adr/0001-open-source-community-model.md) and the [roadmap](docs/roadmap.md) before you open an issue. By participating you also agree to the [code of conduct](CODE_OF_CONDUCT.md).

## How to propose work

1. Open a scoped issue using **Contribution**, **Bug**, or **Data source**.
2. Wait for steward feedback if the change is large or adds text or data-source claims.
3. Fork, branch from `main`, and open a pull request.
4. Sign off every commit (`git commit -s`) for the [DCO](https://developercertificate.org/).
5. If the PR adds text, fill in licence and provenance on the PR template.

Do not open a PR that uploads a training corpus, weights, or a scrape.

## Local check (same as CI)

```bash
python3 -m venv .venv   # Python 3.9 or newer
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest -q
```

To rewrite Python files to match the formatter, run `ruff format .`.

## Coding standards

- Python 3.9 or newer.
- Lint and format with Ruff (`ruff check`, `ruff format`). Config lives in `pyproject.toml`.
- Keep PRs scoped. This repo is still plumbing: no training loops, no data dumps.
- Do not commit `.env`, credentials, or personal data.

CI on each pull request runs lint, format check, tests, and a secret scan. Those must pass, and a steward review is required before merge.
