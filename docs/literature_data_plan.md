# Literature-Derived Data Plan

This document turns the next research step into a concrete data program. The goal is to collect visibility measurements from primary experiments and test whether Constraint Dynamics gives a better apparatus factorization than simpler alternatives.

## Current Register

Candidate studies are listed in:

```text
data/literature_study_register.csv
```

The extraction template is:

```text
data/literature_observation_template.csv
```

No numeric literature points are treated as real data until they have a `study_id`, figure/panel provenance, extraction method, and notes.

First-pass extracted points currently live at:

```text
data/extracted/CHAPMAN_1995_SCATTER.csv
```

Calibrated pixel-digitized points and provenance live at:

```text
data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv
data/extracted/CHAPMAN_1995_DIGITIZATION.json
```

The calibrated points are stronger than the first pass, but they remain extracted from a paper figure rather than author-provided raw data.

## Highest-Priority Sources

### 1. Chapman et al. 1995: photon scattering in an atom interferometer

Why it matters:

- It sweeps path separation at the scattering point, which is the cleanest Lambda-like manipulation found so far.
- It reports both loss of contrast and partial recovery by selecting atoms correlated with restricted photon directions.
- It gives a direct test of the model's reversible-vs-unrecoverable boundary.

Primary source:

- https://doi.org/10.1103/PhysRevLett.75.3783
- Accessible PDF used during scouting: https://chapmanlabs.gatech.edu/papers/scattering_ifm_prl95.pdf

Extraction target:

- Fig. 2: relative contrast versus path separation.
- Fig. 3: recovered contrast under restricted momentum acceptance.
- Current status: calibrated pixel digitization complete for Fig. 2 and two Fig. 3 conditioned branches.

Initial mapping:

```text
Lambda = f(path separation / photon wavelength)
Gamma  = fixed or weakly varying
Theta  = high for traced-out photon directions, lower for accessible/postselected records
marker_visibility = 1 unless a separate reversible marker is modeled
```

### 2. Hackermueller et al. 2004: thermal emission decoherence

Why it matters:

- It varies thermal radiation, a strong Theta-like irreversible environmental record.
- It is closer to standard decoherence theory than quantum eraser demonstrations.
- It provides a good stress test of whether Theta is just a relabeling of known decoherence rate or adds useful factorization.

Primary source:

- https://doi.org/10.1038/nature02276
- arXiv: https://arxiv.org/abs/quant-ph/0402146

Extraction target:

- Decoherence curves / visibility ratio versus heating power or internal temperature.

Initial mapping:

```text
Theta = f(thermal photon emission load)
Lambda = fixed by interferometer geometry
Gamma  = fixed unless velocity/coherence-time bins are separated
```

### 3. Hornberger et al. 2003: collisional decoherence

Why it matters:

- It sweeps gas pressure/collision rate, another strong Theta-like environmental record.
- It is quantitative and directly about loss of spatial coherence.

Primary source:

- https://doi.org/10.1103/PhysRevLett.90.160401
- arXiv: https://arxiv.org/abs/quant-ph/0303093

Extraction target:

- Visibility ratio versus gas pressure or collision probability.

Initial mapping:

```text
Theta = f(collision probability or gas-pressure-derived decoherence load)
Lambda = fixed
Gamma  = fixed
```

### 4. Kwiat, Steinberg, and Chiao 1992: quantum eraser

Why it matters:

- It is a clean reversible-marker experiment.
- It reports how erasure degree controls restored interference.

Primary source:

- https://doi.org/10.1103/PhysRevA.45.7729

Extraction target:

- Visibility versus relative polarizer orientation.

Initial mapping:

```text
marker_visibility = f(polarizer geometry)
Theta = near zero for reversible marking
Lambda/Gamma = fixed
```

## Near-Term Workflow

1. Digitize only one figure at a time.
2. Store points in a study-specific CSV under `data/extracted/`.
3. Add a provenance row to `data/literature_observation_template.csv` or a derived observation file.
4. Run:

```bash
python src/constraint_dynamics_quantum_v3.py decompose-eraser --input data/extracted/<study>.csv --output-dir outputs/<study>_eraser
python src/constraint_dynamics_quantum_v3.py design --input data/extracted/<study>.csv --output-dir outputs/<study>_design
python src/constraint_dynamics_quantum_v3.py fit --input data/extracted/<study>.csv --output-dir outputs/<study>_fit
```

For Chapman specifically, regenerate the extraction with:

```bash
python src/constraint_dynamics_quantum_v3.py digitize-chapman --pdf /tmp/chapman_prl95.pdf --output-dir outputs/chapman_digitization --data-dir data/extracted
```

5. Run `design` and `fit` only after the extracted file has complete `Lambda`/`Gamma`/`Theta` columns or complete apparatus columns. The first-pass Chapman CSV is currently ready for eraser decomposition, not product-law fitting.
6. Do not combine studies until each single-study mapping has been documented.

## Interpretation Rules

- Single-factor sweeps can validate pieces of the mapping but cannot prove the product law.
- Combined cross-study fitting is exploratory unless calibration differences are modeled.
- A balanced new experiment is more valuable than a large confounded literature aggregate.
- A null result is useful if the factor mapping and extraction provenance are clean.
