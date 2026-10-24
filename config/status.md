# Status

Current state of the outreach. Every send run and reply check reads this first. Update it whenever something changes, and commit the change.

- Sending paused: no
- Live markets (sending allowed): US, AU, SG, HK (APAC live from 26 Oct 2026, approved by Ratif on 24 Oct)
- Paused markets: UK, EU opt-out markets, CH (until the privacy section is live)
- Privacy section "Business contacts we write to" live on tiph.agency: no (branch privacy-business-contacts in ratifplus/tiph not merged yet)
- Current ramp week: 1 (week 1 started Mon 19 Oct 2026): 3 emails per day, 1 per hour
- Ramp week last reviewed: 2026-10-19
- Stop-rule baseline: only Zoho notices and bounces received after 2026-10-18 count (earlier blocks cleared by Ratif on 18 Oct 2026)
- Active send batches: 2026-10-19-us (2 of 15 left; send file batches/2026-10-19-us.send.json) and 2026-10-26-apac (7 approved 24 Oct 2026; send file batches/2026-10-26-apac.send.json)
- Outreach task: scheduled task "Kazinga send run" (trig_014G2vg9rHQAvuWfzDVoGt5z), weekdays at 01:45 and 03:45 UTC (APAC mornings) and 13:45, 15:45 and 17:45 UTC (US office hours). The only outreach task since 20 Oct 2026: every run checks the inbox (replies, opt-outs, bounces), writes follow-ups once a weekday, and sends at most one approved email. It stays on when no approved emails are left. Add fire times for any new market's office hours.
- Old reply-check task "Kazinga outreach replies" (trig_01JPvBn1nJoasWabdMT5CUxr): stopped by Ratif on 20 Oct 2026; its duties moved into the task above.
- Inbox checked up to: 2026-10-23T17:46Z (no replies, bounces, unsubscribes or Zoho notices since 19 Oct)
- Follow-ups last checked: 2026-10-23 (none due; first US follow-ups due from Mon 26 Oct)
- Waiting on Ratif: Swiss follow-ups (7 Zoho drafts from 14 Oct; to be rewritten with the footer before sending), UK retries (Baxter, Glenn, International Forwarding). Zoho Drafts also holds 14 untracked UK drafts from 9 and 10 Oct: never send them.
