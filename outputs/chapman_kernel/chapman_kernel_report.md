# Chapman Fourier-Kernel Report

Status: promising empirical structure

This analysis treats the Chapman visibility curves as characteristic functions of unresolved photon momentum-transfer records. It compares the scalar monotone exponential picture against an absolute sinc/Fourier-window kernel on the calibrated Chapman digitization.

- Input CSV: `data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv`
- Branches analyzed: raw, case_III_backward, case_I_forward
- Raw exponential RMSE: 0.0738
- Raw Gaussian-kernel RMSE: 0.0738
- Raw sinc/Fourier RMSE: 0.0257
- Raw exponential LOO RMSE: 0.1000
- Raw sinc/Fourier LOO RMSE: 0.0323

## Record-Bandwidth Proxy

- Raw sinc width: 1.961; first zero at d/lambda = 0.510
- Case I sinc width: 0.910; first zero at d/lambda = 1.099
- Case III sinc width: 1.481; first zero at d/lambda = 0.675
- Peak recoverable loss: 0.620 at d/lambda = 0.500
- Peak recovery fraction: 0.692 at d/lambda = 0.400

## What Would Be Interesting

- Fourier model beats exponential on raw Chapman: True
- Conditioned branches infer narrower sinc-family record bandwidth than raw: True
- Peak recoverable loss aligns with the raw Fourier zero near d/lambda = 0.5: True

## Interpretation

The calibrated data support a sharper operational reading of Theta for Chapman-like experiments: Theta is not merely scattering, entropy, or scalar dephasing strength. It behaves like inaccessible conjugate-record bandwidth. Raw loss follows from marginalizing over a broad photon momentum-transfer record; conditioned recovery follows from narrowing that record window.

The Gaussian kernel is included as a monotone characteristic-function baseline. In this one-dimensional visibility fit it is effectively another exponential-in-d-squared model, so its role is mainly to distinguish monotone bandwidth decay from the sinc zero-and-revival structure.

## What This Does Not Show

- It does not solve collapse.
- It does not validate the Lambda/Gamma/Theta product law.
- It does not show evidence beyond standard quantum mechanics.
- It does not yet use an independently extracted detector-accessibility proxy.
