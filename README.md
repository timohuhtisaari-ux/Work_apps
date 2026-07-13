# Work_apps

## EU Biofuel Regulation Research Team

A Claude Code agent team that researches, for EU member states:

- **current and future biofuel mandates** (blending / GHG-reduction obligations),
- **fuel taxation** (excise duties, CO2 components, biofuel reliefs),
- **sustainability requirements** (RED II/III criteria, certification, registries, UDB).

Official government and EU sources are the mandatory primary basis for every
claim; secondary sources (USDA GAIN, ePURE/EBB, ICCT, ISCC, …) corroborate.
Every fact is date-stamped and carries a confidence label.

### How to run it

In a Claude Code session in this repo:

```
/eu-biofuel-research Germany, Sweden, Netherlands
/eu-biofuel-research all
/eu-biofuel-research Finland tax
```

The skill acts as team lead: it dispatches the researcher agents in parallel,
runs a mandatory independent corroboration pass, and assembles per-country
compliance reports into `research/reports/`.

### Ongoing weekly monitoring

Beyond the point-in-time reports, the repo runs a **weekly EU renewable &
low-carbon fuels policy scan** (`/eu-fuels-monitor`, playbook at
`.claude/skills/eu-fuels-monitor/SKILL.md`). It sweeps the tracked policy surface
— RED III delegated/implementing acts (incl. the RFNBO/hydrogen acts), the
low-carbon-fuels & hydrogen framework, FuelEU Maritime, ReFuelEU Aviation, EU ETS
maritime/aviation and ETS2, the Union Database, certification schemes, and
process signals (consultations, delegated-act scrutiny, infringement packages) —
records changes in `research/monitoring/` (`watchlist.md`, `CHANGELOG.md`,
dated `scans/`), and sends a digest. A scheduled Routine wakes a fresh session
each week to run it; see `research/monitoring/README.md`.

### Current output (as of 2026-07-04)

All **27 EU member states plus Norway, the United Kingdom and Switzerland**
(30 markets) have a completed, corroborated compliance report in
`research/reports/<ISO2>-country-report-2026-07-04.md`, plus a cross-country
comparison at `research/reports/eu-comparison-2026-07-04.md` (the three non-EU
markets are in that file's appendix). The non-EU regimes are described on their
own terms — Norway's *omsetningskrav* (EEA), the UK's post-Brexit RTFO + SAF
Mandate, and Switzerland's CO2-compensation obligation — without imposing EU
RED III or ETS2 obligations. Their registry scaffolding is in
`research/sources/non-eu-states.md`.

Two **EU sectoral regulations** are also covered, as directly-applicable
instruments rather than country reports (template:
`research/templates/regulation-report.md`):

- `research/reports/fueleu-maritime-2026-07-05.md` — **FuelEU Maritime**
  (Regulation (EU) 2023/1805): the well-to-wake GHG-intensity limit on ships
  >5000 GT (−2 % in 2025 → −80 % by 2050), the RFNBO sub-quota, on-shore-power
  rule, the EUR 2400/t FuelEU penalty, and the maritime EU ETS phase-in.
- `research/reports/refueleu-aviation-2026-07-05.md` — **ReFuelEU Aviation**
  (Regulation (EU) 2023/2405): the SAF supply share (2 % in 2025 → 70 % by
  2050), the e-SAF sub-quota, the ≥90 % anti-tankering rule, and the Union
  Database / EASA reporting regime.
- `research/reports/cross-border-reporting-allocation-2026-07-05.md` — companion
  deep-dive on **how the reporting/enforcement obligation is allocated across
  Member States** for multi-country operators: FuelEU's one-administering-State-
  per-company rule vs ReFuelEU's administering-MS-per-aircraft-operator and
  single-competent-authority-per-supplier (principal place of business) model,
  with worked examples. The two regulation reports carry a summary of this in
  their section 6a.
- `research/reports/udb-status-interim-reporting-2026-07-05.md` — current-state
  note (July 2026): the **Union Database is operational (15 Jan 2024) but not yet
  mandatory/sanctioned**, so aviation-fuel volumes are reported today via EASA's
  Sustainability Portal (aircraft operators) and the UDB on a transitional
  footing (suppliers), while FuelEU Maritime reports via **EMSA THETIS-MRV**,
  independent of the UDB. Reflected in the ReFuelEU report's section 6.6.
- `research/reports/red3-delegated-acts-register-2026-07-06.md` — register of the
  **RED III delegated & implementing acts** with each act's current status, deep
  focus on the **hydrogen / RFNBO** acts: Del. Reg. (EU) 2023/1184 (additionality
  / temporal-geographic correlation) and 2023/1185 (RFNBO/RCF GHG methodology,
  70 % threshold), both in force with the additionality review due by 1 Jul 2028;
  plus the ILUC act 2019/807 (in force, under revision — a Jan-2026 Commission
  report now adds soy to palm as high-ILUC), the co-processing act 2023/1640,
  verification/UDB Impl. Reg. 2022/996 (+ 2024/805, 2025/196), the Annex IX
  amendment (Del. Directive (EU) 2024/1405), the separate low-carbon-hydrogen act
  (Del. Reg. (EU) 2025/2359, under the gas-package Directive 2024/1788), and an
  overdue/pending watch-list (the cascading-principle act is overdue). Each country report
covers the biofuel mandate (2026 level + legislated trajectory to 2030),
fuel taxation, and RED II/III sustainability/certification obligations, with a
supplier compliance checklist and a conflicts/gaps section. Every fact carries a
confidence label (`CONFIRMED` / `PRIMARY-ONLY` / `UNCORROBORATED` / `CONFLICT` /
`PROPOSED`) and dated sources; unresolved gaps are listed honestly rather than
filled from memory.

Selected headline findings: obligation designs split across GHG-reduction (e.g.
DE 12 %, SE 10 %, NL sector-based), energy-share (e.g. IE 32 %, FI 19.5 %),
volume-blending, and tax-incentive (FR TIRUERT → IRICC 2027) systems; RED III
transposition is uneven, with PT/EL/MT referred to the CJEU and CY carrying the
most-advanced RED III infringement; and EU ETS2 for road-transport fuels applies
from 1 Jan 2028 (Directive (EU) 2023/959) across all markets.

### Layout

| Path | Purpose |
|---|---|
| `.claude/skills/eu-biofuel-research/` | Team-lead playbook (the `/eu-biofuel-research` command) |
| `.claude/agents/biofuel-mandates-researcher.md` | Mandates & future trajectories researcher |
| `.claude/agents/fuel-tax-researcher.md` | Excise & biofuel tax-relief researcher |
| `.claude/agents/sustainability-researcher.md` | RED sustainability / certification researcher |
| `.claude/agents/source-corroborator.md` | Independent fact-verification pass |
| `research/METHODOLOGY.md` | Source hierarchy, corroboration rules, confidence labels |
| `research/sources/eu-level.md` | EU directives, regulations, and institutional sources |
| `research/sources/member-states.md` | Per-country registry: schemes, authorities, legal databases |
| `research/templates/country-report.md` | Standard compliance report format |
| `research/reports/` | Finished reports (drafts under `reports/drafts/`) |

### Design notes

- The source registry stores **institutions and scheme names, not numbers** —
  mandate levels and tax rates change too often to cache, so agents are
  required to fetch current values live and date-stamp them.
- Corroboration is a separate agent so verification is independent of the
  original research: the corroborator must find sources the researcher didn't
  use, and prefers disproving to rubber-stamping.
