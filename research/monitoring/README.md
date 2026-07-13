# EU Renewable & Low-Carbon Fuels — Policy Monitoring

Weekly horizon-scan of EU-level renewable-fuels and low-carbon-fuels (LCF)
policy. Runs the `/eu-fuels-monitor` skill (playbook at
`.claude/skills/eu-fuels-monitor/SKILL.md`).

## Layout

| Path | Purpose |
|---|---|
| `watchlist.md` | Living register of tracked policy items + status + last-checked dates |
| `CHANGELOG.md` | One line per detected change, newest first |
| `scans/<YYYY-MM-DD>.md` | The weekly scan note (changes + no-change confirmations + gaps) |

## Schedule (two tiers)

1. **Weekly full scan** — `/eu-fuels-monitor`, **Mondays 07:00 UTC**. The broad
   sweep of the whole policy surface (below); commits a dated scan note and
   sends a push+email digest.
2. **Daily trade fast-lane** — `/eu-biofuel-trade-daily`, **every day 06:00 UTC**.
   A tight sweep for **anti-dumping & anti-circumvention** (plus related CVD /
   registration / TARIC / review-initiation) activity on biofuels only, so
   fast-moving trade-defence steps are caught within a day. **Low-noise:** it
   commits and pushes only when something actually changes, and otherwise stays
   quiet; output goes to `trade-daily/<date>.md` and watchlist section G. Push
   alert only (no daily email).

Both wake a fresh session. Change cadence or pause either via the Routine
controls; on-demand runs are `/eu-fuels-monitor` or `/eu-biofuel-trade-daily`
in a session on this repo.

## What it covers

RED III delegated & implementing acts (incl. the RFNBO/hydrogen acts and the
overdue cascading-principle act), the low-carbon-fuels & hydrogen framework
(gas package, Del. Reg. 2025/2359, Hydrogen Bank), FuelEU Maritime & ReFuelEU
Aviation, EU ETS maritime/aviation and ETS2, the Union Database mandatory-use
date, recognised voluntary certification schemes, and process signals
(consultations, delegated-act scrutiny, monthly infringement packages). Full
scope in the playbook's section 2.

## Principle

Same as the rest of the repo: official sources first, corroboration for material
changes, every fact date-stamped and confidence-labelled, honest gaps — nothing
asserted from memory.
