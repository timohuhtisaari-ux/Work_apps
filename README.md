# Work_apps

## Low-Carbon Fuel CRM (`efuel-crm/`)

A lightweight, single-file CRM / monitoring tool for following up with low-carbon fuel
producers — e-fuels/RFNBO and biofuels alike. No server, no build step — open
`efuel-crm/index.html` in any browser. Data is stored locally in the browser
(localStorage), with JSON export/restore for backups.

### Features

**Producers (relationship tracking)**
- Contact information (person, role, email, phone), country, products, notes,
  and a **responsible person** (with autocomplete and a filter).
- **Pipeline stages** for B2B partnership/offtake work: Identified → Contacted →
  In dialogue → Evaluation → Term negotiation → Agreement signed, plus Paused / No fit.
  Legacy status values (Active/Prospect/On hold/Dormant) migrate automatically.
- **Discussion log** per producer; the latest entry shows as "last discussion", and
  contacts silent for more than 30 days get a **stale** flag.
- **Next step + deadline** per producer with a **✓ Done** action that logs the
  completed step into the history and prompts for the next one.

**Filtering & navigation**
- **Product filter**: family chips (All / E-fuels / Biofuels) plus a product dropdown
  with a 12-category taxonomy (Renewable H2, e-methanol, e-ammonia, e-SAF, e-methane,
  e-diesel, bio-methanol, bio-SAF, HVO, biomethane/bio-LNG, ethanol, biodiesel).
  Free-text product names and linked projects are matched to categories automatically.
  The filter is shared across the Producers and Projects tabs.
- Stage, responsible-person and phase filters, full-text search (incl. notes and
  discussion history), result counts, and filters that persist across reloads.

**Reminders**
- Header bell with due/late badge; reminder list grouped Overdue / Due today /
  Due within 7 days with Open, ✓ Done, and +1 week actions; a once-a-day nudge toast;
  and `.ics` calendar export of upcoming deadlines (09:00 alarms).

**Projects**
- Project register: product, capacity (kt/a), electrolyzer MW where relevant,
  COD year, phase — linked to producers.
- **Phase-count chips** (Concept … Operating) that double as filters, plus sort by
  COD, capacity, name or producer.
- **JSON import** (e.g. from the RFNBO model): flexible field mapping, preview with
  per-row selection, automatic producer creation ("Identified" stage) and linking.
  `efuel-crm/rfnbo-projects-import.json` contains a ready 136-project database
  exported from the RFNBO Fuel Availability Model.

**Data**
- JSON backup export/restore, plus **CSV export** of the filtered producer or project
  list for Excel.

### Import format

The importer accepts a single project object, an array, or `{"projects": [...]}`.
Common field-name variants are recognized (case/spacing insensitive), e.g. `project/
name/title`, `producer/company/developer`, `product/fuel` (codes like `emethanol` are
prettified), `capacity_kta/capacityKtPerYear`, `electrolyzer_mw`, `cod/start_year`,
`phase/status`, `notes`.
