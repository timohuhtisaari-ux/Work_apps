# Work_apps

## E-Fuel Producer CRM (`efuel-crm/`)

A lightweight, single-file CRM / monitoring tool for following up with e-fuel & RFNBO
producers. No server, no build step — open `efuel-crm/index.html` in any browser.
Data is stored locally in the browser (localStorage), with JSON export/restore for backups.

### Features

- **Producers** — contact information (person, role, email, phone), status
  (Active / Prospect / On hold / Dormant), products, general notes, and a
  **responsible person** (who on your side owns the follow-up), with a
  responsible-person filter in the producer list.
- **Discussion log** — log every call/meeting with date and summary; the latest entry
  shows as "last discussion" in the overview.
- **Next steps & deadlines** — free-text next steps with a deadline per producer.
  Overdue deadlines are flagged red, deadlines within 7 days amber.
- **Monitoring dashboard** — KPI strip: producers tracked, overdue follow-ups,
  follow-ups due within 7 days, RFNBO projects.
- **Reminders** — a bell in the header (with a badge for due/late counts) opens a
  reminder list grouped into Overdue / Due today / Due within 7 days, each with the
  responsible person, quick "Open" and "+1 wk" postpone actions. A once-a-day toast
  nags when something is due or late, and upcoming deadlines can be exported as an
  `.ics` calendar file (with 09:00 alarms) for Outlook/Google Calendar.
- **RFNBO projects** — track projects (product, capacity kt/a, electrolyzer MW,
  COD year, phase) linked to producers.
- **Import from RFNBO model** — paste or upload a JSON export from the RFNBO model;
  fields are mapped automatically, a preview lets you pick which projects to import,
  and producers named in the file are created and linked automatically.
- **Backup** — export/restore the full dataset as JSON.

### RFNBO model import format

The importer accepts a single project object, an array, or `{"projects": [...]}`.
Common field-name variants are recognized (case/spacing insensitive), e.g.:

```json
[
  {
    "project": "Havvind e-Methanol Phase 1",
    "producer": "Nordlys eFuels",
    "country": "Norway",
    "product": "e-Methanol",
    "capacity_kta": 80,
    "electrolyzer_mw": 120,
    "cod": 2028,
    "phase": "FEED",
    "notes": "Offshore wind PPA under negotiation"
  }
]
```

Recognized aliases include `name/title` for project, `company/developer/owner` for
producer, `fuel/output` for product, `capacity/annual_capacity` for capacity,
`electrolyser_mw/mw_el` for electrolyzer size, and `start_year/startup` for COD.
