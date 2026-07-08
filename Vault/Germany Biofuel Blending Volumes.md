---
title: Germany Biofuel Blending Volumes
aliases:
  - German biofuel blending
  - BAFA biofuel volumes
  - THG-Quote biofuels
tags:
  - energy/biofuels
  - germany
  - data/bafa
  - data/ble
  - commodities/transport-fuels
type: research-report
status: living-document
country: Germany
latest_data: "2026-04"
sources_primary:
  - BAFA Amtliche Mineralöldaten (monthly, tonnes)
  - BLE Evaluations- und Erfahrungsbericht (annual, energy)
created: 2026-07-08
updated: "2026-07-08"
---

> [!info] Related
> [[BAFA]] · [[BLE]] · [[THG-Quote]] · [[HVO]] · [[FAME]] · [[Bioethanol]] · [[Biomethane]] · [[ReFuelEU Aviation]]
> Machine-readable data: `research/data/bafa-monthly-blending.csv`


**Research report — official sources (BAFA, BLE, Zoll, Umweltbundesamt), with fuel-type breakdown**
*Compiled 2026-07-08. Sections 1–7 verified against primary PDFs/pages by three independent verifiers. Section 8 (monthly 2025–2026 update) extracted directly from BAFA's monthly Amtliche Mineralöldaten PDFs.*

> **Latest update (Section 8):** month-by-month BAFA data now runs through **April 2026** (released 2 July 2026). Two structural changes since the original report: (1) BAFA now **reports HVO and FAME as separate line items** from January 2025 — resolving the biggest limitation flagged below — and (2) a **Biokerosin (SAF)** line appeared in 2026. Headline: **blended HVO nearly quadrupled year-on-year** in early 2026 (Jan–Apr: 211.6 kt vs 58.4 kt), while FAME slipped ~11%.

---

## 1. Executive summary

Germany's biofuel blending is documented by **two complementary official statistics** that measure different things:

- **BAFA** (Bundesamt für Wirtschaft und Ausfuhrkontrolle) — *Amtliche Mineralöldaten*: **physical blended tonnages** under the Mineralöldatengesetz. Caveat: FAME, HVO and BTL are reported as **one combined line** and never disaggregated.
- **BLE** (Bundesanstalt für Landwirtschaft und Ernährung) — *Evaluations- und Erfahrungsbericht* (based on the Nabisy sustainability-proof database): **energy content (TJ) applied for crediting** against the THG-Quote, **broken down by fuel type** (FAME, HVO, bioethanol, biomethane, Bio-LNG, bio-methanol, bio-naphtha, …). This is the only official statistic that separates HVO and bionaphtha from FAME.

Headline numbers:

- **BAFA (physical tonnes):** biodiesel-family blending (FAME/HVO/BTL) was ~2.54 Mt (2022) → ~2.60 Mt (2023) → **~2.12 Mt (2024, −18.4 %)**; directly blended bioethanol rose steadily ~1.06 → 1.12 → **1.16 Mt**, plus 90–132 kt of ethanol bound in ETBE.
- **BLE (quota-registered energy):** ~**140 PJ / 3.93 Mt** in 2023 (FAME 60 %, ethanol 24 %, HVO 12 %) → ~**126 PJ / 3.6 Mt** in 2024 (FAME 55 %, ethanol 26 %, HVO 7 %), avoiding ~12 Mt and 11.5 Mt CO₂e respectively.
- **Umweltbundesamt:** biofuels = **5.0 %** of German transport fuel energy consumption in 2024 (excluding electricity).
- Volumes are shaped by the **THG-Quote sub-caps** (administered by Zoll under the 38. BImSchV): crop-based biofuels capped at 4.4 % from 2022, Annex IX Part B waste oils/fats at 1.9 %, palm oil effectively phased out from 2023.

---

## 2. BAFA — physical blending volumes (tonnes)

Source: BAFA *Amtliche Mineralöldaten*, table "Beimischung von Biozusatzstoffen in Mineralölprodukten im Inland" (Dec 2023 and Dec 2024 editions). Verified 3-0.

| Component (BAFA line item) | 2022 (t) | 2023 (t) | 2024 (t) | 2024 y/y |
|---|---:|---:|---:|---:|
| Biodiesel (FAME), HVO, BTL¹ | 2,537,445 | 2,599,249 | 2,121,690 | **−18.4 %** |
| Bioethanol (directly blended) | 1,058,835 | 1,119,897 | 1,157,215 | **+3.3 %** |
| Bioethanol bound in ETBE² | 131,555 | 131,714 | 90,271 | **−31.5 %** |

¹ The 2024 table adds *Bioheizöl* (bio-heating oil) to this combined line. BAFA never disaggregates FAME from HVO/BTL in this statistic.
² **Methodology break:** from 2024 BAFA counts the bioethanol share of ETBE at **37 vol-%** instead of the 47 vol-% used through 2023 (footnote a of the Dec 2024 table). The factor change alone accounts for ~21.3 points of the −31.5 % decline; the 2023 column was not restated, so year-on-year comparability of this line is broken.

**Monthly granularity** exists: BAFA publishes the workbook monthly, and industry body en2x redistributes the BAFA workbook unaltered (verified by forensic inspection of the xlsx — BAFA title/logo, zero edits). Example (June 2023, Table 9): FAME/HVO/BTL into diesel 231,715 t in the month (+16.8 % y/y), 1,269,161 t Jan–Jun; direct ethanol into gasoline 94,836 t in the month, 519,873 t Jan–Jun.

---

## 3. BLE — quota-registered volumes by fuel type (energy basis)

Source: BLE *Evaluations- und Erfahrungsbericht 2023* (published Dec 2024) and BLE press releases 18.12.2024 and 09.12.2025 (2024 report). Verified 3-0.

### Totals

| Quota year | Energy (TJ) | Mass (kt) | GHG avoided (Mt CO₂e) | Avg. GHG reduction vs fossil |
|---|---:|---:|---:|---:|
| 2022 | 140,090 | ~3,900 | 11.6 | — |
| 2023 | 140,294 | 3,929 | ~12.0 | 90 % |
| 2024 | ~126,000 | ~3,600 | 11.5 | **96 %** |

2024 volume fell to ~90 % of 2023, but per-unit GHG-savings intensity rose sharply (96 % vs 90 %) — the quota is met with fewer, higher-performing (waste-based) fuels.

### Breakdown by fuel type

| Fuel type | 2023 (TJ) | 2023 share | 2024 share |
|---|---:|---:|---:|
| **FAME (biodiesel)** | 83,773 | 59.7 % | 55 % |
| **Bioethanol** | 33,061 | 23.5–24 % | 26 % |
| **HVO** | 16,688 | 11.9–12 % (−21 % y/y) | 7 % |
| Biomethane | — | 3.5 % | n/a³ |
| Bio-LNG | — | 0.9 % | n/a³ |
| Bio-methanol | — | 0.3 % | n/a³ |
| **Bio-naphtha** | 46 | 0.03 % | n/a³ |
| Vegetable oil | — | 0.01 % | n/a³ |
| Bio-gasoline | — | 0.002 % | n/a³ |

³ Exact 2024 TJ figures for the minor components were not extracted from the Evaluationsbericht 2024; the press release gives only the FAME/ethanol/HVO shares.

### Feedstock structure (2023)

- HVO registered in Germany was almost entirely **waste/residue-based**: 16,664 TJ = 99.8 % of HVO.
- FAME was **70 % waste/residue-based** (58,780 TJ); rapeseed contributed 21,918 TJ (26 %).
- **Palm-oil biofuels played no further role** — non-creditable against the quota from 2023.

---

## 4. Regulatory context — THG-Quote sub-caps (Zoll, 38. BImSchV)

The greenhouse-gas reduction quota is administered by German customs (Zoll). Sub-caps directly shape which fuels get blended (quantities above a cap are assigned the fossil baseline value of 94.1 kg CO₂eq/GJ, making them uneconomic):

| Rule | Cap |
|---|---|
| Crop-based (food/feed) biofuels, §13 | 6.5 % through 2021; **4.4 % from 2022** (through 2025; RED III implementation raises this to 4.9 % from 2026) |
| Annex IX Part B (used cooking oil, cat. 1–2 animal fats), §13a | **1.9 % from 2022** (measured against energy content of fuel placed on market) |
| High-ILUC-risk feedstocks (palm oil), §13b | 0.9 % in 2022; **0 % from 2023** |

FAME is fully creditable when it meets DIN EN 14214 and the sustainability criteria.

**Refuted claim (0-3):** "HVO from Annex IX Part A wastes/residues counts toward the THG-Quote only from 2024 onward" — this was checked against Zoll's crediting rules and rejected; no such 2024 start date exists.

---

## 5. Who publishes what — data definitions

| Agency | Statistic | Measures | Fuel-type detail |
|---|---|---|---|
| **BAFA** | Amtliche Mineralöldaten (monthly + annual) | Physical blended tonnages (Mineralöldatengesetz) | FAME/HVO/BTL combined; ethanol direct vs ETBE |
| **BLE** | Evaluations- und Erfahrungsbericht (annual, Nabisy-based) | Energy (TJ) **applied for** THG-Quote crediting — BLE explicitly cannot confirm all quantities were actually credited | Full split incl. HVO, bio-naphtha, biomethane, Bio-LNG |
| **Zoll** | THG-Quote rules & fulfilment | Quota obligations, caps, crediting | Regulatory, not volumes |
| **Umweltbundesamt** | Energieverbrauch Kraftstoffe | Aggregate biofuel share of transport energy: **5.0 % in 2024** (energy content, excl. electricity) | Aggregate only |
| **en2x / VDB / BDBe** | Market data (secondary) | en2x redistributes BAFA's workbook unaltered; VDB/BDBe consistent with BAFA totals | Industry views |

---

## 6. Caveats and open questions

**Caveats**
1. No official German statistic reports **standalone HVO tonnage** in physical blending data; the only HVO-specific figures are BLE's quota-registered energy quantities — a different measure (applied-for crediting, not confirmed consumption).
2. BAFA's 2024 table added Bioheizöl to the biodiesel line **and** changed the ETBE ethanol factor (47 → 37 vol-%) without restating prior years — part of the reported −18.4 % / −31.5 % declines is definitional.
3. BLE volumes are quantities *applied* for crediting via Nabisy; "produced for the German market" is not identical to "placed on market."
4. Verified detail covers **2022–2024**; 2025 data were not yet published at research time (BLE's 2024 report appeared Dec 2025; BAFA final 2024 data Jul 2025). 2019–2021 figures did not survive verification and would need earlier report editions.

**Open questions**
- Exact 2019–2021 annual volumes by fuel type (earlier BAFA/BLE editions would extend the series).
- How much of the −18.4 % BAFA drop in 2024 is real volume vs definitional, and the roles of carried-over quota credits, the UER/biofuel-certificate fraud scandal, and diesel market contraction.
- Standalone **HVO100** sales after retail approval (10. BImSchV amendment, April/May 2024) — pure B100/HVO100 volumes are not captured by BAFA's "Beimischung" table.
- Detailed 2024 TJ volumes for biomethane, Bio-LNG, bio-methanol, bio-naphtha in the Evaluationsbericht 2024.

---

## 7. Key sources

**Primary (official)**
- BAFA, Amtliche Mineralöldaten Dez 2024: <https://www.bafa.de/SharedDocs/Downloads/DE/Energie/Mineraloel/moel_amtliche_daten_2024_12.pdf>
- BAFA, Amtliche Mineralöldaten Dez 2023: <https://www.bafa.de/SharedDocs/Downloads/DE/Energie/Mineraloel/moel_amtliche_daten_2023_12.pdf>
- BAFA Mineralölstatistik landing page: <https://www.bafa.de/DE/Energie/Rohstoffe/Mineraloelstatistik/mineraloel_node.html>
- BLE, Evaluations- und Erfahrungsbericht 2023: <https://www.ble.de/SharedDocs/Downloads/DE/Klima-Energie/Nachhaltige-Biomasseherstellung/Evaluationsbericht_2023.pdf>
- BLE, Evaluationsbericht 2024: <https://www.ble.de/SharedDocs/Downloads/DE/Klima-Energie/Nachhaltige-Biomasseherstellung/Evaluationsbericht_2024.pdf>
- BLE press releases 18.12.2024 and 09.12.2025 (quota years 2023, 2024)
- Zoll, Anrechnung von Biokraftstoffen (THG-Quote): <https://www.zoll.de/DE/Fachthemen/Steuern/Verbrauchsteuern/Treibhausgasquote-THG-Quote/Quotenverpflichtung/Erfuellung-Quotenverpflichtung/Anrechnung-Biokraftstoffe/anrechnung-biokraftstoffe_node.html>
- Umweltbundesamt, Energieverbrauch nach Kraftstoffen: <https://www.umweltbundesamt.de/daten/umweltzustand-trends/verkehr/energieverbrauch-kraftstoffe>
- Eurostat SHARES (EU-harmonized cross-check): <https://ec.europa.eu/eurostat/web/energy/database/additional-data>
- DBFZ background papers on the THG-Quote (2022, 2023)

**Secondary (industry)**
- en2x monthly statistics (redistributed BAFA workbooks): <https://en2x.de>
- VDB market data: <https://biokraftstoffverband.de/biokraftstoffe/marktdaten/>
- BDBe bioethanol market data: <https://www.bdbe.de/bioethanol/marktdaten>

---

## 8. Monthly update — BAFA blending data, January 2025 – April 2026

*Source: BAFA, Amtliche Mineralöldaten, monthly editions Jan 2025 – Apr 2026 (table 9, "Beimischung von Biozusatzstoffen in Mineralölprodukten im Inland"), extracted directly from the published PDFs. April 2026 is the latest available (released 2 July 2026); BAFA data run ~2–3 months behind the reporting month. All figures in tonnes.*

### 8.1 What changed in the statistic itself
- **HVO now reported separately.** From the January 2025 edition, BAFA splits the old combined "Biodiesel (FAME), HVO, BTL" line into **"davon FAME"** and **"davon HVO"** sub-lines. This is the first time standalone HVO *blending* tonnage appears in the physical mineral-oil statistic — directly answering open question #3 from the original report.
- **Biokerosin (SAF) line added in 2026.** A "Biokerosin" row appears in the 2026 editions (bio-jet fuel / SAF, reflecting the ReFuelEU Aviation 2% blending mandate in force from 2025). Prior-year comparators are shown as 0.
- **Combined line label** is now "Biodiesel (FAME), HVO, BTL und andere Biozusätze"; the ETBE bioethanol factor remains 37 vol-% (vs 47% through 2023).

### 8.2 Monthly blended volumes (tonnes)

| Month | FAME | HVO | BTL/other | Biodiesel family (total) | Bioethanol (direct) | Ethanol in ETBE | Biokerosin |
|---|---:|---:|---:|---:|---:|---:|---:|
| Jan 2025 | 172,480 | 8,709 | 227 | 181,416 | 86,022 | 8,204 | – |
| Feb 2025 | 198,902 | 15,825 | 141 | 214,868 | 116,865 | 5,605 | – |
| Mar 2025 | 185,345 | 24,315 | 180 | 209,840 | 93,510 | 7,641 | – |
| Apr 2025 | 182,929 | 9,515 | 259 | 192,703 | 86,303 | 6,479 | – |
| May 2025 | 183,155 | 6,486 | 450 | 190,091 | 98,993 | 5,586 | – |
| Jun 2025 | 180,222 | 13,680 | 359 | 194,261 | 95,391 | 6,069 | – |
| Jul 2025 | 183,771 | 9,711 | 367 | 193,849 | 101,681 | 6,946 | – |
| Aug 2025 | 169,781 | 9,140 | 99 | 179,020 | 86,905 | 8,614 | – |
| Sep 2025 | 180,980 | 4,877 | 375 | 186,232 | 108,894 | 9,160 | – |
| Oct 2025 | 190,147 | 5,183 | 347 | 195,677 | 117,616 | 6,763 | – |
| Nov 2025 | 184,750 | 3,644 | 608 | 189,002 | 110,470 | 6,080 | – |
| Dec 2025 | 182,230 | 7,838 | 146 | 190,214 | 119,355 | 7,150 | – |
| **FY 2025** | **2,194,692** | **118,923** | **3,558** | **2,317,173** | **1,222,005** | **84,298** | **0** |
| Jan 2026 | 145,333 | 27,596 | 92 | 173,021 | 80,921 | 6,087 | n/a¹ |
| Feb 2026 | 154,712 | 48,256 | 347 | 203,315 | 81,880 | 7,434 | n/a¹ |
| Mar 2026 | 167,796 | 58,084 | 149 | 226,029 | 87,432 | 9,622 | n/a¹ |
| Apr 2026 | 189,800 | 77,692 | 41 | 267,533 | 98,349 | 7,965 | 3,197 |
| **Jan–Apr 2026** | **657,641** | **211,628** | **~629** | **869,898** | **350,616** | **31,107** | **8,375** |

¹ The Biokerosin row is present in the Jan–Mar 2026 editions but the monthly value was not populated/legible in those files; the Jan–Apr 2026 cumulative of 8,375 t (from the April edition) is the reliable figure.

### 8.3 Year-on-year trends (cumulative)

| Metric | FY 2025 | vs FY 2024 | Jan–Apr 2026 | vs Jan–Apr 2025 |
|---|---:|---:|---:|---:|
| FAME (blended) | 2,194,692 t | +11.6 % | 657,641 t | **−11.1 %** |
| **HVO (blended)** | 118,923 t | **−17.0 %** | 211,628 t | **+262.6 %** |
| Biodiesel family total | 2,317,173 t | +9.2 %² | 869,898 t | +8.9 % |
| Bioethanol (direct) | 1,222,005 t | +5.3 % | 350,616 t | −6.3 % |
| Ethanol in ETBE | 84,298 t | −6.7 % | 31,107 t | +11.4 % |

² FY2024 comparator is the 2,121,690 t combined line from the original report (which included Bioheizöl); definitions are close but not identical, so treat the +9.2 % as indicative.

### 8.4 The story in the 2025–2026 data
- **Blended HVO collapsed through 2025, then exploded in 2026.** Monthly blended HVO fell from ~8–24 kt in early 2025 to a low of 3.6 kt in November 2025 (FY2025 −17% y/y). It then ramped hard: 27.6 kt (Jan) → 48.3 kt (Feb) → 58.1 kt (Mar) → **77.7 kt (Apr 2026)** — year-on-year growth of **+139% to +716%** per month, and **+263% cumulative** for Jan–Apr. HVO went from ~5% to nearly **30% of the biodiesel-family blend** within a year.
- **FAME gave way to HVO.** FAME blending, up 11.6% in FY2025, fell 11.1% in Jan–Apr 2026 — the mirror image of the HVO surge. The total biodiesel family still grew ~9%, so this is substitution within the diesel pool, not a demand collapse.
- **Bioethanol stayed broadly flat**, ~80–119 kt/month, with a mild soft patch in early 2026 (−6.3% cumulative).
- **SAF/Biokerosin is now visible in the official blend data** for the first time (~3.2 kt/month, 8.4 kt Jan–Apr 2026), reflecting the ReFuelEU aviation mandate.

### 8.5 Caveats specific to this section
- This is BAFA's **physical blending ("Beimischung") table only** — it captures biocomponents *blended into* mineral-oil products. **Neat fuels sold unblended (B100, HVO100, E85) are not in this table**, so total HVO placed on the German market is higher than the blended figure shown here.
- BAFA labels the 2026 editions "vorläufige Daten" (provisional); monthly figures are routinely revised in later editions and in the December annual consolidation.
- The Jan–Mar 2026 PDFs use a subset-font encoding; figures were recovered by decoding and cross-checked against the cumulative columns in the April 2026 edition, which agree.

---

## 9. Gaseous fuels — biomethane, Bio-LNG/LNG, Bio-CNG/CNG

**BAFA does not report gaseous fuels at all.** Its *Amtliche Mineralöldaten* cover only liquid mineral-oil products and their liquid biocomponents. The only gas-adjacent lines in the whole publication are "Flüssiggas" (LPG/Autogas — petroleum, not bio, not LNG/CNG) and "Erdgaskondensat" (a crude-side feedstock). There is no methane/CNG/LNG row anywhere.

### 9.1 Is there ANY monthly source for gaseous transport fuels?
**Bottom line: no official, BAFA-equivalent monthly statistic splits gaseous transport fuel into bio vs. fossil.** Nothing in the German or EU statistical system publishes a scheduled monthly time series of biomethane / Bio-CNG / Bio-LNG (or fossil CNG/LNG) dispensed to vehicles. The choices are: a monthly *industry proxy* with no clean bio split, or an *annual* official source with a proper bio split.

| # | Source | Cadence | Reports | Bio vs fossil? | Transport isolated? |
|---|---|---|---|---|---|
| 1 | **Zukunft Gas** LNG/CNG station-sales tonnage (industry, ex-"erdgas mobil") | Monthly-resolvable but **published irregularly** | Physical LNG dispensed at truck stations (tonnes) | Weak (fossil LNG historically; Bio-LNG only qualitative) | Yes |
| 2 | **BLE** Evaluationsbericht (Nabisy/THG-Quote) | **Annual** (mid-following-year) | Biomethane + **Bio-LNG** shares of quota energy (2023: biomethane 3.5%, Bio-LNG 0.9%) | **Yes — the only clean bio split** | Yes |
| 3 | **Eurostat** monthly gas balance `nrg_cb_gasm` | **Monthly** (~2-mo lag) | Natural-gas balance (G3000 only) | No (no biomethane code) | No (no transport field — verified via API) |
| 4 | **Destatis** Energiesteuerstatistik (Erdgas als Kraftstoff) | **Annual** (large lag) | Taxed gas volume at reduced fuel rate | No | Yes (via tax base) |
| 5 | **Trading Hub Europe** aggregated consumption / biogas balancing | Daily/monthly | Aggregated gas withdrawal (kWh); biogas balancing groups | Partial (biogas groups) | No |
| 6 | **BNetzA** biomethane monitoring | Annual | Biomethane grid feed-in (GWh), plant counts | Bio (feed-in, not end-use) | No |
| 7 | **MaStR** / **dena Biogasregister** | Register (no cadence) | Plant master data / origin certificates — **no throughput volumes** | — | — |

### 9.2 Practical recommendation
There is **no single monthly source** that gives bio-split gaseous transport volumes. The workable approach is to **combine Zukunft Gas monthly LNG/CNG tonnage** (proxy for total gaseous transport fuel) **with the BLE annual bio-share percentages** to estimate the bio vs. fossil split within each month. Track BLE annually for the authoritative biomethane/Bio-LNG figures; treat any monthly gaseous number as an industry estimate, not an official statistic.

Key URLs: Zukunft Gas <https://www.zukunft-gas.com/>; BLE Evaluationsbericht <https://www.ble.de/SharedDocs/Downloads/DE/Klima-Energie/Nachhaltige-Biomasseherstellung/Evaluationsbericht_2024.pdf>; Eurostat `nrg_cb_gasm` <https://ec.europa.eu/eurostat/databrowser/view/nrg_cb_gasm/default/table?lang=en>; BNetzA biomethane <https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/ErneuerbareEnergien/Biogas/artikel.html>; Destatis Energiesteuer <https://www.destatis.de/DE/Themen/Staat/Steuern/Verbrauchsteuern/>.

---

## 10. Reproducibility & automation

- **Extraction script:** `scripts/extract_bafa_blending.py` downloads every published monthly BAFA edition (2025→present), parses Table 9 (auto-handling the subset-font encoding in some 2026 editions), and writes the machine-readable dataset. Run `python3 scripts/extract_bafa_blending.py`.
- **Dataset:** `research/data/bafa-monthly-blending.csv` — one row per month, all fuel-type columns in tonnes.
- **Monthly refresh:** a scheduled routine re-runs the script, appends any new month(s) to Section 8, and notifies (push + email) when BAFA publishes a new edition.

---

*Method: Sections 1–7 — 5 parallel search angles → 22 sources fetched → 107 claims extracted → top 25 verified by 3 independent adversarial verifiers each (24 confirmed unanimously, 1 refuted) → synthesis; 104 agents total. Section 8 — direct extraction of 16 monthly BAFA PDFs (Jan 2025 – Apr 2026), figures cross-checked against cumulative columns. Section 9 — targeted source audit of German/EU gaseous-fuel statistics.*
