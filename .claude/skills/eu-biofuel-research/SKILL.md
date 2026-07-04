---
name: eu-biofuel-research
description: Lead the EU biofuel regulation research team — spawn the mandates, fuel-tax, and sustainability researchers for the requested member states, run the corroboration pass, and assemble compliance reports. Use when asked to research EU/member-state biofuel mandates, fuel taxation, or sustainability requirements. Args - country names/ISO codes, "all", and/or a topic filter (mandates|tax|sustainability).
---

# EU Biofuel Regulation Research — Team Lead Playbook

You are the lead of a research team defined in this repository. Your
researchers are the subagents `biofuel-mandates-researcher`,
`fuel-tax-researcher`, `sustainability-researcher`, and `source-corroborator`
(see `.claude/agents/`). The shared ground rules live in
`research/METHODOLOGY.md`; source registries in `research/sources/`;
the report template in `research/templates/country-report.md`.

## 1. Parse the assignment

From the arguments (or the user's message), determine:
- **Countries:** explicit list, or "all" (= all 27 member states). If none
  given, ask which markets matter, or default to a sensible batch the user
  named earlier in the conversation.
- **Topics:** default is all three (mandates, taxation, sustainability); honor
  a topic filter if given.
- **Output:** one file per country at
  `research/reports/<ISO2>-country-report-<YYYY-MM-DD>.md`; for multi-country
  runs also produce `research/reports/eu-comparison-<YYYY-MM-DD>.md`.

## 2. Dispatch researchers

- Batch countries so each agent run covers **1–3 countries** (research depth
  drops beyond that). For "all 27", process in waves rather than 27 parallel
  agents; 3–4 concurrent agents is a good ceiling.
- For each batch and each in-scope topic, spawn the matching agent with a
  prompt that states: the assigned countries, the exact output file path(s) to
  write (researchers write their section into
  `research/reports/drafts/<ISO2>-<topic>-<date>.md`), a pointer to
  `research/METHODOLOGY.md`, and the reminder that current numeric values must
  come from live official sources, never memory.
- The three topic agents for the same country can run in parallel — their
  scopes don't overlap.

## 3. Corroboration pass (mandatory)

When a country's drafts are in, spawn `source-corroborator` on those draft
files. Do not skip this even for "quick" requests — uncorroborated output
violates the methodology. If the corroborator reports corrections, sanity-check
that the researchers' summaries you relay to the user reflect the corrected
values, not the originals.

## 4. Assemble

- Merge the verified drafts into the country report using
  `research/templates/country-report.md`: write the executive summary and the
  section-4 compliance checklist yourself from the verified content, keep every
  per-fact confidence label, and consolidate the source logs.
- Move/merge content out of `drafts/` so the final report is self-contained;
  delete merged draft files.
- For multi-country runs, build the comparison table (obligation type, current
  level, next step-up, headline excise rates, certification regime, one
  flag column).

## 5. Report back and persist

- Commit the reports on the designated branch and push (follow the session's
  git instructions).
- In your reply, lead with the headline findings per country and every
  `CONFLICT`/`UNCORROBORATED` flag — those are compliance risks the user must
  see. Link the report files.
- If researchers found registry errors (moved domains, renamed ministries),
  apply the fixes to `research/sources/member-states.md` in the same commit.

## Quality gate before replying

- [ ] Every key fact in the final report has a confidence label and dated sources
- [ ] Corroboration pass ran on everything included
- [ ] No numeric value originates from model memory
- [ ] Future mandates marked adopted vs `PROPOSED`
- [ ] Gaps section honestly lists what wasn't found
