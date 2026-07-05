# FuelEU Maritime — Compliance Report (Sections 5–6 + §7 checklist draft)

- **Instrument:** FuelEU Maritime — Regulation (EU) 2023/1805 of 13 September 2023 on the use of renewable and low-carbon fuels in maritime transport, and amending Directive 2009/16/EC
- **Legal form:** directly applicable EU Regulation (no national transposition; Member States designate an *administering authority* and *competent authorities* only)
- **Report date:** 2026-07-05
- **Researched by:** fuel-eligibility + MRV/verification/compliance researcher (this agent)
- **Corroboration pass:** pending (drafted with per-fact confidence labels; corroborator to re-verify Tier-2 items independently)
- **Scope of this draft:** Section 5 (fuel eligibility & sustainability) and Section 6 (MRV / verification / compliance) only. Trajectory numbers, pooling/banking mechanics, and ETS interaction are cross-referenced but owned by other slices.

---

## 5. Fuel eligibility & sustainability criteria

### 5.1 Metric and boundary — well-to-wake

FuelEU Maritime does **not** set a fuel-blending mandate; it caps the **yearly average GHG intensity of the energy used on board** a ship, expressed in **gCO2eq/MJ**, on a **well-to-wake (WtW)** basis — i.e. Well-to-Tank (WtT, upstream/production) **plus** Tank-to-Wake (TtW, on-board combustion, including CO2, CH4 and N2O). The calculation methodology is set out in **Annex I**, and the emission factors / default values in **Annex II**.

| Item | Value / rule | Legal basis | Confidence | Sources |
|---|---|---|---|---|
| Boundary | Well-to-wake (WtT + TtW), covering CO2, CH4, N2O | Art. 4(1)–(3); Annex I | CONFIRMED | EUR-Lex 32023R1805; DG MOVE Q&A |
| Metric | Yearly average GHG intensity of energy used on board, gCO2eq/MJ | Art. 4(1) | CONFIRMED | EUR-Lex; DG MOVE Q&A |
| Baseline / reference | 91.16 gCO2eq/MJ (2020 fleet average), reduced −2% (2025) → −80% (2050) | Art. 4(2) | CONFIRMED (cross-ref: trajectory slice) | EUR-Lex; EUR-Lex LSU summary |

### 5.2 Which fuels count, and how GHG value is demonstrated

FuelEU is **fuel-agnostic and technology-neutral**: any energy carrier used on board counts (fossil residual/distillate fuels, LNG, LPG, methanol, ammonia, hydrogen, biofuels, biogas, RFNBOs, renewable/low-carbon fuels, plus OPS/on-board renewable electricity). What differs is the **emission factor** applied:

- **Fossil fuels** — must use the **default WtT and TtW factors in Annex II**; companies may **not** substitute more favourable actual values for the CO2 factors (Art. 10(4)–(5)). `CONFIRMED` (EUR-Lex Art. 10; DG MOVE Q&A 10.x).
- **Biofuels, biogas and RFNBOs** — may be counted with their **actual certified WtT value** only if the fuel meets the **RED II/III sustainability and GHG-saving criteria** (Directive (EU) 2018/2001) and is certified through a **voluntary scheme recognised under RED** using **mass-balance** chain of custody. If a compliant certificate is not provided, the fuel is treated as its fossil equivalent (Annex II default). `CONFIRMED` (EUR-Lex Art. 10(1)–(3); DG MOVE Q&A; ICCT).
- **Chain of custody** — the FuelEU value is demonstrated via **RED "proof of sustainability"** documentation carried through a recognised voluntary scheme (e.g. ISCC EU, REDcert-EU). The Commission Q&A confirms **mass balance** is the accepted principle and that **"book & claim" is not supported** (double-counting risk). `CONFIRMED` (DG MOVE Q&A 10.1; Tier-2 Zero Carbon Shipping explainer).

### 5.3 Food- and feed-crop biofuels — the "fossil default" rule (VERIFIED)

**Verified true.** Fuels produced from **food and feed crops are assigned the same emission factor as the least favourable fossil-fuel pathway** — i.e. they receive no GHG credit and cannot help a ship meet its target. Recital 28 states these fuels "be considered to have the same emission factors as the least favourable [fossil] pathway"; operationalised in Art. 10 / Annex I. Effect: crop-based biofuels are **de facto excluded** from rewarding compliance. `CONFIRMED` (Tier 1: EUR-Lex Recital 28 + Art. 10; Tier 2: ICCT "Fit for 55" fuels paper; Sustainable-Ships FuelEU explainer).

### 5.4 RFNBOs, RCFs and LNG methane slip

| Item | Rule | Legal basis | Confidence | Sources |
|---|---|---|---|---|
| RFNBO reward multiplier | Energy from RFNBOs may be counted **×2** for the period **1 Jan 2025 – 31 Dec 2033** | Art. 5(1) | CONFIRMED | EUR-Lex Art. 5; ICCT; carboneer |
| RFNBO sub-target (safeguard) | If RFNBO share in 2031 report < 1%, a **2% RFNBO sub-target** applies from **1 Jan 2034** | Art. 5(3)–(5) | PRIMARY-ONLY (cross-ref: mandate slice) | EUR-Lex Art. 5; DG MOVE Q&A 5.2 |
| RFNBO GHG threshold | Must meet RED RFNBO rules (≥70% GHG saving vs 94 gCO2eq/MJ comparator) to earn value | Art. 10; RED II Art. 25/Del. Reg. 2023/1185 | CONFIRMED | EUR-Lex; ICCT |
| RCFs (recycled carbon fuels) | Eligible where they meet RED criteria; counted per Annex II / actual values | Art. 3(4), Art. 10 | PRIMARY-ONLY | EUR-Lex; DG MOVE Q&A |
| LNG methane slip (Cslip) | **Default Cslip factors in Annex II by engine type** (e.g. slow-speed LNG-Otto ≈ 1.7%); actual TtW non-CO2 (CH4 slip) values allowed only if certified by lab testing / direct measurement per the Commission methane-slip guideline | Art. 10(5)–(6); Annex II | CONFIRMED | EUR-Lex Art. 10; DG MOVE methane-slip guideline (2025); DNV |

**Actual vs default values (rule of thumb):** default (Annex II) is the fallback for every pathway; **actual values are permitted for WtT of certified renewable fuels** and for **TtW non-CO2 emissions** (incl. LNG methane slip) where certified to a recognised international standard — but **never** to improve the CO2 factors of fossil fuels (Art. 10(4)–(6)). `CONFIRMED`.

---

## 6. Monitoring, reporting, verification & compliance (MRV)

### 6.1 Reporting period and monitoring plan

- **Reporting period = calendar year.** First reporting period is **2025** (data 1 Jan – 31 Dec 2025). The following year is the **verification period**. `CONFIRMED` (EUR-Lex Art. 2/4; LR timetable; DG MOVE).
- **Monitoring plan (Art. 8):** companies submit a **FuelEU monitoring plan per ship to an accredited verifier by 31 August 2024**; for ships entering scope later, **within 2 months of their first EU/EEA port call**. Plan describes the method for monitoring/reporting the amount, type and emission factor of energy used. Modifications require re-assessment. `CONFIRMED` (EUR-Lex Art. 8; DG MOVE; LR).

### 6.2 Reporting, verification and the FuelEU Document of Compliance — annual cycle

| Step | Deadline | Actor | Legal basis | Confidence | Sources |
|---|---|---|---|---|---|
| Submit **FuelEU report** for prior calendar year to verifier | **31 January** of the verification period (first: 31 Jan 2026) | Company | Art. 15 | CONFIRMED | EUR-Lex Art. 15; LR; DG MOVE |
| Verifier assesses report, calculates GHG intensity & **compliance balance**, records the verified report in the **FuelEU database** | **by 31 March** of the verification period | Accredited verifier | Art. 16 / 17 | CONFIRMED | LR timetable; DG MOVE; EMSA THETIS-MRV |
| Company records **flexibility choices** (banking / borrowing / pooling) | ~**30 April** (cross-ref: flexibility slice) | Company | Art. 20–21 | PRIMARY-ONLY | LR timetable; EUR-Lex |
| **FuelEU penalty** paid (if compliance deficit / non-compliant port call) | **before 30 June** of the verification period | Company → administering State | Art. 23 | CONFIRMED | EUR-Lex Art. 23; LR; DG MOVE Q&A 23.1 |
| **FuelEU Document of Compliance (DoC)** issued | **by 30 June** of the verification period | Verifier | Art. 24 | CONFIRMED | EUR-Lex Art. 24; LR; EMSA |
| DoC validity | valid for **18 months after the end of the reporting period** (or until a new DoC is issued) | — | Art. 24 | CONFIRMED | EUR-Lex Art. 24; LR |

**DoC issuance condition (Art. 24):** the verifier issues the DoC only if the ship has **no compliance deficit** and **no non-compliant port call** (or these have been settled via penalty/flexibility). A ship must carry a **valid DoC** to call at EU/EEA ports; port-State control checks it. `CONFIRMED` (EUR-Lex Art. 24; EMSA/DG MOVE). Note a minor cross-source nuance: some trade guidance describes the DoC as "valid until 30 June of the following year" — this is consistent with the legal "18 months after end of reporting period" once account is taken of the issuance date. `CONFIRMED`.

### 6.3 Accredited verifiers

- Verifiers are **independent, accredited legal entities**, accredited by **national accreditation bodies** under **Regulation (EC) No 765/2008**. `CONFIRMED` (EUR-Lex Art. 11; Del. Reg. 2025/192).
- **Commission Delegated Regulation (EU) 2025/192 of 9 September 2024** lays down the **procedures for accreditation of verifiers** under FuelEU. Scope of accreditation covers: assessment of monitoring plans; verification of (partial) FuelEU reports; verification of GHG-intensity conformity, compliance balance and non-compliant port calls; and **issuance of the FuelEU Document of Compliance**. Assessment references **ISO/IEC 17029:2019** and **ISO 14065:2021**. `CONFIRMED` (Tier 1: EUR-Lex 32025R0192; corroborated COFRAC accreditation register). Entered into force 20 days after OJ publication.

### 6.4 FuelEU database (EMSA / THETIS-MRV)

- **Art. 16** obliges the Commission to develop, operate and update an electronic **FuelEU database** recording verification activities, ship compliance balances (incl. use of flexibility mechanisms), application of exceptions, FuelEU-penalty payments, and DoC issuance. `CONFIRMED` (EUR-Lex Art. 16).
- Operationally the database is delivered through **EMSA's THETIS-MRV** platform (shared gateway with EU MRV/EU ETS maritime). EMSA deployed the FuelEU building block on **1 August 2024**; within weeks ~10,000 ships (>80% of those in scope) had FuelEU status assigned and monitoring plans created. Companies **associate each ship with a FuelEU-accredited verifier** and **submit monitoring plans** in THETIS-MRV; verifiers record verified reports there. `CONFIRMED` (Tier 1: EMSA news item + THETIS-MRV pages; corroborated DNV). *Onboarding obligation for operators in this market: register the company/fleet in THETIS-MRV, link an accredited FuelEU verifier, and submit/maintain the per-ship monitoring plan there.*

### 6.5 Administering authority ("administering State") and penalty collection

- Each company is allocated to **one administering State** — the Member State responsible for supervising/enforcing FuelEU for that company. Assignment uses **Art. 3(40) of FuelEU** referencing **Article 3gf(1) of the EU ETS Directive (2003/87/EC)**: broadly, the Member State of registration for EU-registered companies, and for non-EU companies the Member State where the company had the greatest number of port calls in the preceding monitoring years. The Commission publishes the list of administering authorities. `CONFIRMED` (EUR-Lex Art. 3(40); DG MOVE Q&A 23.1).
- **Penalty formula (Art. 23 / Annex IV):**
  - *GHG-intensity deficit:* compliance deficit converted to non-compliant energy and multiplied by **EUR 2,400 per tonne of VLSFO energy equivalent** (≈ EUR 0.058/MJ). `CONFIRMED` (EUR-Lex Annex IV; carboneer; bettersea).
  - *Non-compliant OPS/port call:* **EUR 1.5 per kWh** of the ship's total electrical power demand at berth × hours in non-compliance. `CONFIRMED` (EUR-Lex Art. 23(5); DG MOVE Q&A 23.1).
  - *Escalation:* penalty **increases by 10% for each consecutive reporting period** with a deficit (i.e. ×1.1, ×1.2, …). `CONFIRMED` (EUR-Lex Art. 23(3); carboneer).
- **Collection:** the **administering State ensures payment** of the FuelEU penalty (due before 30 June). Penalty revenue is ring-fenced by Member States to promote **renewable/low-carbon fuels and OPS infrastructure** in maritime. Paying the penalty **does not** make the fuel compliant; it discharges the deficit for that period only. `CONFIRMED` (EUR-Lex Art. 23(9)–(11); DG MOVE Q&A 23.1).

---

## 7. Compliance checklist — items in this slice (draft)

For a shipping **company** operating ships > 5,000 GT calling at EU/EEA ports (each item: deadline → authority/system):

1. **Assign/verify administering State** for the company (Art. 3(40) via ETS Art. 3gf) — confirm against the Commission-published list. `CONFIRMED`
2. **Register the company and fleet in THETIS-MRV** and **link each ship to a FuelEU-accredited verifier** (verifier accredited under Del. Reg. 2025/192). → EMSA THETIS-MRV. `CONFIRMED`
3. **Submit/maintain a per-ship FuelEU monitoring plan** — by 31 Aug 2024, or within 2 months of first EU port call for new-in-scope ships; update on material change (Art. 8). → accredited verifier via THETIS-MRV. `CONFIRMED`
4. **Only claim GHG credit for fuels with valid RED proof of sustainability** via a recognised voluntary scheme (mass balance); ensure crop-based biofuels are **not** relied on (fossil-default). Retain certificates per consignment. `CONFIRMED`
5. **Apply correct emission factors** — Annex II defaults, actual WtT only for certified renewables, actual TtW non-CO2 (LNG methane slip) only if certified to the Commission methane-slip guideline (Art. 10). `CONFIRMED`
6. **Submit the annual FuelEU report** for the prior calendar year to the verifier **by 31 January** of the verification period (Art. 15). → verifier / FuelEU database. `CONFIRMED`
7. **Ensure verifier records the verified report** and compliance balance in the FuelEU database **by 31 March** (Art. 16–17). `CONFIRMED`
8. **Elect and record flexibility** (bank/borrow/pool) if applicable (~30 April) — cross-ref flexibility slice. `PRIMARY-ONLY`
9. **Pay any FuelEU penalty before 30 June** to the administering State (Art. 23; EUR 2,400/t VLSFO-eq for GHG deficit, EUR 1.5/kWh OPS, +10%/consecutive year). `CONFIRMED`
10. **Obtain and keep on board a valid FuelEU Document of Compliance** — issued by the verifier **by 30 June**, valid 18 months after end of reporting period; required for port access / PSC (Art. 24). `CONFIRMED`

---

## 8. Conflicts and gaps

- **DoC validity wording:** legal text = "18 months after end of reporting period" (Art. 24); some trade guidance says "valid until 30 June of the following year." Reconciled — consistent given the 30 June issuance date. `CONFIRMED`, no substantive conflict.
- **Exact article split for reporting vs verification (Art. 15/16/17):** article *numbers* corroborated by Tier-2 (LR) and the Commission Q&A; verbatim article-by-article deadline text was not re-read line-by-line from EUR-Lex (the long HTML truncated in automated fetches). Deadlines themselves are `CONFIRMED` across DG MOVE + LR + EMSA; the precise Art. 15 vs 16 attribution for the 31 March recording step is `PRIMARY-ONLY` and flagged for the corroborator to confirm against the consolidated text.
- **RCF treatment detail** (Art. 3(4)/10) is `PRIMARY-ONLY` — recognised as eligible where RED criteria met, but delegated methodology detail not separately fetched.
- **Consolidated EUR-Lex URL** (CELEX 02023R1805) returned 404 on the dated consolidation; base act 32023R1805 (HTML) and the LSU summary were used instead. No amendments to the MRV/penalty articles are known as of 2026-07-05, so the base text is operative.

---

## 9. Source log

| # | URL | Tier | Access date | Supported |
|---|---|---|---|---|
| 1 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1805 | 1 | 2026-07-05 | Base regulation: scope, Art. 4 trajectory/baseline, Art. 5 RFNBO, Art. 8/10/15/16/17/23/24, Annexes I/II/IV, Recital 28 |
| 2 | https://eur-lex.europa.eu/legal-content/en/LSU/?uri=CELEX:32023R1805 | 1 | 2026-07-05 | Legislative summary: scope, trajectory, application dates, RFNBO incentive |
| 3 | https://transport.ec.europa.eu/transport-modes/maritime/decarbonising-maritime-transport-fueleu-maritime_en | 1 | 2026-07-05 | DG MOVE: timeline, reporting period, verifier role, Del. Reg. 2025/192 reference |
| 4 | https://transport.ec.europa.eu/transport-modes/maritime/decarbonising-maritime-transport-fueleu-maritime/questions-and-answers-regulation-eu-20231805-use-renewable-and-low-carbon-fuels-maritime-transport_en | 1 | 2026-07-05 | DG MOVE Q&A: fuel eligibility, mass balance, Art. 10 actual/default, methane slip, administering State (Art. 3gf), penalty €2400/€1.5, collection |
| 5 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32025R0192 | 1 | 2026-07-05 | Del. Reg. (EU) 2025/192: verifier accreditation scope, ISO 17029/14065, 765/2008 |
| 6 | https://www.emsa.europa.eu/reducing-emissions/news-activities/item/5306-fueleu-maritime-monitoring-plans-in-thetis-mrv.html | 1 | 2026-07-05 | EMSA: THETIS-MRV FuelEU building block (1 Aug 2024), monitoring-plan submission, verifier linkage |
| 7 | https://www.emsa.europa.eu/thetis-mrv.html | 1 | 2026-07-05 | EMSA THETIS-MRV platform (FuelEU database delivery) |
| 8 | https://www.lr.org/en/services/statutory-compliance/fueleu-regulation/timetable-for-compliance/ | 2 | 2026-07-05 | Corroboration: full deadline calendar (31 Aug / 31 Jan / 31 Mar / 30 Apr / 30 Jun), DoC validity |
| 9 | https://www.dnv.com/news/2025/eu-guideline-for-reporting-and-verifying-actual-methane-slip-for-fueleu-and-eu-mrvets/ | 2 | 2026-07-05 | Corroboration: methane-slip actual-value guideline |
| 10 | https://theicct.org/wp-content/uploads/2023/07/fuels-fit-for-55-red-iii-jul23.pdf | 2 | 2026-07-05 | Corroboration: food/feed-crop = least-favourable-fossil rule; RFNBO thresholds |
| 11 | https://www.zerocarbonshipping.com/news/fueleu-explainer-fuel-certification-essentials | 2 | 2026-07-05 | Corroboration: RED certification / mass balance chain of custody |
| 12 | https://carboneer.earth/en/2025/08/fueleu-maritime-compliance-2025/ | 2 | 2026-07-05 | Corroboration: €2,400/t VLSFO penalty, 10% escalation, DoC |
| 13 | https://www.cofrac.fr/en/search/accredited-eu-ets-verifiers-according-to-commission-implementing-regulation-eu-20182067 | 2 | 2026-07-05 | Corroboration: verifiers accredited under Del. Reg. 2025/192 |
| 14 | https://www.sustainable-ships.org/rules-regulations/fueleu | 2 | 2026-07-05 | Corroboration: crop-biofuel treatment, fuel eligibility |

---

### 4-line summary

1. **Fuel eligibility:** WtW GHG intensity (Annex I/II) with RED II/III-certified actual values only for sustainable biofuels/RFNBOs (mass balance); fossil fuels use Annex II defaults; **food/feed-crop biofuels are assigned the least-favourable fossil emission factor** (verified — effectively not rewarded); RFNBOs earn a ×2 multiplier 2025–2033.
2. **Verifier role:** independent verifiers accredited under Reg. 765/2008 and Del. Reg. (EU) 2025/192 assess monitoring plans, verify annual FuelEU reports/compliance balance in the FuelEU database (THETIS-MRV) by 31 March, and issue the DoC.
3. **Document of Compliance deadline:** issued by the verifier **by 30 June** of the verification period (penalties due before 30 June), valid 18 months after the reporting period; a valid DoC is required for EU/EEA port access.
4. **Administering State:** each company is supervised by one administering State (FuelEU Art. 3(40) via ETS Art. 3gf) which ensures collection of the FuelEU penalty (EUR 2,400/t VLSFO-eq GHG deficit; EUR 1.5/kWh OPS; +10% per consecutive year).
