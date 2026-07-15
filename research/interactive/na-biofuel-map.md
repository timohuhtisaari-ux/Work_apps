---
title: North America — State & Provincial Fuel Regulation Map
tags: [biofuel, LCFS, RFS, clean-fuel-regulations, north-america, map, research]
created: 2026-07-15
units: 64
---

# North America — State & Provincial Fuel Regulation Map

> [!info] Interactive map
> The interactive map lives in **`na-biofuel-map.html`** (keep it in the same folder as this note). Real admin-1 borders (Albers equal-area conic) for **all 51 US units (50 states + DC) and 13 Canadian provinces/territories**. Click any unit for its instrument; colour by program type; zoom to the US or Canada.

## The federal floor (applies everywhere)

- **United States — RFS2 (EPA):** a national *volume* mandate via RINs. 2026 RVO **26.81 bn RINs** (advanced 11.10, biomass-based diesel 9.07, cellulosic 1.36), plus the **§45Z Clean Fuel Production Credit**. There is **no federal blend mandate**.
- **Canada — Clean Fuel Regulations (SOR/2022-140, ECCC):** a *carbon-intensity* standard on gasoline/diesel suppliers, **3.5 gCO₂e/MJ (2023) → 14 gCO₂e/MJ (2030)** below the 2016 baseline; volumetric floor **≥5% gasoline / ≥3% diesel** (Newfoundland & Labrador and the three territories are exempt from the volumetric floor).

"Program type" on the map reflects the **most stringent in-force state/provincial instrument on top of that floor**. A unit can run both an LCFS and a blend mandate — the card lists both. Every unit not in the tables below runs the **federal program only** (44 units).

## United States — units with a state instrument

| State | Code | Program type | Headline instrument | Status |
|---|---|---|---|---|
| California | `CA` | Low-carbon / CI | California LCFS (CARB) — 30% carbon-intensity cut by 2030, 90% by 2045 | In force — the model US low-carbon fuel standard |
| Oregon | `OR` | Low-carbon / CI | Oregon Clean Fuels Program (DEQ) — 20% CI cut by 2030, 37% by 2035 | In force — LCFS + blend mandates layered |
| Washington | `WA` | Low-carbon / CI | Washington Clean Fuel Standard (Ecology) — raised to 45% CI cut by 2038 | In force — stronger 2025 target |
| New Mexico | `NM` | Low-carbon / CI | New Mexico Clean Transportation Fuel Standard (NMED/EIB) — 20% CI cut by 2030, 30% by 2040 | Adopted — starts 1 Apr 2026 |
| Minnesota | `MN` | Volumetric blend | Minnesota — B20 (Apr–Sep) / B5 (Oct–Mar) biodiesel + E10 ethanol | In force (Minn. Stat. §§239.75/239.77/239.761) |
| Pennsylvania | `PA` | Volumetric blend | Pennsylvania — B2 biodiesel in force | In force at B2 only (Act 78/2008, am. 2010) |
| Missouri | `MO` | Volumetric blend | Missouri — E10 in all gasoline (premium exempt) | E10 in force (Mo. Rev. Stat. §414.255) |
| Iowa | `IA` | Tax incentive | Iowa — retailer tax credits, no blend mandate | Federal RFS only for content; incentive-led |
| Illinois | `IL` | Tax incentive | Illinois — sales-tax treatment tied to blend level, no mandate | Federal RFS only for content; incentive-led |
| Rhode Island | `RI` | Tax incentive | Rhode Island — Bioheat heating-oil mandate (NOT motor fuel) | Heating-oil mandate in force; road fuel = federal RFS only |
| Montana | `MT` | Repealed / suspended | Montana — former E10 requirement REPEALED | Repealed — federal RFS only |
| Hawaii | `HI` | Repealed / suspended | Hawaii — former E10 (≥85% of pool) REPEALED | Repealed — federal RFS only |
| Louisiana | `LA` | Repealed / suspended | Louisiana — 2% biodiesel / 2% ethanol mandates dormant | Dormant / not enforced |
| Massachusetts | `MA` | Repealed / suspended | Massachusetts — Advanced Biofuels Mandate SUSPENDED | Mandate suspended; fleet-only in force |

## Canada — provinces & territories

| Province / territory | Code | Program type | Headline instrument | Status |
|---|---|---|---|---|
| British Columbia | `BC` | Low-carbon / CI | British Columbia LCFS — CI cut 20.6% (2026) → 30% (2030) | In force — most stringent provincial regime |
| Québec | `QC` | Low-carbon / CI | Québec — low-CI fuel content: gasoline 10%→15%, diesel 3%→10% by 2030 | In force |
| Alberta | `AB` | Volumetric blend | Alberta — 5% ethanol in gasoline / 2% renewable diesel | In force |
| Saskatchewan | `SK` | Volumetric blend | Saskatchewan — 7.5% ethanol / 2% renewable diesel | In force |
| Manitoba | `MB` | Volumetric blend | Manitoba — 10% ethanol / 5% renewable content in diesel | In force |
| Ontario | `ON` | Volumetric blend | Ontario — gasoline renewable content 11% (2025) → 13% (2028) → 15% (2030) | In force (13%/15% steps adopted) |
| Newfoundland and Labrador | `NL` | Federal only | Newfoundland & Labrador — federal Clean Fuel Regulations only | Federal CFR only (volumetric-exempt) |
| Yukon | `YT` | Federal only | Yukon — federal Clean Fuel Regulations only | Federal CFR only (volumetric-exempt) |
| Northwest Territories | `NT` | Federal only | Northwest Territories — federal Clean Fuel Regulations only | Federal CFR only (volumetric-exempt) |
| Nunavut | `NU` | Federal only | Nunavut — federal Clean Fuel Regulations only | Federal CFR only (volumetric-exempt) |

## Notes & flags

- Several oft-cited US "state mandates" are **not in force**: New Mexico B5 (suspended), Louisiana 2% (dormant), Montana & Hawaii E10 (repealed), Massachusetts advanced-biofuels (suspended; state-fleet only).
- Oregon and Washington run **both** an LCFS/clean-fuel standard **and** blend mandates — coloured as low-carbon/CI (the more stringent), with the blend mandate noted in the card.
- Rhode Island's B5→B50 mandate is **heating oil, not road fuel** — shown as tax-incentive/other.
- **California** 2026 24.20% benchmark is PRIMARY-ONLY (CARB host returned HTTP 403; Tier-2 corroborated). **Québec** 2026 interim step is UNCORROBORATED (LégisQuébec 403).

## Sources

- **US:** `research/reports/drafts/us-lcfs-headline-2026-07-13.md` (federal RFS2 + CA/OR/WA/NM LCFS) and `us-blend-mandates-headline-2026-07-13.md` (state blend mandates + tax incentives).
- **Canada:** `research/reports/drafts/canada-biofuel-headline-2026-07-13.md` (federal CFR + BC/AB/SK/MB/ON/QC).

Basemap © Natural Earth (public domain), 1:50m admin-1 states/provinces, Albers equal-area conic. Confidence labels per `research/METHODOLOGY.md`.
