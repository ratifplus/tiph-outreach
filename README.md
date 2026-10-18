# tiph-outreach

Prospect database and operating rules for Kazinga outreach by Tiph Ltd (company no. 17199579).

**Private repository.** It holds business contact data. Never make it public, never copy it into the website repo.

## Layout

| Path | What it holds |
| --- | --- |
| `PLAYBOOK.md` | How each outreach run works: research, writing, approval, paced sending, replies |
| `compliance/jurisdictions.md` | Which countries we email, under what rule, and what each email must contain |
| `compliance/legitimate-interest.md` | UK/EU GDPR legitimate interest assessment for B2B prospecting |
| `compliance/privacy-notice-section.md` | Added to tiph.agency/privacy-policy on branch privacy-business-contacts (18 Oct 2026); live once merged |
| `config/ramp.md` | Daily send limits by week, pacing and stop rules |
| `config/status.md` | Current state: live and paused markets, ramp week, pauses, scheduled tasks. Read first by every run |
| `data/companies.csv` | One row per company researched |
| `data/contacts.csv` | One row per address we may email (always tied to a company) |
| `data/messages.csv` | Every email: draft, approved, sent, bounced, replied |
| `data/suppression.csv` | Permanent do-not-contact list (addresses and domains). Checked before every draft |
| `batches/` | One file per batch with the full text of each email, for Ratif's approval, plus `<batch>.send.json` with the exact HTML the send run sends once approved |

## Data rules

- Only business data a company publishes itself (website, official directory, press release). No scraped personal profiles, no bought lists.
- Prefer role addresses (info@, sales@) in strict markets. Named work addresses only where published by the company.
- Record the source URL of every address.
- Non-responders: delete contact rows 12 months after the last email. Keep only the suppression entry.
- Erasure request: remove the person from every file, add the address to `suppression.csv` with reason `erasure`, and if needed rewrite history (this repo exists separately so that never touches the website).

## Schema

### companies.csv
`company_id` (COUNTRY-slug), `name`, `country` (ISO-2), `city`, `website`, `segment`, `size_note`, `source`, `source_url`, `hook` (the researched reason to write), `researched_at`, `status` (new | contacted | replied | closed | excluded), `notes`

### contacts.csv
`contact_id` (company_id + n), `company_id`, `name`, `role`, `email`, `email_type` (role | named), `email_source_url`, `language`, `added_at`, `status` (active | bounced | replied | opted_out | closed)

### messages.csv
`message_id`, `contact_id`, `kind` (initial | followup | reply), `subject`, `batch_id`, `status` (draft | approved | sent | bounced | cancelled | failed), `zoho_message_id`, `sent_at`, `outcome` (none | replied_interest | replied_question | not_interested | ooo | bounced | forwarded), `notes`

### suppression.csv
`value` (address or @domain), `reason` (opted_out | not_interested | bounced_hard | erasure | excluded_market), `added_at`, `notes`
