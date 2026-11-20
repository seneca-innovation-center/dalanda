# Security policy

## Reporting a vulnerability

Please do not report security problems in public GitHub issues.

Report them privately through [GitHub private vulnerability reporting](https://github.com/seneca-innovation-center/dalanda/security/advisories/new), or by email to [dalanda@seneca.center](mailto:dalanda@seneca.center).

Please include:

- what the problem is and what someone could do with it;
- how to reproduce it;
- the commit, file or page affected;
- a fix or workaround, if you know one.

We acknowledge reports within 5 working days and tell you what we plan to do.

## Scope

In scope:

- this repository: the registry checker, CI workflows, and anything that could harm people who clone or contribute to it;
- the [dalanda.ai](https://dalanda.ai) website;
- personal data that should not be in the [source registry](registry/sources.md).

To ask for a source to be removed for rights or privacy reasons, follow the [data policy](docs/data-policy.md#ask-for-a-link-to-be-removed).

## Supported versions

Only the latest commit on `main` is supported.

## Secrets

Never commit API keys, tokens or `.env` files. CI scans the full Git history with Gitleaks on every pull request.
