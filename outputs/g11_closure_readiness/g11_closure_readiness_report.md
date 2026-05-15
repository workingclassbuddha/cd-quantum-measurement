# G11 Closure Readiness Audit

Verdict: no dataset currently clears the G11 closure contract

This audit turns the missing second independent measured-distribution-to-visibility validation into a hard acceptance contract. It is designed to prevent a near miss, control dataset, or visibility-derived proxy from being counted as a closure.

## Summary

- Contract gates: 7
- Possible G11 closure targets in intake schema: 4
- Author-data G11-ready rows already received: 0
- Closure-ready targets now: 0
- Current public G11 path exhausted: True
- Current breakthrough path exhausted without closure: True
- Objective can be marked complete: False

## Contract Gates

- **G11A independent_record_variable**: record distribution, width, or load calibration is measured independently of the visibility curve being predicted
- **G11B paired_visibility_curve**: each record/load setting has a paired visibility, contrast, or decoherence measurement under the same apparatus setting
- **G11C uncertainty_budget**: record-variable and visibility uncertainties are explicit enough for stress propagation
- **G11D no_refit_prediction_map**: the record variable predicts visibility without fitting the record bandwidth to the target visibility curve
- **G11E null_controls**: paired-data result beats shuffle, branch-swap, or wrong-pairing null controls
- **G11F stress_threshold**: bootstrap or stress profile clears the joint pass threshold used by the G11 audit
- **G11G provenance_permission**: source, license or permission, extraction method, and reproducible file hashes are recorded

## Prospective Closure Targets

- **kokorowski_2001_beam_calibration** (`kokorowski_beam_calibration`): nbar, sigma_n, or kappa_prime uncertainty must come from beam calibration independent of Fig. 4 contrast fitting; next CLI: `extend profile-kokorowski-kappa-uncertainty with author calibration input`
- **hochrainer_2017_independent_widths** (`hochrainer_visibility_widths`): record width must be measured or simulated independently of the visibility FWHM being predicted; next CLI: `new analyze-hochrainer-no-refit-widths command`
- **mir_2007_visibility_context** (`mir_pwv_visibility_pairing`): P_wv(q) and visibility/contrast must be paired by controlled which-way settings; next CLI: `new analyze-mir-pwv-visibility command`
- **eibenberger_2014_recoil_controls** (`eibenberger_held_out_recoil_load`): sigma_abs or equivalent recoil/load calibration must not be inferred from the same visibility reduction; next CLI: `extend scout-eibenberger-recoil-absorption with held-out calibration input`

## Boundary

- This does not send outreach.
- This does not close G11.
- This does not mark the active goal complete.
- A future dataset must pass the schema, this closure contract, and a dedicated no-refit stress analysis before it can update the breakthrough scorecard.
