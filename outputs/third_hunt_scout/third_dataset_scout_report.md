# Third Dataset Scout Report

## Question

After Chapman and Xiao, the next useful test should be a held-out experiment where an independently controlled environmental record variable predicts interference loss without adding Chapman-specific or Xiao-specific freedom.

The target is not a collapse claim. The target is a stricter operational test of:

```text
Theta = inaccessible durable record load / bandwidth
```

## Sources Checked

### Hackermueller et al. 2004

- Source: https://arxiv.org/abs/quant-ph/0402146
- Journal DOI: https://doi.org/10.1038/nature02276
- arXiv source package: available and extracted under ignored scratch space.
- Extracted source files: `Figure1_150dpi.eps`, `Figure2.eps`, `Figure3.eps`, `Figure4.eps`, `letter.tex`.
- Best figure target: `Figure4.eps`, captioned as decoherence curves showing interference visibility as a function of laser heating power and molecular temperature.
- Secondary target: `Figure3.eps`, spectral photon emission rate used for the decoherence calculation.

Verdict: build next.

Reason: this is the cleanest held-out empirical lane for Theta as an inaccessible environmental record variable. Heating power/internal temperature changes the thermal photon emission load while the Talbot-Lau geometry is fixed. That lets the scaffold ask whether the CD language gives a clean operational variable without pretending to beat standard decoherence theory.

### Hornberger et al. 2003

- Source: https://arxiv.org/abs/quant-ph/0303093
- Journal DOI: https://doi.org/10.1103/PhysRevLett.90.160401
- arXiv source package: available and extracted under ignored scratch space.
- Extracted source files: `fig1.eps`, `fig2.eps`, `fig3.eps`, `stossletter.tex`.
- Best figure target: `fig2.eps`, fullerene fringe visibility vs methane gas pressure.
- Secondary target: `fig3.eps`, decoherence pressure for several gases.

Verdict: strong backup.

Reason: this is a clean irreversible environmental scattering sweep. It is excellent for checking whether Theta-as-record-load remains honest in a standard collisional decoherence setting. It is less likely to produce a breakthrough-shaped Fourier signal because the expected behavior is close to monotone exponential pressure damping.

### Durr/Nonn/Rempe 1998

- Source checked: APS PRL record and Nature record.
- Journal DOI: https://doi.org/10.1103/PhysRevLett.81.5705
- Scout issue: no clean arXiv figure source was found in the quick pass. One arXiv e-print candidate was unrelated.

Verdict: defer.

Reason: it remains a good complementarity guardrail, but it is not the best immediate route to a record-bandwidth or record-load breakthrough test.

## Recommended Next Implementation

Build Hackermueller first:

```bash
python src/constraint_dynamics_quantum_v3.py digitize-hackermueller-thermal \
  --source-dir outputs/tmp/third_hunt_sources/hackermueller \
  --output-dir outputs/hackermueller_thermal_digitization \
  --data-dir data/extracted

python src/constraint_dynamics_quantum_v3.py analyze-thermal-decoherence \
  --input data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZED.csv \
  --output-dir outputs/hackermueller_thermal
```

Minimum artifacts:

```text
data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZED.csv
data/extracted/HACKERMUELLER_2004_THERMAL_DIGITIZATION.json
outputs/hackermueller_thermal_digitization/hackermueller_digitization_report.md
outputs/hackermueller_thermal/thermal_decoherence_summary.csv
outputs/hackermueller_thermal/thermal_decoherence_predictions.csv
outputs/hackermueller_thermal/hackermueller_thermal_report.md
```

## What Would Be Interesting

- A record-load variable derived from heating power / temperature / photon-emission rate predicts normalized visibility without refitting an arbitrary visibility curve.
- The inferred Theta-like load is monotone and externally interpretable.
- The result survives a pressure-style null by not merely tracking count-rate loss or plotting-axis artifacts.
- Chapman/Xiao/Hackermueller can be written as three versions of the same operational sentence: interference visibility is controlled by the accessible or inaccessible conjugate record made available to the environment.

## What Would Falsify The Next Step

- Visibility is extractable, but the independent thermal-emission proxy is too indirect to define without fitting the same curve.
- The figure provenance is too weak to separate visibility loss from count-rate/fragmentation effects.
- A simple exponential in heating power performs just as well and no independent emission-load mapping improves interpretation.
- The result cannot be stated without exceeding standard decoherence theory.

## Strict Verdict

No breakthrough yet. The project now has a strong two-experiment structure:

```text
Chapman: Fourier record kernel from unresolved photon momentum records.
Xiao: no-refit distribution-to-visibility bridge from reconstructed momentum disturbance.
```

The best next move is Hackermueller 2004 because it tests the irreversible, durable-record side of Theta in a different matter-wave platform. If it works, the claim becomes broader but still conservative: record accessibility/load is a useful empirical organizing variable across multiple standard-QM experiments.
