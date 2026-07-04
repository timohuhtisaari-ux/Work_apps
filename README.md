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
