# Hackermueller Thermal Stress Report

Status: thermal record-load survives uncertainty

This stress pass jitters normalized visibility, laser-power anchors, and temperature anchors, then refits the Hackermueller Figure 4 thermal-decoherence models.

- Input CSV: `data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZED.csv`
- Digitization JSON: `data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZATION.json`
- Bootstrap samples: 1000
- Observed best model: `thermal_delta_T4`
- Observed thermal delta-T4 RMSE: 0.0768
- Observed exp(power) RMSE: 0.0923
- P(thermal delta-T4 beats exp power): 0.994
- P(thermal delta-T4 beats exp power squared): 0.701
- P(thermal delta-T4 is best model): 0.701

## Interpretation

This is a robustness check for the durable environmental-record lane. It does not claim new physics; it asks whether an independently interpretable thermal-load proxy remains competitive under digitization uncertainty.
