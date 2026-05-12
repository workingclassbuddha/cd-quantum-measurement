# Kokorowski 2001 Multiphoton Stress Test

Status: Kokorowski no-refit candidate needs more stress evidence

This stress test asks whether the Kokorowski Fig. 4 no-refit result survives reasonable digitization, calibration, and independent-parameter uncertainty. It perturbs the vector-digitized point coordinates, visibility values, and independently reported kappa values; then it compares the independent-kappa prediction with a per-branch refit and two null controls.

- Input CSV: `data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv`
- Bootstrap samples: 1000
- Component-sensitivity samples per component: 300
- Seed: 28044
- d/lambda jitter: one EPS-pixel equivalent (0.00090)
- visibility jitter: row-level `visibility_se`
- kappa jitter: row-level `kappa_prime_calculated_se_k0`

## Robust Quantities

- Observed independent-kappa RMSE: 0.0240
- Observed refit-kappa RMSE: 0.0193
- Observed independent/refit RMSE ratio: 1.241
- Bootstrap P(RMSE < 0.05): 0.866
- Bootstrap P(independent RMSE <= 1.5 * refit RMSE): 0.743
- Bootstrap P(joint stress gate): 0.727
- Independent-kappa RMSE 95% CI: [0.0270, 0.0605]
- Calibration sensitivity pass fraction: 0.733

## Component Sensitivity

- d_axis_and_visibility: median RMSE 0.0339; P(RMSE < 0.05) 1.000; P(joint gate) 0.997
- d_axis_only: median RMSE 0.0244; P(RMSE < 0.05) 1.000; P(joint gate) 1.000
- full_uncertainty_recheck: median RMSE 0.0389; P(RMSE < 0.05) 0.850; P(joint gate) 0.713
- independent_kappa_only: median RMSE 0.0300; P(RMSE < 0.05) 0.950; P(joint gate) 0.447
- visibility_only: median RMSE 0.0340; P(RMSE < 0.05) 1.000; P(joint gate) 0.990

## Null Controls

- Within-branch visibility-shuffle P(RMSE <= observed): 0.000
- Branch-kappa-swap P(RMSE <= observed): 0.000

## Interpretation

Passing this stress test would strengthen Kokorowski as a public second-experiment no-refit candidate. It still remains a standard quantum decoherence check and does not validate the Constraint Dynamics product law.

## What This Does Not Show

- No collapse solution.
- No beyond-standard-quantum-mechanics claim.
- No Lambda/Gamma/Theta product-law validation.
- No author-table provenance yet.
