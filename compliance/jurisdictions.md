# Jurisdictions

Working rules for cold B2B email from Tiph Ltd. This is an operating summary, not legal advice. Check with a lawyer before large volume in any market. Last reviewed 18 October 2026.

## Every email, every market

- Sender identified: Ratif Ssemujju, Tiph Ltd, 128 City Road, London EC1V 2NX, United Kingdom, Company No. 17199579.
- Honest subject line, no "Re:" or "Fwd:" tricks on first contact.
- One sentence saying where we found the address (e.g. "I found your address on your website"), in the footer below the signature.
- An Unsubscribe link in the footer (mailto:hello@tiph.agency?subject=Unsubscribe), kept out of the main body so the email ends on the demo ask (Ratif, 18 Oct 2026). Treat an Unsubscribe email or any reply asking us to stop as an opt-out: honour it immediately and add to `data/suppression.csv`.
- Link to https://tiph.agency/privacy-policy in the footer (required for EU/UK/CH recipients).
- Only addresses the company publishes itself. No guessed addresses (no firstname@ guessing).
- Each email individually researched and written. No mail merge.
- At most one follow-up, then stop unless they reply.

## Go

| Market | Rule | Extra conditions |
| --- | --- | --- |
| UK | PECR: companies and LLPs ("corporate subscribers") may be emailed without consent, with opt-out. UK GDPR legitimate interest for named contacts. | No sole traders or partnerships. Check Companies House status is "Ltd" or "LLP". |
| USA | CAN-SPAM: opt-out model. | Physical postal address in every email, working opt-out honoured within 10 business days, no deceptive headers or subjects. |
| Netherlands | Telecommunicatiewet 11.7: B2B to legal persons allowed with opt-out. | Legal entities only (BV, NV). GDPR for named contacts. |
| Belgium | B2B to legal persons allowed with opt-out (impersonal or functional addresses safest). | Prefer role addresses. |
| France | CNIL: B2B email allowed without consent if the message relates to the recipient's profession. | Message must be about their freight work. Write in French. |
| Ireland | ePrivacy Regs 2011: corporate addresses allowed with opt-out. | |
| Sweden, Finland | B2B to legal persons allowed with opt-out. | Legal entities only. |
| Portugal | Legal persons may be emailed with opt-out. | Legal entities only. |
| Australia | Spam Act 2003: "inferred consent" where the address is conspicuously published, the message relates to the recipient's business role, and no statement on the site refuses unsolicited messages. | Check the contact page for "no unsolicited" wording. Keep the source URL. |
| Singapore | Spam Control Act: unsubscribe facility required. Above 100 similar messages in 24 h, 1,000 in 30 days, or 1 million in a year it counts as bulk and needs `<ADV>` in the subject. | Keep Singapore under 20 per day and 300 per month. PDPA applies to named contacts. |
| Hong Kong | UEMO: opt-out model. Unsubscribe statement required; honour within 10 working days. | Check the Do-Not-Call registers do not cover email (they cover phone/fax/SMS). |

## Careful

| Market | Rule | Our position |
| --- | --- | --- |
| Switzerland | UWG Art. 3(1)(o): mass advertising by email needs prior consent. | Individual, researched one-to-one emails only. Low volume (max 5 per day). No new Swiss sends without Ratif's say-so per batch. |

## Skip (consent required even for B2B)

Germany, Austria, Italy, Spain, Poland, Denmark, mainland China, South Korea. Add `@domain` rows to `suppression.csv` with reason `excluded_market` if one of their companies turns up in research.

Not yet reviewed (do not email until reviewed): Japan, Canada (CASL is strict), UAE, India, Norway, Czechia, Luxembourg, other EU states.
