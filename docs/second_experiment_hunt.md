# Second Experiment Hunt

## Goal

Chapman is now a useful boundary case:

- Visibility strongly favors a Fourier/record-bandwidth interpretation over monotone scalar dephasing.
- Conditioned branches recover a forward/backward acceptance-window structure.
- Raw phase still breaks the current complex Chapman model family.

The next experiment should not add more freedom to Chapman. It should provide an independent empirical axis for the refined Constraint Dynamics language:

```text
Theta = inaccessible conjugate-record bandwidth
```

The strongest useful second dataset is one where the record bandwidth, momentum disturbance, or complex eraser phase is observed directly enough that the scaffold is not merely fitting visibility curves.

## Ranked Candidates

| Rank | Experiment | Primary source | What it gives | Extraction feasibility | Verdict |
| --- | --- | --- | --- | --- | --- |
| 1 | Xiao, Wiseman, Xu, Kedem, Li, Guo 2019, double-slit which-way momentum disturbance | https://arxiv.org/abs/1805.02059 and https://doi.org/10.1126/sciadv.aav9547 | Direct relation between fringe visibility and measured Bohmian momentum-disturbance distribution in partial which-way measurements | High. arXiv source includes separate vector PDFs: `visibility.pdf`, `probability.pdf`, `trajv.pdf`, plus TeX methods | Best next target |
| 2 | Cormann, Remy, Kolaric, Caudano 2016, quantum eraser modular/weak values | https://arxiv.org/abs/1508.01353 and https://doi.org/10.1103/PhysRevA.93.042124 | Joint visibility and phase in a quantum eraser for multiple measurement strengths | High. arXiv source includes `VisibilityPhaseMeasurement.eps` and `WeakValues.eps` | Best backup for complex phase |
| 3 | Durr, Nonn, Rempe 1998, atom interferometer visibility/distinguishability | https://doi.org/10.1103/PhysRevLett.81.5705 | Independently measured fringe visibility and which-way distinguishability | Medium. Figure digitization likely, but source data not found in the quick pass | Strong complementarity check, weaker record-bandwidth check |
| 4 | Bertet et al. 2001, quantum-classical boundary Ramsey/cavity eraser | https://doi.org/10.1038/35075517 | Tunable microscopic/macroscopic beam-splitter and unconditional eraser behavior | Medium-low. Nature figures are accessible, but raw data/provenance is less direct | Conceptually rich, slower empirical path |
| 5 | Banaszek, Horodecki, Karpinski, Radzewicz 2013, internal-degree which-way experiment | https://arxiv.org/abs/1311.0017 and https://doi.org/10.1038/ncomms3594 | Internal-state visibility, distinguishability, and erasure by classical uncertainty | Medium. Open paper and figures, but less direct momentum-record proxy | Good later test of accessibility language |

## Recommendation

Use Xiao et al. 2019 as the second empirical pass.

Reason: it attacks the strongest surviving Chapman claim from another angle. Chapman inferred a photon momentum-record bandwidth from visibility zero/revival structure. Xiao et al. directly reconstruct a momentum-disturbance distribution and compare its mean absolute size to remaining visibility under partial which-way measurements.

This does not test the same physical system. That is good. If the record-bandwidth language is real enough to be useful, it should translate across:

```text
Chapman: unresolved scattered-photon direction bandwidth -> atom-fringe contrast loss/revival
Xiao: measured WWM momentum-disturbance bandwidth -> photon-fringe visibility loss
```

## What Would Count As Interesting

- The digitized Xiao visibility data show a monotone relation between visibility loss and measured momentum-disturbance scale.
- The measured points respect the published lower-bound structure.
- A bandwidth-style predictor explains the visibility loss better than a pure scalar erasure label.
- The inferred operational variable can be written without Chapman-specific acceptance parameters.

## What Would Not Count

- It would not validate the Lambda/Gamma/Theta product law.
- It would not solve collapse.
- It would not prove Bohmian mechanics is the only interpretation.
- It would not repair the Chapman raw phase failure.

## Proposed Next CLI

```bash
python src/constraint_dynamics_quantum_v3.py digitize-xiao-momentum \
  --source-dir outputs/tmp/second_hunt_sources/xiao \
  --output-dir outputs/xiao_momentum_digitization \
  --data-dir data/extracted

python src/constraint_dynamics_quantum_v3.py analyze-xiao-momentum \
  --input data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv \
  --output-dir outputs/xiao_momentum
```

Expected committed-style artifacts, if this phase is later accepted:

```text
data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv
data/extracted/XIAO_2019_MOMENTUM_DIGITIZATION.json
outputs/xiao_momentum/xiao_momentum_summary.csv
outputs/xiao_momentum/xiao_momentum_predictions.csv
outputs/xiao_momentum/xiao_momentum_report.md
outputs/xiao_momentum_stress/xiao_momentum_stress_report.md
outputs/xiao_probability/xiao_probability_report.md
```

## Scout And First Implementation Result

The two-track scout selected Xiao for full implementation. The implemented commands write:

```text
data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv
data/extracted/XIAO_2019_MOMENTUM_DIGITIZATION.json
outputs/xiao_momentum_digitization/xiao_digitization_report.md
outputs/xiao_momentum/xiao_momentum_summary.csv
outputs/xiao_momentum/xiao_momentum_predictions.csv
outputs/xiao_momentum/xiao_momentum_report.md
```

Current Xiao result:

```text
status: candidate cross-experiment structure
rows: 6
best model: linear_bandwidth
linear bandwidth RMSE: 0.0034
published-bound RMSE: 0.0693
loss-vs-momentum Pearson r: 0.9999
all points above published lower-bound line: true
```

This is a stronger second empirical target for the record-bandwidth idea, not a breakthrough claim.

The stress pass gives:

```text
status: xiao relation survives uncertainty
P(linear bandwidth beats published bound): 1.000
P(linear bandwidth beats scaled-loss fit): 1.000
P(all points remain above published bound): 1.000
P(monotone relation survives): 1.000
linear slope 95% CI: [0.6665, 0.7047]
Pearson r 95% CI: [0.9985, 0.9999]
pairing-null P(Pearson r >= observed): 0.004
pairing-null P(linear RMSE <= observed): 0.004
```

This makes Xiao the best next foundation for a cross-experiment record-bandwidth comparison with Chapman.

The probability-distribution pass adds the mechanism-side check:

```text
status: probability distribution supports record-bandwidth target
extracted rows: 365
mean absolute disturbance growth: 0.568 hbar/d
late mean absolute disturbance: 0.681 hbar/d
phi=0 peak location: p = -0.022
phi=pi side-peak |p| mean: 1.586
phi=pi central density / peak density: 0.314 / 1.234
```

This is the strongest Xiao signal so far because it checks the distribution shape behind the visibility-loss relation.

The raster no-refit distribution prediction first closed the loop inside Xiao:

```text
status: within-paper held-out distribution prediction passes
phi=0 mean |p| from Fig. 3b: 0.0639 hbar/d
phi=pi mean |p| from Fig. 3b: 1.4109 hbar/d
Fig. 3 distribution no-refit RMSE on Fig. 4: 0.0155
published-bound RMSE on Fig. 4: 0.0693
direct Fig. 4 linear-refit RMSE: 0.0034
```

This is the best Xiao result because the bandwidth scale comes from the distribution figure rather than from refitting the visibility tradeoff. It is still within-paper, so the next upgrade is an outside held-out experiment.

The raster stress run changed the priority:

```text
status: distribution prediction is fragile under robustness checks
P(no-refit beats published bound): 0.135
P(no-refit RMSE < 0.025): 0.000
pairing-null P(RMSE <= observed): 0.003
branch-label-swap P(RMSE <= observed): 0.000
baseline sensitivity pass fraction: 0.250
```

This means the Xiao no-refit bridge has nonrandom structure, but it is not yet publication-grade. The immediate bottleneck is Fig. 3 probability-curve baseline extraction, not a missing Constraint Dynamics parameter.

The vector extraction repairs that immediate bottleneck by reading Fig. 3b curves directly from `probability.pdf` drawing paths:

```text
status: vector probability extraction supports record-bandwidth target
extracted rows: 511
phi=0 mean |p| from Fig. 3b: 0.0610 hbar/d
phi=pi mean |p| from Fig. 3b: 1.4112 hbar/d
vector Fig. 3 distribution no-refit RMSE on Fig. 4: 0.0133
published-bound RMSE on Fig. 4: 0.0693
```

The vector-aware stress result is now:

```text
status: distribution prediction survives robustness checks
uncertainty mode: vector
P(no-refit beats published bound): 1.000
P(no-refit RMSE < 0.025): 0.957
pairing-null P(RMSE <= observed): 0.003
branch-label-swap P(RMSE <= observed): 0.000
baseline sensitivity pass fraction: 0.750
```

This is the strongest second-experiment signal so far: a within-paper, no-refit, cross-figure prediction survives vector-coordinate uncertainty and null controls. It is not a breakthrough claim because the Fig. 3 and Fig. 4 data come from the same paper and the record-bandwidth variable is not independently controlled across apparatus families.

## Cross-Experiment Synthesis

The follow-up synthesis command is:

```bash
python src/constraint_dynamics_quantum_v3.py synthesize-record-bandwidth --output-dir outputs/record_bandwidth_synthesis
```

Current synthesis verdict:

```text
status: robust cross-experiment record-bandwidth target
Chapman raw sinc/Fourier width: 1.961
Chapman raw first zero: d/lambda = 0.510
Xiao linear bandwidth slope: 0.6866
Xiao phi=pi side-peak |p| scale: 1.586
Xiao side-peak scale / Chapman raw sinc width: 0.809
```

This is the first point where the project has something stronger than a single-experiment anomaly. Chapman and Xiao do not share units or apparatus geometry, so the synthesis is structural: one experiment infers a Fourier momentum-record kernel from visibility zero/revival, while the other reconstructs a momentum-disturbance distribution that tracks visibility loss and develops side peaks.

The recommended next full implementation is no longer another free-parameter Chapman repair. It is a held-out prediction attempt: find or digitize a dataset where an independently measured record distribution predicts visibility without refitting the bandwidth.

## Implementation Notes

- Do not commit the paper PDFs.
- Prefer the arXiv source package because it separates the figures into vector PDFs.
- Use the same provenance discipline as Chapman: source URL, SHA256, figure name, axis anchors, pixel anchors, extraction uncertainty, and extraction method.
- Start with `visibility.pdf`, because Fig. 4 already contains the direct relation between total mean absolute momentum disturbance and fringe visibility.
- Add `probability.pdf` next only if the Fig. 4 relation is useful enough to justify distribution extraction.
- Treat the Bohmian momentum variable as an experimentally reconstructed momentum-disturbance proxy, not as a required ontological commitment.

## Strict Verdict Before Starting

This is the right second experiment, but it is not a breakthrough yet. It is a falsification opportunity. The question is:

```text
Does an independently reconstructed momentum-record bandwidth predict visibility loss in a way that strengthens the Chapman record-bandwidth interpretation?
```

If yes, the project has a cross-experiment empirical pattern. If no, Chapman remains an isolated visibility-kernel result.

## Third-Candidate Scout: Cormann

The Cormann backup track is now implemented as a scout:

```bash
python src/constraint_dynamics_quantum_v3.py scout-cormann-visibility-phase \
  --source-dir outputs/tmp/third_hunt_sources/cormann \
  --output-dir outputs/third_hunt_scout/cormann \
  --data-dir data/extracted
```

Current scout verdict:

```text
status: cormann is viable as a phase-control scout, not a record-bandwidth win
extracted rows: 211
setup 1 visibility RMSE / r: 0.0357 / 0.986
setup 2 visibility RMSE / r: 0.0655 / 0.958
setup 3 visibility RMSE: 0.2538
mean phase-sign accuracy: 0.877
```

This is useful but not the breakthrough-grade third test. Cormann gives a clean visibility-plus-phase quantum-eraser control with known measurement strengths and purities, so it can help keep the scaffold honest about phase/sign behavior. It does not provide an independently measured momentum-record distribution comparable to Xiao Fig. 3. The next breakthrough hunt should therefore continue toward author-level numerical data or another experiment where a measured record variable predicts visibility without refitting.

## Near-Miss Scout: Mir

The Mir weak-value scout is implemented as a source-figure availability check:

```bash
python src/constraint_dynamics_quantum_v3.py scout-mir-weak-value \
  --source-dir outputs/tmp/second_no_refit_sources/mir \
  --output-dir outputs/mir_weak_value_scout \
  --data-dir data/extracted
```

Current scout verdict:

```text
status: measured momentum-transfer distribution found, visibility sweep missing
momentum-transfer distribution available: true
visibility-loss sweep available: false
eraser/phase structure available: true
```

Mir et al. 2007 is scientifically close to Xiao because it directly measures a weak-valued momentum-transfer distribution in a double-slit which-way experiment. The source includes Fig. 3 for the unconditional `P_wv(q)` distribution and Fig. 4 for quantum-eraser conditional patterns. It is still a near miss for the breakthrough gate because it does not provide the paired controlled visibility-loss sweep needed for a no-refit distribution-to-visibility prediction.
