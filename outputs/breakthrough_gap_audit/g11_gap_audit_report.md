# G11 Breakthrough Gap Audit

Verdict: second independent no-refit candidate found

This audit checks the missing gate directly: can a second experiment, independent of Xiao, provide a measured record distribution that predicts a visibility/decoherence curve without refitting the key record-bandwidth/load parameter?

## Current Answer

- Candidates audited: 15
- Eligible second no-refit targets: 1
- Stress-closed second no-refit targets: 0
- Top current candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Top blocker class: stress_or_calibration_uncertainty_limited
- Next move: tighten independent-kappa calibration provenance/uncertainty or find a cleaner second no-refit dataset

## Candidate Readout

- **Kokorowski et al. 2001** (`KOKOROWSKI_2001_MULTIPHOTON_SCATTERING`): stress_or_calibration_uncertainty_limited. Next: tighten independent-kappa calibration provenance/uncertainty or find a cleaner second no-refit dataset
- **Xiao et al. 2019** (`XIAO_2019_INTERNAL_LEAD`): internal_lead_not_second_experiment. Next: keep as lead benchmark; use it to validate extraction and stress-test standards
- **Cormann et al. 2016** (`CORMANN_2016_MODULAR_VALUE`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Eibenberger et al. 2014** (`EIBENBERGER_2014_RECOIL_ABSORPTION`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Hackermueller/Hornberger et al. 2003** (`HORNBERGER_2003_COLLISIONAL_DECOHERENCE`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Hochrainer et al. 2017** (`HOCHRAINER_2017_INDUCED_COHERENCE_MOMENTUM_CORRELATION`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Mir et al. 2007** (`MIR_2007_WEAK_VALUE_MOMENTUM_TRANSFER`): paired_visibility_curve_missing. Next: obtain paired visibility or contrast sweep for the measured record distribution
- **Lahiri et al. 2017** (`LAHIRI_2017_TWIN_PHOTON_CORRELATIONS`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility

## Blocker Summary

- `record_variable_not_independent`: 9
- `paired_visibility_curve_missing`: 4
- `internal_lead_not_second_experiment`: 1
- `stress_or_calibration_uncertainty_limited`: 1

## Strict Interpretation

Kokorowski is now an eligible public second no-refit candidate, so the old scouting gap is no longer the bottleneck. G11 still does not close because the candidate has not passed the stress/provenance gate: the public vector prediction is strong, but independent-kappa uncertainty and missing raw beam-calibration tables remain limiting evidence.

## Non-Claims

- No collapse solution.
- No beyond-QM claim.
- No Lambda/Gamma/Theta product-law validation.
- No claim that a control dataset closes G11.
