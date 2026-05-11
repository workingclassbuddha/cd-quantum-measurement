# Chapman Complex Mixture Report

Status: model still fails

This pass tests whether the raw phase failure in the simple complex-kernel model is repaired by adding Chapman-style 0/1/2-photon mixture terms and optional velocity/phase smearing.

```text
A_raw(d) = w0*A0(d) + w1*A1(d) + w2*A2(d)
A2(d) ~= A1(d)^2
```

- Source URL: https://chapmanlabs.gatech.edu/papers/scattering_ifm_prl95.pdf
- PDF SHA256: `27c288986e414efb43a776bd7c02b79208cba51beb1598e40915ceaa3c3f5b72`
- Visibility CSV: `data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv`
- Phase CSV: `data/extracted/CHAPMAN_1995_PHASE_DIGITIZED.csv`
- Best raw mixture model: `complex_mixture_with_smear`

## Raw Phase Repair Test

- Simple beta complex raw visibility RMSE: 0.0305
- Simple beta complex raw phase RMSE: 1.4733 rad
- Best mixture raw visibility RMSE: 0.0652
- Best mixture raw phase RMSE: 1.3088 rad
- Best mixture stable-phase RMSE: 1.1337 rad
- Best mixture wrap-sensitive phase RMSE: 1.6355 rad
- Empirical raw sinc/Fourier visibility RMSE: 0.0257

## Best Mixture Parameters

- w0 / w1 / w2: 0.060 / 0.900 / 0.040
- one-photon beta alpha / beta: 1.500 / 1.100
- velocity sigma: 0.500

## Conditioned Branch Check

- Case I accepted q center: 0.000
- Case III accepted q center: 2.000
- Case I / III predicted phase slopes: 0.146 / 3.224 pi per d/lambda
- Forward/backward center ordering recovered: True
- Forward/backward phase-slope ordering recovered: True

## Verdict

Current binary verdict: **model still fails**.

`raw phase repaired` requires substantial full raw-phase improvement, competitive raw visibility, and preserved conditioned ordering. `digitization-limited` means the stable raw phase looks repairable while wrap-sensitive points dominate the failure. `model still fails` means added mixture freedom does not rescue the raw complex phase.

## What This Does Not Show

- It does not solve collapse.
- It does not validate the Lambda/Gamma/Theta product law.
- It does not establish physics beyond standard quantum mechanics.
- The 0-photon and 2-photon terms are fitted effective components, not independent measurements.
- If this fails, the next step is publication-grade Fig. 2 phase digitization, not more model freedom.
