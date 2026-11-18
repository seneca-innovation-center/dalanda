# ADR 0002: Privacy, retention, and logging

- Status: Proposed
- Date: 2026-11-17 (updated 2026-11-18)
- Deciders: Raed Brahem, Amel Omri, Dalanda maintainers

## Context

The Dalanda site lets contributors propose datasets for the project. They do not upload data. They submit a **link** to a dataset, with the same details the [source registry](../registry.md) records: source name, URL, what is in it, licence, and provenance. Maintainers (see [ADR 0001](0001-open-source-community-model.md)) then review each submission.

That means the site and API handle three kinds of personal data:

- **Account data.** Sign-in goes through Clerk, which holds the contributor's email address.
- **Submissions.** The link plus the free-text fields the contributor writes, tied to their Clerk user ID. Free text can contain anything, including names or contact details. A URL can carry secrets (signed links, share tokens, `user:password@`).
- **IP addresses.** The API sees each caller's IP. We need it for rate limiting, and for nothing else.

There is also data we do not collect but are close to: **the people who appear inside linked datasets**. Derja text is often scraped from social media, so a linked dataset can contain other people's posts and names.

There is no chat. The site does not take conversational text from users.

We are setting these rules before the site and API exist, so the first version is built to them. The public [privacy policy](../privacy-policy.md) and [terms](../terms.md) promise exactly what this ADR requires. If they ever disagree, fix the code or change all three documents in the same PR.

## Decision

### 1. IP addresses are hashed, never stored raw

- The API turns each IP address into `HMAC-SHA256(salt, ip)` before it reaches the rate limiter or any other component. Only the hash is used after that point.
- `salt` is 32 random bytes from a CSPRNG. It lives only in process memory, or in the shared rate-limit store if there is more than one API instance. It is never written to disk, logs, the database, or backups, and never put in config or environment variables. If the shared store is Redis, its disk persistence is turned off (no RDB snapshots, no AOF), so the salt never reaches disk.
- The salt rotates every **24 hours**. The old salt is deleted when it rotates, not archived. After rotation, nobody (including us) can link a hash to an IP or to hashes from the day before.
- A plain unsalted hash is not allowed. There are only about 4 billion IPv4 addresses, so an unsalted hash can be brute-forced back to the IP within minutes.

### 2. Hashed IPs are kept only for the rate-limit window

- Rate-limit counters are keyed by the IP hash and given a TTL equal to the rate-limit window (for example, 60 seconds for a per-minute limit). The counter expires with the window.
- IP hashes are not copied into the submissions table, analytics, or logs.
- The longest window any limit may use is 24 hours, so no IP hash can outlive its salt.

### 3. Logs contain no submission text and no raw IPs

Application logs may contain request ID, route, method, status code, latency, error type, submission ID, review status, the **host name** of a submitted URL (for example `huggingface.co`), and the Clerk user ID.

Application logs must never contain:

- Free-text submission fields: source name, description, licence text, provenance notes, or reviewer comments.
- The **full** submitted URL. Path and query string can hold tokens or identify a private resource; log the host only.
- Raw IP addresses, `X-Forwarded-For`, or any other header that carries a client IP.
- Email addresses or any other Clerk profile field besides the user ID.
- `Authorization` headers, session tokens, or cookies.

This is enforced in four places:

1. **Logger config.** Request-body logging is off for submission routes. Validation errors log the field name and error code, never the value. Exception handlers log the error type and stack trace, never the exception message or the payload: messages often contain user input.
2. **Redaction filter.** A last-line filter on the root logger replaces anything shaped like an IPv4 or IPv6 address, an email address, or a full `http(s)://` URL with `[redacted]`.
3. **Edge and proxy logs.** The web server's own access log (for example nginx `access_log`, or the app server's request log) is turned off, because it records the raw IP before the API hashes it. If a reverse proxy or CDN access log is needed, it uses a format without the client IP and without request bodies. Where the provider cannot drop the IP, its log retention is set to the provider's minimum and the policy says so.
4. **Test.** CI submits a link whose free-text fields and URL query string contain a known marker string, from a known test IP. It captures every log line and fails if the marker, the full URL, or the IP shows up.

Third-party error trackers, if added later, must have request-body capture and IP collection turned off.

### 4. Submitted URLs are checked before they are stored

- The API rejects URLs that are not `https://` (or `http://`), and URLs with embedded credentials (`user:password@host`).
- The form tells contributors to submit public links only, never private share links or signed URLs.
- At submission time, the service may make one request to the URL to check it is reachable. It does **not** download or store the dataset. Any such fetch must block private, loopback, and link-local addresses (to prevent SSRF), follow a small number of redirects, and read headers only.
- Downloading a dataset for processing happens later, only after a maintainer accepts the source, and only as its licence allows, as set by [ADR 0001](0001-open-source-community-model.md#data). Raw dumps are never committed to the repo.

### 5. Retention

| Data | Kept for |
| --- | --- |
| Pending submission | Until a maintainer reviews it. |
| Rejected or withdrawn submission | Hard-deleted **30 days** after the decision or withdrawal. |
| Accepted submission | The source record (name, URL, description, licence, provenance) becomes part of the project's public list of data sources and is kept while the project uses that source. |
| Link between an accepted source and its contributor | Until the contributor deletes their account or asks to be unlinked. |
| Account (email, Clerk user ID) | Until the contributor deletes their account. |
| Hashed IPs | The rate-limit window, at most 24 hours. |
| Application logs | 14 days. |
| Backups | Roll off within 30 days. |

- A scheduled job runs at least daily and hard-deletes expired rows. A soft-delete flag does not count as deletion.
- Contributors can withdraw a pending submission at any time.
- When a Clerk account is deleted (via the Clerk `user.deleted` webhook), within 24 hours: pending, rejected and withdrawn submissions from that user are deleted, and accepted source records are kept but have the contributor's user ID and display name removed.
- Public source records never show a contributor's email address. Credit, if any, uses a display name the contributor chooses. The public registry is a git repo: removing a name changes the current file, but earlier commits still contain it. We do not rewrite git history, and the policy says so.
- Because backups roll off within 30 days, deleted data is gone from backups no more than 30 days after it is deleted live. The policy states the total worst case: 60 days.

### 6. People who appear in linked datasets

- Maintainers reject sources that are not public, or that clearly contain sensitive personal data (health, religion, political views, private messages, contact details) without a lawful basis.
- Anyone can ask us to stop using a source, or to exclude content about them, by emailing the contact address in the policy. Maintainers answer within 30 days. If the request is upheld, the content is excluded from future processing and the source record is updated or removed. A model already trained on that content cannot have it removed; it is excluded from the next version.

### 7. Policy and terms live in this repo

- The canonical text is [docs/privacy-policy.md](../privacy-policy.md) and [docs/terms.md](../terms.md). The front end (FE-8) renders these files at `/privacy` and `/terms` rather than keeping its own copy.
- Both documents show a "Last updated" date at the top. Material changes go through a PR with maintainer review and update that date. They take effect no sooner than 14 days after the new text is published, except where the law requires a faster change.

## Consequences

- Before the submission form goes public, the API ticket(s) must implement: the HMAC hasher and rate-limit TTLs, URL validation and the SSRF-safe reachability check, the log redaction filter, the log-leak CI test, the retention purge job, and the Clerk deletion webhook.
- Debugging is harder because logs never show what a contributor typed or the full link. That cost is accepted. Maintainers see the full submission in the review tool, not in logs.
- Abuse investigation relies on the Clerk user ID; we cannot trace an IP across days by design.
- The policy still has one placeholder (the postal address of Seneca Innovation Center) that a maintainer must fill in.
- **Legal review before launch.** Under Tunisian Organic Law 2004-63, Seneca Innovation Center may need to declare this processing to the INPDP, and may need its authorisation to transfer personal data abroad (Clerk and our hosting provider process data in the United States). Legal review must confirm both, and the policy's transfer section must be updated with the outcome, before the submission form goes public.
