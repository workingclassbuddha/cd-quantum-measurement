# Hornberger Collisional Decoherence Scout

Status: collisional record-load guardrail supports standard decoherence

This scout adds Hornberger et al. 2003 as a conservative collisional-decoherence control. It is not the missing Xiao-like no-refit distribution test. It asks whether a plain environmental collision record-load variable behaves as standard decoherence predicts.

- Source URL: https://arxiv.org/abs/quant-ph/0303093
- DOI: https://doi.org/10.1103/PhysRevLett.90.160401
- Source SHA256: `6b5c170322c909b961f45710ff09e96c2bd9379d67363ac4c7dfb862d541ce76`
- Extraction method: `manual_eps_render_scout_v1`
- Fig. 2 methane rows: 19
- Fig. 3 gas-species rows: 9

## Methane Visibility Fit

- Fitted V0: 38.45 %
- Fitted decoherence pressure p_v: 0.807 x 10^-6 mbar
- RMSE visibility: 0.888 percentage points

## Gas-Species Guardrail

- Theory-vs-experiment pressure RMSE: 0.185 x 10^-6 mbar
- Theory-vs-experiment pressure correlation: 0.888
- CH4 Fig. 3 pressure: 0.810 x 10^-6 mbar
- Fig. 2 methane p_v minus Fig. 3 CH4 pressure: -0.003 x 10^-6 mbar

## Interpretation

Hornberger is a guardrail, not a breakthrough lane. It supports the boring but important point that irreversible environmental records should decohere monotonically and quantitatively under standard theory. That helps keep the Constraint Dynamics language honest: record load is useful only if it organizes data without pretending every visibility loss is a new Fourier revival problem.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not provide an independently measured record distribution like Xiao.
- It does not show physics beyond standard quantum mechanics.
