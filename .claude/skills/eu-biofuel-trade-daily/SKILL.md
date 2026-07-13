---
name: eu-biofuel-trade-daily
description: Daily tight sweep for EU anti-dumping and anti-circumvention activity on biofuels (plus closely related CVD, import registration, TARIC and expiry/interim-review initiations). Catches fast-moving trade-defence steps between the weekly full scan. Quiet on no-change; alerts and commits only on a real new/changed measure. Use for the scheduled daily run or an on-demand trade check.
---

# EU Biofuel Trade-Defence — Daily Monitor (AD & anti-circumvention)

Narrow, fast, low-noise. Goal: catch **new or changed anti-dumping (AD) and
anti-circumvention** activity on biofuels within a day, plus the tightly related
CVD / registration-of-imports / TARIC-surveillance / expiry- & interim-review
steps. This is the fast lane; the weekly `/eu-fuels-monitor` remains the broad
scan. Same rigor as the repo (`research/METHODOLOGY.md`): official sources first,
corroborate a real hit, never assert from memory.

## Products in scope
Biodiesel (FAME) and blends, **HVO / renewable diesel**, **SAF**, bioethanol,
and waste/residue feedstocks (**UCO/UCOME**, PFAD, palm/soy) — all origins.

## 1. Orient (cheap)
- Read watchlist **section G** in `research/monitoring/watchlist.md` (current
  measures + their review dates) and the tail of `research/monitoring/CHANGELOG.md`
  and any recent `research/monitoring/trade-daily/*.md`, so you know the baseline
  and don't re-flag a known item.
- The verified baseline register is
  `research/reports/eu-biofuel-trade-measures-2026-07-13.md`.

## 2. Sweep (only what moves fast)
Check for anything dated since the last daily run (default: last 1–2 days):
1. **Official Journal — C series** (notices): new **initiation** of AD /
   anti-circumvention / anti-subsidy investigations; **expiry-review** and
   **interim-review** initiation notices; notices concerning registration.
2. **Official Journal — L series** (legislation): new or amended **Implementing
   Regulations** imposing provisional/definitive duties, extending measures
   (anti-circumvention), making imports **subject to registration**, or
   correcting TARIC codes.
3. **DG TRADE trade-defence investigations database** — the "ongoing
   investigations" and "measures in force" lists; look for biofuel product codes
   and any status change.
4. **TARIC** — new/changed surveillance or duty codes for the scope products.
Prioritised watch (from section G): the **US biodiesel AD+CVD expiry review**
(measures expiring ~Aug 2026 — an initiation notice is expected), the
**Indonesia CVD** post-WTO-DS618 steps, and any **first move on SAF** (currently
monitoring-only).

## 3. Verify a hit
For any candidate change: confirm from the **OJ text itself** (the C/L notice)
and one independent source (DG TRADE page, EBB/ePURE, trade press). Capture:
product + origin, action type, regulation/notice number, key rate/date, and what
stage it is at. Label confidence. If EUR-Lex direct fetch fails, verify the
identifier via the Commission page + Tier-2 and say so.

## 4. Act on the outcome
- **No new activity (the usual case):** do **NOT** commit. End with a one-line
  report: `No new AD/anti-circumvention activity — checked OJ C/L + DG TRADE +
  TARIC for [scope], as of <date>.` (Keep the run quiet; avoid commit/notification
  noise.)
- **A real change:**
  1. Append a dated entry to the register
     `research/reports/eu-biofuel-trade-measures-2026-07-13.md` (a
     "Daily monitoring updates" note or a new/updated row) with sources + label.
  2. Update watchlist **section G** (status + last-checked) and append a
     `CHANGELOG.md` line.
  3. Write `research/monitoring/trade-daily/<YYYY-MM-DD>.md` with the detail.
  4. If it materially affects a country/regulation report, name the file to update.
  5. Commit and push (retry with backoff).
  6. Alert: lead the final message with the change (product, origin, action,
     rate/date, stage, source).

## Quality gate
- [ ] Real hits verified from the OJ text + one independent source, with a label
- [ ] No change asserted from memory
- [ ] Quiet + no commit when nothing new; commit + alert only on a real change
- [ ] Section G / CHANGELOG updated when something changed
