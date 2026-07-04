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

### Current output (as of 2026-07-04)

All **27 EU member states** have a completed, corroborated compliance report in
`research/reports/<ISO2>-country-report-2026-07-04.md`, plus a cross-country
comparison at `research/reports/eu-comparison-2026-07-04.md`. Each country report
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
