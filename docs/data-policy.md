# Data policy

This page explains what Dalanda collects, what it leaves out, and how to ask for a link to be removed. It covers the **sources** of Derja text. How the dalanda.ai website handles your account and personal data is in the [privacy policy](privacy-policy.md), and the rules for using the site are in the [terms of use](terms.md).

## What we collect

**Links, not data.** Contributors share links to places where Derja is written. With each link we keep:

- the link and the source's name;
- what kind of text it holds and how it is written (Arabic script, Arabizi, French mixed in);
- its licence or terms of use;
- where it comes from: who published it and how.

Accepted sources are listed in the public [source registry](../registry/sources.yaml). The fields are described in [registry.md](registry.md). The registry never holds contributor email addresses or account IDs. A contributor is credited only if they choose a display name.

When the processing phase opens (see the [roadmap](../ROADMAP.md)), text will be collected only from accepted sources and only as each source's licence allows. No source text or dataset copy is stored in this repository.

## What we exclude

We do not accept, or we remove, sources that:

- are not public: private groups or chats, paywalled content, or links that need a password or access token;
- were obtained unlawfully, for example through a data breach or a leak;
- have terms that forbid the use we would make of them, or an unclear licence we cannot resolve;
- consist mainly of personal details: phone numbers, national ID numbers, addresses, health information, religious or political views, or private messages;
- sexualise minors or exist to harass people;
- are not Derja: Modern Standard Arabic, other Arabic dialects, or text in other languages only.

When processing opens, personal details such as phone numbers, ID numbers and email addresses that appear inside accepted sources will be removed or held back. They will not be published.

## Ask for a link to be removed

You can ask us to remove a source if:

- you own the rights to it;
- it contains text you wrote or content about you;
- you think it breaks this policy.

Email [admin@seneca.center](mailto:admin@seneca.center) with the link and the reason. Please do not open a public issue when the request involves your personal information. If it does not, you can also open an issue in this repository.

We reply within 30 days. If we agree, we remove the source from the registry and exclude it, or the content about you, from every future build. A model trained before the removal cannot "unlearn" the text, but the next release will not include it.

## Licence of the data

Each source keeps its own licence. The licence for corpora and models that Dalanda publishes is still being decided and will be added here. The code in this repository is licensed under [Apache-2.0](../LICENSE).

## Changes

Changes to this policy go through a pull request, so every version is visible in the repository history.
