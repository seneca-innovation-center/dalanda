# Source registry

[registry/sources.yaml](../registry/sources.yaml) lists every source that has been shared on dalanda.ai and accepted by a maintainer. It is public so anyone can see what Dalanda collects from, and check its licence and origin.

## How entries are added

1. A contributor shares a link on [dalanda.ai](https://dalanda.ai) and describes it: what type of source it is
   and how it is written, and if they know them, its name, a short description and its licence.
2. A maintainer reviews it against the [data policy](data-policy.md) and accepts or declines it.
3. The dalanda.ai admin Sync opens a pull request that adds the accepted links, built from what the
   contributor wrote. CI checks the entries, and a maintainer merges the pull request.

Fixes to existing entries (a dead link, a wrong licence) are welcome as pull requests from anyone.

## Fields

| Field | Required | What it holds |
| --- | --- | --- |
| `id` | yes | Short unique name: lowercase letters, digits and hyphens, for example `tunisian-forum-archive`. |
| `name` | yes | The source's name, as the contributor gave it. Without one, the link's site and path, or `Private dataset` and a short id when the link is withheld. |
| `url` | yes, unless withheld | `https://` or `http://` link. No user names, passwords, access tokens or signed links (`X-Amz-Signature=`, `token=`, `sig=` and similar). |
| `link_withheld` | no | `true` when the contributor did not allow the link to be shown. The entry then has no `url`, and maintainers trace it to the private record by its `id`. |
| `type` | yes | One of `website`, `archive`, `dataset`, `repository`, `social-media`, `other`. |
| `domains` | no | What kind of text: one or more of `forum`, `news`, `subtitle`, `chat`, `literary`, `instruction`, `transcript`, `other`. `chat` means public chats only, such as open channels or public comment threads, never private messages or closed groups. |
| `writing` | no | How it is written: one or more of `arabic-script`, `arabizi`, `french-mixed`. |
| `description` | no | What is in it, in at most 500 characters. |
| `licence` | no | An SPDX identifier such as `CC-BY-4.0`, or a short description of the terms. Left out when nobody knows it: `unknown`, `not sure` and similar values are rejected. |
| `licence_url` | no | Link to the licence or terms of use. |
| `provenance` | no | Who published it, how it was collected, and whether it is public-only. |
| `added` | yes | The date it was accepted, `YYYY-MM-DD`. |
| `credit` | no | The display name of the contributor, if they asked to be credited. Never an email. Removing it later changes the current file only: earlier commits keep it (see the [privacy policy](privacy-policy.md#credit-in-the-public-list)). |

Example:

```yaml
sources:
  - id: example-forum
    name: Example Forum
    url: https://forum.example.org/derja
    type: website
    domains: [forum]
    writing: [arabic-script, arabizi, french-mixed]
    description: Public discussion threads, mostly in Derja.
    licence: CC-BY-4.0
    licence_url: https://creativecommons.org/licenses/by/4.0/
    provenance: Run by the forum owners. Only public threads are linked.
    added: 2026-11-18
```

## What the registry leaves out

- Contributor email addresses, account IDs and anything else from the contributor's account.
- Review notes and rejected submissions.
- Any copy or sample of the source's text.

## Checks

`uv run dalanda-registry check --links` runs the same checks as CI:

- the file is valid YAML with one top-level key, `sources`, and no repeated keys;
- every entry has the required fields (`id`, `name`, `type`, `added`), and every field it has uses allowed values;
- every entry has a `url`, or `link_withheld: true` and no `url`;
- no two entries share an `id`, a `name`, or a link (`http`/`https`, `www.` and a trailing `/` do not make a link different);
- every `url` and `licence_url` resolves. A server that answers 401, 403 or 429 counts as resolving, because many sites refuse automated requests.

CI also runs the link check once a week, so a link that dies later is caught.
