# Hackermueller Thermal Decoherence Report

Status: thermal record-load proxy is viable for full digitization

This first pass tests Hackermueller et al. 2004 as a third held-out dataset for the irreversible-record side of the Constraint Dynamics language.

- Input CSV: `data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZED.csv`
- Rows analyzed: 31
- Best combined model: `thermal_delta_T4`
- Best combined RMSE: 0.0767
- Thermal delta-T4 RMSE: 0.0767
- Simple exp(power) RMSE: 0.0923

## What This Means

Hackermueller is not a Fourier-revival experiment like Chapman. It is a standard decoherence experiment where thermal photons carry inaccessible environmental records. That makes it a good test of whether `Theta` can be used conservatively as durable environmental record load.

## What Would Be Interesting

- The temperature/emission-load proxy remains competitive with plain laser-power damping.
- The result survives publication-grade extraction of `Figure4.eps`.
- `Figure3.eps` photon-emission information can be connected to the same load variable without fitting the visibility curve itself.

## What This Does Not Show

- No product-law validation.
- No collapse solution.
- No evidence beyond standard quantum mechanics.
- No final claim until Figure 4 is upgraded from seeded scout points to calibrated vector/pixel extraction.
