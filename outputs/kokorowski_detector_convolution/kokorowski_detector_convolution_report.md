# Kokorowski Detector-Convolution Kappa Check

Status: detector-convolution reconstruction supports reported kappa-prime values

This check reconstructs the public formula path from Fig. 4 caption parameters to the reported calculated `kappa_prime` values. It uses the source formula `kappa^2 = nbar*sigma_k^2 + sigma_n^2*k0^2`, the source value `sigma_k = 2/5 k0`, and the detector acceptance relation `1/kappa_prime^2 = 1/kappa^2 + 1/kappa_d^2` with `kappa_d = 3.3(1) k0`.

- Input CSV: `data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv`
- Bootstrap samples per branch: 1000
- Seed: 28046
- All branches within two reported SE: True
- Max absolute predicted-minus-reported kappa-prime: 0.0884 k0
- Minimum Monte Carlo fraction within reported kappa-prime SE: 0.604
- Clears G11: False

## Branch Reconstruction

- **bullet_lower_intensity**: raw kappa 2.002 k0; detector-convolved 1.712 k0; reported 1.800(0.100) k0; within 2 reported SE: True
- **circle_high_intensity**: raw kappa 3.680 k0; detector-convolved 2.457 k0; reported 2.500(0.100) k0; within 2 reported SE: True

## Interpretation

This public-source reconstruction strengthens the Kokorowski provenance chain: the caption parameters, recoil-width formula, and detector convolution reproduce the reported calculated kappa-prime values closely. It does not close G11 because it still depends on published summarized beam-calibration values rather than raw beam-deflection/broadening tables.

## Boundary

- No new fit to Fig. 4 visibility was introduced.
- This does not narrow the reported kappa-prime uncertainty enough to pass the stress gate.
- This does not validate the Lambda/Gamma/Theta product law.
