# Experimental Design Notes

The hardest problem is not curve fitting. It is separating Lambda, Gamma, and Theta in real apparatus data.

## The Identifiability Problem

If better spatial selectivity, faster timing, and stronger irreversible records all improve together as a single "detector quality" knob, then many models can appear to work. A product law can win without proving that the factors are independently meaningful.

V3 now includes:

```bash
python src/constraint_dynamics_quantum_v3.py design --input your_data.csv --output-dir outputs/design_diagnostics
python src/constraint_dynamics_quantum_v3.py benchmark-designs --output-dir outputs
```

The diagnostics report:

- Pairwise correlations among `Lambda`, `Gamma`, and `Theta`.
- Variance inflation factors for the three constraint factors.
- Condition number of the full second-order design matrix.
- Ranges covered by each factor.

## Suggested Apparatus Manipulations

### Lambda Sweep: Spatial Selectivity

Goal: vary path distinguishability while holding temporal bandwidth and record irreversibility approximately fixed.

Possible knobs:

- Slit/path separation.
- Detector point-spread width.
- Imaging optics resolution.
- Spatial mode overlap at the which-path marker.

Keep fixed:

- Detector timing window.
- Record storage/amplification.
- Total photon flux and coincidence window.

### Gamma Sweep: Timing/Bandwidth

Goal: vary temporal path resolution while holding spatial selectivity and irreversible record load approximately fixed.

Possible knobs:

- Detector gate width.
- Coincidence timing window.
- Detector response time.
- Coherence time of the source.
- Bandwidth filtering.

Keep fixed:

- Spatial path geometry.
- Marker overlap.
- Record gain/amplification.

### Theta Sweep: Irreversible Record Load

Goal: vary durable environmental record formation while holding reversible marker overlap and raw distinguishability as stable as possible.

Possible knobs:

- Detector amplification gain.
- Whether a record is latched, erased, dumped, or thermally amplified.
- Coupling to uncontrolled environmental modes.
- Record retention time.
- Temperature or thermal load, if it changes record durability without changing path geometry.

Keep fixed:

- Marker angle or overlap.
- Spatial distinguishability.
- Timing window.

## Minimum Useful Dataset

A credible first dataset should include:

- At least three levels per factor.
- Replicates at each condition.
- One-factor sweeps plus a balanced factorial subset.
- Raw and conditioned eraser visibilities where possible.
- Direct records of apparatus settings, not only inferred Lambda/Gamma/Theta.
- Observation uncertainty or bootstrap standard errors for visibility.

## What Would Count Against the Product Law

- Additive or pairwise models win on held-out balanced-factorial data.
- The product coefficient is unstable across apparatus families.
- High product-law evidence appears only in confounded designs with large factor correlations.
- Conditioned eraser visibility depends on delayed-choice timing in the absence of irreversible record lock-in.
- A standard decoherence nuisance parameter absorbs the apparent Theta dependence.

## Practical Interpretation of Diagnostics

These are rules of thumb, not hard laws:

- `max_abs_factor_correlation < 0.3`: good separation.
- `0.3-0.7`: usable, but model comparison should be treated cautiously.
- `> 0.7`: strong confounding; product-law wins are suggestive at best.
- `full_second_order_condition_number > 1000`: coefficients in flexible models are likely unstable.
- `VIF > 5`: factor-level interpretation is fragile.

The scaffold should prefer failed clean tests over impressive ambiguous fits. A falsifiable model earns its keep by showing where it can be wrong.

## Literature-Derived Data

Candidate real-data sources and extraction priorities are tracked in [literature_data_plan.md](literature_data_plan.md) and `data/literature_study_register.csv`. The first extraction target should be Chapman et al. 1995 because it is the cleanest spatial distinguishability sweep and includes a recovery branch.
