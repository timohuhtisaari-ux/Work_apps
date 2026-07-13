---
name: eu-fuels-monitor
description: Run the weekly EU renewable & low-carbon fuels policy scan. Sweep the tracked EU-level policy surface (RED III delegated/implementing acts, FuelEU Maritime, ReFuelEU Aviation, ETS2, the low-carbon fuels / hydrogen framework, the Union Database, certification schemes, consultations and infringement packages) for changes since the last scan, corroborate material changes, write a dated scan note, update the watchlist, and commit. Use for the scheduled weekly monitoring run or an on-demand scan.
---

# EU Renewable & Low-Carbon Fuels — Weekly Monitoring Playbook

You are the monitoring lead. Goal: detect and record **changes** in EU-level
renewable-fuels and low-carbon-fuels (LCF) policy since the last scan — new or
amended acts, advanced legislative/scrutiny steps, consultations, infringement
decisions, and status shifts of the items already on the watchlist. Same rigor
as the rest of this repo (`research/METHODOLOGY.md`): official sources first,
corroboration for material changes, honest gaps, **never assert a change from
memory**.

## 1. Orient

- Read `research/monitoring/watchlist.md` — the living register of tracked items,
  each with a **status** and a **last-checked** date. This is your checklist.
- Read the last few entries of `research/monitoring/CHANGELOG.md` and the most
  recent `research/monitoring/scans/*.md` so you know what was already reported
  (don't re-report an old change as new).
- Note today's date; the scan file is `research/monitoring/scans/<YYYY-MM-DD>.md`.

## 2. Scope — the policy surface to sweep

Renewable **and** low-carbon transport/energy fuels at EU level:

1. **RED III (Dir (EU) 2023/2413) delegated & implementing acts** — see
   `research/reports/red3-delegated-acts-register-2026-07-06.md`. Track status of:
   the RFNBO acts (2023/1184 additionality, 2023/1185 GHG methodology; the
   1 Jul 2028 additionality review), the ILUC act 2019/807 (soy/palm high-ILUC
   revision), Annex IX amendments (last: Del. Dir (EU) 2024/1405), co-processing
   2023/1640, verification/UDB Impl. Reg 2022/996 (+ amendments), the
   **cascading-principle** DA (overdue), default GHG values (Art. 31), and any
   transport-GHG-intensity / biomethane-injection accounting act.
2. **Low-Carbon Fuels / hydrogen** — the gas-package (Dir (EU) 2024/1788, Reg
   (EU) 2024/1789); the low-carbon-hydrogen methodology Del. Reg (EU) 2025/2359;
   any forthcoming low-carbon-fuels framework, LCF definitions, and the EU
   Hydrogen Bank auction rounds / results.
3. **FuelEU Maritime (Reg 2023/1805)** and **ReFuelEU Aviation (Reg 2023/2405)**
   — implementing/delegated acts, guidance, and the built-in reviews; the FuelEU
   database (THETIS-MRV) acts (e.g. 2026/394) and EASA reporting-tool updates.
4. **Carbon pricing** — EU ETS maritime/aviation phase-in; **ETS2** (road
   transport & buildings, obligation from 1 Jan 2028) implementing acts, the
   Social Climate Fund, and any change to the 2028 start.
5. **Union Database (UDB)** — the mandatory-use / sanction date (currently unset)
   and any Impl. Reg amending 2022/996.
6. **Certification** — DG ENER recognition/withdrawal of **voluntary schemes**
   (ISCC EU, REDcert-EU, 2BSvs, etc.) and the recognised-schemes list.
7. **Process signals** — Commission **consultations / calls for evidence**,
   **delegated-act scrutiny** periods (Parliament/Council objection windows),
   the monthly **infringement packages** (RED III transposition), and relevant
   **State-aid** decisions.

## 3. Method — detect and verify changes

- For each watchlist item, check its authoritative source for movement since the
  item's last-checked date. Prefer: **EUR-Lex** (new OJ publications; the RED III
  NIM page), **European Commission** DG ENER / CLIMA / MOVE / TAXUD news &
  delegated-acts pages, **EASA**, **EMSA**, **Council/Parliament** procedure
  files, and the Commission **infringement** and **consultation** registers.
- Classify each item this scan: **NEW** (act/consultation appeared), **CHANGED**
  (amended / status shifted), **ADVANCED** (moved a procedural step — adopted,
  entered scrutiny, published), or **NO CHANGE** (confirmed still as recorded).
- **Corroborate every material change** with a second independent source (Tier-1
  + Tier-2) and label confidence per the methodology. If EUR-Lex direct fetch
  fails (a known issue), verify the identifier via the Commission page + a
  reputable Tier-2 and say so.
- If a change **materially affects an existing report** (a country report, a
  regulation report, or the acts register), note exactly which file and what
  needs updating. For a big change you may spawn the relevant researcher agent
  (`biofuel-mandates-researcher` / `fuel-tax-researcher` /
  `sustainability-researcher`) then `source-corroborator`; for small ones, just
  flag it in the scan note for the next deep-dive.

## 4. Write the outputs

- **`research/monitoring/scans/<YYYY-MM-DD>.md`** — this week's scan:
  - a 2–4 line headline ("N material changes this week" or "no material changes");
  - a **Changes** section: each NEW/CHANGED/ADVANCED item with act/procedure
    reference, what changed, effective/next date, confidence, sources, and which
    repo file it affects;
  - a **No-change confirmations** list for the key watch items (cascading DA,
    2019/807 soy/palm, UDB mandatory date, Annex IX, default GHG values, ETS2
    start, FuelEU/ReFuelEU reviews) so a reader sees they were actually checked;
  - a **Gaps** note for anything unreachable this scan.
- **`research/monitoring/watchlist.md`** — update each item's status and
  last-checked date; add new tracked items discovered this scan.
- **`research/monitoring/CHANGELOG.md`** — append one dated line per change.

## 5. Persist and report

- Commit and push to the working branch (follow the session's git instructions).
- End with a concise **digest** of what changed this week (or "no material
  changes; N items checked") — this is what reaches the user as the run
  notification. Lead with anything that changes a compliance obligation or a
  date.

## Quality gate

- [ ] Every reported change has ≥1 official source + corroboration and a confidence label
- [ ] No change asserted from memory; identifiers verified live
- [ ] Key watch items explicitly marked checked (even when unchanged)
- [ ] Watchlist last-checked dates advanced; CHANGELOG appended
- [ ] Affected existing reports named for follow-up
