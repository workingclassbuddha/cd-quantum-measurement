# Kokorowski G11 Closure Gap Audit

Verdict: Kokorowski G11 closure gaps remain

This audit isolates the remaining Kokorowski-specific blockers after the public closure contract. It does not add model freedom and does not update the breakthrough scorecard.

## Summary

- Candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Failed tracked gates: 3
- Failed gate ids: G11C;G11F;G11G
- Joint stress pass probability: 0.727
- Full reported-SE joint pass probability: 0.4166666666666667
- Max kappa-SE scale with joint pass >= 0.80: 0.25
- Raw public calibration tables found: False
- Source inventory files / calibration-hit files: 7 / 5
- Detector-convolution reconstruction is within two reported SE: True; max delta = 0.088 k0; clears G11 = False.
- Can update G11 scorecard: False

## Gate Matrix Context

- Closure gate matrix: passed=G11A;G11B;G11D;G11E; failed=G11C;G11F;G11G

## Remaining Gaps

- **G11C uncertainty_budget**: observed `full_reported_se_joint_pass` = 0.417; threshold: full reported-SE joint pass >= 0.80; next: raw beam-deflection/broadening calibration tables or an independently reproduced kappa-prime uncertainty budget
- **G11F stress_threshold**: observed `bootstrap_p_joint_stress_gate` = 0.727; threshold: bootstrap joint stress pass >= 0.80; next: tightened independent kappa uncertainty that raises both RMSE and ratio stress gates without refitting visibility
- **G11G provenance_permission**: observed `public_source_raw_calibration_tables_found` = 0.000; threshold: public or permitted raw calibration tables present; next: permitted raw calibration tables with source, permission, extraction method, and reproducible hashes

## Boundary

- This does not close G11.
- This does not make Kokorowski a second validation.
- The next valid move is new or permitted calibration evidence, not relaxing the stress gate.
