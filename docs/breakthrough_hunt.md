# Breakthrough Hunt

## Current Signal

The first-pass Chapman analysis found a strong recoverability window:

```text
raw visibility at d/lambda = 0.5:         0.04
best conditioned visibility at d/lambda = 0.5: 0.64
recoverable loss:                         0.60
recovery fraction:                        0.625
```

That is the most interesting result so far. It says the scaffold can separate visibility hidden in correlations from visibility unavailable after coarse-graining.

## What It Is Not

This is not a discovery of collapse dynamics and not a validation of the Lambda/Gamma/Theta product law. Chapman et al. explicitly explain the result with standard quantum mechanics: the atom becomes entangled with the scattered photon, and restricted acceptance of correlated atoms/photon directions recovers part of the contrast.

The original Chapman CSV is first-pass visual digitization. The upgraded calibrated extraction records pixel anchors, point picks, PDF hash, and source provenance. It is stronger than the first pass but still not a substitute for author-provided raw data.

## What It May Teach Constraint Dynamics

The useful refinement is about Theta. In this scaffold, Theta should not mean "energy was dissipated" in a simple thermodynamic sense. Chapman is elastic scattering, yet unconditioned visibility is lost when photon directions are traced over and partially regained when the record is filtered.

The better operational definition is:

```text
Theta = inaccessible durable record load
```

Accessible records can still carry which-path information, but they should not count as fully irreversible if a later conditioning operation can use them. V3 therefore includes `record_accessibility` as a factor that reduces effective Theta.

## Near-Term Breakthrough Test

A serious test needs two axes at once:

- Vary spatial distinguishability, giving a Lambda-like sweep.
- Independently vary record accessibility, from fully traced-out to selectively conditioned.

If the same apparatus can move visibility between raw loss, recoverable loss, and unrecoverable loss while the product-law parameterization predicts held-out branches, that would be the first genuinely interesting Constraint Dynamics result.

The scaffold now includes a synthetic version of this test:

```bash
python src/constraint_dynamics_quantum_v3.py benchmark-accessibility --output-dir outputs/accessibility_benchmark
```

This benchmark intentionally generates data from the accessibility-aware Theta definition, then asks whether a naive record-load product can fit it. Passing the benchmark is not evidence for the theory; it defines the empirical pattern that would matter.

The real-data push is the calibrated Chapman command:

```bash
python src/constraint_dynamics_quantum_v3.py digitize-chapman --pdf /tmp/chapman_prl95.pdf --output-dir outputs/chapman_digitization --data-dir data/extracted
python src/constraint_dynamics_quantum_v3.py decompose-eraser --input data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv --output-dir outputs/chapman_digitized
```

The criterion is strict: the recoverable-visibility window near d/lambda = 0.5 must remain after calibrated pixel extraction.

The calibrated pass retains that window:

```text
peak recovery fraction: 0.692 at d/lambda = 0.4
recovery fraction at d/lambda = 0.5: 0.646
raw / conditioned visibility at d/lambda = 0.5: 0.040 / 0.660
```

This strengthens the accessibility interpretation as an empirical target. It still does not validate the product law because detector acceptance and record accessibility have not been independently parameterized.

## Current Verdict

We have a stronger Chapman-backed target and a sharper theory variable. We do not yet have a breakthrough.
