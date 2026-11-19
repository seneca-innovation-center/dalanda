# Contributing to Dalanda

Thanks for helping build AI models for Tunisian Derja. Today the main way to contribute is to share links to Derja text. Model work comes later and will open as GitHub issues (see [what's coming](#whats-coming)).

By taking part you agree to the [code of conduct](CODE_OF_CONDUCT.md).

## Share a source

1. Sign in at [dalanda.ai](https://dalanda.ai) with your email.
2. Paste the link and describe the source: what kind of text it holds, how it is written, its licence, and where it comes from.
3. Submit it. A maintainer reviews it.

You share a link only. Do not upload files, scrape a site, or send us a copy of a dataset.

If you cannot use the website, open a [Suggest a source](https://github.com/seneca-innovation-center/dalanda/issues/new?template=suggest-source.yml) issue with the same details.

## Wanted sources

We welcome:

- **Public sources:** websites, forums, blogs, news sites, archives, subtitle collections, and open datasets with Derja text.
- **Data you collected yourself:** text you gathered and have the right to share, such as transcripts of your own recordings or a corpus you built. Publish it first with a licence (for example on Hugging Face, Zenodo or GitHub) and share that link. Tell us how you collected it and whether the people in it agreed.
- **Related repositories and projects:** code, tools, papers or datasets about Tunisian or Derja language work, even if they are small or unfinished.

## What makes a good source

A good source:

- **is mostly Derja.** Text in Modern Standard Arabic, or in Algerian, Moroccan or Libyan Arabic, is not what we need. A few MSA phrases inside Derja are fine.
- **is written the way people write.** Arabic script, Arabizi and French mixed in are all welcome. Do not "fix" the spelling.
- **has a clear licence or terms of use.** Open licences (such as Creative Commons or open-data licences) are best. If you are not sure, say so: we would rather know.
- **is yours to share.** Public sources are best. A private dataset is welcome if you are allowed to share it and give us access; you can choose to keep its link out of the public registry. No leaked data, no content taken from behind a paywall or access control you were not given, and no passwords or access tokens inside the link.
- **is not mainly about private people.** We do not want sources whose main content is personal details: phone numbers, ID numbers, addresses, health information, or private messages.
- **is substantial.** A site with thousands of posts is worth more than one article. Small sources are still welcome if the text is rare, for example a regional variety.

See the [data policy](docs/data-policy.md) for exactly what we collect and exclude.

## How review works

1. A maintainer checks the source against the list above: language, licence, provenance and personal data.
2. The source is accepted, rejected, or held while we ask you a question. Rejected sources are not added anywhere.
3. Accepted sources are added to the public [source registry](registry/sources.md), and CI checks every entry. If the contributor chose not to show the link, the entry is listed without it.
4. Each source keeps its own licence. The project only uses a source as its licence allows.

Anyone can ask for a source to be removed later. The [data policy](docs/data-policy.md#ask-for-a-link-to-be-removed) explains how.

## Improve this repository

You can also fix the docs, report a dead link in the registry, or improve the registry checker.

```bash
git clone https://github.com/seneca-innovation-center/dalanda.git
cd dalanda
uv sync --extra dev
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy
uv run dalanda-registry check
```

Then:

1. Create a branch, for example `docs/fix-roadmap-typo` or `registry/fix-dead-link`.
2. Make your change and add or update tests if you changed code.
3. Sign off every commit with `git commit -s`. This certifies the [Developer Certificate of Origin](https://developercertificate.org/). No CLA is required.
4. Open a pull request using the template and link the issue it closes.

Every pull request needs green CI (lint, type check, tests with at least 80% coverage, the registry check, secret scanning and the dependency audit) and an approval from a maintainer. Who the maintainers are and how they decide is in [ADR 0001](docs/adr/0001-open-source-community-model.md).

Code style: Ruff formats and lints Python, and mypy runs in strict mode. The settings are in `pyproject.toml`.

New registry entries come from accepted submissions on dalanda.ai, so please do not open a pull request that adds a new source. Corrections to existing entries are welcome.

## What's coming

Processing, training and evaluation are next (see the [roadmap](ROADMAP.md)). When each one opens, its tasks will be posted as issues labelled `phase: processing`, `phase: training` or `phase: evaluation`, with `good first issue` on the easier ones. Comment on an issue to take it, and a maintainer will assign it to you. Until then, sharing sources is the most useful thing you can do.

## Questions

Open a [GitHub issue](https://github.com/seneca-innovation-center/dalanda/issues/new/choose). For security problems, follow [SECURITY.md](SECURITY.md) instead.
