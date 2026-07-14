# Switzerland — Biofuel Mineral-Oil-Tax EXEMPTION: Eligibility Criteria & Permit/Proof Process

- **Country:** Switzerland (CH) — non-EU / non-EEA (bilateral relationship)
- **Topic:** Eligibility gate and permit/proof procedure for the **mineral-oil-tax relief
  (Steuererleichterung)** on renewable/biogenic fuels. Companion to the tax-mechanics slice.
- **Draft date:** 2026-07-13 · **Researcher:** sustainability-requirements researcher
- **Facts date-stamped:** 2026-07-13 (per lead instruction; work performed 2026-07-13/14)
- **Framing:** Switzerland does **not** apply EU RED II/III. It runs its **own** ecological +
  social criteria under the **Umweltschutzgesetz (USG) Art. 35d**, the **CO2 Act (SR 641.71)**
  and the **Mineralölsteuergesetz (MinöStG, SR 641.61)**, implemented by the **IBTV** and
  **ETrV** ordinances (2025). The criteria **parallel** RED but are Swiss-autonomous and, on
  feedstock, **stricter** (categorical food/feed-crop ban). This draft goes **deeper** than
  §3 of `CH-country-report-2026-07-04.md`; it does not re-derive the compensation-obligation
  (Kompensationspflicht) figures, which are that report's scope.

> **FEDLEX REACHABILITY FLAG:** `fedlex.admin.ch` is JavaScript-gated and returned only a
> language-selection interface on every attempt (IBTV `eli/cc/2025/250`, and the ETrV ELI).
> The official IBTV/ETrV newsd PDFs did **not** decode (compressed streams; no `poppler`
> locally). Article-level text below therefore rests on **BAFU/BAZG/SECO/Pronovo admin.ch
> pages** (Tier 1) and the fedlex **search-index metadata** (SR number, ELI). Items that could
> not be pinned to the legal text are labelled **UNCORROBORATED / GAP**.

---

## 1. The statutory eligibility gate

Two cumulative gates must be passed before a biogenic fuel can receive the mineral-oil-tax
relief: an **ecological** gate (positive overall environmental balance) and a **social** gate.
Both are set by USG Art. 35d and detailed in the IBTV/ETrV/MinöStV.

### 1.1 Ecological requirements (positive overall environmental balance)

| Requirement | Threshold / rule | Legal basis | Confidence | Sources |
|---|---|---|---|---|
| **Minimum GHG saving** over the whole lifecycle | Emits **at least 40% less** greenhouse gas than the conventional fossil comparator ("mindestens 40 Prozent weniger Treibhausgase … über den gesamten Lebensweg") | USG Art. 35d; IBTV (SR 814.311.1); ETrV | PRIMARY-ONLY (Tier-1 BAFU IBTV, verbatim) | S1 |
| **Overall environmental impact** vs fossil comparator | Total environmental burden **not more than 25% greater** than the fossil equivalent → i.e. **≤ 125%** of the fossil comparator ("Umweltbelastung … gesamthaft höchstens 25 Prozent grösser") — ecological-scarcity / LCA method | USG Art. 35d; IBTV | PRIMARY-ONLY (Tier-1 BAFU IBTV, verbatim German) | S1 |
| **Land-use / no land conversion** | Feedstock must **not** come from conversion of land with **high carbon stock** — esp. forests, peatbogs, wetlands ("Flächen mit hohem Kohlenstoffbestand (insb. Wälder, Torfmoore, Feuchtgebiete)") — or land with **high biodiversity / protected areas** | USG Art. 35d; IBTV | PRIMARY-ONLY (Tier-1 BAFU IBTV, verbatim) | S1 |
| LCA method | BAFU/authority assess GHG + total environmental impact via **ecoinvent-based** LCA (ecological-scarcity method) | ETrV | PRIMARY-ONLY | S1, prior report §3.2 |

Notes:
- The **≤125%** figure is expressed in the ordinance as "höchstens 25 Prozent grösser," i.e. the
  fuel may be up to 25% worse than fossil on *aggregate* environmental impact but no more — this
  is the "positive overall environmental balance" (positive ökologische Gesamtbilanz) test that
  goes **beyond** the single GHG number. Verbatim German captured; the exact article number is a
  minor GAP (Fedlex JS-gated).
- The GHG threshold (≥40%) is the Swiss autonomous number; it **parallels** but is set
  independently of RED II/III. Corroboration to a second independent Tier-1/Tier-2 for the "40%"
  digit specifically is **pending** (the BAZG and ETrV pages state "ökologische Anforderungen"
  without re-quoting the digit) — kept **PRIMARY-ONLY**; it matches the figure in the
  already-corroborated §3 country report.

### 1.2 Social requirements (socially acceptable production)

| Requirement | Rule | Legal basis | Confidence | Sources |
|---|---|---|---|---|
| **Socially acceptable production conditions** | Production/cultivation must respect the **social legislation in force at the place of cultivation and production**, **at minimum the ILO core conventions** ("mindestens die Kernübereinkommen der Internationalen Arbeitsorganisation (ILO)") | MinöStG; MinöStV (SR 641.611) | PRIMARY-ONLY (admin.ch, via SECO/BAZG) | S4, S6 |
| **Land rights** | Raw materials may be cultivated **only on land that was lawfully acquired** ("nur auf Flächen erfolgt sein, die rechtmässig erworben wurden") | MinöStV (SR 641.611) | PRIMARY-ONLY | S4, S6 |
| **Assessment / verifier** | **SECO** (State Secretariat for Economic Affairs) directly reviews the credibility of social-criteria compliance ("Die Glaubhaftmachung … der sozialen Kriterien wird direkt vom SECO geprüft") and forwards its finding to BAZG | MinöStG; ETrV/MinöStV | PRIMARY-ONLY | S4, S6 |
| **Form of proof** | A properly completed and signed **self-declaration / sworn personal declaration** (Selbstdeklaration / persönliche Erklärung) is normally sufficient legal proof | MinöStV | PRIMARY-ONLY | S6 |

Note: The dedicated SECO page (`seco.admin.ch/.../Soziale_Kriterien.html`) returned **HTTP 404**
on direct fetch; the wording above is taken from the admin.ch **search index** of that page and
the BAZG renewable-fuels pages. Re-locate the live SECO URL for a clean citation — minor GAP.

---

## 2. The permit / proof procedure (how an operator obtains the relief)

Lead authority for the **tax-relief decision** is **BAZG**; it decides **in agreement with
("im Einvernehmen mit") BAFU and SECO**. BAFU verifies the **ecological** proof; SECO verifies
the **social** proof. A separate, second permit — the **IBTV market-placement authorisation** —
is run by BAFU, but a granted BAZG tax relief **automatically** carries the IBTV placement
permission with it.

### 2.1 Roles

| Authority | Role in the relief/permit chain | Confidence | Sources |
|---|---|---|---|
| **BAZG** (Federal Office for Customs and Border Security) | Owns the application procedure ("Federführung"); issues the producer's **Betriebsbewilligung** (operating authorisation); **formally decides** grant/refusal of the tax relief, in agreement with BAFU + SECO | PRIMARY-ONLY | S2, S4 |
| **BAFU** (FOEN) | Verifies the **ecological requirements** (GHG ≤ threshold, ≤125% total impact, land-use); runs the parallel **IBTV Inverkehrbringen** (market-placement) authorisation | PRIMARY-ONLY | S1, S4 |
| **SECO** | Verifies the **social criteria** (Glaubhaftmachung), forwards finding to BAZG | PRIMARY-ONLY | S4, S6 |

### 2.2 Step-by-step (tax-relief route)

1. **Producer operating authorisation.** A domestic producer needs a **Betriebsbewilligung des
   BAZG** ("operating authorisation") before producing renewable fuel for the relief. (Importers
   without domestic production do not need this, but do file the application below.) `PRIMARY-ONLY` [S2]
2. **File the relief application to BAZG.** Submit the application form + ecological proof form
   (official form: applicant declares fuel type/quality, the **land used**, and the **entire
   production chain from raw-material cultivation to delivery to the consumer**). Where **not all
   input materials appear on the BAZG positive list ("Positivliste BAZG eTS")**, the applicant
   must additionally file **Formular 45.85** ("Gesuch um Steuererleichterung für erneuerbare
   Treibstoffe / Nachweis"). `PRIMARY-ONLY` [S4]
3. **Social self-declaration.** Submit the **Selbstdeklaration** confirming respect for social
   legislation (ILO core conventions) and lawful land acquisition — reviewed by **SECO**. `PRIMARY-ONLY` [S4, S6]
4. **BAFU ecological check.** BAFU verifies the LCA (≥40% GHG saving, ≤125% total impact,
   land-use). `PRIMARY-ONLY` [S1, S4]
5. **BAZG decision "im Einvernehmen."** BAZG grants (or refuses) the relief — up to **full
   exemption, ~75 Rappen/litre depending on product** — in agreement with BAFU + SECO. `PRIMARY-ONLY` [S2, S4]
6. **Automatic IBTV placement permission.** "Eine Bewilligung zur Steuererleichterung des BAZG
   hat automatisch die Bewilligung zur Inverkehrbringung durch das BAFU zur Folge" — a granted
   tax relief **automatically** confers the IBTV market-placement authorisation. `PRIMARY-ONLY` [S1]
7. **Guarantee-of-origin recording.** Record the production/import in the **Pronovo**
   guarantee-of-origin (Herkunftsnachweis) system and cancel/devalue the GO on delivery (§4). `CONFIRMED` [S5]

### 2.3 The prior-approval requirement and the 1 Nov 2025 transition

| Item | Rule | Legal basis | Confidence | Sources |
|---|---|---|---|---|
| **Prior BAFU approval to place on the market** | Before placing a renewable/low-emission fuel on the market (e.g. before import), a **BAFU Bewilligung must be in place** ("muss vor dem Inverkehrbringen … eine Bewilligung des BAFU vorliegen") — unless it flows automatically from a BAZG relief grant | IBTV (SR 814.311.1) | PRIMARY-ONLY (Tier-1 BAFU) | S1 |
| **Transition / grace period** | Renewable or low-emission fuels **could be placed on the market WITHOUT prior BAFU approval until 1 November 2025** ("dürfen bis zum 1. November 2025 ohne vorgängige Bewilligung des BAFU in Verkehr gebracht werden"); **from that date prior IBTV approval is mandatory** | IBTV Übergangsbestimmung | PRIMARY-ONLY (Tier-1 BAFU IBTV, verbatim; single source) | S1 |

The reported "prior BAFU approval required from 1 Nov 2025" is **VERIFIED** against the BAFU IBTV
page (verbatim German quote captured). It remains **PRIMARY-ONLY** (one Tier-1 source; the fedlex
transition article could not be machine-read to confirm the exact article number).

### 2.4 Documentation / proof-of-sustainability an operator must submit

- Ecological proof form: fuel type & quality, **land used**, and **full production process**
  (cultivation → delivery). `PRIMARY-ONLY` [S4]
- **Formular 45.85** where inputs are not fully on the BAZG positive list. `PRIMARY-ONLY` [S4]
- **Social self-declaration** (Selbstdeklaration). `PRIMARY-ONLY` [S4, S6]
- One of the **three IBTV proof pathways** (§5.2). `PRIMARY-ONLY` [S1]
- Records retained for BAFU/BAZG inspection; BAFU contact `ibtv@bafu.admin.ch`. `PRIMARY-ONLY` [S1]

---

## 3. The framework ordinances (SR numbers)

| Ordinance | Full title | SR number | Adopted / in force | Role | Confidence | Sources |
|---|---|---|---|---|---|---|
| **IBTV** | Verordnung über das Inverkehrbringen von erneuerbaren oder emissionsarmen Brenn- und Treibstoffen | **SR 814.311.1** (ELI `eli/cc/2025/250`) | Verordnung of **2 April 2025**, in force **2025** | Market-placement permit + ecological requirements + proof pathways (BAFU-run; CO2 Act/USG route) | PRIMARY-ONLY (SR number from fedlex search index + ELI; text JS-gated) | S1, S3 |
| **ETrV** | Verordnung des UVEK über den Nachweis der Erfüllung der ökologischen Anforderungen an erneuerbare Treibstoffe | **UNCORROBORATED — likely SR 641.611.2x** (successor to the 2009 **TrÖbiV, SR 641.611.21**); one search index cited "641.611.2" | Amended via Annex No. 2 of the 2 April 2025 ordinance; effective 1 Jan 2025 | Proof of ecological requirements for the **MinöStG tax-relief** route (UVEK) | UNCORROBORATED / GAP (Fedlex JS-gated; SR digit not pinned) | S3 |
| **MinöStV** | Mineralölsteuerverordnung | **SR 641.611** | 20 Nov 1996 (amended) | Houses the **social criteria** (ILO, lawful land) and relief mechanics | PRIMARY-ONLY | S6 |
| **MinöStG** | Mineralölsteuergesetz (Art. 12b relief link) | **SR 641.61** | in force | Statutory tax-relief basis; relief limited **by law to 31 Dec 2030** | CONFIRMED (relief sunset, cross-ref §2 country report) | S2 |
| **CO2 Act** | CO2-Gesetz | **SR 641.71** | in force | Anchors USG Art. 35d revision / renewable-fuel promotion | CONFIRMED (cross-ref) | prior report |
| **USG Art. 35d** | Umweltschutzgesetz, Art. 35d | SR 814.01 | rev. via CO2 Act (Parl. 15 Mar 2024) | Statutory eligibility gate + food/feed ban | PRIMARY-ONLY | S1 |

> **Two-ordinance structure — important:** the Swiss regime runs on **two parallel permits**.
> (a) **IBTV (SR 814.311.1)** = the *market-placement* authorisation (BAFU, CO2-Act/USG route),
> mandatory to sell the fuel at all. (b) **ETrV** (UVEK) = the *ecological proof* used for the
> *MinöStG tax-relief* decision (BAZG). Social proof sits in **MinöStV (SR 641.611)** via SECO.
> A granted BAZG relief auto-triggers the IBTV placement permission.

---

## 4. Guarantees of origin / traceability (Pronovo)

| Item | Rule | Legal basis | Confidence | Sources |
|---|---|---|---|---|
| **Mandatory GO recording** | "Seit dem 1. Januar 2025 besteht die gesetzliche **Pflicht**, dass die schweizerische Produktion sowie der Import von erneuerbaren Treib- und Brennstoffen mittels Herkunftsnachweisen … erfasst werden müssen." | CO2 Act / IBTV; Herkunftsnachweis regime | CONFIRMED (Pronovo, Tier-1, verbatim) | S5 |
| **Operator** | **Pronovo AG** operates the Herkunftsnachweis (GO) system | — | CONFIRMED | S5 |
| **Who must register** | Swiss **producers**, **importers**, and **suppliers** delivering to end customers | — | PRIMARY-ONLY | S5 |
| **Recording cadence** | Data entry **monthly, by the 6th of the following month** | Pronovo rules | PRIMARY-ONLY | S5 |
| **Devaluation (Entwertung)** on delivery | For renewable **gases** delivered as fuel: GO must be devalued **by the 25th day of the first month of the following quarter**; GO valid **18 months** from issue month | Pronovo rules | PRIMARY-ONLY | S5 |
| **Mass-balance ↔ tax relief (KEY NUANCE)** | **Mass-balanced** renewable fuels "erhalten aber **keine** Mineralölsteuererleichterung" — i.e. mass-balanced consignments get **NO** mineral-oil-tax relief. The relief route requires **physical/segregated** traceability; mass balance is accepted for **IBTV market placement** but not for the **tax exemption**. | IBTV / Pronovo | PRIMARY-ONLY (Pronovo, verbatim) — **FLAG, cross-check ETrV** | S5 |

> This mass-balance nuance sharpens the earlier report: mass-balance is an IBTV **placement**
> pathway (Art. 3 §5c) but does **not** by itself unlock the **tax relief**. Verify the exact
> boundary in the ETrV text once Fedlex is reachable.

---

## 5. Feedstock restrictions

### 5.1 Categorical food/feed-crop exclusion (KEY FLAG — stronger than EU high-ILUC)

| Rule | Legal basis | Confidence | Sources |
|---|---|---|---|
| Placing on the market of renewable fuels **made from food or feed crops**, or fuels that **directly compete with food production**, is **prohibited** ("Die Inverkehrbringung von erneuerbaren Brenn- und Treibstoffen, welche aus Nahrungs- oder Futtermitteln hergestellt werden, sowie von Brenn- und Treibstoffen, welche die Nahrungsmittelproduktion direkt konkurrenzieren, wird untersagt") | USG Art. 35d; IBTV | CONFIRMED (Tier-1 BAFU IBTV verbatim + USG Art. 35d + BAZG framing) | S1 |
| **Effect:** palm oil, soy oil and other food-crop oils are **effectively excluded** — a categorical **ban**, not a phase-out cap. This is **stronger** than the EU high-ILUC-risk (palm) phase-out, which allows capped/certified volumes. Palm/soy are **not named individually** in the text; the exclusion operates via the food/feed-crop category. | USG Art. 35d | PRIMARY-ONLY (interpretation) | S1 |

### 5.2 Waste/residue feedstocks & proof pathways

| Pathway | Rule | Confidence | Sources |
|---|---|---|---|
| **Positive list (simplified)** | Fuels from **biogenic waste or production residues** on the **BAZG positive list ("Positivliste")**, produced **"nach dem Stand der Technik"** (best available technology), qualify via a **simplified procedure** | PRIMARY-ONLY | S1, S4 |
| **Individual-case application** | Full documentation per IBTV (Art. 4 / Annex 2) | PRIMARY-ONLY | S1 |
| **Mass-balance certification** | Valid certificate + Begleitdokumentation per IBTV Annex 1 (Art. 3 §5c) — accepted for **market placement**; NB **not** for tax relief (§4) | PRIMARY-ONLY | S1, S5 |
| **Off-list inputs** | If inputs are **not fully** on the BAZG positive list, **Formular 45.85** (Nachweis) is additionally required for BAZG review | PRIMARY-ONLY | S4 |

---

## 6. Compliance calendar (operator obligations)

| When | What | To whom | Confidence | Sources |
|---|---|---|---|---|
| **Before market placement** | Obtain BAFU **IBTV** authorisation (or rely on the auto-trigger from a BAZG relief grant). Mandatory since **1 Nov 2025** (grace period ended). | BAFU | PRIMARY-ONLY | S1 |
| **Per application / per new pathway** | File relief application + ecological proof form (+ Formular 45.85 if off-list) + social Selbstdeklaration | BAZG (BAFU ecol., SECO social) | PRIMARY-ONLY | S4, S6 |
| **Producers, before production** | Hold BAZG **Betriebsbewilligung** | BAZG | PRIMARY-ONLY | S2 |
| **Monthly, by the 6th of the following month** | Record production/imports of renewable fuels in the Pronovo GO system | Pronovo AG | PRIMARY-ONLY | S5 |
| **On delivery (gases): by 25th of first month of following quarter** | Devalue (entwerten) the guarantee of origin | Pronovo AG | PRIMARY-ONLY | S5 |
| **Rolling: 18 months** | GO validity — must be cancelled within 18 months of issue | Pronovo AG | PRIMARY-ONLY | S5 |
| **Statutory horizon** | Whole relief regime **sunsets 31 Dec 2030** unless re-extended | (legislature) | CONFIRMED | S2 |

Note: a distinct **annual sustainability report / fixed annual filing deadline** for the tax-relief
route (beyond the per-application proof + monthly Pronovo recording) was **not located** in
primary sources — **GAP**. Penalty for false/insufficient proof: not pinned (MinöStG/USG penal
provisions) — **GAP**.

---

## 7. Draft compliance-checklist items (this slice)

1. **Feedstock is NOT a food/feed crop** and does not directly compete with food production —
   palm and soy effectively banned (USG Art. 35d). `CONFIRMED`
2. **Ecological gate:** demonstrate ≥ **40% lifecycle GHG saving** AND total environmental impact
   **≤125%** of fossil (no more than 25% greater) AND no high-carbon/high-biodiversity land
   conversion, via ecoinvent-based LCA (ETrV/IBTV). `PRIMARY-ONLY`
3. **Social gate:** file the **Selbstdeklaration** — respect for ILO core conventions and lawful
   land acquisition; assessed by **SECO**. `PRIMARY-ONLY`
4. **Producers:** obtain BAZG **Betriebsbewilligung** before production. `PRIMARY-ONLY`
5. **Market placement:** hold BAFU **IBTV** authorisation before placing on the market (mandatory
   since **1 Nov 2025**); a BAZG relief grant confers it automatically. `PRIMARY-ONLY`
6. **Relief application:** submit to **BAZG** (form + ecological proof + Formular 45.85 if inputs
   off the positive list); BAZG decides **im Einvernehmen** with BAFU + SECO. `PRIMARY-ONLY`
7. **Traceability:** relief requires **physical/segregated** proof — **mass-balanced** consignments
   get **no** mineral-oil-tax relief. `PRIMARY-ONLY / FLAG`
8. **Pronovo:** record production/imports **monthly by the 6th**; devalue GO on delivery. `PRIMARY-ONLY`
9. **Horizon:** relief runs **by law to 31 Dec 2030**. `CONFIRMED`

---

## 8. Gaps / follow-ups

- **ETrV SR number** not pinned (Fedlex JS-gated; PDFs undecodable). Likely SR 641.611.2x,
  successor to TrÖbiV (SR 641.611.21). **GAP.**
- **IBTV/ETrV article numbers** for the ≥40% GHG, ≤125% impact, food/feed ban, and the
  1 Nov 2025 transition — verbatim German captured from BAFU, but the exact articles unread
  (Fedlex). **FLAG.**
- **Independent corroboration of the "40%" digit** to a second source (BAFU is Tier-1 primary;
  the country report already corroborated). **Follow-up.**
- **Mass-balance ⇒ no tax relief** — verify the precise ETrV boundary and whether any segregated
  mass-balance variant qualifies. **FLAG.**
- **Live SECO social-criteria URL** (direct fetch 404) — relocate for a clean citation. **GAP.**
- **Annual filing deadline** (if any) and **penalty for non-compliant proof** — not located. **GAP.**
- **BAZG positive list** content not enumerated. **GAP.**

---

## 9. Source log (access date 2026-07-13)

| ID | URL | Tier | Accessed | Supports |
|---|---|---|---|---|
| S1 | https://www.bafu.admin.ch/de/ibtv | 1 | 2026-07-13 | IBTV; ≥40% GHG (verbatim "mindestens 40%"); "höchstens 25 Prozent grösser" (≤125%); land-use verbatim; food/feed ban verbatim; three proof pathways; prior BAFU Bewilligung; **1 Nov 2025** transition verbatim; auto-trigger from BAZG relief; page published 23 Jun 2025 / forms 12 Sep 2025 |
| S2 | https://www.bazg.admin.ch/de/erneuerbare-treibstoffe-mineraloelsteuer | 1 | 2026-07-13 | Relief up to ~75 Rp/L "sofern die ökologischen und sozialen Anforderungen erfüllt sind"; "von Gesetzes wegen bis zum 31. Dezember 2030 befristet"; producer **Betriebsbewilligung des BAZG**; Hersteller/Importeure must prove compliance |
| S3 | https://www.fedlex.admin.ch/eli/cc/2025/250/de (+ fedlex search index) | 1 | 2026-07-13 | IBTV **SR 814.311.1**, Verordnung 2 April 2025 (JS-gated — SR/ELI from search index; body not rendered). ETrV = UVEK ordinance on ecological-requirement proof (SR digit unpinned) |
| S4 | BAZG "Erneuerbare Treibstoffe" (bazg.admin.ch/bazg/de/.../erneuerbare-treibstoffe.html) + admin.ch search index | 1 | 2026-07-13 | BAZG Federführung; decides "im Einvernehmen mit BAFU und SECO"; SECO prüft soziale Kriterien; **Formular 45.85**; Positivliste BAZG eTS; ecological proof form (fuel type, land, full production chain) |
| S5 | https://pronovo.ch/de/herkunftsnachweise/erneuerbare-treib-und-brennstoffe-bt/ | 1 | 2026-07-13 | GO **Pflicht seit 1.1.2025** (verbatim); producers/importers/suppliers register; **monthly by the 6th**; Entwertung by 25th of first month of following quarter; 18-month validity; **mass-balanced fuels get NO tax relief** (verbatim) |
| S6 | SECO "Soziale Kriterien" (seco.admin.ch/.../Soziale_Kriterien.html — direct 404) via admin.ch search index; MinöStV SR 641.611 | 1 | 2026-07-13 | Social criteria = ILO core conventions + lawful land acquisition; **Selbstdeklaration** sufficient proof; SECO reviews Glaubhaftmachung |
| S7 | https://www.newsd.admin.ch/newsd/message/attachments/92722.pdf ; /88455.pdf | 1 | 2026-07-13 | Official IBTV ordinance PDFs — **did not decode** (compressed; no poppler). Logged as attempted. |
| S8 | Prior team report `research/reports/CH-country-report-2026-07-04.md` §2–§3 | (internal) | 2026-07-13 | Cross-ref: relief to 31 Dec 2030 CONFIRMED; ecoinvent LCA; framing |

---

## 4-line summary

1. **Ecological gate:** ≥40% lifecycle GHG saving vs fossil AND total environmental impact ≤125%
   ("höchstens 25% grösser") AND no high-carbon/high-biodiversity land conversion — USG Art. 35d /
   IBTV (SR 814.311.1) / ETrV, verified verbatim from BAFU (PRIMARY-ONLY).
2. **Social gate:** production must meet ILO core conventions + lawful land acquisition, proven by
   a Selbstdeklaration and assessed by **SECO** (MinöStV SR 641.611) — PRIMARY-ONLY.
3. **Permit/prior-approval:** BAZG grants the relief "im Einvernehmen" with BAFU (ecological) and
   SECO (social) and issues producer Betriebsbewilligungen; separate BAFU **IBTV** market-placement
   approval is mandatory since **1 Nov 2025** (grace period ended) and is auto-conferred by a relief
   grant; Pronovo GO recording mandatory since 1 Jan 2025 — mass-balanced consignments get **no**
   relief (FLAG). Relief sunsets 31 Dec 2030.
4. **Feedstock exclusion:** categorical **ban** on fuels from food/feed crops or that directly
   compete with food production — effectively excludes **palm and soy**, stronger than the EU
   high-ILUC phase-out (CONFIRMED); Fedlex JS-gated so ETrV SR number and article numbers remain a GAP.
