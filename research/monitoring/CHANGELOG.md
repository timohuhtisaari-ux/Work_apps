# EU Fuels Policy Monitoring — Changelog

One line per detected change, newest first. Appended by the weekly
`/eu-fuels-monitor` scan. Format: `YYYY-MM-DD — [NEW|CHANGED|ADVANCED] item — what changed (source)`.

- 2026-07-13 — [SEED] Watchlist section G (trade measures) verified & populated
  from the new register `eu-biofuel-trade-measures-2026-07-13.md`. Baseline:
  China biodiesel AD 10.0–35.6% (Reg 2025/261) in force; Indonesia biodiesel CVD
  8–18% (Reg 2019/2092) under expiry review + WTO DS618; US biodiesel AD+CVD
  (2021/1266-1267) expiring ~Aug 2026; US bioethanol AD lapsed (2019/765);
  **SAF-China = no duty, TARIC monitoring only (Reg 2025/1866)** — corrects the
  "under surveillance" premise.
- 2026-07-13 — [SEED] Watchlist established from the repo's reports (30 country
  reports, FuelEU/ReFuelEU regulation reports, RED III delegated-acts register,
  UDB status note). No change events yet — this is the baseline.## 2026-07-16 — Global expansion batch 2 (world map: 45 → 53 markets)

- **New markets researched, corroborated and mapped** (drafts
  `research/reports/drafts/*-headline-2026-07-16.md`, verification in
  `batch2-corroboration-2026-07-16.md` — 17 CONFIRMED, 6 PRIMARY-ONLY, 1 CONFLICT):
  - **India** — E20 operative (achieved 2025) + legislated SAF path (1% 2027 → 5% 2030),
    CBG blending 1% → 5%, excise exemption for E20–E30. The regulatory frontrunner.
  - **China** — **no national blend mandate** (2017 nationwide-E10 target abandoned Jan 2020);
    provincial E10 in ~15 provinces, no expansion since 2019; SAF 1% pilot at 4 airports vs
    2% announced (policy–implementation gap flagged); biodiesel export-focused.
  - **Japan** — ETBE route: 824 ML/yr bioethanol obligation to Mar 2028; SAF supplier
    obligation legislated Sep 2024 (10% by 2030); E10 pilot FY2028 PROPOSED.
  - **Australia** — no federal mandate; NSW 6% ethanol / 2% biodiesel, QLD 4% / 0.5%
    (increase to 9%/2% PROPOSED, Bill 2026); federal low-carbon-fuels support in build-out.
  - **Mexico** — **no mandate**; Supreme Court blocked the E10 expansion — corroboration
    **corrected the ruling date to 22 Jan 2020** (draft said 2025).
  - **Uruguay** — E8.5 operative (Ley 19.996); **B5 biodiesel repealed 2021** (B0 since 2022).
  - **Bolivia** — E12 operative; E21 (2026) / E25 (2027–28) legislated (dates granular-TBD).
  - **Ecuador** — Ecopaís E10 nominal but **only 2–4% actual** (capacity bottleneck).
- Batch 3 promoted to QUEUED for the weekly Routine: Central America, Türkiye,
  South Africa, Kenya, Nigeria, Zimbabwe/Zambia, UAE/Saudi (SAF), Taiwan, New Zealand,
  Pakistan, Bangladesh.

## 2026-07-15 — Global expansion batch 1 (world map: 32 → 45 markets)

- **New markets researched, corroborated and mapped** (Haiku researcher agents +
  independent corroboration pass; drafts in `research/reports/drafts/*-headline-2026-07-15.md`,
  verification in `batch1-corroboration-2026-07-15.md` — 24 CONFIRMED, 13 PRIMARY-ONLY, 1 CONFLICT):
  - **South America:** Brazil (E32 temporary + B15 + RenovaBio 10.1% CBIO offset; hybrid),
    Argentina (E12/B7.5 static), Paraguay (E30 — world's highest ethanol minimum, B8–B10),
    Colombia (E10/B13), Peru (E7.8/B5), Chile (**no mandate** — new map class).
  - **Asia:** Indonesia (**B50 from 1 Jul 2026** + regional E5), Malaysia (B15 transport from
    1 Jun 2026), Philippines (E10 + B3; **B4/B5 suspended** since Jul 2025 — CONFLICT open),
    Thailand (E20/B7 + 1% SAF from 2026), Vietnam (**E10 from 1 Jun 2026**),
    Singapore (1% SAF — **corroboration corrected the uplift date to 1 Jan 2027**,
    levy collection from 1 Oct 2026), South Korea (B4 → B5 by 2030).
- **Master map** now merges the world layer with the North-America admin-1 drill-down
  (`world-biofuel-map.html`); new region zooms S. America and SE Asia; new obligation
  class "No mandate / voluntary".
- **Team infrastructure:** `global-fuels-researcher` agent (Haiku),
  `/global-fuels-research` team-lead skill, expansion queue
  (`research/monitoring/global-queue.md`), weekly Routine (Wed 06:00 UTC, fresh
  session, push+email digest) that change-scans mapped markets and advances the queue
  (next: IN, CN, JP, AU, UY, BO, EC).

