# United Kingdom (GB) — Sustainability & Compliance Requirements (draft)

- **Scope:** Section 3 of country report + Section 4 checklist items in sustainability scope
- **Researched by:** sustainability-researcher
- **Access dates:** all live fetches 2026-07-05
- **Corroboration pass:** completed 2026-07-05 (source-corroborator)

> Framing: The UK **left the EU**; RED/EU voluntary-scheme law does not apply. Sustainability & GHG criteria are set nationally under the **Renewable Transport Fuel Obligation (RTFO)**, administered by the **Department for Transport (DfT)** as RTFO Administrator. The UK does **not** use the EU Union Database — it uses the **RTFO Operating System (ROS)**.

## 3. Sustainability & compliance requirements

### 3.1 Transposition / legal instruments
- **Renewable Transport Fuel Obligations Order 2007 (as amended)** — the operative UK instrument (certificate-based RTFC scheme). Sustainability/GHG criteria are set by DfT and detailed in the annual **RTFO/SAF Mandate Technical Guidance** and **Compliance Guidance** (2026 editions, valid 01/01/26–31/12/26). Related: **Motor Fuel (Road Vehicle and Mobile Machinery) GHG Emissions Reporting Regulations** for the parallel GHG-credit route. `PRIMARY-ONLY` (gov.uk guidance) — corroborator to confirm the amending SI reference on legislation.gov.uk.
- Post-Brexit divergence: the UK runs its **own** approved-schemes list and its **own** registry; it is not bound by RED III or the EU UDB. `CONFIRMED` (gov.uk).

### 3.2 GHG-saving thresholds
| Threshold | Applies | Confidence |
|---|---|---|
| **50%** GHG saving vs fossil comparator | installations operating before 5 Oct 2015 | `CONFLICT` (see below) |
| **60%** GHG saving | installations that started operating on/after 5 Oct 2015 | `CONFLICT` (see below) |

- **CONFLICT — NOT RESOLVED (both Tier 1 gov.uk, disagreeing):**
  - The **"RTFO: an essential guide"** (re-fetched 2026-07-05, current general-facing DfT page) states GHG savings of **"at least 55 to 65% (depending on when the production installation started operating)"** [1].
  - The **RTFO statistics "Notes & definitions"** page (last updated Aug 2021) states **50% / 60%** by installation date [2].
  - Neither figure could be reconciled to a machine-readable primary threshold table: the authoritative **RTFO Carbon & Sustainability Guidance Part Two** is a gov.uk PDF that did **not** text-render in this environment (no poppler / PDF fetch 403). Per methodology, **no winner is picked**. The essential guide is the more current, forward-facing DfT statement ("55 to 65%"); the statistics page ("50/60%") predates recent updates. Corroborator flag: retrieve the 2026 Technical/C&S Guidance threshold table to settle which applies for the 2026 obligation period.
- Land criteria: no feedstock from land with high biodiversity value or high carbon stock (status referenced to **January 2008**); forestry legality/regeneration and (for agricultural-waste feedstocks) soil-quality criteria apply. `PRIMARY-ONLY`.

### 3.3 Accepted certification / proof of sustainability
- The UK maintains its **own DfT-approved list** of voluntary schemes (published on gov.uk; page updated **27 Nov 2025** per draft — not independently re-fetched this pass). Approved schemes include: **2BSvs, Better Biomass, Bonsucro EU, ISCC EU, KZR INiG, REDcert-EU, Red Tractor, RSB EU RED, RTRS EU RED, SSAP-RED, SQC, TASCC** (≈13 schemes). Several UK national schemes exclude soil-carbon criteria / lack full GHG coverage, so extra evidence may be required. `PRIMARY-ONLY` (gov.uk list) + Tier-2 (ISCC/REDcert notices of DfT approval).
- Using a voluntary scheme does **not** discharge the operator: the **Administrator may demand additional evidence across the entire chain of custody**, and all C&S data must be **independently verified** (below). `PRIMARY-ONLY`.

### 3.4 Independent verification requirement
- **All RTFC applications must be independently verified** by an approved verifier and demonstrate compliance with RTFO sustainability criteria; the Administrator checks C&S data against the RTFO Guidance. There is a dedicated **RTFO and SAF Mandate Third-Party Assurance Guidance 2026**. `PRIMARY-ONLY` (gov.uk essential guide + assurance guidance).

### 3.5 National registry & UDB status
- **RTFO Operating System (ROS)** — suppliers use ROS to report fuel volumes, submit RTFC applications, and redeem/trade RTFCs; ROS validates volumes against **HMRC** duty data. `PRIMARY-ONLY` (gov.uk).
- **UDB:** the UK does **not** participate in the EU Union Database; ROS is the equivalent national system. `CONFIRMED`.

### 3.6 Feedstock rules — crop cap, waste/UCO
- **Crop cap** ("relevant crop" RTFCs): introduced 2018 at **4%** of a supplier's total relevant fuel supply, **decreasing to 3% by 2026** and **2% by 2032**. `CONFIRMED` (Notes & definitions + DfT statutory review + Compliance/technical guidance).
- **Wastes/residues, dedicated energy crops, RFNBOs** earn **double RTFCs**; recycled carbon fuels earn single **development** RTFCs. `CONFIRMED`.
- **UCO** is a major waste feedstock; eligible wastes/residues are on the **RTFO and SAF Mandate list of feedstocks (wastes and residues)** published on gov.uk. Waste/residue claims still require chain-of-custody evidence and independent verification. `PRIMARY-ONLY`.
- No EU-style Annex IX; the UK "wastes and residues" list and "development fuel" categories are the UK equivalents. `PRIMARY-ONLY`.

### 3.7 Reporting / verification calendar
| Obligation | Detail | Confidence |
|---|---|---|
| **Obligation period** | calendar year (01 Jan–31 Dec) | `PRIMARY-ONLY` |
| **RTFC applications** | submitted via ROS, independently verified | `PRIMARY-ONLY` |
| **Compliance / buy-out** | obligation met **by 15 September** in the year following the obligation period, or pay the **buy-out price** | `CONFIRMED` (essential guide, re-fetched) |
| **Buy-out price** | **50p** per standard RTFC; **80p** per development-fuel RTFC | `CONFIRMED` (essential guide + DfT statutory review, corroborator) |

## 4. Draft compliance-checklist items (sustainability scope)
1. If supplying ≥ **450,000 L/yr**, register with the RTFO Administrator and obtain **ROS** access. [DfT/gov.uk]
2. For every RTFC claim, hold C&S data showing the applicable **GHG saving** (essential guide: "at least 55–65%"; statistics page: 50/60% — CONFLICT, resolve against 2026 Technical/C&S Guidance) and land criteria (Jan 2008 baseline). [RTFO Technical Guidance 2026]
3. Use a **DfT-approved voluntary scheme** (ISCC EU, REDcert-EU, 2BSvs, etc.) as evidence; be ready to supply **whole-chain** evidence on request. [gov.uk approved-schemes list, upd. 27 Nov 2025]
4. Obtain **independent third-party verification** of all C&S data before RTFC award. [Third-Party Assurance Guidance 2026]
5. Track the **crop cap**: 3% (2026) falling to 2% (2032) of relevant fuel supply. [Compliance Guidance 2026]
6. Apply **double-counting** correctly for wastes/residues/RFNBOs; confirm feedstocks against the gov.uk wastes-and-residues list. [gov.uk feedstock list]
7. Meet the obligation by **15 September** of the following year via ROS or pay buy-out (50p/80p). [essential guide]

## 5. Conflicts / gaps
- **GHG threshold CONFLICT — NOT RESOLVED:** essential guide "at least 55–65%" [1] vs statistics Notes & definitions "50/60%" [2]. Both Tier-1 gov.uk; no winner picked. The C&S Guidance Part Two PDF (authoritative threshold table) did not render (no poppler; PDF fetch 403). Resolve against the 2026 Technical/C&S Guidance. `FLAG`.
- **Buy-out values — RESOLVED / CONFIRMED:** 50p standard / 80p development, confirmed by the essential guide [1] and the DfT statutory-review page (cross-ref GB-mandates [13]).
- **Crop cap — CONFIRMED:** 3% (2026) → 2% (2032) (Notes & definitions + DfT statutory review).
- **Approved-schemes list date (27 Nov 2025)** — carried from draft; not independently re-fetched this pass.
- Underlying **RTFO Order 2007 amending SI** not yet cited from legislation.gov.uk — corroborator to pin the exact instrument in force for 2026.

## 6. Source log
| # | URL | Tier | Access | Supports |
|---|---|---|---|---|
| 1 | https://www.gov.uk/government/publications/about-the-rtfo/the-rtfo-an-essential-guide | 1 | 2026-07-05 (re-fetched, corroborator) | 450,000 L threshold; RTFCs; verification; 15 Sept buy-out (50p/80p); ROS; **GHG "at least 55 to 65%" (verbatim)** |
| 2 | https://www.gov.uk/government/publications/renewable-fuel-statistics-information/renewable-fuel-statistics-notes-and-definitions | 1 | 2026-07-05 | GHG 50/60% (page last updated Aug 2021); crop cap 4%→3%(2026)→2%(2032); double counting; ROS |
| 3 | https://www.gov.uk/government/publications/use-of-voluntary-schemes-as-evidence-of-rtfo-and-saf-mandate-compliance/list-of-voluntary-schemes-approved-for-the-rtfo-and-saf-mandate | 1 | 2026-07-05 | DfT-approved voluntary schemes list (upd. 27 Nov 2025); coverage caveats |
| 4 | https://assets.publishing.service.gov.uk/media/69a80c033b5b78231d1a9b78/dft-rtfo-compliance-guidance-26.pdf | 1 | 2026-07-05 | Compliance Guidance 2026; PDF did not text-render (no poppler) — to re-parse |
| 5 | https://assets.publishing.service.gov.uk/media/69a80f34a2495f2d259f142b/dft-rtfo-saf-mandate-third-party-assurance-26.pdf | 1 | 2026-07-05 (listed) | Third-Party Assurance Guidance 2026 (independent verification) |
| 6 | https://www.gov.uk/government/publications/rtfo-and-saf-mandate-feedstock-materials-used-for-creating-low-carbon-fuels/rtfo-and-saf-mandate-list-of-feedstocks-including-wastes-and-residues | 1 | 2026-07-05 (listed) | UK wastes/residues feedstock list (UCO etc.) |
| 7 | https://redcert.org/en/16-news-en/298-redcert-eu-approved-for-rtfo-in-the-united-kingdom-uk.html | 2 | 2026-07-05 (search) | corroborates REDcert-EU DfT/RTFO approval |
| 8 | https://www.gov.uk/government/calls-for-evidence/rtfo-statutory-review-and-future-of-the-scheme/rtfo-statutory-review-and-future-of-the-scheme | 1 | 2026-07-05 (corroborator) | buy-out 50p/80p; crop cap 3%(2026)→2%(2032) |

## 4-line summary — United Kingdom
1. **Transposition:** independent post-Brexit regime — RTFO Order 2007 (as amended) + annual DfT RTFO/SAF Technical & Compliance Guidance 2026; not bound by RED III. `PRIMARY-ONLY`.
2. **Certification regime:** DfT's own approved voluntary-scheme list (ISCC EU, REDcert-EU, 2BSvs, RSB, UK schemes; upd. 27 Nov 2025); mandatory **independent third-party verification** of all C&S data. `CONFIRMED`.
3. **Registry/UDB:** **RTFO Operating System (ROS)**, validated against HMRC data — **no EU UDB**; obligation met by 15 September (buy-out 50p/80p, CONFIRMED). `PRIMARY-ONLY / CONFIRMED (buy-out)`.
4. **Flags:** GHG-saving figures remain CONFLICT (essential guide 55–65% vs stats page 50/60%) — not resolved (C&S Guidance PDF unreadable); crop cap 3%(2026)→2%(2032) CONFIRMED; buy-outs 50p/80p CONFIRMED.
