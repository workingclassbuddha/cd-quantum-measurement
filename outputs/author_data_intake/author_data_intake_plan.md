# Author Data Intake Plan

Purpose: make incoming author/numerical data immediately testable against G11.

## Intake Rule

Data can affect G11 only when the record distribution, bandwidth, width, or load proxy is independent of the visibility/decoherence curve it predicts. Calibration data for Xiao are still valuable, but they tighten the current lead rather than closing the second-experiment gate.

## Schemas

- **xiao_2019_author_data**: lead calibration only; can close G11 = False; rule: recompute Fig. 3 branch moments and Fig. 4 no-refit RMSE; compare to current vector extraction
- **hochrainer_2017_independent_widths**: possible second no-refit test; can close G11 = True; rule: record width must be measured or simulated independently of the visibility FWHM being predicted
- **mir_2007_visibility_context**: possible weak-value distribution control; can close G11 = True; rule: P_wv(q) and visibility/contrast must be paired by controlled which-way settings
- **eibenberger_2014_recoil_controls**: possible held-out recoil/load control; can close G11 = True; rule: sigma_abs or equivalent recoil/load calibration must not be inferred from the same visibility reduction

## Summary

- Intake targets: 4
- Targets that could close G11 if the independence rule is satisfied: 3
- Manifest template: `author_data_received_manifest_template.csv`

## Next Step

When data arrives, fill the manifest, commit only data with clear permission/provenance, and add a dedicated analysis CLI before updating the breakthrough scorecard.
