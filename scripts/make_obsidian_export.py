#!/usr/bin/env python3
"""
Generate an Obsidian-ready copy of the biofuel report.

Reads:  research/germany-biofuel-blending-volumes.md
Writes: Vault/Germany Biofuel Blending Volumes.md
        (YAML frontmatter + wikilinks/tags, then the report body)

Run after updating the report so the vault copy stays in sync:
  python3 scripts/make_obsidian_export.py
Then copy Vault/*.md into your Obsidian vault.
"""
import os, re, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "research", "germany-biofuel-blending-volumes.md")
DST = os.path.join(HERE, "..", "Vault", "Germany Biofuel Blending Volumes.md")

FRONTMATTER = """---
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
latest_data: "{latest_data}"
sources_primary:
  - BAFA Amtliche Mineralöldaten (monthly, tonnes)
  - BLE Evaluations- und Erfahrungsbericht (annual, energy)
created: 2026-07-08
updated: "{updated}"
---

> [!info] Related
> [[BAFA]] · [[BLE]] · [[THG-Quote]] · [[HVO]] · [[FAME]] · [[Bioethanol]] · [[Biomethane]] · [[ReFuelEU Aviation]]
> Machine-readable data: `research/data/bafa-monthly-blending.csv`

"""


def latest_data_month():
    csv = os.path.join(HERE, "..", "research", "data", "bafa-monthly-blending.csv")
    try:
        rows = [l for l in open(csv).read().splitlines()[1:] if l.strip()]
        y, m = rows[-1].split(",")[0], int(rows[-1].split(",")[1])
        return f"{y}-{m:02d}"
    except Exception:
        return "2026-04"


def main():
    body = open(SRC, encoding="utf-8").read()
    # drop the H1 title line — Obsidian uses the filename/frontmatter title
    body = re.sub(r"^# .*\n", "", body, count=1)
    today = datetime.date.today().isoformat()
    fm = FRONTMATTER.format(latest_data=latest_data_month(), updated=today)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(fm + body)
    print(f"Wrote {os.path.normpath(DST)} (latest data {latest_data_month()})")


if __name__ == "__main__":
    main()
