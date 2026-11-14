# Ramp, pacing and stop rules

One mailbox: hello@tiph.agency (Zoho, EU). Zoho limits outside mail on a rolling one-hour window (50 to 500 per hour, depending on reputation) and does not allow bursts. We stay far below that.

## Daily cap for new outreach (first emails only)

Ratif, 14 Nov 2026: the ramp caps below limit new outreach (first emails) only. Follow-ups do not count toward them; they have their own limits in "Follow-up limits" below. Replies to people who wrote to us are never capped.

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

## Follow-up limits (separate from the ramp caps, Ratif 14 Nov 2026)

Follow-ups are single replies in the thread of our own first email, sent 7 or more days later, so their number per day is about the number of first emails sent a week earlier. They still leave the same Zoho mailbox, and Zoho judges all outgoing mail together (hourly volume, bursts, bounces, complaints), so they get their own limits instead of none:

- Follow-up daily cap: the same number as the current week's first-email daily cap (week 4: 15, week 5: 20, and so on). This only matters when follow-ups pile up (for example after a pause).
- Follow-up hourly cap: the same number as the current week's first-email hourly cap.
- Combined ceiling for all mail from hello@tiph.agency: at most 2 x the week's daily cap per UTC day and 2 x the hourly cap per hour, far below Zoho's 50 to 500 per hour.
- Pacing, office hours, country and provider rotation, suppression and stop rules apply to follow-ups exactly as to first emails. Any stop rule pauses both.
- Ramp review on Mondays counts bounces and complaints from all sends (first emails and follow-ups).

Primary frequency objective (Ratif, 9 Nov 2026): hit the daily cap every working day. The send task runs every hour, around the clock, and sends up to the hourly cap per run whenever recipients are in their own working hours (Mon to Fri, 08:30 to 16:30 local). The daily cap counts per UTC date. The fixed UTC send windows above are replaced by this recipient-local rule. The limit in practice is the approved queue: keep enough approved emails ready to fill the cap.

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
