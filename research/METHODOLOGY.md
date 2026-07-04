# Research Methodology — EU Biofuel Regulation Team

This document governs how every agent on the team gathers, validates, and reports
regulatory information. All agents must follow it. The orchestrating skill
(`/eu-biofuel-research`) injects a pointer to this file into every agent prompt.

## Scope

For each EU member state (and the EU level itself), the team researches:

1. **Biofuel mandates** — current blending / GHG-reduction / energy-share
   obligations in transport fuels, the national scheme that implements them
   (quota, certificate, or tax-incentive based), sub-targets (advanced biofuels
   Annex IX-A, RFNBOs, caps on crop-based and Annex IX-B feedstocks),
   double-counting rules, penalties/buy-out prices, and **announced future
   trajectories** (legislated step-ups and pending bills, incl. RED III
   transposition status).
2. **Fuel taxation** — excise duty rates on petrol, diesel, and biofuel blends;
   reduced rates or exemptions for biofuels/HVO/biogas; CO2 components; energy
   taxation acts implementing the Energy Taxation Directive (2003/96/EC); and
   announced rate changes.
3. **Sustainability requirements** — national transposition of RED II/III
   sustainability and GHG-saving criteria, accepted certification schemes
   (ISCC EU, REDcert-EU, 2BSvs, etc.), national registries (e.g. Nabisy,
   HBE register, elNa), Union Database (UDB) onboarding status, feedstock
   restrictions (palm/soy phase-outs, high-ILUC rules), and verification/audit
   obligations on economic operators.

## Source hierarchy

**Tier 1 — Primary (mandatory basis for every claim):**
- Official legal gazettes and consolidated law databases
  (EUR-Lex, Légifrance, gesetze-im-internet.de, BOE, wetten.overheid.nl, …).
- Ministries, tax/customs authorities, and regulators/scheme administrators
  listed in `research/sources/member-states.md`.
- Official EU institutions: European Commission (DG ENER, DG TAXUD, DG CLIMA),
  Council, Parliament.

**Tier 2 — Secondary (mandatory corroboration, never the sole basis):**
- Intergovernmental and agency reports: IEA, EEA, USDA FAS GAIN country reports.
- Industry and NGO trackers: ePURE, EBB, Transport & Environment, ICCT,
  certification-scheme guidance (ISCC country updates).
- Reputable trade press and law-firm client briefings.

**Rule:** every regulatory fact must cite at least one Tier 1 source. Every
*key* fact (a mandate level, a tax rate, an effective date) must additionally be
corroborated by at least one independent Tier 2 source **or** a second Tier 1
source. Facts that cannot be corroborated are reported with confidence
`UNCORROBORATED` and flagged for follow-up — never silently dropped or
presented as settled.

## Working rules

- **Never trust training data for current values.** Mandate percentages, tax
  rates, and dates change yearly (sometimes mid-year). Always fetch the value
  from a live source and record the "as of" date. The source registry in this
  repo lists *institutions and schemes*, deliberately not numeric values.
- **Prefer the legal text over the press release.** When a ministry news page
  and the gazette disagree, the gazette wins; note the discrepancy.
- **Language:** primary sources are often only in the national language. Fetch
  them anyway and translate; do not substitute an English-language secondary
  source as the primary citation.
- **Date-stamp everything.** Each fact carries: value, legal basis (act +
  article where possible), effective date, "checked on" date, and source URLs.
- **Distinguish in force / adopted-not-yet-in-force / proposed.** Future
  mandates are only "legislated" if the amending act is adopted; otherwise mark
  them `PROPOSED` with the bill reference.
- **Record misses.** If an official source is unreachable or a fact cannot be
  located, log it in the report's "Gaps" section with what was tried.

## Confidence labels

| Label | Meaning |
|---|---|
| `CONFIRMED` | Tier 1 source + independent corroboration agree |
| `PRIMARY-ONLY` | Tier 1 source found, no corroboration yet |
| `UNCORROBORATED` | Only secondary sources found; primary not located |
| `CONFLICT` | Sources disagree — report both with citations |
| `PROPOSED` | Not yet adopted law; cite the proposal |

## Team roles

| Role | Definition | Responsibility |
|---|---|---|
| Lead (orchestrator) | `/eu-biofuel-research` skill, run in the main session | Splits work, spawns researchers, merges output, owns the final report |
| Mandates researcher | `.claude/agents/biofuel-mandates-researcher.md` | Scope item 1 |
| Fuel-tax researcher | `.claude/agents/fuel-tax-researcher.md` | Scope item 2 |
| Sustainability researcher | `.claude/agents/sustainability-researcher.md` | Scope item 3 |
| Corroborator | `.claude/agents/source-corroborator.md` | Independently re-verifies key facts, assigns final confidence labels |

Researchers draft; the corroborator verifies; the lead assembles. The
corroborator must not reuse the researcher's secondary sources — it looks for
*independent* confirmation.

## Output

Reports go to `research/reports/<ISO2>-<topic>-<YYYY-MM-DD>.md` (or
`<ISO2>-country-report-<date>.md` for full-country reports) using the template
in `research/templates/country-report.md`. Cross-country comparisons go to
`research/reports/eu-comparison-<date>.md`.
