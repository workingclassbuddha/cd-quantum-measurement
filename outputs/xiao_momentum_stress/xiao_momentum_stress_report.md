# Xiao Momentum Stress Report

Status: xiao relation survives uncertainty

This stress test asks whether the Xiao momentum-disturbance relation survives digitization uncertainty and a simple pairing-null control. It jitters visibility and momentum values using the stored extraction uncertainties, then refits the same model families used by `analyze-xiao-momentum`.

- Input CSV: `data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv`
- Digitization JSON: `data/extracted/XIAO_2019_MOMENTUM_DIGITIZATION.json`
- Source SHA256: `d2d51429e956de450ad66029e16ebdbdd8f162b0cd39a458f8ac4bf35f028213`
- Bootstrap samples: 1000
- Seed: 20260424

## Robust Quantities

- P(linear bandwidth beats published bound): 1.000
- P(linear bandwidth beats scaled-loss fit): 1.000
- P(all points remain above published bound): 1.000
- P(momentum remains monotone with visibility loss): 1.000
- Linear slope 95% CI: [0.6665, 0.7047]
- Pearson r 95% CI: [0.9985, 0.9999]

## Null Control

- Pairing-null P(Pearson r >= observed): 0.004
- Pairing-null P(linear RMSE <= observed): 0.004

## Interpretation

The Xiao relation is a useful cross-experiment stress target only if it survives visibility/momentum jitter and is not reproduced by shuffling the momentum values across visibility settings. A robust result supports the narrower claim that an independently reconstructed momentum-record scale tracks visibility loss.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not solve collapse.
- It does not require Bohmian mechanics as an ontology.
- It does not repair the Chapman raw-phase failure.
