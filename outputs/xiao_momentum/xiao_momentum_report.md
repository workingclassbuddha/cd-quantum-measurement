# Xiao Momentum-Visibility Report

Status: candidate cross-experiment structure

This analysis tests Xiao et al. 2019 as a second empirical target for the Chapman-derived record-bandwidth language. The measured variable is the reconstructed total mean absolute momentum disturbance, plotted against remaining fringe visibility in partial which-way measurements.

- Input CSV: `data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv`
- Rows analyzed: 6
- Best model by AICc: `linear_bandwidth`
- Best RMSE: 0.0034
- Published-bound RMSE: 0.0693
- Linear bandwidth RMSE: 0.0034
- Loss-vs-momentum Pearson r: 0.9999
- All points above published lower-bound line: True

## What Would Be Interesting

- Momentum disturbance rises monotonically with visibility loss: True
- The data remain above the published lower bound: True
- A simple bandwidth-style loss predictor fits tightly: True

## Interpretation

Xiao is promising because it supplies an independently reconstructed momentum-disturbance scale, not merely a contrast curve. In Constraint Dynamics language, this is the right kind of second experiment for testing whether `Theta` as inaccessible conjugate-record bandwidth travels beyond Chapman.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not solve collapse.
- It does not require Bohmian mechanics as an ontology.
- It does not repair the Chapman raw-phase failure.
