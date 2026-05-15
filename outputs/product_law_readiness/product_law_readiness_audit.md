# Product-Law Readiness Audit

Verdict: G12 blocked: no empirical independent-factor product-law dataset

This audit asks whether the current public empirical artifacts can validate:

```text
kappa_eff = kappa0 * Lambda * Gamma * Theta
```

It deliberately separates empirical readiness from the synthetic identifiability benchmark. A synthetic benchmark can define the target design, but it cannot validate G12.

## Empirical Dataset Scan

- CSV datasets scanned: 19
- Datasets with complete product-law rows: 0
- Empirical product-law-ready datasets: 0
- Partial apparatus-proxy candidates: 14
- Proxy-rich apparatus candidates: 2
- Named proxy-rich blockers: 2

Top blockers:

- missing Lambda/Gamma/Theta columns: 17
- Lambda/Gamma/Theta columns are empty or unpaired to visibility: 2

Top proxy candidates:

- CHAPMAN_1995_SCATTER.csv: proxy-rich but formal factors missing or confounded; proxy_axes=3; blocker=Lambda/Gamma/Theta columns are empty or unpaired to visibility
- CHAPMAN_1995_SCATTER_DIGITIZED.csv: proxy-rich but formal factors missing or confounded; proxy_axes=3; blocker=Lambda/Gamma/Theta columns are empty or unpaired to visibility
- KOKOROWSKI_2001_FIG3_DECAY_THEORY_CURVES.csv: single/partial apparatus-control proxy; proxy_axes=2; blocker=missing Lambda/Gamma/Theta columns
- HORNBERGER_2003_COLLISIONAL_SCOUT.csv: single/partial apparatus-control proxy; proxy_axes=2; blocker=missing Lambda/Gamma/Theta columns
- KOKOROWSKI_2001_FIG3_DECAY_DIGITIZED.csv: single/partial apparatus-control proxy; proxy_axes=2; blocker=missing Lambda/Gamma/Theta columns
- KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv: single/partial apparatus-control proxy; proxy_axes=2; blocker=missing Lambda/Gamma/Theta columns

Candidate blocker details:

- CHAPMAN_1995_SCATTER.csv: missing_axes=none; closure_gap=proxy-rich candidate lacks formal independently measured Lambda/Gamma/Theta rows and held-out product-law comparison; next=provenance map from proxy controls to Lambda/Gamma/Theta plus low-confounding held-out validation
- CHAPMAN_1995_SCATTER_DIGITIZED.csv: missing_axes=none; closure_gap=proxy-rich candidate lacks formal independently measured Lambda/Gamma/Theta rows and held-out product-law comparison; next=provenance map from proxy controls to Lambda/Gamma/Theta plus low-confounding held-out validation
- KOKOROWSKI_2001_FIG3_DECAY_THEORY_CURVES.csv: missing_axes=Gamma; closure_gap=partial apparatus-control candidate is missing Gamma axis; next=add independent controls for the missing product-law axes before testing held-out predictions
- HORNBERGER_2003_COLLISIONAL_SCOUT.csv: missing_axes=Lambda; closure_gap=partial apparatus-control candidate is missing Lambda axis; next=add independent controls for the missing product-law axes before testing held-out predictions
- KOKOROWSKI_2001_FIG3_DECAY_DIGITIZED.csv: missing_axes=Gamma; closure_gap=partial apparatus-control candidate is missing Gamma axis; next=add independent controls for the missing product-law axes before testing held-out predictions
- KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv: missing_axes=Gamma; closure_gap=partial apparatus-control candidate is missing Gamma axis; next=add independent controls for the missing product-law axes before testing held-out predictions

## Synthetic Benchmark

- Synthetic benchmark rows: 63
- Balanced synthetic product delta AICc: 0.0
- Balanced synthetic max factor correlation: 6.644793704683637e-16

The balanced synthetic benchmark says the scaffold can recognize a product-law-shaped design when the factors are independently varied. The confounded synthetic benchmark says the opposite danger is real: a single latent load can look excellent under a product term while Lambda, Gamma, and Theta are not separately identifiable.

The proxy scan is only a triage layer. It identifies empirical files with visibility-like columns and apparatus-control-like columns, but those proxy columns are not treated as measured Lambda/Gamma/Theta factors until a provenance mapping and held-out product-law comparison exist.

## Needed Before G12 Can Pass

1. Independently varied Lambda, Gamma, and Theta factors.
2. Low factor correlation and acceptable VIF.
3. Held-out factor-combination prediction against additive, pairwise, and background alternatives.
4. Provenance showing the factors were measured or set by apparatus controls, not inferred from the same visibility curve.

## Boundary

- This does not validate the product law.
- This does not affect the Xiao/Kokorowski no-refit distribution gates.
- This keeps G12 failed until an empirical independent-factor dataset exists.
