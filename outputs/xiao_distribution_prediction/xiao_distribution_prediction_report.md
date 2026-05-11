# Xiao Distribution-To-Visibility Prediction Report

Status: within-paper held-out distribution prediction passes

This command uses Xiao et al. 2019 Fig. 3 as an independently digitized momentum-record distribution and asks whether it predicts Fig. 4 without refitting the bandwidth to Fig. 4. The phase-mixture mapping is:

```text
eta_pi = (1 - V) / 2
eta_0  = (1 + V) / 2
predicted mean |p| = eta_0 * M_phi0 + eta_pi * M_phipi
```

The main result is `distribution_no_refit`, where `M_phi0` and `M_phipi` are computed from the baseline-subtracted Fig. 3b branch distributions. `distribution_panel_a_scaled` is a secondary check that rescales those branch moments to the Fig. 3a late equal-weight mean; it still uses no Fig. 4 fit.

- Momentum input: `data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv`
- Probability input: `data/extracted/XIAO_2019_PROBABILITY_DIGITIZED.csv`
- Density baseline method: `edge_median`

## Extracted Fig. 3 Branch Moments

- phi=0 mean |p|: 0.0639 hbar/d
- phi=pi mean |p|: 1.4109 hbar/d
- Fig. 3a late equal-weight mean |p|: 0.6807 hbar/d
- Fig. 3b equal-weight mean |p| before panel-a scaling: 0.7374 hbar/d

## Fig. 4 Prediction Quality

- Distribution no-refit RMSE: 0.0155
- Distribution panel-a-scaled RMSE: 0.0256
- Published-bound RMSE: 0.0693
- Linear Fig. 4 refit RMSE: 0.0034
- No-refit / published-bound RMSE ratio: 0.223
- No-refit / linear-refit RMSE ratio: 4.577

## Interpretation

This is stronger than the previous scalar Xiao fit because the bandwidth scale comes from Fig. 3 distributions, not from Fig. 4. The no-refit prediction lands close to the fitted Fig. 4 line and substantially beats the published lower-bound line as a point predictor.

## What This Does Not Show

- It is a within-paper held-out figure test, not a fully independent experiment.
- It does not validate the Lambda/Gamma/Theta product law.
- It does not solve collapse.
- It does not require Bohmian mechanics as an ontology.
- It does not repair the Chapman raw-phase failure.
