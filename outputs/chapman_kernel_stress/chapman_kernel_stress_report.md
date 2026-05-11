# Chapman Kernel Stress Report

Status: fragile under current stress tests

This stress test asks whether the Chapman Fourier-kernel result survives visibility uncertainty and simple null controls. It uses the calibrated Chapman CSV as the empirical input and does not alter the source data.

- Source URL: https://chapmanlabs.gatech.edu/papers/scattering_ifm_prl95.pdf
- PDF SHA256: `27c288986e414efb43a776bd7c02b79208cba51beb1598e40915ceaa3c3f5b72`
- Extraction method: `calibrated_pixel_digitization_v1`
- Bootstrap samples: 1000
- Seed: 20260424

## Bootstrap Robustness

- P(raw sinc/Fourier beats exponential): 1.000
- P(raw first zero aligns with peak recoverable loss): 1.000
- P(conditioned sinc-family widths are narrower than raw): 0.752
- Raw sinc minus exponential RMSE, mean: -0.0415
- Raw sinc minus exponential RMSE, 95% CI: [-0.0545, -0.0257]
- Raw sinc first zero, median: 0.510
- Raw sinc first zero, 95% CI: [0.489, 0.525]

## Null Controls

- Pairing null probability of recovery alignment: 0.269
- Branch-label null probability of conditioned-width ordering: 0.724

The pairing null shuffles conditioned visibility values across x positions before recomputing the recovery peak. The branch-label null shuffles conditioned branch labels before testing whether both conditioned sinc-family widths remain narrower than raw.

## Verdict

Uncertainty criterion passed: False

Null-control criterion passed: False

This result should be read conservatively. A robust pass would support the claim that Chapman favors a record-bandwidth/Fourier-kernel interpretation over scalar monotone exponential dephasing within calibrated digitization limits. A fragile result means the kernel direction is still useful, but the current evidence should not be expanded beyond Chapman without better digitization or a second real experiment.

## What This Does Not Show

- It does not solve collapse.
- It does not validate the Lambda/Gamma/Theta product law.
- It does not show evidence beyond standard quantum mechanics.
- It does not replace independent detector-accessibility extraction.
