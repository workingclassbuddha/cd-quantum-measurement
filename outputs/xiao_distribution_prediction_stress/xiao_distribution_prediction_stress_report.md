# Xiao Distribution Prediction Stress Report

Status: distribution prediction is fragile under robustness checks

This stress test asks whether the Xiao Fig. 3 distribution-to-Fig. 4 no-refit prediction survives reasonable digitization and analysis alternatives. It jitters the Fig. 3 probability curves and Fig. 4 points, cycles through baseline-subtraction methods, and runs two null controls.

- Momentum input: `data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv`
- Probability input: `data/extracted/XIAO_2019_PROBABILITY_DIGITIZED.csv`
- Bootstrap samples: 1000
- Seed: 20260425

## Robust Quantities

- Observed no-refit RMSE: 0.0155
- Observed published-bound RMSE: 0.0693
- P(no-refit beats published bound): 0.135
- P(no-refit RMSE < 0.025): 0.000
- P(no-refit / published-bound RMSE < 0.5): 0.000
- P(phi=pi branch mean > phi=0 branch mean): 1.000
- No-refit RMSE 95% CI: [0.0542, 0.3581]
- phi=0 mean |p| 95% CI: [0.1130, 0.5041]
- phi=pi mean |p| 95% CI: [1.4004, 1.4453]
- Baseline sensitivity pass fraction: 0.250

## Baseline Bootstrap Summary

| baseline | n | median RMSE | P(beats bound) | P(RMSE < 0.025) | median phi0 | median phipi |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| edge_median | 334 | 0.0735 | 0.404 | 0.000 | 0.1377 | 1.4164 |
| min | 333 | 0.3031 | 0.000 | 0.000 | 0.4320 | 1.4336 |
| quantile_05 | 333 | 0.2076 | 0.000 | 0.000 | 0.3093 | 1.4237 |

## Null Controls

- Pairing-null P(RMSE <= observed): 0.003
- Branch-label-swap P(RMSE <= observed): 0.000

## Interpretation

A robust result means the Fig. 3 distribution-to-Fig. 4 prediction is not just an artifact of one baseline choice, small digitization perturbations, or arbitrary pairing of visibility and momentum points. It is still a within-paper held-out figure test rather than an independent experiment.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not solve collapse.
- It does not show physics beyond standard quantum mechanics.
- It does not replace a third held-out experiment.
