# Roadmap

Dalanda moves through four phases. Each one opens when the one before it has enough to work with. There are no dates.

The language model comes first. Speech-to-text and text-to-speech follow, through the same phases, once the text work is in place.

## 1. Data collection

**Status: open now.**

**Goal:** find enough public Derja text, in every way people write it, to train a first model.

Contributors share links to sources on [dalanda.ai](https://dalanda.ai). Maintainers review each one for licence, provenance and content, and accepted sources go into the public [source registry](registry/sources.yaml). See [CONTRIBUTING.md](CONTRIBUTING.md).

## 2. Processing

**Status: coming soon.**

**Goal:** turn accepted sources into a clean, documented Derja corpus that someone outside the project could rebuild.

- Collect text only from accepted sources, under their licences.
- Clean and normalise the text while keeping Arabic script, Arabizi and French code-switching. Mixed text is a feature of Derja, not noise.
- Separate Derja from Modern Standard Arabic and from other Maghrebi dialects.
- Remove duplicates and remove personal data such as phone numbers and ID numbers.
- Record where every piece of text came from, so a source can be taken out of later builds.

## 3. Training

**Status: coming soon.**

**Goal:** train a language model that reads and writes Derja the way people do.

- Start from an open base model and train it on the Dalanda corpus.
- Share the training setup so others can reproduce the results.
- Then train speech-to-text and text-to-speech models for Derja.

## 4. Evaluation and release

**Status: coming soon.**

**Goal:** measure honestly whether the models understand and produce Derja, then publish them.

- Build test sets that cover Arabic script, Arabizi and code-switched text.
- Have native Tunisian speakers score the model's answers.
- Publish the models with their licence, how they were trained and their evaluation results.

## How the phases open

When a phase opens, its work is posted as GitHub issues with a `phase:` label. The README explains [how issues will work](README.md#how-issues-will-work). Changes to this roadmap go through a pull request.
