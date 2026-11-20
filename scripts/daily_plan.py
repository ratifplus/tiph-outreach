#!/usr/bin/env python3
"""Daily regional send plan for first emails (Ratif, 20 Nov 2026).

Each UTC date, the first-email daily cap D is split evenly across the three
regions (APAC, Europe, Americas) and the plan picks which approved first
emails go out that day, oldest batch first within each region. Each planned
email is only sent when its own recipient is in office hours (the send task
still checks that and every other rule before sending).

Balance without waste: a region only gets as many slots as it has emails that
can actually go out today. Slots it cannot use go to the other regions. The
script is re-run on every send run: it keeps what was planned, drops rows that
became ineligible (opt-out, bounce, cancelled, company already emailed today),
releases the unsent slots of a region whose office hours for the UTC date are
over, and refills free slots with the same even split.

Usage: python3 scripts/daily_plan.py --cap D [--date YYYY-MM-DD] [--now 2026-11-23T00:45Z] [--dry-run]
Writes plans/<date>.json and prints a one-line summary.
"""
import argparse, csv, glob, json, os, re, sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGIONS = ["APAC", "Europe", "Americas"]
PER_MARKET_DAILY = {"CH": 5, "SG": 19}  # CH max 5/day; SG under 20/day (first emails + follow-ups)


def region_of(tz):
    if tz.startswith("America/"):
        return "Americas"
    if tz.startswith("Europe/"):
        return "Europe"
    return "APAC"


def read_csv(name):
    raw = open(os.path.join(ROOT, "data", name), "rb").read()
    try:
        txt = raw.decode("utf-8")
    except UnicodeDecodeError:
        txt = raw.decode("cp1252", errors="replace")  # some rows were saved in a legacy encoding
    return list(csv.DictReader(txt.splitlines()))


def live_markets():
    txt = open(os.path.join(ROOT, "config", "status.md"), encoding="utf-8").read()
    m = re.search(r"^- Live markets[^:]*:\s*([^(\r\n]*)", txt, re.M)
    codes = set(re.findall(r"\b[A-Z]{2}\b", m.group(1))) if m else set()
    if "UK" in codes:
        codes.add("GB")
    return codes


def can_send_before(tz, start, end):
    """True if some moment in [start, end) is Mon-Fri 08:30-16:30 local in tz."""
    z = ZoneInfo(tz)
    t = start
    first = True
    while t < end:
        lt = t.astimezone(z)
        mins = lt.hour * 60 + lt.minute
        if lt.weekday() < 5 and 510 <= mins < 990:
            return True
        if first:
            t = t.replace(minute=(t.minute // 15) * 15, second=0, microsecond=0) + timedelta(minutes=15)
            first = False
        else:
            t += timedelta(minutes=15)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cap", type=int, required=True, help="first-email daily cap D in force on the date")
    ap.add_argument("--date", help="UTC date, default today")
    ap.add_argument("--now", help="UTC time, default now (for tests)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    now = datetime.now(timezone.utc) if not a.now else datetime.strptime(a.now, "%Y-%m-%dT%H:%MZ").replace(tzinfo=timezone.utc)
    date = a.date or now.strftime("%Y-%m-%d")
    day_start = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    day_end = day_start + timedelta(days=1)
    start = max(now, day_start)
    D = a.cap

    messages = read_csv("messages.csv")
    contacts = {c["contact_id"]: c for c in read_csv("contacts.csv")}
    companies = {c["company_id"]: c for c in read_csv("companies.csv")}
    supp = {r["value"].strip().lower() for r in read_csv("suppression.csv") if r.get("value")}
    live = live_markets()

    send = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "batches", "*.send.json"))):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for e in d.get("emails", []):
            send[e["message_id"]] = e

    def info(m):
        c = contacts.get(m["contact_id"], {})
        e = send.get(m["message_id"], {})
        to = (e.get("to") or c.get("email") or "").strip().lower()
        comp = c.get("company_id", "")
        country = companies.get(comp, {}).get("country", "")
        tz = e.get("recipient_tz", "")
        return c, e, to, comp, country, tz

    sent_today = {r: 0 for r in REGIONS}
    companies_today = set()
    market_today = {}
    sent_addresses = set()
    for m in messages:
        c, e, to, comp, country, tz = info(m)
        if m["status"] in ("sent", "bounced") and m.get("sent_at"):
            sent_addresses.add(to)
            if m["sent_at"].startswith(date):
                companies_today.add(comp)
                market_today[country] = market_today.get(country, 0) + 1
                if m["kind"] == "initial" and tz:
                    sent_today[region_of(tz)] += 1

    def eligible(m):
        if m["kind"] != "initial" or m["status"] != "approved":
            return None
        c, e, to, comp, country, tz = info(m)
        if not e or not tz or not to:
            return None
        if c.get("status") != "active" or country not in live:
            return None
        if to in supp or to.split("@")[-1] in supp:
            return None
        if to in sent_addresses or comp in companies_today:
            return None
        if not can_send_before(tz, start, day_end):
            return None
        return {"message_id": m["message_id"], "region": region_of(tz), "batch_id": m["batch_id"],
                "send_order": int(e.get("send_order") or 0), "recipient_tz": tz, "company_id": comp,
                "country": country, "to": to}

    by_id = {m["message_id"]: m for m in messages}
    path = os.path.join(ROOT, "plans", f"{date}.json")
    old = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {"planned": []}

    pool = {r: [] for r in REGIONS}
    for m in messages:
        x = eligible(m)
        if x:
            pool[x["region"]].append(x)
    for r in REGIONS:
        pool[r].sort(key=lambda x: (x["batch_id"], x["send_order"]))

    # capacity per region = already sent today + what can still go out today
    alloc = dict(sent_today)
    cap = {r: sent_today[r] + len(pool[r]) for r in REGIONS}
    remaining = D - sum(sent_today.values())
    oldest = {r: (pool[r][0]["batch_id"] if pool[r] else "~") for r in REGIONS}
    while remaining > 0:
        open_r = [r for r in REGIONS if alloc[r] < cap[r]]
        if not open_r:
            break
        r = min(open_r, key=lambda r: (alloc[r], oldest[r]))
        alloc[r] += 1
        remaining -= 1

    kept_ids = [p["message_id"] for p in old.get("planned", [])]
    planned, used_companies, market_plan = [], set(), dict(market_today)
    for r in REGIONS:
        need = alloc[r] - sent_today[r]
        cand = [x for x in pool[r] if x["message_id"] in kept_ids] + [x for x in pool[r] if x["message_id"] not in kept_ids]
        for x in cand:
            if need <= 0:
                break
            if x["company_id"] in used_companies:
                continue
            lim = PER_MARKET_DAILY.get(x["country"])
            if lim is not None and market_plan.get(x["country"], 0) >= lim:
                continue
            used_companies.add(x["company_id"])
            market_plan[x["country"]] = market_plan.get(x["country"], 0) + 1
            planned.append(x)
            need -= 1

    out = {
        "date": date, "cap": D, "updated_at": now.strftime("%Y-%m-%dT%H:%MZ"),
        "rule": "Even split of the first-email cap across APAC, Europe, Americas; unusable slots go to the other regions; each email sent only in its recipient's office hours (config/status.md, Daily regional plan).",
        "sent_today": sent_today, "allocation": alloc,
        "unfilled": D - sum(alloc.values()),
        "planned": sorted(planned, key=lambda x: (x["batch_id"], x["send_order"])),
    }
    summary = (f"{date} cap {D}: allocation " + ", ".join(f"{r} {alloc[r]} (sent {sent_today[r]}, planned {sum(1 for p in planned if p['region']==r)})" for r in REGIONS)
               + f"; unfilled {out['unfilled']}")
    if not a.dry_run:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        old_cmp = {k: v for k, v in old.items() if k != "updated_at"}
        new_cmp = {k: v for k, v in out.items() if k != "updated_at"}
        if old_cmp != new_cmp:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                json.dump(out, f, indent=1)
                f.write("\n")
    print(summary)


if __name__ == "__main__":
    main()
