#!/usr/bin/env python3
"""B100 (pure biodiesel / FAME) sales economics in Germany, 2026.

Builds up the price of one litre of B100 sold for road use, and compares it with
fossil diesel: product cost, energy tax (EnergieStG), national CO2 price (BEHG),
GHG quota (THG-Quote, §37a BImSchG) and VAT.

All inputs are in the PARAMS dict or can be overridden on the command line, e.g.
    python3 b100_calc.py --quota-price 250 --b100-product 1.20
"""

import argparse

PARAMS = {
    # --- Market inputs (EUR per litre, excl. taxes) -- adjust to your quotes ---
    "b100_product": 1.10,     # FAME ex-works/ex-tank, WITHOUT quota value
    "diesel_product": 0.70,   # fossil diesel ex-refinery, excl. tax/CO2/quota
    "logistics_margin": 0.10, # freight, storage, retail margin (both fuels)

    # --- Taxes ---
    "energy_tax": 0.4704,     # EUR/L, §2(1) Nr.4 EnergieStG, same for FAME and diesel
    "vat": 0.19,
    "co2_price": 60.0,        # EUR/t, BEHG/nEHS 2026 corridor 55-65
    "diesel_co2_kg_per_l": 2.65,  # BEHG emission factor diesel (~74.1 t/TJ)
    # Sustainable (certified) biodiesel has emission factor 0 under BEHG.

    # --- GHG quota (THG-Quote) ---
    "quota_pct": 0.12,        # 2026 obligation (17.5% in 2027, 26.5% in 2030)
    "quota_price": 320.0,     # EUR/t CO2e, market Aug 2026 ~308-338
    "fossil_ref": 94.1,       # gCO2e/MJ, German baseline (Basiswert)
    "b100_ci": 12.0,          # gCO2e/MJ: UCOME ~10-15, RME ~40-50
    "b100_mj_per_l": 33.0,    # RED III Annex III
    "diesel_mj_per_l": 36.0,
}


def quota_tonnes_per_litre(p):
    """Net tradeable GHG reduction (t CO2e) per litre of B100.

    Selling B100 creates its own obligation (quota% of baseline) and delivers
    the reduction baseline - actual; the surplus is what can be sold or used to
    cover fossil volumes.
    """
    mj = p["b100_mj_per_l"]
    gross = mj * (p["fossil_ref"] - p["b100_ci"])
    obligation = mj * p["fossil_ref"] * p["quota_pct"]
    return (gross - obligation) / 1e6, gross / 1e6


def diesel_quota_cost_per_litre(p):
    """Compliance cost a fossil diesel seller carries (t CO2e x price)."""
    t = p["diesel_mj_per_l"] * p["fossil_ref"] * p["quota_pct"] / 1e6
    return t * p["quota_price"]


def build(p):
    net_t, gross_t = quota_tonnes_per_litre(p)
    quota_credit = net_t * p["quota_price"]

    b100 = {
        "Product (ex quota)": p["b100_product"],
        "Logistics / margin": p["logistics_margin"],
        "Energy tax": p["energy_tax"],
        "CO2 price (BEHG)": 0.0,
        "THG quota": -quota_credit,
    }
    diesel = {
        "Product (ex quota)": p["diesel_product"],
        "Logistics / margin": p["logistics_margin"],
        "Energy tax": p["energy_tax"],
        "CO2 price (BEHG)": p["co2_price"] * p["diesel_co2_kg_per_l"] / 1000,
        "THG quota": diesel_quota_cost_per_litre(p),
    }
    for d in (b100, diesel):
        d["Net (excl. VAT)"] = sum(d.values())
        d["VAT"] = d["Net (excl. VAT)"] * p["vat"]
        d["Pump price (gross)"] = d["Net (excl. VAT)"] + d["VAT"]
    return b100, diesel, net_t, gross_t


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for k, v in PARAMS.items():
        ap.add_argument("--" + k.replace("_", "-"), type=float, default=v)
    p = vars(ap.parse_args())

    b100, diesel, net_t, gross_t = build(p)
    energy_ratio = p["b100_mj_per_l"] / p["diesel_mj_per_l"]

    print(f"THG saving per litre B100: gross {gross_t*1000:.2f} kg, "
          f"net of own obligation {net_t*1000:.2f} kg CO2e "
          f"(CI {p['b100_ci']:.0f} g/MJ, quota {p['quota_pct']:.1%})")
    print(f"Quota value at {p['quota_price']:.0f} EUR/t: "
          f"{net_t*p['quota_price']:.3f} EUR/L\n")

    print(f"{'EUR per litre':<22}{'B100':>10}{'Diesel':>10}")
    for k in b100:
        if k in ("Net (excl. VAT)", "Pump price (gross)"):
            print("-" * 42)
        print(f"{k:<22}{b100[k]:>10.3f}{diesel[k]:>10.3f}")

    b_gross, d_gross = b100["Pump price (gross)"], diesel["Pump price (gross)"]
    print(f"\nPer diesel-equivalent litre (energy {energy_ratio:.1%} of diesel):")
    print(f"  B100 {b_gross/energy_ratio:.3f}  vs  diesel {d_gross:.3f} EUR")

    # Break-even B100 product price for parity on energy basis
    target_net = d_gross * energy_ratio / (1 + p["vat"])
    others = b100["Net (excl. VAT)"] - b100["Product (ex quota)"]
    print(f"\nBreak-even B100 product price (energy parity): "
          f"{target_net - others:.3f} EUR/L "
          f"(~{(target_net - others)/0.883*1000:.0f} EUR/t)")

    print("\nSensitivity: B100 pump price (EUR/L) by quota price")
    for qp in (100, 200, 320, 400):
        b, _, _, _ = build({**p, "quota_price": qp})
        print(f"  {qp:>4} EUR/t -> {b['Pump price (gross)']:.3f}")


if __name__ == "__main__":
    main()
