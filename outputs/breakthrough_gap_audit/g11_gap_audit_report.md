# G11 Breakthrough Gap Audit

Verdict: G11 still failed

This audit checks the missing gate directly: can a second experiment, independent of Xiao, provide a measured record distribution that predicts a visibility/decoherence curve without refitting the key record-bandwidth/load parameter?

## Current Answer

- Candidates audited: 8
- Eligible second no-refit targets: 0
- Top current candidate: XIAO_2019_INTERNAL_LEAD
- Top blocker class: internal_lead_not_second_experiment
- Next move: keep as lead benchmark; use it to validate extraction and stress-test standards

## Candidate Readout

- **Xiao et al. 2019** (`XIAO_2019_INTERNAL_LEAD`): internal_lead_not_second_experiment. Next: keep as lead benchmark; use it to validate extraction and stress-test standards
- **Cormann et al. 2016** (`CORMANN_2016_MODULAR_VALUE`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Eibenberger et al. 2014** (`EIBENBERGER_2014_RECOIL_ABSORPTION`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Hackermueller/Hornberger et al. 2003** (`HORNBERGER_2003_COLLISIONAL_DECOHERENCE`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Hochrainer et al. 2017** (`HOCHRAINER_2017_INDUCED_COHERENCE_MOMENTUM_CORRELATION`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Mir et al. 2007** (`MIR_2007_WEAK_VALUE_MOMENTUM_TRANSFER`): paired_visibility_curve_missing. Next: obtain paired visibility or contrast sweep for the measured record distribution
- **Duerr/Nonn/Rempe 1998** (`DURR_1998_COMPLEMENTARITY`): record_variable_not_independent. Next: obtain author/supplemental record distribution or calibration not inferred from visibility
- **Kocsis et al. 2011** (`KOCSIS_2011_AVERAGE_TRAJECTORIES`): paired_visibility_curve_missing. Next: obtain paired visibility or contrast sweep for the measured record distribution

## Blocker Summary

- `record_variable_not_independent`: 5
- `paired_visibility_curve_missing`: 2
- `internal_lead_not_second_experiment`: 1

## Strict Interpretation

G11 remains the central missing breakthrough gate unless `eligible_second_no_refit_targets` becomes nonzero. Chapman, Hackermueller, Hornberger, Eibenberger, Mir, Hochrainer, and Cormann are useful controls or near misses, but they do not yet give a second held-out distribution-to-visibility prediction.

## Non-Claims

- No collapse solution.
- No beyond-QM claim.
- No Lambda/Gamma/Theta product-law validation.
- No claim that a control dataset closes G11.
