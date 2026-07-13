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

## Schedule

A weekly scheduled run (Routine/trigger) wakes a fresh session, runs the scan,
commits the results, and sends a digest notification. Cadence: **Mondays 07:00
UTC**. Change the cadence or pause it via the Routine controls; an on-demand scan
is just `/eu-fuels-monitor` in a session on this repo.

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
