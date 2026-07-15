# Global expansion queue — world biofuel regulation map

The global research team works through this queue batch by batch, and
re-scans DONE markets for changes on every run. Maintained by
`/global-fuels-research` (see `.claude/skills/global-fuels-research/SKILL.md`).

Status legend: **DONE** (in map, corroborated) · **DRAFT** (researched, awaiting
corroboration/integration) · **QUEUED** · **—** (not yet scheduled)

## Completed markets (change-monitor these on every run)

| Market | Status | Report | Last verified |
|---|---|---|---|
| EU-27 | DONE | `research/reports/<ISO2>-country-report-2026-07-04.md` | 2026-07-04 |
| Norway, UK, Switzerland | DONE | same series + `non-eu-states.md` | 2026-07-04 |
| United States (federal + state) | DONE | `us-lcfs`/`us-blend-mandates` drafts | 2026-07-13 |
| Canada (federal + provincial) | DONE | `canada-biofuel` draft | 2026-07-13 |

## Batch 1 — South America + Southeast/East Asia (completed 2026-07-15, corroborated)

| Country | ISO | Status |
|---|---|---|
| Brazil | BR | DONE |
| Argentina | AR | DONE |
| Paraguay | PY | DONE |
| Chile | CL | DONE |
| Peru | PE | DONE |
| Colombia | CO | DONE |
| Indonesia | ID | DONE |
| Malaysia | MY | DONE |
| Philippines | PH | DONE |
| Thailand | TH | DONE |
| Vietnam | VN | DONE |
| Singapore | SG | DONE |
| South Korea | KR | DONE |

## Batch 2 — completed 2026-07-16, corroborated (map: 45 → 53 markets)

| Country | ISO | Status |
|---|---|---|
| India | IN | DONE |
| China | CN | DONE |
| Japan | JP | DONE |
| Australia | AU | DONE |
| Mexico | MX | DONE |
| Uruguay | UY | DONE |
| Bolivia | BO | DONE |
| Ecuador | EC | DONE |

## Batch 3 — next up (QUEUED for the weekly Routine)

Guatemala/Costa Rica/Panama (Central America), Türkiye, South Africa,
Kenya, Nigeria, Zimbabwe/Zambia (E10-E15 mandates), UAE/Saudi Arabia (SAF),
Taiwan, New Zealand, Pakistan, Bangladesh.

## Geometry notes for map integration

Numeric world-atlas IDs already mapped in the master map build for batch 1.
For batch 2+: IN 356, CN 156, JP 392, AU 36, UY 858, BO 68, EC 218, MX 484,
TR 792, ZA 710, KE 404, NG 566, TW 158, NZ 554, PK 586, BD 50. Small city
states (like SG) need a marker — see `WORLD.markers` in the build script.
