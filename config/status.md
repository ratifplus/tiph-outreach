# Status

Current state of the outreach. Every send run and reply check reads this first. Update it whenever something changes, and commit the change.

- Sending paused: no
- Live markets (sending allowed): US
- Paused markets: UK, EU opt-out markets, CH (until the privacy section is live)
- Privacy section "Business contacts we write to" live on tiph.agency: no (branch privacy-business-contacts in ratifplus/tiph not merged yet)
- Current ramp week: 1 (week 1 started Mon 19 Oct 2026): 3 emails per day, 1 per hour
- Ramp week last reviewed: 2026-10-19
- Stop-rule baseline: only Zoho notices and bounces received after 2026-10-18 count (earlier blocks cleared by Ratif on 18 Oct 2026)
- Active send batch: 2026-10-19-us (15 approved 19 Oct 2026; send file batches/2026-10-19-us.send.json)
- Send task: scheduled task "Kazinga send run" (trig_014G2vg9rHQAvuWfzDVoGt5z), weekdays 09:45, 11:45 and 13:45 New York time. It disables itself when nothing approved is left; re-enable it after approving a new batch, and add fire times for any new market's office hours.
- Reply check: scheduled task "Kazinga outreach replies" (trig_01JPvBn1nJoasWabdMT5CUxr), weekdays 08:52 Berlin time
- Waiting on Ratif: Swiss follow-ups (7 Zoho drafts from 14 Oct; to be rewritten with the footer before sending), UK retries (Baxter, Glenn, International Forwarding). Zoho Drafts also holds 14 untracked UK drafts from 9 and 10 Oct: never send them.
