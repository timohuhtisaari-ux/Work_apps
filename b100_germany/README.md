# B100 Germany sales calculator (2026)

`python3 b100_calc.py` prints a per-litre price build-up for B100 vs fossil diesel:
product, logistics/margin, energy tax (47.04 ct/L), BEHG CO2 price (0 for certified
biodiesel), THG-Quote credit/cost, and 19% VAT. Every input is a CLI flag, e.g.

    python3 b100_calc.py --b100-ci 45 --b100-product 1.00   # RME case
    python3 b100_calc.py --quota-price 200                  # lower quota market

Default assumptions (Sep 2026): quota 12% (2026), quota price 320 EUR/t CO2e,
CO2 price 60 EUR/t, baseline 94.1 gCO2e/MJ, UCOME 12 gCO2e/MJ, 33 MJ/L B100.
Product prices are placeholders; replace with your own quotes.
