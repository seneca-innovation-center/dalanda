# Privacy policy

Last updated: 2026-11-19 · Draft, not yet in effect

<!--
Before publishing, legal review must confirm the INPDP declaration and transfer authorisation (see ADR 0002, Consequences).
-->

Dalanda is a community project building a language model for Tunisian Arabic (Derja). On the Dalanda website you can try a Derja chat demo and help the project by sharing links to datasets. This policy explains what personal data the site collects, why, how long we keep it, and what you can do about it. It also covers people whose content may appear in datasets that contributors link to.

## Who is responsible

The service is run by Seneca Innovation Center ("we", "us"), which is the data controller:

Seneca Innovation Center
5bis Rue Dag Hammarskjoeld, El Menzah 5
Ariana 2091, Tunisia

Contact: [admin@seneca.center](mailto:admin@seneca.center)

## What we collect

| Data | Where it comes from | Why we need it |
| --- | --- | --- |
| Email address and sign-in details | You, when you create an account. Handled by our sign-in provider, Clerk. | To create and secure your account and let you sign in. |
| Sign-in cookies, and the IP address and device information of each sign-in | Your browser, when you sign in. Set and stored by Clerk. | To keep you signed in, and to protect your account from misuse. |
| Account ID | Created by Clerk when you sign up. | To link your chats and submissions to your account. |
| Your chats | You, when you use the chat: your messages and the answers you get. | To answer you, and to show you your chat history. Used for training only if you opt in (see below). |
| Usage records | Our servers, when you chat. Number of chats and messages, message length, model used, and cost. Never the text of a message. | To apply the free-use limits and keep the demo's costs under control. |
| Your training choice | You, if you opt in to letting your chats help train Dalanda. | To know whether we may use your chats for training, and since when. |
| Your submissions | You, when you share a dataset: the link, how it is written, an optional short note, and whether the link may be shown publicly. | So maintainers can review the dataset, and so accepted sources can be listed with their licence and origin. |
| Display name (optional) | You, if you want credit for an accepted source. | To credit you publicly. We never publish your email address. |
| IP address | Your device, on every request. | To stop abuse through rate limiting. We do not store it as-is (see below). |
| Basic technical records | Our servers. Request time, page or endpoint, status code, response time, error type, account ID. | To keep the service running and fix bugs. |

The sign-in cookies are needed for the site to work. We do not use advertising trackers or analytics cookies, and we do not sell or rent personal data.

## The chat

The chat is a demo. Its answers come from third-party AI models that we tested for Derja, not from a Dalanda model. To get an answer, the text of your messages is sent to the model provider through FreeLLM API (see "Who else processes your data"). Please do not type sensitive personal information, such as health details, passwords, or other people's contact details, into the chat.

We store your chats so you can see your history. Messages about self-harm, distress or abuse get a fixed, caring reply instead of a model answer; to do that, each message is checked automatically by our own systems, and nothing extra is stored about it. Messages flagged by this check are never used for training.

### Training is opt-in

Your chats are used to help train Dalanda only if you opt in. You can opt out at any time. After you opt out, your chats are no longer used for new training. Chats that were already used to train a model cannot be removed from that model, but they are excluded from future versions. Chats are never published.

## What happens to the links you submit

We store the link and the details you give us so maintainers can review it. When you submit, we may check once that the link works. We do not download or copy the dataset at that point.

You can share links to public or private datasets, as long as you are allowed to share them. By sharing a link, you give the project the right to access and use the dataset, as its licence allows. Do not put passwords or access tokens inside a link.

If a maintainer accepts the source, its record (name, description, licence, and provenance) becomes part of the project's public list of data sources. The link itself is shown only if you allowed it; otherwise the record is listed without it. Only after acceptance may the project use the data to build Dalanda.

### Credit in the public list

If you choose a display name, it is shown next to the sources you shared in the [public source registry](https://github.com/seneca-innovation-center/dalanda/blob/main/registry/sources.md). The registry is a file in a public git repository. When you delete your account or ask us to remove your name, we remove it from the current registry within 24 hours. Earlier versions of the file stay in the repository's history, and copies made by others (for example forks) are outside our control. If you do not want that, do not choose a display name.

## How we handle IP addresses

Before your IP address is used for anything, we run it through a one-way keyed hash. The key changes every 24 hours and the old key is deleted, so after that nobody, including us, can turn the hash back into your IP address or link it to your activity on another day. The hash is kept only as long as the rate limit it belongs to, and never longer than 24 hours.

Clerk sees and stores the IP address of each sign-in, as described in [Clerk's privacy policy](https://clerk.com/legal/privacy).

## What we do not log

Our application logs never contain the text of your chat messages, the text you write in a submission, the full link you submit (only its domain, such as `huggingface.co`), your raw IP address, or your email address.

## How long we keep data

| Data | How long |
| --- | --- |
| Chats and usage records | Until you delete your account. Deleted within 24 hours of account deletion. |
| Your training choice | Until you delete your account. |
| Submissions waiting for review | Until a maintainer reviews them. You can withdraw one at any time. |
| Rejected or withdrawn submissions | Deleted automatically 30 days after the decision or withdrawal. |
| Accepted sources | Kept in the public list while the project uses that source. |
| The link between you and an accepted source | Until you delete your account or ask us to remove it. |
| Account (email, account ID) | Until you delete your account. Within 24 hours of deletion, we delete your chats, your pending, rejected and withdrawn submissions, and remove your display name and account from any accepted source. |
| Hashed IP addresses | Only for the length of the rate-limit window, never more than 24 hours. |
| Technical logs | 14 days. |
| Backups | Backups roll off within 30 days. Data deleted from the live service can stay in a backup for up to 30 more days, so it is fully gone within 60 days at most. |

## If you appear in a linked dataset

Datasets that contributors link to may include posts or other content written by people who never used this site. We reject sources that clearly contain sensitive personal data, such as health information, religious or political views, private messages, or contact details.

If you think a source we use contains content about you, or content you wrote, email [admin@seneca.center](mailto:admin@seneca.center) with the source and what you want us to do. Some sources are listed without their link, at the contributor's request; you can name those by their name or description in the [public source registry](https://github.com/seneca-innovation-center/dalanda/blob/main/registry/sources.md). We will reply within 30 days. If we agree, we stop using that content in future work and update or remove the source record.

Content that was already used to train a model cannot be removed from that model. It will be excluded from future versions.

## Who else processes your data

We run our servers and database ourselves, on machines operated by Seneca Innovation Center. We also use a small number of service providers who process data for us under contract:

- **Clerk** (authentication): stores your email address, sign-in details, sign-in cookies, and the IP address and device information of each sign-in. See [Clerk's privacy policy](https://clerk.com/legal/privacy).
- **FreeLLM API and the AI model providers it connects to** (chat answers): receive the text of your chat messages to generate answers. The models we use change as we test them; email us for the current list.

We only share personal data beyond this if the law requires it. Accepted source records are public by design, as explained above.

Dalanda is linked to Seneca Circle, the community run by Seneca Innovation Center where members are rewarded for contributing. The Dalanda site does not share your account, chat or submission data with Seneca Circle. If that changes, we will update this policy first.

Your data may be processed outside Tunisia: Clerk processes data in the United States, and AI model providers may process chat messages in the United States and other countries.

## Your rights

Depending on where you live (for example under Tunisia's Organic Law No. 2004-63 on personal data protection, or the EU GDPR), you may have the right to:

- see the personal data we hold about you and get a copy;
- correct it;
- delete it (you can withdraw submissions and delete your account yourself on the site);
- withdraw your consent to training at any time;
- object to or restrict how we use it;
- complain to your data protection authority. In Tunisia that is the INPDP (Instance Nationale de Protection des Données Personnelles).

To use any of these rights, email [admin@seneca.center](mailto:admin@seneca.center). We will reply within 30 days.

## Legal basis

Where the law asks for one, we rely on:

- **Contract**, to run your account, answer your chats, show your chat history, and handle the submissions you send.
- **Consent**, to use your chats for training. You can withdraw it at any time.
- **Legitimate interest** for three things: keeping the service secure, working and affordable (sign-in cookies, IP hashes, usage records and technical logs); publishing accepted source records so the project's data is traceable; and using datasets to build an open language model for Derja.

## Children

Dalanda is not for anyone under 16. If you believe someone under 16 has given us personal data, contact us and we will delete it.

## Security

Traffic is encrypted in transit. Access to production data is limited to the people who run the service. No system is perfectly secure; if we learn of a breach affecting your data, we will tell you and the relevant authority as the law requires. To report a security problem, see [SECURITY.md](../SECURITY.md).

## Changes

We publish changes to this policy in the [public repository](https://github.com/seneca-innovation-center/dalanda/commits/main/docs/privacy-policy.md), so every version and change is visible, and update the date at the top. For material changes, we will also tell signed-in users at least 14 days before the change takes effect.

## Contact

[admin@seneca.center](mailto:admin@seneca.center)
