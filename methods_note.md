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
Theta  = 1 - exp[-entropy_nats * record_survival_probability * environment_coupling]
```

These are intentionally simple and replaceable. Their role is to make the scaffold fit-ready, not to assert final apparatus physics.

## Quantum Eraser Branch

Unconditioned visibility is suppressed by both reversible marker entanglement and irreversible dephasing. Conditioning on the eraser basis removes the reversible marker factor, but leaves the irreversible dephasing factor:

```text
V_raw       = marker_visibility * eta
V_erased    = eta
eta         = exp(-2 * integral kappa(t) dt)
```

This reproduces the qualitative quantum eraser distinction: reversible which-path information can be erased; irreversible dephasing cannot.

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

## Limitations

The model is deliberately effective. It does not derive the Born rule, does not solve the measurement problem, and does not supersede environmental decoherence. Its intended scientific use is narrower: fit apparatus-parameterized visibility data and ask whether the Constraint Dynamics product factorization is empirically useful.
