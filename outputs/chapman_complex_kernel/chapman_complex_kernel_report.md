# Chapman Complex Kernel Report

Status: phase breaks or underdetermines the model

This pass tests Chapman Eq. (3) as a complex characteristic function:

```text
A(d) = integral P_eff(q) exp(i 2*pi*q*d/lambda) dq
visibility(d) = |A(d)|
phase(d) = unwrap(arg(A(d)))
```

- Source URL: https://chapmanlabs.gatech.edu/papers/scattering_ifm_prl95.pdf
- PDF SHA256: `27c288986e414efb43a776bd7c02b79208cba51beb1598e40915ceaa3c3f5b72`
- Visibility CSV: `data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv`
- Phase CSV: `data/extracted/CHAPMAN_1995_PHASE_DIGITIZED.csv`
- Phase extraction method: `rough_phase_digitization_v1`

## Model Comparison

- Raw scalar exponential RMSE: 0.0738
- Raw empirical sinc/Fourier RMSE: 0.0257
- Raw physical visibility-only RMSE: 0.0284
- Raw complex-kernel visibility RMSE: 0.0305
- Raw complex-kernel phase RMSE: 1.4733 rad

## Complex Phase Checks

- Raw observed / predicted small-d phase slope: 2.000 pi per d/lambda / 2.271 pi per d/lambda
- Case I accepted q center: 0.150
- Case III accepted q center: 2.000
- Case I / III predicted phase slopes: 0.231 / 3.367 pi per d/lambda
- Case I / III phase RMSE: 0.2578 / 0.4694 rad
- Case I / III visibility RMSE: 0.0230 / 0.0396
- Forward/backward center ordering recovered: True
- Forward/backward phase-slope ordering recovered: True

## Verdict

The complex kernel is an overconstrained test of the previous visibility-only story. A pass means the same inferred record distribution family can carry both contrast loss/revival and phase shift. A fail means the earlier Fourier visibility result remains interesting, but the stronger record-accessibility bridge is not yet validated.

Current binary verdict: **phase breaks or underdetermines the model**.

## What This Shows

Chapman continues to favor a Fourier/characteristic-function reading over scalar monotone dephasing for the raw curve. Adding phase makes the operational variable sharper: the relevant record is not generic scattering load, but the distribution of inaccessible or accepted transverse momentum-transfer records.

## What This Does Not Show

- It does not solve collapse.
- It does not validate the Lambda/Gamma/Theta product law.
- It does not show physics beyond standard quantum mechanics.
- It does not replace independent detector-acceptance geometry.
- The phase digitization is a rough first pass and should be upgraded before strong claims.
