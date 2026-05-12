# Kokorowski Kappa-Uncertainty Profile

Status: reported kappa uncertainty is the limiting stress factor

This profile isolates the independent-kappa uncertainty that limited the broader Kokorowski stress test. It rescales only the reported independent `kappa_prime` uncertainty while holding the vector-digitized points fixed, then asks when the no-refit prediction clears the joint stress gate.

- Input CSV: `data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv`
- Bootstrap samples per scale: 600
- Seed: 28045
- Full reported-SE joint pass probability: 0.417
- Largest tested kappa-SE scale with P(joint gate) >= 0.80: 0.25

## Scale Profile

- 0.00x reported SE: P(joint gate) 1.000; median RMSE 0.0240
- 0.25x reported SE: P(joint gate) 0.975; median RMSE 0.0244
- 0.50x reported SE: P(joint gate) 0.783; median RMSE 0.0253
- 0.75x reported SE: P(joint gate) 0.567; median RMSE 0.0276
- 1.00x reported SE: P(joint gate) 0.417; median RMSE 0.0307
- 1.25x reported SE: P(joint gate) 0.393; median RMSE 0.0317
- 1.50x reported SE: P(joint gate) 0.268; median RMSE 0.0373

## Interpretation

This does not rescue or reject Kokorowski by itself. It turns the next provenance question into a measurable one: whether the independent beam-deflection/broadening calibration supports a narrower effective kappa uncertainty than the conservative stress model used here.

## Boundary

- No model freedom was added.
- No collapse or beyond-standard-quantum-mechanics claim follows.
- This is a targeting aid for provenance and author-data follow-up.
