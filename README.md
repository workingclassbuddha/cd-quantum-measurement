# Constraint Dynamics Quantum Measurement Test

Exploratory, falsifiable scaffold for testing whether Constraint Dynamics gives a useful effective factorization of apparatus-dependent quantum visibility loss.

The central V3 hypothesis is:

```text
kappa_eff = kappa0 * Lambda * Gamma * Theta
visibility_raw = marker_visibility * exp(-2 * kappa_eff * t_eff)
```

This is not a derivation of wavefunction collapse. It is not a replacement for standard decoherence theory. It is a compact way to ask whether spatial selectivity, temporal resolution, and irreversible record load explain measurement-induced classicalization better than constant, additive, or pairwise parameterizations.

## What V3 Adds

- Joint path-plus-marker density matrix for reversible which-path marking.
- Quantum eraser conditioning that restores only reversible marker information.
- Timing-aware delayed-choice branch: delay matters only when an irreversible record has begun to lock in.
- Stochastic phase-flip trajectory simulation whose ensemble reproduces the master-equation dephasing curve.
- Apparatus-to-constraint mappings for Lambda, Gamma, and Theta.
- Model comparison across constant, product, additive, pairwise, and extended interaction laws using AICc, BIC, Akaike weights, and k-fold cross-validation.
- Identifiability diagnostics for deciding whether a dataset actually separates Lambda, Gamma, and Theta.
- Eraser decomposition utility for paired raw/conditioned literature visibility data.

## Quick Start

Install dependencies in your preferred Python environment:

```bash
python -m pip install -r requirements.txt
```

Generate the demo outputs:

```bash
python src/constraint_dynamics_quantum_v3.py demo --output-dir outputs --data-dir data
```

Fit your own visibility dataset:

```bash
python src/constraint_dynamics_quantum_v3.py fit --input data/visibility_fit_template.csv --output-dir outputs
```

Diagnose whether a dataset is separable enough to interpret:

```bash
python src/constraint_dynamics_quantum_v3.py design --input data/visibility_fit_template.csv --output-dir outputs/design_diagnostics
```

Decompose paired raw/conditioned quantum eraser visibility data:

```bash
python src/constraint_dynamics_quantum_v3.py decompose-eraser --input data/extracted/CHAPMAN_1995_SCATTER.csv --output-dir outputs/chapman
```

Generate the balanced-vs-confounded benchmark:

```bash
python src/constraint_dynamics_quantum_v3.py benchmark-designs --output-dir outputs
```

## Repository Layout

```text
README.md
theory_notes.md
methods_note.md
docs/literature_review.md
docs/experimental_design.md
docs/literature_data_plan.md
docs/v2_audit.md
src/constraint_dynamics_quantum_v3.py
data/visibility_fit_template.csv
data/literature_study_register.csv
data/extracted/CHAPMAN_1995_SCATTER.csv
outputs/figures/
outputs/chapman/
outputs/demo_fit_summary.csv
```

## Demo Figures

![Raw and conditioned eraser patterns](outputs/figures/figure_quantum_eraser_patterns.svg)

![Delayed choice timing](outputs/figures/figure_delayed_choice_timing.svg)

![Trajectory convergence](outputs/figures/figure_trajectory_convergence.svg)

![Model comparison](outputs/figures/figure_model_comparison.svg)

![Identifiability conditioning](outputs/figures/figure_identifiability_conditioning.svg)

## Minimal Data Schema

You can provide either direct constraint columns:

```text
Lambda,Gamma,Theta,marker_visibility,t_meas,visibility_obs
```

or apparatus columns that V3 maps into constraints:

```text
path_separation,detector_spatial_resolution,coherence_time,
detector_response_time,record_entropy_bits,
record_survival_probability,environment_coupling,
marker_angle,t_meas,visibility_obs
```

`visibility_se` is optional and used as a fitting weight when present.

## Limits

The model respects standard quantum eraser behavior: reversible path marking can suppress raw interference, conditioned eraser data can recover it, and irreversible dephasing cannot be recovered by changing the marker basis later. The claims here remain effective and phenomenological until real apparatus datasets can discriminate the product law from alternatives.

Use [docs/experimental_design.md](docs/experimental_design.md) before taking a product-law fit seriously. The scaffold now treats high factor correlation and poor design conditioning as first-class warnings rather than afterthoughts.

The included Chapman extraction is a first-pass visual digitization from the paper PDF, intended to exercise the workflow and identify promising signals. It should be replaced by publication-grade digitization before making quantitative claims.
