# Cormann Visibility/Phase Scout Report

Status: cormann is viable as a phase-control scout, not a record-bandwidth win

This scout tests Cormann et al. 2016 as a third dataset candidate. The source is the arXiv package for `1508.01353`, specifically `VisibilityPhaseMeasurement.eps`. The extraction is scout-grade: the EPS is rendered by Ghostscript, colored markers are component/binned extracted, and the extracted visibility is compared against the paper's caption parameters without fitting visibility bandwidth to the data.

- Source URL: https://arxiv.org/abs/1508.01353
- DOI: https://doi.org/10.1103/PhysRevA.93.042124
- Source file: `VisibilityPhaseMeasurement.eps`
- Source SHA256: `d9807edf7e9e2c13a2905223df3d80d403d7bf6ee8e169c6323183c85e64820a`
- Extraction method: `calibrated_component_scout_v1`
- Extracted rows: 211
- Scout CSV: `data/extracted/CORMANN_2016_VISIBILITY_PHASE_SCOUT.csv`
- Provenance JSON: `data/extracted/CORMANN_2016_VISIBILITY_PHASE_SCOUT.json`

## No-Refit Visibility Check

- setup 1 visibility RMSE: 0.0357, Pearson r: 0.986
- setup 2 visibility RMSE: 0.0655, Pearson r: 0.958
- setup 3 visibility RMSE: 0.2538
- mean phase-sign accuracy: 0.877

## Interpretation

Cormann is useful, but it is a different kind of test from Xiao. It gives a visibility-plus-phase quantum-eraser control with known measurement strengths and purities. That can stress whether the scaffold respects eraser phase/sign behavior, especially around the weak-value singularity. It does not provide an independently measured momentum-record distribution comparable to Xiao Fig. 3, so it is not the third held-out record-bandwidth prediction we ultimately need.

## Recommended Next Move

Use Cormann as a phase-control implementation only if we want to broaden the eraser/phase side of the scaffold. For the breakthrough hunt, continue looking for a third experiment with author data or extractable distributions where a record variable predicts visibility without refitting.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not solve collapse.
- It does not provide a new record-bandwidth dataset.
- It does not replace a true outside held-out distribution-to-visibility test.
