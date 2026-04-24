# Methods Note

## Purpose

This project implements a minimal effective model for two-path interference with reversible which-path marking, irreversible path dephasing, delayed erasure, stochastic trajectories, and apparatus-level model comparison.

## State Model

The quantum state is a path qubit tensored with a marker qubit:

```text
|psi> = (|L>|m_L> + exp(i phi)|R>|m_R>) / sqrt(2)
```

The marker states are parameterized by an angle `alpha`, with raw reversible marker visibility:

```text
marker_visibility = |<m_L|m_R>| = |cos(alpha)|
```

Irreversible measurement dephasing acts on the path off-diagonal terms:

```text
rho_LR(t) = rho_LR(0) * exp(-2 * integral kappa(t) dt)
```

The Constraint Dynamics product-law hypothesis sets:

```text
kappa_eff = kappa0 * Lambda * Gamma * Theta
```

## Apparatus-to-Constraint Maps

The default maps are saturating and dimensionless:

```text
Lambda = 1 - exp[-0.5 * (path_separation / detector_spatial_resolution)^2]
Gamma  = 1 - exp[-(coherence_time / detector_response_time)^2]
Theta  = 1 - exp[-entropy_nats * record_survival_probability * environment_coupling * (1 - record_accessibility)]
```

These are intentionally simple and replaceable. Their role is to make the scaffold fit-ready, not to assert final apparatus physics.

`record_accessibility` captures the Chapman-style lesson that a record can be entangling without being operationally irreversible. A traced-out photon direction or detector reservoir contributes strongly to Theta; a record still available for postselection or erasure contributes less.

## Quantum Eraser Branch

Unconditioned visibility is suppressed by both reversible marker entanglement and irreversible dephasing. Conditioning on a suitable eraser basis can remove the reversible marker factor, but leaves the irreversible dephasing factor:

```text
V_raw            = marker_visibility * eta
V_erased_optimal = eta
eta              = exp(-2 * integral kappa(t) dt)
```

The fixed plus/minus eraser basis included in the demo is intentionally not guaranteed to be optimal for every marker angle; it can recover less than `eta`. The optimal branch is the bound used to check physical consistency. This reproduces the qualitative quantum eraser distinction: reversible which-path information can be erased; irreversible dephasing cannot.

## Delayed Choice

V3 separates clock delay from irreversible record formation. The record lock-in fraction grows only after `record_onset_time`. An eraser before record lock-in prevents later amplification into a durable path record; an eraser after lock-in cannot undo the exposure already accumulated.

This is an effective timing model, not a relativistic account of delayed-choice experiments.

## Stochastic Trajectories

The master equation is represented by a phase-flip unraveling. Each trajectory remains pure. Random path `Z` flips occur with Poisson rate `kappa(t)`. The ensemble average reproduces the Lindblad-style dephasing curve:

```text
E[(-1)^N] = exp(-2 * integral kappa(t) dt)
```

The generated trajectory figure compares the stochastic ensemble mean with the analytic master-equation expectation.

## Model Comparison

The fitter transforms visibility to an effective dephasing target:

```text
y = -log(visibility_obs / marker_visibility) / (2 * t_meas)
```

It then compares constant, product, product-plus-background, additive, additive-plus-background, pairwise, pairwise-plus-product, and full second-order laws. Reported metrics include RMSE, visibility MAE, AICc, BIC, Akaike weight, and k-fold cross-validation RMSE.

## Eraser Decomposition

The `decompose-eraser` command accepts paired raw and conditioned visibility rows. For each matched x-value, it treats the best conditioned branch as a first-pass estimate of the irreversible visibility bound:

```text
eta_irreversible_hat = max(V_raw, best V_conditioned)
marker_visibility_hat = V_raw / eta_irreversible_hat
recoverable_loss = eta_irreversible_hat - V_raw
unrecoverable_loss = 1 - eta_irreversible_hat
```

This is bookkeeping, not a derivation. Its purpose is to separate "visibility hidden in correlations" from "visibility lost to durable dephasing" before attempting a Lambda/Gamma/Theta fit.

## Identifiability Diagnostics

The `design` command checks whether a dataset can actually distinguish the three proposed factors. It reports factor correlations, variance inflation factors, factor ranges, and the condition number of the full second-order feature matrix. The benchmark command compares a balanced factorial synthetic design with a confounded latent-load design where Lambda, Gamma, and Theta rise together.

The intended interpretation is conservative: a product-law win in a confounded design is not strong evidence for the theory. It only becomes meaningful when the same law predicts held-out data in designs where spatial selectivity, timing resolution, and record irreversibility have been varied independently.

## Accessibility Benchmark

The `benchmark-accessibility` command varies path separation and record accessibility independently. It compares an accessibility-aware product law against a naive record-load product that treats all records as inaccessible. This is a falsification target rather than a claim of empirical success: real experiments would need to show the same two-axis visibility surface before the refined Theta variable earns its keep.

## Limitations

The model is deliberately effective. It does not derive the Born rule, does not solve the measurement problem, and does not supersede environmental decoherence. Its intended scientific use is narrower: fit apparatus-parameterized visibility data and ask whether the Constraint Dynamics product factorization is empirically useful.
