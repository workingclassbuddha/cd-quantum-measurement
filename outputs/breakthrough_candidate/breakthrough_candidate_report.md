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
- Synthesis statuses: collisional record-load guardrail supports standard decoherence; side-peak distribution supports bandwidth proxy; supports Fourier record-bandwidth over scalar exponential; survives uncertainty and pairing null; thermal record-load proxy supports durable environmental record lane
- Second no-refit scout verdict: second no-refit distribution target found
- Eligible second no-refit targets: 1
- Recommended second-target candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Kokorowski stress status: Kokorowski no-refit candidate needs more stress evidence
- Kokorowski stress P(joint gate): 0.727
- Kokorowski stress P(RMSE < 0.05): 0.866
- Kokorowski stress P(independent <= 1.5 * refit): 0.743
- Kokorowski stress null p-values: 0.0 / 0.0
- Eibenberger recoil-control status: control_fit
- Eibenberger best recoil model: visibility_fit_sigma_abs
- Eibenberger best RMSE: 0.0247268685940939
- Eibenberger paper-sigma RMSE: 0.0251372179762769
- Eibenberger inferred sigma_abs: 1.9345911949685537e-21

## Blockers

- Chapman raw phase verdict: model still fails
- Chapman best mixture raw phase RMSE: 1.3087718496350118
- Second independent distribution-to-visibility experiment: second no-refit distribution target found; Kokorowski stress status: Kokorowski no-refit candidate needs more stress evidence
- Lambda/Gamma/Theta product law validation: not yet

## Gate Score

Passed gates: 9 / 12

The evidence is strongest where the key variable is measured or reconstructed independently of the fitted visibility curve. Xiao remains the centerpiece because it gives the cleanest distribution-to-visibility bridge. Kokorowski now supplies the first second-experiment public no-refit candidate: independently reported many-photon beam-deflection/broadening parameters predict Fig. 4 contrast after vector digitization, but the current stress result is not yet publication-grade. Chapman, Hackermueller, and Hornberger provide supporting standard-QM record bandwidth/load controls.

Eibenberger is now logged as a useful recoil-control lane: the known photon recoil mechanism predicts visibility reduction at roughly the paper absorption cross section. It strengthens the standard-QM compatibility of the record-kernel framing, but it does not close G11 because the absorption cross section is still extracted from visibility rather than independently measured as a held-out record distribution.

## Strict Claim

```text
We have a stronger lead candidate: Xiao gives a within-paper no-refit momentum-distribution prediction, and Kokorowski gives a second-experiment public no-refit decoherence prediction from independently reported many-photon parameters.
```

## Strict Non-Claims

- This does not solve collapse.
- This does not validate the Lambda/Gamma/Theta product law.
- This does not show physics beyond standard quantum mechanics.
- This does not repair the Chapman raw phase failure.

## Next Move

Tighten Kokorowski independent-kappa provenance or find a cleaner second no-refit target, then keep the breakthrough language blocked until Kokorowski stress, Chapman raw phase, and independent Lambda/Gamma/Theta product-law gates clear.
