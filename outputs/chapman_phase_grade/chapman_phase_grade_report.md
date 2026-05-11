# Chapman Phase-Grade Report

Status: phase still fails

This pass redigitizes Chapman Fig. 2 raw phase as displayed phase plus explicit unwrap and quality labels. It then reruns the complex and mixture models on all phase points and on a high-confidence raw subset.

- Source URL: https://chapmanlabs.gatech.edu/papers/scattering_ifm_prl95.pdf
- PDF SHA256: `27c288986e414efb43a776bd7c02b79208cba51beb1598e40915ceaa3c3f5b72`
- Phase extraction method: `calibrated_phase_pixel_digitization_v1`
- Fit grid mode: `focused`
- Phase CSV: `data/extracted/CHAPMAN_1995_PHASE_GRADED.csv`
- Raw phase rows: 21
- High-confidence raw phase rows used in masked fits: 16

## Raw Phase Fit Comparison

- All-points simple complex raw phase RMSE: 1.4753 rad
- All-points best mixture raw phase RMSE: 1.8943 rad
- High-confidence simple complex raw phase RMSE: 1.6207 rad
- High-confidence best mixture raw phase RMSE: 1.6390 rad
- High-confidence simple / mixture raw visibility RMSE: 0.0592 / 0.0525
- All-points mixture raw visibility RMSE: 0.0786

## Phase Quality

- Raw high-quality picks: 9
- Raw medium-quality picks: 7
- Raw low-quality or wrap-sensitive picks: 5

## Conditioned Branch Check

- Case I / III accepted q centers: 0.000 / 2.000
- Case I / III predicted phase slopes: 0.275 / 3.210 pi per d/lambda
- Forward/backward center ordering recovered: True
- Forward/backward phase-slope ordering recovered: True

## Verdict

Current binary verdict: **phase still fails**.

`phase-grade repairs full raw phase` means the model survives all graded phase points. `phase failure is wrap-limited` means the high-confidence raw phase subset is compatible while ambiguous wrap/low-contrast points dominate the failure. `phase still fails` means the raw phase problem remains after quality masking.

## What This Does Not Show

- It does not solve collapse.
- It does not validate the Lambda/Gamma/Theta product law.
- The phase picks are calibrated and quality-labeled, but still manual.
- A positive masked result would require independent replication or a second experiment.
