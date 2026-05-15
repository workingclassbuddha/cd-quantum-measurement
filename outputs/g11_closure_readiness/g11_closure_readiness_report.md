# G11 Closure Readiness Audit

Verdict: no dataset currently clears the G11 closure contract

This audit turns the missing second independent measured-distribution-to-visibility validation into a hard acceptance contract. It is designed to prevent a near miss, control dataset, or visibility-derived proxy from being counted as a closure.

## Summary

- Contract gates: 7
- Possible G11 closure targets in intake schema: 4
- Author-data G11-ready rows already received: 0
- Closure-ready targets now: 0
- Public candidates scored against contract: 14
- Public candidates clearing all contract gates: 0
- Top public candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; failed gates: G11C;G11F;G11G
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

## Public Candidate Gate Matrix

- **KOKOROWSKI_2001_MULTIPHOTON_SCATTERING**: score=0.84; passed=G11A;G11B;G11D;G11E; failed=G11C;G11F;G11G
- **EIBENBERGER_2014_RECOIL_ABSORPTION**: score=0.70; passed=G11B; failed=G11A;G11C;G11D;G11E;G11F;G11G
- **HORNBERGER_2003_COLLISIONAL_DECOHERENCE**: score=0.68; passed=G11B; failed=G11A;G11C;G11D;G11E;G11F;G11G
- **HOCHRAINER_2017_INDUCED_COHERENCE_MOMENTUM_CORRELATION**: score=0.60; passed=G11B; failed=G11A;G11C;G11D;G11E;G11F;G11G
- **LAHIRI_2017_TWIN_PHOTON_CORRELATIONS**: score=0.58; passed=G11B; failed=G11A;G11C;G11D;G11E;G11F;G11G
- **MIR_2007_WEAK_VALUE_MOMENTUM_TRANSFER**: score=0.52; passed=G11A; failed=G11B;G11C;G11D;G11E;G11F;G11G
- **DING_2025_WAVE_PARTICLE_ENTANGLEMENT_TRIAD**: score=0.50; passed=G11B; failed=G11A;G11C;G11D;G11E;G11F;G11G
- **CHEN_2022_ASYMMETRIC_BEAM_DUALITY**: score=0.48; passed=G11B; failed=G11A;G11C;G11D;G11E;G11F;G11G

## Boundary

- This does not send outreach.
- This does not close G11.
- This does not mark the active goal complete.
- A future dataset must pass the schema, this closure contract, and a dedicated no-refit stress analysis before it can update the breakthrough scorecard.
