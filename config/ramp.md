# Ramp, pacing and stop rules

One mailbox: hello@tiph.agency (Zoho, EU). Zoho limits outside mail on a rolling one-hour window (50 to 500 per hour, depending on reputation) and does not allow bursts. We stay far below that.

## Daily cap (all emails, first contacts and follow-ups together)

Week 1 starts on the first send day under this plan. Working days only (Mon to Fri in the recipient's time zone).

| Week | Max per day | Max per hour |
| --- | --- | --- |
| 1 | 3 | 1 |
| 2 | 5 | 2 |
| 3 | 10 | 2 |
| 4 | 15 | 3 |
| 5 | 20 | 3 |
| 6 | 30 | 4 |
| 7 | 40 | 5 |
| 8+ | 50 | 6 |

Move up a week only if the previous week had: bounces under 3%, zero spam complaints, no Zoho warning. Otherwise repeat the week.

## Pacing

- At least 6 minutes between any two sends, randomised (6 to 14 minutes).
- Only inside the recipient's office hours, 08:30 to 16:30 local time.
- Send windows (UTC, adjust for daylight saving): APAC 00:00 to 07:00, Europe/UK 07:30 to 15:30, USA 13:30 to 21:00.
- Never more than 2 emails in a row to the same country or the same email provider domain. Exception (Ratif, 18 Oct 2026): while only one market is live, the country limit does not apply. Once two or more markets are live, mix them through each day so we can compare which markets respond.
- Never two contacts at the same company on the same day.

## Stop rules (pause all sending and alert Ratif)

- Any Zoho "Email Outgoing Blocked" or policy notice.
- Any bounce saying "Sender Address Blocked" or naming a blocklist (Spamhaus, Barracuda, etc.).
- Hard bounces above 3% of the day's sends, or 2 hard bounces in a row.
- Any spam complaint or abuse report.

The Zoho outgoing blocks of 7 and 10 Oct 2026 were cleared by Ratif on 18 Oct 2026. Only notices received after that count.

## Hygiene before a send

- Address published on the company's own site or official directory (source URL recorded).
- Domain has MX records and the website is live.
- Address and domain not in `data/suppression.csv`.
- No previous email to that address in `data/messages.csv` unless it is the single follow-up.
