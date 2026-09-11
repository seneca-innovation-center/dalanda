# Security

Please do not open a public issue for a vulnerability.

## How to report

Use GitHub's [private vulnerability reporting](https://github.com/seneca-innovation-center/dalanda/security/advisories/new) on this repository.

Include:

- what the issue is
- how to reproduce it
- versions or commit hashes if you have them
- any workaround you already know

We will acknowledge the report and tell you how we plan to handle it.

## What is in scope

This repository is still a public scaffold (docs, CI, contribution process). Reports about leaked secrets, unsafe GitHub workflows, dependency issues, or anything that could harm people who clone the repo are in scope.

Model weights, training data, and hosted inference are not in this tree yet. When they appear, this file will say how to report problems with those too.

## Secrets

Never commit API keys, tokens, or `.env` files. Use `.env.example` as the template. CI runs Gitleaks on the full git history of every pull request. GitHub secret scanning and push protection are on. That does not replace careful review.

Full history was scanned with Gitleaks on 2026-09-11 (all commits then on `main`). No secrets or API keys were found, so nothing to rotate. There is no Dockerfile or docker-compose in this repository; do not add credentials if those files land later.

## Dependency scanning

Dependabot is enabled for pip and GitHub Actions. CI also runs `pip-audit` on every pull request.
