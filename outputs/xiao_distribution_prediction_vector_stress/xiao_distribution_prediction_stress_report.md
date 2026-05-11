# Xiao Distribution Prediction Stress Report

Status: distribution prediction survives robustness checks

This stress test asks whether the Xiao Fig. 3 distribution-to-Fig. 4 no-refit prediction survives reasonable digitization and analysis alternatives. It jitters the Fig. 3 probability curves and Fig. 4 points, uses extraction-specific bootstrap baseline methods, separately reports baseline sensitivity, and runs two null controls.

- Momentum input: `data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv`
- Probability input: `data/extracted/XIAO_2019_PROBABILITY_VECTOR_DIGITIZED.csv`
- Bootstrap samples: 1000
- Seed: 20260425
- Probability uncertainty mode: `vector`
- Probability jitter sigmas: p = 0.0020, density = 0.0020, mean |p| = 0.0020
- Bootstrap baseline methods: `edge_median`

## Robust Quantities

- Observed no-refit RMSE: 0.0133
- Observed published-bound RMSE: 0.0693
- P(no-refit beats published bound): 1.000
- P(no-refit RMSE < 0.025): 0.957
- P(no-refit / published-bound RMSE < 0.5): 1.000
- P(phi=pi branch mean > phi=0 branch mean): 1.000
- No-refit RMSE 95% CI: [0.0136, 0.0256]
- phi=0 mean |p| 95% CI: [0.0639, 0.0717]
- phi=pi mean |p| 95% CI: [1.4094, 1.4132]
- Baseline sensitivity pass fraction: 0.750

## Baseline Bootstrap Summary

| baseline | n | median RMSE | P(beats bound) | P(RMSE < 0.025) | median phi0 | median phipi |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| edge_median | 1000 | 0.0192 | 1.000 | 0.957 | 0.0672 | 1.4112 |

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
