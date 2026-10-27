# Status

Current state of the outreach. Every send run and reply check reads this first. Update it whenever something changes, and commit the change.

- Sending paused: no
- Live markets (sending allowed): US, AU, SG, HK (APAC live from 26 Oct 2026, approved by Ratif on 24 Oct)
- Paused markets: UK, EU opt-out markets, CH (until the privacy section is live)
- Privacy section "Business contacts we write to" live on tiph.agency: no (branch privacy-business-contacts in ratifplus/tiph not merged yet)
- Current ramp week: 2 (week 1 started Mon 19 Oct 2026; raised to week 2 on 26 Oct after 13 sends, 0 bounces, 0 complaints, no Zoho warning): 5 emails per day, 2 per hour
- Ramp week last reviewed: 2026-10-26
- Stop-rule baseline: only Zoho notices and bounces received after 2026-10-18 count (earlier blocks cleared by Ratif on 18 Oct 2026)
- Active send batches: 2026-10-19-us (1 of 15 left; send file batches/2026-10-19-us.send.json) and 2026-10-26-apac (7 approved 24 Oct 2026; send file batches/2026-10-26-apac.send.json)
- Outreach task: scheduled task "Kazinga send run" (trig_014G2vg9rHQAvuWfzDVoGt5z), weekdays at 01:45 and 03:45 UTC (APAC mornings) and 13:45, 15:45 and 17:45 UTC (US office hours). The only outreach task since 20 Oct 2026: every run checks the inbox (replies, opt-outs, bounces), writes follow-ups once a weekday, and sends at most one approved email. It stays on when no approved emails are left. Add fire times for any new market's office hours.
- Old reply-check task "Kazinga outreach replies" (trig_01JPvBn1nJoasWabdMT5CUxr): stopped by Ratif on 20 Oct 2026; its duties moved into the task above.
- Inbox checked up to: 2026-10-27T13:52Z (no replies, bounces, unsubscribes or Zoho notices since 19 Oct; one unrelated website enquiry from a freelance writer on 27 Oct, ignored)
- Send authorization (Ratif, in chat, 27 Oct 2026 03:5xZ): "You have authorization to send all the remaining emails autonomously." Covers the approved rows of 2026-10-19-us and 2026-10-26-apac. Ramp caps, pacing, office hours and stop rules still apply. Follow-up batches still need his explicit "send".
- Send tool: SG-globalalliance-1-m1 sent 2026-10-27T01:47Z. The 03:45Z run was blocked by tool permission on AU-bullocks-1-m1; Ratif then had it sent from chat at 03:50Z. Blocks happen in unattended runs (4 times on 26 Oct); fix is the task's "Automatically approve" setting. The 13:45Z run on 27 Oct was also blocked by tool permission on US-rlswearer-1-m1 Ratif then had it sent from chat at 13:48Z.
- Follow-ups last checked: 2026-10-27 (3 US follow-ups in batch 2026-10-26-us-fu and 3 in batch 2026-10-27-us-fu, all waiting for Ratif's approval)
- Waiting on Ratif: Swiss follow-ups (7 Zoho drafts from 14 Oct; to be rewritten with the footer before sending), UK retries (Baxter, Glenn, International Forwarding). Zoho Drafts also holds 14 untracked UK drafts from 9 and 10 Oct: never send them.
