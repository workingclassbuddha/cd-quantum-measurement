# Breakthrough Candidate Dossier

Verdict: lead candidate found, breakthrough not yet

Lead candidate: Xiao 2019 vector Fig. 3 distribution-to-Fig. 4 no-refit prediction.

This dossier does not fit a new model. It scores the current outputs against strict gates for whether the project has found a breakthrough-grade result.

## Core Result

- Xiao no-refit RMSE: 0.0133
- Published-bound RMSE: 0.0693
- Direct Fig. 4 refit RMSE: 0.0034
- No-refit / published-bound RMSE ratio: 0.193
- No-refit / direct-refit RMSE ratio: 3.949
- Bootstrap P(no-refit beats published bound): 1.000
- Bootstrap P(no-refit RMSE < 0.025): 0.957
- Pairing-null P(RMSE <= observed): 0.003
- Branch-label-null P(RMSE <= observed): 0.000
- Baseline sensitivity pass fraction: 0.750

## Cross-Experiment Support

- Chapman exponential/sinc RMSE ratio: 2.871
- Chapman raw first zero: d/lambda = 0.510
- Hackermueller P(thermal delta-T4 beats exp power): 0.994
- Hackermueller P(thermal delta-T4 is best): 0.701
- Synthesis statuses: side-peak distribution supports bandwidth proxy; supports Fourier record-bandwidth over scalar exponential; survives uncertainty and pairing null; thermal record-load proxy supports durable environmental record lane
- Second no-refit scout verdict: no second no-refit distribution target yet
- Eligible second no-refit targets: 0
- Recommended second-target candidate: EIBENBERGER_2014_RECOIL_ABSORPTION
- Eibenberger recoil-control status: control_fit
- Eibenberger best recoil model: visibility_fit_sigma_abs
- Eibenberger best RMSE: 0.0247268685940939
- Eibenberger paper-sigma RMSE: 0.0251372179762769
- Eibenberger inferred sigma_abs: 1.9345911949685537e-21

## Blockers

- Chapman raw phase verdict: model still fails
- Chapman best mixture raw phase RMSE: 1.3087718496350118
- Second independent distribution-to-visibility experiment: no second no-refit distribution target yet
- Lambda/Gamma/Theta product law validation: not yet

## Gate Score

Passed gates: 9 / 12

The evidence is strongest where the key variable is measured or reconstructed independently of the fitted visibility curve. Xiao is therefore the centerpiece. Chapman and Hackermueller provide cross-experiment support for record bandwidth/load, but they do not by themselves clear the no-refit breakthrough gate.

Eibenberger is now logged as a useful recoil-control lane: the known photon recoil mechanism predicts visibility reduction at roughly the paper absorption cross section. It strengthens the standard-QM compatibility of the record-kernel framing, but it does not close G11 because the absorption cross section is still extracted from visibility rather than independently measured as a held-out record distribution.

## Strict Claim

```text
We have a lead breakthrough candidate: an independently digitized Xiao momentum distribution predicts visibility loss better than scalar baselines without refitting the key record-bandwidth parameter.
```

## Strict Non-Claims

- This does not solve collapse.
- This does not validate the Lambda/Gamma/Theta product law.
- This does not show physics beyond standard quantum mechanics.
- This is not yet a cross-experiment no-refit prediction.

## Next Move

Find a second independent experiment with both measured record distribution and visibility/decoherence output. Do not add model freedom until that search fails.
