# Privacy policy

Last updated: 2026-11-18 · Draft, not yet in effect

<!--
Before publishing, a maintainer must replace the [TBD: ...] placeholder, and legal review must confirm the INPDP declaration and transfer authorisation (see ADR 0002, Consequences).
-->

Dalanda is a community project building a language model for Tunisian Arabic (Derja). On the Dalanda website, contributors propose datasets for the project by sharing links to them. This policy explains what personal data the site collects, why, how long we keep it, and what you can do about it. It also covers people whose content may appear in datasets that contributors link to.

## Who is responsible

The service is run by Seneca Innovation Center ("we", "us"), which is the data controller:

Seneca Innovation Center
[TBD: postal address]

Contact: [admin@seneca.center](mailto:admin@seneca.center)

## What we collect

| Data | Where it comes from | Why we need it |
| --- | --- | --- |
| Email address and sign-in details | You, when you create an account. Handled by our sign-in provider, Clerk. | To create and secure your account and let you sign in. |
| Sign-in cookies, and the IP address and device information of each sign-in | Your browser, when you sign in. Set and stored by Clerk. | To keep you signed in, and to protect your account from misuse. |
| Account ID | Created by Clerk when you sign up. | To link your submissions to your account. |
| Your submissions | You, when you propose a dataset: the link, source name, description, licence, and provenance notes. | So maintainers can review the dataset, and so accepted sources can be listed with their licence and origin. |
| Display name (optional) | You, if you want credit for an accepted source. | To credit you publicly. We never publish your email address. |
| IP address | Your device, on every request. | To stop abuse through rate limiting. We do not store it as-is (see below). |
| Basic technical records | Our servers. Request time, page or endpoint, status code, response time, error type, account ID. | To keep the service running and fix bugs. |

The sign-in cookies are needed for the site to work. We do not use advertising trackers or analytics cookies, and we do not sell or rent personal data.

## What happens to the links you submit

We store the link and the details you give us so maintainers can review it. When you submit, we may check once that the link works. We do not download or copy the dataset at that point.

If a maintainer accepts the source, its record (name, link, description, licence, and provenance) becomes part of the project's public list of data sources. Only then, and only under that dataset's own licence, may the project use the data to build Dalanda.

Please only submit links to public datasets. Do not submit private share links, links containing passwords or access tokens, or anything you are not allowed to share.

### Credit in the public list

If you choose a display name, it is shown next to the sources you shared in the [public source registry](https://github.com/seneca-innovation-center/dalanda/blob/main/registry/sources.yaml). The registry is a file in a public git repository. When you delete your account or ask us to remove your name, we remove it from the current registry within 24 hours. Earlier versions of the file stay in the repository's history, and copies made by others (for example forks) are outside our control. If you do not want that, do not choose a display name.

## How we handle IP addresses

Before your IP address is used for anything, we run it through a one-way keyed hash. The key changes every 24 hours and the old key is deleted, so after that nobody, including us, can turn the hash back into your IP address or link it to your activity on another day. The hash is kept only as long as the rate limit it belongs to, and never longer than 24 hours.

Clerk sees and stores the IP address of each sign-in, as described in [Clerk's privacy policy](https://clerk.com/legal/privacy).

## What we do not log

Our application logs never contain the text you write in a submission, the full link you submit (only its domain, such as `huggingface.co`), your raw IP address, or your email address.

## How long we keep data

| Data | How long |
| --- | --- |
| Submissions waiting for review | Until a maintainer reviews them. You can withdraw one at any time. |
| Rejected or withdrawn submissions | Deleted automatically 30 days after the decision or withdrawal. |
| Accepted sources | Kept in the public list while the project uses that source. |
| The link between you and an accepted source | Until you delete your account or ask us to remove it. |
| Account (email, account ID) | Until you delete your account. Within 24 hours of deletion, we delete your pending, rejected and withdrawn submissions and remove your display name and account from any accepted source. |
| Hashed IP addresses | Only for the length of the rate-limit window, never more than 24 hours. |
| Technical logs | 14 days. |
| Backups | Backups roll off within 30 days. Data deleted from the live service can stay in a backup for up to 30 more days, so it is fully gone within 60 days at most. |

## If you appear in a linked dataset

Datasets that contributors link to may include public posts or other content written by people who never used this site. We only accept sources that are public. We reject sources that clearly contain sensitive personal data, such as health information, religious or political views, private messages, or contact details.

If you think a source we use contains content about you, or content you wrote, email [admin@seneca.center](mailto:admin@seneca.center) with the source and what you want us to do. We will reply within 30 days. If we agree, we stop using that content in future work and update or remove the source record.

Content that was already used to train a model cannot be removed from that model. It will be excluded from future versions.

## Who else processes your data

We use a small number of service providers who process data for us under contract:

- **Clerk** (authentication): stores your email address, sign-in details, sign-in cookies, and the IP address and device information of each sign-in. See [Clerk's privacy policy](https://clerk.com/legal/privacy).
- **Amazon Web Services**: runs our servers and database.

We only share personal data beyond this if the law requires it. Accepted source records are public by design, as explained above.

Dalanda is linked to Seneca Circle, the community run by Seneca Innovation Center where members are rewarded for contributing. The Dalanda site does not share your account or submission data with Seneca Circle. If that changes, we will update this policy first.

Your data may be processed outside your country, including in the United States.

## Your rights

Depending on where you live (for example under Tunisia's Organic Law No. 2004-63 on personal data protection, or the EU GDPR), you may have the right to:

- see the personal data we hold about you and get a copy;
- correct it;
- delete it (you can withdraw submissions and delete your account yourself on the site);
- object to or restrict how we use it;
- complain to your data protection authority. In Tunisia that is the INPDP (Instance Nationale de Protection des Données Personnelles).

To use any of these rights, email [admin@seneca.center](mailto:admin@seneca.center). We will reply within 30 days.

## Legal basis

Where the law asks for one, we rely on:

- **Contract**, to run your account and handle the submissions you send.
- **Legitimate interest** for three things: keeping the service secure and working (sign-in cookies, IP hashes and technical logs); publishing accepted source records so the project's data is traceable; and using public datasets to build an open language model for Derja.

## Children

Dalanda is not for anyone under 16. If you believe someone under 16 has given us personal data, contact us and we will delete it.

## Security

Traffic is encrypted in transit. Access to production data is limited to the people who run the service. No system is perfectly secure; if we learn of a breach affecting your data, we will tell you and the relevant authority as the law requires. To report a security problem, see [SECURITY.md](../SECURITY.md).

## Changes

We publish changes to this policy in the [public repository](https://github.com/seneca-innovation-center/dalanda/commits/main/docs/privacy-policy.md), so every version and change is visible, and update the date at the top. For material changes, we will also tell signed-in users at least 14 days before the change takes effect.

## Contact

[admin@seneca.center](mailto:admin@seneca.center)
