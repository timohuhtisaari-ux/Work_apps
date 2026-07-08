#!/usr/bin/env python3
"""
Extract Germany's monthly biofuel blending volumes from BAFA's
'Amtliche Mineralöldaten' (Table 9: "Beimischung von Biozusatzstoffen in
Mineralölprodukten im Inland").

BAFA publishes one PDF per reporting month at:
  https://www.bafa.de/SharedDocs/Downloads/DE/Energie/Mineraloel/moel_amtliche_daten_<EDITION>.pdf
where <EDITION> is e.g. "2025_01" (zero-padded in 2025) or "2026_1" (not padded in 2026).

Some 2026 editions use a subset font whose glyph codes are the intended
character minus 29; this script auto-detects that and de-shifts.

Usage:
  python3 extract_bafa_blending.py                 # probe all months 2025->now, write CSV
  python3 extract_bafa_blending.py 2026_4          # print one edition as JSON
Output CSV: research/data/bafa-monthly-blending.csv

NOTE: BAFA reports only LIQUID mineral-oil products and their liquid
biocomponents. Gaseous fuels (biomethane, Bio-LNG/LNG, Bio-CNG/CNG) are NOT
in this statistic — see the report's gaseous-fuels section for sources.
"""
import re, sys, json, os, urllib.request

BASE = "https://www.bafa.de/SharedDocs/Downloads/DE/Energie/Mineraloel/moel_amtliche_daten_{}.pdf?__blob=publicationFile"
HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "..", "research", "data", "bafa-monthly-blending.csv")

# Each label pattern ends positioned just before the numeric columns. The
# "combined" line label is "…und andere Biozusätze"; in some 2026 editions the
# ä decodes to a stray control char, so we use \S* (not \w*) and swallow any
# non-numeric separators before the digits.
LABELS = [
    ("etbe",     r"Bioethanol an ETBE\s*a?\)?\s+"),
    ("ethanol",  r"Bioethanol\s+"),
    ("combined", r"Biozus\S*tze[^\d+-]*"),
    ("hvo",      r"davon HVO\s+"),
    ("fame",     r"davon FAME\s+"),
    ("biokerosin", r"Biokerosin\s+"),
]


def deshift(t):
    return "".join(chr(ord(c) + 29) if ord(c) < 0x2000 else c for c in t)


def to_int(s):
    s = s.strip().replace("−", "-")
    if s in ("", "-", "="):
        return None
    neg = s.startswith("-")
    s = s.replace("+", "").replace("-", "").replace(".", "")
    return -int(s) if (neg and s.isdigit()) else (int(s) if s.isdigit() else None)


def fetch(edition):
    url = BASE.format(edition)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
    except Exception:
        return None
    if not data.startswith(b"%PDF"):
        return None  # 404 pages come back as HTML
    return data


def parse_pdf(data):
    from pypdf import PdfReader
    import io
    r = PdfReader(io.BytesIO(data))
    for shift in (False, True):
        tab = None
        for p in r.pages:
            t = p.extract_text() or ""
            if shift:
                t = deshift(t)
            t = t.replace("\xa0", " ")
            if "Bioethanol an ETBE" in t and "davon FAME" in t:
                tab = t
        if tab:
            break
    if not tab:
        return None
    flat = re.sub(r"[=\n]+", " ", tab)
    rec = {}
    for key, lbl in LABELS:
        m = re.search(lbl + r"((?:[+-]?[\d\.]+\s*){1,6})", flat)
        if m:
            nums = re.findall(r"[+-]?[\d\.]+", m.group(1))
            rec[key + "_month"] = to_int(nums[0]) if nums else None
    return rec


def editions_to_probe():
    eds = [f"2025_{m:02d}" for m in range(1, 13)]
    eds += [f"2026_{m}" for m in range(1, 13)]
    return eds


def main():
    if len(sys.argv) > 1:
        data = fetch(sys.argv[1])
        print(json.dumps(parse_pdf(data) if data else {"error": "not found"}, indent=2))
        return
    rows = []
    for ed in editions_to_probe():
        data = fetch(ed)
        if not data:
            continue
        rec = parse_pdf(data)
        if not rec:
            continue
        yr, mo = ed.split("_")
        fame = rec.get("fame_month")
        hvo = rec.get("hvo_month")
        comb = rec.get("combined_month")
        btl = (comb - fame - hvo) if None not in (comb, fame, hvo) else None
        rows.append({
            "year": yr, "month": int(mo), "edition": ed,
            "fame_t": fame, "hvo_t": hvo, "btl_other_t": btl,
            "biodiesel_family_t": comb,
            "bioethanol_direct_t": rec.get("ethanol_month"),
            "ethanol_in_etbe_t": rec.get("etbe_month"),
            "biokerosin_t": rec.get("biokerosin_month"),
        })
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    cols = ["year", "month", "edition", "fame_t", "hvo_t", "btl_other_t",
            "biodiesel_family_t", "bioethanol_direct_t", "ethanol_in_etbe_t", "biokerosin_t"]
    with open(CSV_PATH, "w") as f:
        f.write(",".join(cols) + "\n")
        for r in rows:
            f.write(",".join("" if r[c] is None else str(r[c]) for c in cols) + "\n")
    print(f"Wrote {len(rows)} months to {os.path.normpath(CSV_PATH)}")
    print(f"Latest edition: {rows[-1]['edition'] if rows else 'none'}")


if __name__ == "__main__":
    main()
