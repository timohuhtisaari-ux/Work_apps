# Spain — Royal Decree 611/2026 analysis (impact on the ES country card)

- **Instrument:** Real Decreto 611/2026, de 22 de julio, *de impulso a la
  descarbonización del sector del transporte y fomento de los combustibles
  renovables* — BOE-A-2026-16011, published 23 Jul 2026.
- **Analysed:** 2026-08-04 · Sources accessed live (Tier-1 BOE consolidated text;
  Tier-2 PwC Periscopio Fiscal y Legal corroboration).
- **Confidence:** headline trajectory + entry into force **CONFIRMED**
  (BOE primary + PwC independent); 2030 road value 17.6 % **CONFIRMED (primary
  text)**, endpoints (8.5 % 2027 / 30 % 2040) independently corroborated;
  penalty amounts **GAP** (not extracted); infringement-closure status
  **UNVERIFIED**.

## What RD 611/2026 does

1. **Regime change: energy quotas → GHG-intensity reduction.** From
   **1 Jan 2027** the SICBIOS energy-content obligation (14 % in 2026 under
   RD 5/2026) is superseded by a **modal GHG-emission-reduction framework**
   (fossil comparator 94 gCO₂eq/MJ), running **2027–2040** (art. 4.1).
2. **Road transport trajectory (art. 9):** 8.5 % (2027) → 11 % (2028) →
   14 % (2029) → **17.6 % (2030)** → … → **30 % (2040)**.
3. **Sub-targets, road (art. 10, energy content):** advanced biofuels + biogas
   + RFNBO combined **4 % (2027) → 5.5 % (2030) → 11 % (2040)**; RFNBO minimum
   **0.2 % (2027) → 0.7 % (2028) → 1.5 % (2029) → 2.5 % (2030) → 6 % (2035) →
   11 % (2040)**.
4. **Other modes:** maritime cabotage GHG cut 6.5 % (2027) → 9 % (2030) →
   33 % (2040) + renewables share 2 %/7 %/20 %; non-electrified rail GHG cut
   6 % (2027) → 10 % (2030) → 50 % (2040); aviation handled via ReFuelEU
   (excluded from national calculus).
5. **Institutions:** Secretaría de Estado de Energía is the certification
   entity; obligated parties are fuel suppliers per mode; new *sujetos
   habilitados* (incl. renewable-H2 / e-fuel producers) can generate credits;
   renewable-electricity-to-EV credits introduced.
6. **RED III transposition:** transposes (partially) arts. 2, 19, 25, 26, 27,
   29 bis, 30, 31 bis + Annex IX of Dir. (EU) 2018/2001 as amended by
   **Dir. (EU) 2023/2413 (RED III)**, plus Del. Dir. 2024/1405 (Annex IX
   amendment) and Dir. 2024/1788 provisions.
7. **Housekeeping:** derogates RD 1085/2015 (from 1 Jan 2027); narrows
   RD 376/2022 to biofuel sustainability criteria; new GHG methodology in
   Annex III.

## Impact on the ES map card (current vs proposed)

| Field | Current card | Change needed |
|---|---|---|
| type | `energy` (SICBIOS 14 %) | **Keep `energy` for 2026** (operative year unchanged) — flip to `ghg` on 1 Jan 2027 |
| level | "SICBIOS certificates — 14 % (raised from 12 % by RD 5/2026)" | Add: final year of the energy-quota system |
| target | "14 % rolls forward (GHG-model draft PROPOSED)" | **Obsolete** — GHG model now ADOPTED: 8.5 % (2027) → 17.6 % (2030) → 30 % (2040) |
| adv | "1.2 % → 3.5 %" | Replace 2030 leg with RD 611/2026 values: adv+biogas+RFNBO 4 % (2027) → 5.5 % (2030); RFNBO min 0.2 % → 2.5 % |
| status | "NOT transposed — reasoned opinions Feb & Dec 2025" | **Materially changed**: transport transposition adopted 22 Jul 2026, applies 1 Jan 2027 |
| st | `serious` (reasoned opinion) | Keep `serious` until Commission case-closure is verified (adoption ≠ closure) |
| flag | "Temporary excise cuts below ETD minima (Jul–Sep 2026)" | Keep (still current in Aug 2026) + add: infringement-closure unverified; penalty amounts GAP |

## Proposed replacement mapcard

```mapcard
{"iso":"ES","name":"Spain","eu":true,"type":"energy","st":"serious","short":"14% → GHG 2027","level":"SICBIOS certificates — 14% energy content (raised from 12% by RD 5/2026); FINAL YEAR of the energy-quota system — RD 611/2026 switches Spain to modal GHG-intensity targets from 1 Jan 2027","target":"RD 611/2026 (BOE 23 Jul 2026): road GHG-intensity cut 8.5% (2027) → 17.6% (2030) → 30% (2040); maritime cabotage 9%, rail 10% by 2030; aviation via ReFuelEU","adv":"1.2% (2026); from 2027 adv.+biogas+RFNBO 4% → 5.5% (2030) → 11% (2040), RFNBO min 0.2% → 2.5% (2030)","tax":"No — bioethanol/biodiesel track the petrol/diesel epigraphs","cert":"EU schemes + SNVS; SICBIOS (to 2026) → Secretaría de Estado de Energía certification system with tradable credits incl. renewable-electricity and H2/e-fuel credits (from 2027)","status":"RED III transport transposition ADOPTED — RD 611/2026 in force 1 Jan 2027 (obligations 2027–2040), replacing the energy-quota system; Feb & Dec 2025 reasoned opinions predate it","flag":"Temporary excise cuts below ETD minima (Jul–Sep 2026); closure of the RED III infringement not yet verified; RD 611/2026 penalty amounts not yet extracted (GAP)"}
```

**Follow-ups for the weekly monitor:** (1) verify whether the Commission closes
INFR reasoned opinions after notification — until then `st` stays `serious`;
(2) on 1 Jan 2027 flip `type` → `ghg` and make the 8.5 % target the headline;
(3) extract the pago compensatorio / sanction amounts from Título IV.

## Sources

| Source | Tier | Access date |
|---|---|---|
| BOE-A-2026-16011 — RD 611/2026 full text, https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-16011 | 1 | 2026-08-04 |
| PwC Periscopio Fiscal y Legal — "Real Decreto 611/2026: principales medidas regulatorias en materia energética", https://periscopiofiscalylegal.pwc.es/real-decreto-611-2026-principales-medidas-regulatorias-en-materia-energetica/ | 2 | 2026-08-04 |
| Interempresas — "El Gobierno fija la hoja de ruta para implementar los combustibles renovables en el transporte" (headline corroboration), https://www.interempresas.net/Estaciones-servicio/659532-Real-Decreto-611-2026-fija-desde-2027-objetivos-combustibles-renovables-descarbonizacion.html | 2 | 2026-08-04 (index) |
