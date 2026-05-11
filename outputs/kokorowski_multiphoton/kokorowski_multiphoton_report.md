# Kokorowski 2001 Multiphoton Analysis

Status: independent multiphoton no-refit candidate passes digitized Fig. 4

This analysis asks whether the independently reported many-photon parameters in Kokorowski Fig. 4 predict visibility without refitting the record-load width. The model is the standard decoherence expression:

```text
V(d) = exp[-0.5 * (kappa_prime * 2*pi*d/lambda)^2]
```

## Result

- Combined independent-kappa RMSE: 0.0240
- Combined refit-kappa RMSE: 0.0193
- Passes no-refit digitized-Fig. 4 criterion: True

- **bullet_lower_intensity**: independent kappa RMSE 0.0245; reported fit kappa 1.71 k0; independent kappa 1.80 k0
- **circle_high_intensity**: independent kappa RMSE 0.0233; reported fit kappa 2.39 k0; independent kappa 2.50 k0

## Interpretation

This is a stronger public-data lead than the previous near misses because the source text says the Fig. 4 parameters were determined from independent beam-deflection/broadening measurements. It is still standard quantum decoherence and does not validate the Constraint Dynamics product law.

## What This Does Not Show

- No collapse solution.
- No beyond-standard-quantum-mechanics claim.
- No Lambda/Gamma/Theta product-law validation.
- No author-table provenance yet.
