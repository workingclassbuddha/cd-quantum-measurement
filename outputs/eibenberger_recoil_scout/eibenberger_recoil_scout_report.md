# Eibenberger Recoil-Absorption Scout

Status: recoil-control candidate, not second no-refit gate

This scout implements the Eq. (2)-style recoil visibility reduction from Eibenberger et al. 2014 as a record-kernel control. Photon absorption gives a known momentum recoil, and the observed visibility reduction follows from averaging shifted and unshifted molecular fringes over the measured velocity distribution.

- Source URL: https://arxiv.org/abs/1402.5307
- DOI: https://doi.org/10.1103/PhysRevLett.112.250402
- Source SHA256: `f3d54323ea94b06ba8bdab0cbc97d4245408e94d64b90ec3ca02444b2124c23b`
- Extraction method: `seeded_visual_scout_v1`
- Extracted Fig. 2b rows: 12

## Fit Quality

- Paper sigma_abs: 1.970e-21 m^2
- Paper-sigma RMSE: 0.0251
- Previous-absorption midpoint sigma_abs: 1.800e-21 m^2
- Previous-midpoint RMSE: 0.0302
- Visibility-fit sigma_abs: 1.935e-21 m^2
- Visibility-fit RMSE: 0.0247
- Best model: `visibility_fit_sigma_abs`

## Interpretation

This is mathematically close to the record-bandwidth idea because visibility is a characteristic-function-like average over recoil phases. It does **not** clear the missing second no-refit gate, because the paper uses the visibility reduction to extract the absorption cross section. It is still useful as a standard-QM recoil-control lane.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not provide an independently measured record distribution like Xiao.
- It does not show physics beyond standard quantum mechanics.
