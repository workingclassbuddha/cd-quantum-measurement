# Product-Law Readiness Audit

Verdict: G12 blocked: no empirical independent-factor product-law dataset

This audit asks whether the current public empirical artifacts can validate:

```text
kappa_eff = kappa0 * Lambda * Gamma * Theta
```

It deliberately separates empirical readiness from the synthetic identifiability benchmark. A synthetic benchmark can define the target design, but it cannot validate G12.

## Empirical Dataset Scan

- CSV datasets scanned: 16
- Datasets with complete product-law rows: 0
- Empirical product-law-ready datasets: 0

Top blockers:

- missing Lambda/Gamma/Theta columns: 14
- Lambda/Gamma/Theta columns are empty or unpaired to visibility: 2

## Synthetic Benchmark

- Synthetic benchmark rows: 63
- Balanced synthetic product delta AICc: 0.0
- Balanced synthetic max factor correlation: 6.644793704683637e-16

The balanced synthetic benchmark says the scaffold can recognize a product-law-shaped design when the factors are independently varied. The confounded synthetic benchmark says the opposite danger is real: a single latent load can look excellent under a product term while Lambda, Gamma, and Theta are not separately identifiable.

## Needed Before G12 Can Pass

1. Independently varied Lambda, Gamma, and Theta factors.
2. Low factor correlation and acceptable VIF.
3. Held-out factor-combination prediction against additive, pairwise, and background alternatives.
4. Provenance showing the factors were measured or set by apparatus controls, not inferred from the same visibility curve.

## Boundary

- This does not validate the product law.
- This does not affect the Xiao/Kokorowski no-refit distribution gates.
- This keeps G12 failed until an empirical independent-factor dataset exists.
