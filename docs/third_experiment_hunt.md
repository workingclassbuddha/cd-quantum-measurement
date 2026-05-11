# Third Experiment Hunt

## Current Position

Chapman and Xiao now form the strongest empirical spine of the project:

- Chapman supports a Fourier/record-kernel reading of visibility loss and recovery in unresolved photon-scattering records.
- Xiao supports a no-refit distribution-to-visibility bridge using a reconstructed momentum-disturbance distribution.

The next experiment should not add model freedom. It should test whether the refined Constraint Dynamics variable remains useful when the record is plainly environmental and irreversible.

## Recommended Third Dataset

Build the next pass on Hackermueller et al. 2004, *Decoherence of matter waves by thermal emission of radiation*:

- arXiv: https://arxiv.org/abs/quant-ph/0402146
- DOI: https://doi.org/10.1038/nature02276
- Scout status: source package available and extracted.
- Key figure: `Figure4.eps`, decoherence curves of visibility vs heating power / molecular temperature.
- Secondary figure: `Figure3.eps`, spectral photon emission rate used for the decoherence model.

Scientific reason:

```text
Thermal photon emission is an inaccessible, durable environmental record.
```

That makes Hackermueller the cleanest held-out test of Theta as record load rather than merely a fitted dephasing coefficient.

## Backup Dataset

Hornberger et al. 2003, *Collisional decoherence observed in matter wave interferometry*:

- arXiv: https://arxiv.org/abs/quant-ph/0303093
- DOI: https://doi.org/10.1103/PhysRevLett.90.160401
- Scout status: source package available and extracted.
- Key figure: `fig2.eps`, fringe visibility vs methane gas pressure.
- Secondary figure: `fig3.eps`, decoherence pressure for several gases.

This is an excellent irreversible scattering control. It is slightly less exciting than Hackermueller because pressure damping is expected to be close to monotone exponential decay, but that also makes it a good falsification guardrail.

## Proposed Commands

```bash
python src/constraint_dynamics_quantum_v3.py digitize-hackermueller-thermal \
  --source-dir outputs/tmp/third_hunt_sources/hackermueller \
  --output-dir outputs/hackermueller_thermal_digitization \
  --data-dir data/extracted

python src/constraint_dynamics_quantum_v3.py analyze-thermal-decoherence \
  --input data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZED.csv \
  --output-dir outputs/hackermueller_thermal
```

## First Implementation Result

The first Hackermueller pass is now implemented as scout-grade seeded Figure 4 digitization plus a thermal-load analysis:

```text
data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZED.csv
data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZATION.json
outputs/hackermueller_thermal_digitization/hackermueller_digitization_report.md
outputs/hackermueller_thermal/thermal_decoherence_summary.csv
outputs/hackermueller_thermal/thermal_decoherence_predictions.csv
outputs/hackermueller_thermal/hackermueller_thermal_report.md
```

Current combined-model result:

```text
thermal_delta_T4 RMSE: 0.0767
exp_power2 RMSE: 0.0802
thermal_temperature_excess RMSE: 0.0911
exp_power RMSE: 0.0923
```

The stress pass now gives:

```text
status: thermal record-load survives uncertainty
P(thermal_delta_T4 beats exp_power): 0.994
P(thermal_delta_T4 beats exp_power2): 0.701
P(thermal_delta_T4 is best model): 0.701
thermal RMSE 95% CI: [0.0686, 0.0949]
```

This is encouraging, but still not a beyond-QM claim. It says the thermal record-load proxy survives the current uncertainty model and is worth upgrading further with fully automated vector/pixel extraction.

## Success Criteria

- The digitization includes figure provenance, EPS SHA256, axis anchors, point extraction uncertainty, and source metadata.
- The analysis separates normalized visibility from count-rate/fragmentation effects.
- A thermal-emission/load proxy is compared against a plain exponential-in-power baseline.
- The report says explicitly whether this strengthens, weakens, or merely repeats standard decoherence expectations.

## Strict Scientific Boundary

The strongest allowed claim after a successful Hackermueller pass is:

```text
Chapman, Xiao, and Hackermueller jointly support record accessibility/load as a useful empirical organizing variable across standard-QM measurement and decoherence experiments.
```

This would still not validate the Lambda/Gamma/Theta product law, solve collapse, or show physics beyond standard quantum mechanics.
