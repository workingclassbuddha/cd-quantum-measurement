# Breakthrough Hunt

## Executive Snapshot

The current project state is:

```text
lead candidate found, breakthrough not yet
```

That is the strongest honest claim so far. The lead candidate is now Xiao 2019 vector Fig. 3 distribution-to-Fig. 4 visibility prediction: an independently digitized momentum distribution predicts the visibility-loss tradeoff without refitting the key bandwidth parameter. Chapman and Hackermueller provide cross-experiment support for the broader record-variable reading, but they do not clear the missing second independent no-refit distribution gate.

The new reproducible gate is:

```bash
python src/constraint_dynamics_quantum_v3.py evaluate-breakthrough-candidate --output-dir outputs/breakthrough_candidate
```

Current dossier verdict:

```text
lead candidate found, breakthrough not yet
passed gates: 9 / 12
```

It means Chapman and Xiao now point toward the same operational variable:

```text
Theta = inaccessible conjugate-record bandwidth
```

Chapman contributes the Fourier visibility structure: raw contrast has a zero/revival pattern better fit by a sinc-style momentum-record kernel than by scalar exponential dephasing. Xiao contributes the independent momentum-disturbance side: reconstructed disturbance grows as visibility is lost, survives bootstrap and pairing-null checks, and shows side peaks in the far-field distribution.

Current anchor numbers:

```text
Chapman raw sinc RMSE: 0.0257
Chapman raw exponential RMSE: 0.0738
Chapman raw first zero: d/lambda = 0.510
Xiao linear bandwidth RMSE: 0.0034
Xiao published-bound RMSE: 0.0693
Xiao stress P(linear beats bound): 1.000
Xiao pairing-null P(Pearson r >= observed): 0.004
Xiao phi=pi side-peak |p|: 1.586
Xiao vector Fig. 3 distribution no-refit prediction RMSE: 0.0133
Xiao vector distribution stress P(no-refit beats bound): 1.000
Xiao vector distribution stress P(RMSE < 0.025): 0.957
Xiao no-refit / published-bound RMSE ratio: 0.193
Xiao distribution pairing-null P(RMSE <= observed): 0.003
Xiao distribution branch-label-null P(RMSE <= observed): 0.000
Hackermueller stress P(thermal delta-T4 beats exp power): 0.994
```

This is not a breakthrough yet. It does not solve collapse, validate the Lambda/Gamma/Theta product law, or show physics beyond standard quantum mechanics. The Xiao vector result is a strong within-paper cross-figure prediction; the next breakthrough-grade move is an outside held-out prediction where an independently measured record distribution predicts visibility without refitting the bandwidth.

## Breakthrough-Readiness Dossier

The `evaluate-breakthrough-candidate` command writes:

```text
outputs/breakthrough_candidate/breakthrough_candidate_scorecard.csv
outputs/breakthrough_candidate/next_breakthrough_steps.csv
outputs/breakthrough_candidate/breakthrough_candidate_report.md
outputs/breakthrough_candidate/figures/figure_breakthrough_gate_scores.svg
```

Current pass/fail summary:

- Xiao no-refit distribution prediction: pass.
- Xiao bootstrap and null controls: pass.
- Chapman raw Fourier-kernel support: pass.
- Hackermueller durable thermal-record support: pass.
- Chapman raw complex phase repair: fail.
- Second independent distribution-to-visibility experiment: fail.
- Lambda/Gamma/Theta product-law validation: fail.

Therefore the working breakthrough target is narrow:

```text
Find a second independent experiment where a measured record distribution predicts
visibility/decoherence without refitting the key bandwidth or load parameter.
```

## Second No-Refit Target Scout

The follow-up command is:

```bash
python src/constraint_dynamics_quantum_v3.py scout-no-refit-targets --output-dir outputs/no_refit_target_scout
```

Current verdict:

```text
no second no-refit distribution target yet
eligible second distribution targets: 0
recommended next candidate: EIBENBERGER_2014_RECOIL_ABSORPTION
```

The Eibenberger recoil-control command is:

```bash
python src/constraint_dynamics_quantum_v3.py scout-eibenberger-recoil-absorption --source-dir outputs/tmp/second_no_refit_sources/eibenberger --output-dir outputs/eibenberger_recoil_scout --data-dir data/extracted
```

Current Eibenberger result:

```text
status: recoil-control candidate, not second no-refit gate
paper-sigma RMSE: 0.0251
visibility-fit sigma RMSE: 0.0247
previous-absorption midpoint RMSE: 0.0302
```

This is a valuable standard-QM control because the recoil visibility reduction is a characteristic-function-like average over recoil phases. It does not clear the missing gate because the absorption cross section is extracted from the same visibility reduction.

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

## Fourier-Kernel Turn

The sharper follow-up is the Chapman kernel analysis:

```bash
python src/constraint_dynamics_quantum_v3.py analyze-chapman-kernel --input data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv --output-dir outputs/chapman_kernel
```

The calibrated raw curve is not just a monotone loss curve. It has a zero and revival, and the current fit captures that structure much better with an absolute sinc/Fourier window than with scalar exponential dephasing:

```text
raw exponential RMSE: 0.0738
raw sinc/Fourier RMSE: 0.0257
raw exponential LOO RMSE: 0.1000
raw sinc/Fourier LOO RMSE: 0.0323
raw sinc first zero: d/lambda = 0.510
peak recoverable loss: d/lambda = 0.500
```

This suggests a more precise operational refinement:

```text
Theta = inaccessible conjugate-record bandwidth
```

The conditioned branches infer narrower sinc-family bandwidths, although their own smooth curves can be fit well by monotone Gaussian/exponential baselines. The important empirical structure is the raw zero/revival plus recoverable conditioned contrast, not a claim that every branch is sinc-dominated.

## Stress-Test Result

The robustness command is:

```bash
python src/constraint_dynamics_quantum_v3.py stress-test-chapman-kernel --input data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv --digitization-json data/extracted/CHAPMAN_1995_DIGITIZATION.json --output-dir outputs/chapman_kernel_stress --n-bootstrap 1000 --seed 20260424
```

The current 1000-sample run gives a split verdict:

```text
P(raw sinc/Fourier beats exponential): 1.000
P(raw first zero aligns with peak recoverable loss): 1.000
P(conditioned widths narrower than raw): 0.752
pairing-null recovery-alignment probability: 0.269
branch-label-null width-ordering probability: 0.724
```

This is not a full robustness pass. The raw Fourier-kernel signal survives uncertainty very strongly, and the recovery peak is not explained well by random conditioned pairing. But the conditioned branch bandwidth ordering is fragile because a branch-label null often preserves the ordering. The honest next claim is narrower: Chapman robustly supports the raw record-bandwidth/Fourier-kernel correction to scalar dephasing, while the stronger branch-specific Constraint Dynamics interpretation remains unproven.

## Physical Acceptance-Kernel Result

The physical follow-up command is:

```bash
python src/constraint_dynamics_quantum_v3.py analyze-chapman-physical-kernel --input data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv --digitization-json data/extracted/CHAPMAN_1995_DIGITIZATION.json --output-dir outputs/chapman_physical_kernel
```

This implements Chapman Eq. (3) as a characteristic function over a photon transverse momentum-transfer distribution:

```text
V(d) = | integral P_eff(q) exp(i 2*pi*q*d/lambda) dq |
```

The current run gives:

```text
uniform recoil raw RMSE: 0.0285
fitted beta recoil raw RMSE: 0.0284
empirical raw sinc/Fourier RMSE: 0.0257
case I physical RMSE / empirical sinc RMSE: 0.0134 / 0.0396
case III physical RMSE / empirical sinc RMSE: 0.0399 / 0.0700
case I accepted q center / width: 1.500 / 0.375
case III accepted q center / width: 1.950 / 0.885
forward/backward center ordering recovered: true
```

This repairs part of the stress-test weakness: the conditioned branches are better modeled as accepted momentum-transfer windows than as generic sinc widths. But the accepted centers are still inferred from contrast data alone. Without the phase curve or independent detector-acceptance geometry, this remains a physically motivated reconstruction rather than an independent validation.

## Complex Kernel Result

The overconstrained follow-up command is:

```bash
python src/constraint_dynamics_quantum_v3.py analyze-chapman-complex-kernel --pdf /tmp/chapman_prl95.pdf --data-dir data/extracted --output-dir outputs/chapman_complex_kernel
```

This adds rough phase digitization and fits the full complex Eq. (3) amplitude:

```text
A(d) = integral P_eff(q) exp(i 2*pi*q*d/lambda) dq
visibility(d) = |A(d)|
phase(d) = unwrap(arg(A(d)))
```

The current run gives:

```text
raw complex visibility RMSE: 0.0305
raw complex phase RMSE: 1.4733 rad
raw observed / predicted small-d phase slope: 2.000 / 2.271 pi per d/lambda
case I accepted q center: 0.150
case III accepted q center: 2.000
case I / III predicted phase slopes: 0.231 / 3.367 pi per d/lambda
case I / III phase RMSE: 0.2578 / 0.4694 rad
forward/backward center ordering recovered: true
forward/backward phase-slope ordering recovered: true
```

This is the sharpest result so far, and it is not a breakthrough. Phase improves the conditioned-branch story: case I trends forward and case III trends backward. But the same simple raw beta-family recoil model does not yet predict the full rough raw phase curve. The likely explanations are model incompleteness, rough phase digitization, and the Fig. 2 phase wrapping near visibility zeros. The stronger record-accessibility interpretation remains underdetermined until the raw phase problem is repaired with better phase digitization, Chapman-style multi-photon/velocity terms, or independent detector acceptance geometry.

## Raw-Phase Repair Target

The next repair command is:

```bash
python src/constraint_dynamics_quantum_v3.py analyze-chapman-complex-mixture --pdf /tmp/chapman_prl95.pdf --data-dir data/extracted --output-dir outputs/chapman_complex_mixture
```

This tests whether the raw phase failure is caused by omitting Chapman-style 0-photon, 1-photon, 2-photon, and velocity-smearing terms:

```text
A_raw(d) = w0*A0(d) + w1*A1(d) + w2*A2(d)
A2(d) ~= A1(d)^2
```

The only acceptable stronger outcome is `raw phase repaired`: raw full-phase error must improve substantially, raw visibility must remain competitive, and conditioned forward/backward ordering must survive. If the mixture only improves stable phase points while wrap-sensitive Fig. 2 points dominate the error, the verdict is `digitization-limited`. If the added terms do not rescue raw phase, the verdict is `model still fails`, and the next honest step is publication-grade Fig. 2 phase digitization rather than adding more freedom.

The current run gives:

```text
verdict: model still fails
simple beta complex raw phase RMSE: 1.4733 rad
best mixture raw phase RMSE: 1.3088 rad
simple beta complex raw visibility RMSE: 0.0305
best mixture raw visibility RMSE: 0.0652
mixture weights w0 / w1 / w2: 0.060 / 0.900 / 0.040
velocity sigma: 0.500
case I / III accepted q centers: 0.000 / 2.000
case I / III phase slopes: 0.146 / 3.224 pi per d/lambda
```

The mixture preserves conditioned forward/backward ordering, but it does not repair raw phase and it degrades raw visibility. This is useful: the next rational move is not more free parameters. It is a better Fig. 2 phase extraction, especially around the phase-wrap and low-contrast regions.

## Phase-Grade Digitization Target

The raw phase hygiene command is:

```bash
python src/constraint_dynamics_quantum_v3.py digitize-chapman-phase-grade --pdf /tmp/chapman_prl95.pdf --data-dir data/extracted --output-dir outputs/chapman_phase_grade
```

It writes `CHAPMAN_1995_PHASE_GRADED.csv` with separate displayed and unwrapped phase columns:

```text
phase_display_rad
phase_unwrapped_rad
phase_quality
unwrap_group
wrap_ambiguous
low_contrast_ambiguous
```

The key decision is whether the raw phase failure survives the high-confidence mask. If high-confidence raw phase fits but all-points phase fails, the result is `phase failure is wrap-limited`. If both fail, the Chapman phase bridge remains unsupported and the visibility-only Fourier result is the honest stopping point.

The current focused-grid run gives:

```text
verdict: phase still fails
raw phase rows: 21
high-confidence raw phase rows: 16
all-points simple complex raw phase RMSE: 1.4753 rad
all-points best mixture raw phase RMSE: 1.8943 rad
high-confidence simple complex raw phase RMSE: 1.6207 rad
high-confidence best mixture raw phase RMSE: 1.6390 rad
case I / III accepted q centers: 0.000 / 2.000
case I / III phase slopes: 0.275 / 3.210 pi per d/lambda
```

This closes the current Chapman phase loop negatively. The high-confidence mask does not rescue raw phase. Conditioned forward/backward ordering remains real and useful, but the stronger claim that one simple inferred record distribution predicts Chapman raw visibility and raw phase is not supported by this scaffold.

## Current Verdict

We have a stronger Chapman-backed target and a sharper theory variable. Chapman supports a raw record-bandwidth/Fourier-kernel interpretation more strongly than scalar exponential dephasing, and a physical acceptance-kernel model improves the conditioned branch fits. The complex phase, mixture, and phase-grade tests recover the expected conditioned forward/backward ordering, but raw phase still breaks the current model family. We do not yet have a breakthrough.

## Second Experiment Target

The next empirical target is not another Chapman knob. The current shortlist is in `docs/second_experiment_hunt.md`.

The recommended second pass is Xiao, Wiseman, Xu, Kedem, Li, and Guo 2019, "Observing momentum disturbance in double-slit which-way measurements." It is a good match because the paper directly reconstructs a momentum-disturbance distribution and compares total mean absolute momentum disturbance with fringe visibility in partial which-way measurements.

The scientific question becomes:

```text
Does an independently reconstructed momentum-record bandwidth predict visibility loss in a way that strengthens the Chapman record-bandwidth interpretation?
```

This would still be standard quantum-mechanics compatible. A positive result would be a cross-experiment empirical pattern, not a collapse solution and not product-law validation.

## Xiao Momentum Result

The implemented second-experiment commands are:

```bash
python src/constraint_dynamics_quantum_v3.py digitize-xiao-momentum --source-dir outputs/tmp/second_hunt_sources/xiao --output-dir outputs/xiao_momentum_digitization --data-dir data/extracted
python src/constraint_dynamics_quantum_v3.py analyze-xiao-momentum --input data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv --output-dir outputs/xiao_momentum
```

The current run gives:

```text
status: candidate cross-experiment structure
rows analyzed: 6
best model by AICc: linear_bandwidth
linear bandwidth RMSE: 0.0034
published-bound RMSE: 0.0693
loss-vs-momentum Pearson r: 0.9999
all points above published lower-bound line: true
```

This is the first real cross-experiment support for the refined target. Chapman says unresolved photon momentum-transfer records produce a Fourier visibility structure; Xiao independently reconstructs a momentum-disturbance scale and shows it tracks visibility loss in a partial which-way experiment.

The verdict is still conservative: Xiao gives `candidate cross-experiment structure`. It does not validate the Lambda/Gamma/Theta product law, does not solve collapse, does not require Bohmian mechanics as an ontology, and does not repair the Chapman raw-phase failure.

## Xiao Momentum Stress Result

The robustness command is:

```bash
python src/constraint_dynamics_quantum_v3.py stress-test-xiao-momentum --input data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv --digitization-json data/extracted/XIAO_2019_MOMENTUM_DIGITIZATION.json --output-dir outputs/xiao_momentum_stress --n-bootstrap 1000 --seed 20260424
```

The current run gives:

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

This strengthens the cross-experiment target. The Xiao relation is not an artifact of the exact digitized point locations under the current extraction uncertainty, and random momentum/visibility pairings rarely reproduce the observed correlation or fit error. The honest claim is now: Chapman plus Xiao support pursuing `inaccessible conjugate-record bandwidth` as an operational variable. It is still not product-law validation.

## Xiao Probability Distribution Result

The distribution-shape command is:

```bash
python src/constraint_dynamics_quantum_v3.py digitize-xiao-probability --source-dir outputs/tmp/second_hunt_sources/xiao --output-dir outputs/xiao_probability --data-dir data/extracted
python src/constraint_dynamics_quantum_v3.py digitize-xiao-probability-vector --source-dir outputs/tmp/second_hunt_sources/xiao --output-dir outputs/xiao_probability_vector --data-dir data/extracted
```

The current run gives:

```text
status: probability distribution supports record-bandwidth target
extracted rows: 365
mean absolute disturbance growth: 0.568 hbar/d
late mean absolute disturbance: 0.681 hbar/d
phi=0 peak location: p = -0.022
phi=pi mean absolute side-peak location: |p| = 1.586
phi=pi central density: 0.314
phi=pi peak density: 1.234
```

This matters because the Xiao result is no longer only a six-point scalar tradeoff. The underlying distribution shows the `phi=pi` branch developing side peaks near the expected momentum-transfer scale while `phi=0` stays centered near p=0, and the mean absolute disturbance grows during propagation. That is exactly the sort of distributional record-bandwidth structure the Chapman interpretation needs as an external check.

The vector extraction repairs the baseline bottleneck by reading Fig. 3b red/blue curves directly from PDF path commands:

```text
status: vector probability extraction supports record-bandwidth target
extracted rows: 511
phi=0 peak location: p = -0.013
phi=0 baseline-subtracted mean |p|: 0.0610
phi=pi baseline-subtracted mean |p|: 1.4112
phi=pi mean absolute side-peak location: |p| = 1.613
```

## Record-Bandwidth Synthesis Result

The current synthesis command is:

```bash
python src/constraint_dynamics_quantum_v3.py synthesize-record-bandwidth --output-dir outputs/record_bandwidth_synthesis
```

It deliberately does not merge Chapman, Xiao, and Hackermueller into a shared apparatus-factor fit. It asks a narrower question: do different experiments support treating the operative record as accessibility / bandwidth / durable load rather than scalar dephasing strength?

The current run gives:

```text
status: three-experiment record-variable structure survives
Chapman raw sinc/Fourier width: 1.961
Chapman raw first zero: d/lambda = 0.510
Chapman raw sinc RMSE / exponential RMSE: 0.0257 / 0.0738
Chapman exponential/sinc RMSE ratio: 2.87
Xiao linear bandwidth slope / intercept: 0.6866 / 0.0429
Xiao linear RMSE / published-bound RMSE: 0.0034 / 0.0693
Xiao published-bound/linear RMSE ratio: 20.51
Xiao stress P(linear beats bound): 1.000
Xiao pairing-null P(Pearson r >= observed): 0.004
Xiao vector phi=pi side-peak |p| scale: 1.613
Xiao vector distribution no-refit RMSE: 0.0133
Xiao vector distribution stress P(no-refit beats bound): 1.000
Xiao side-peak scale / Chapman raw sinc width: 0.823
Hackermueller thermal delta-T4 RMSE / exp(power) RMSE: 0.0767 / 0.0923
Hackermueller stress P(thermal beats exp power): 0.994
Hackermueller stress P(thermal best): 0.701
```

This is the closest thing to a real signal so far. Chapman supplies the Fourier visibility zero/revival, Xiao supplies an independently reconstructed momentum-disturbance bandwidth with distributional side peaks, and Hackermueller supplies the durable environmental-record load lane through thermal photon emission. The agreement is structural, not a unit-level numerical identity.

The conservative verdict remains: robust cross-experiment target, not breakthrough. The next breakthrough-grade step would be a held-out experiment where an independently measured record distribution predicts visibility without refitting the bandwidth or thermal-load curve.

## Xiao Distribution Prediction Result

The next no-refit command is:

```bash
python src/constraint_dynamics_quantum_v3.py predict-xiao-visibility-from-distribution --momentum-input data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv --probability-input data/extracted/XIAO_2019_PROBABILITY_DIGITIZED.csv --output-dir outputs/xiao_distribution_prediction
python src/constraint_dynamics_quantum_v3.py predict-xiao-visibility-from-distribution --momentum-input data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv --probability-input data/extracted/XIAO_2019_PROBABILITY_VECTOR_DIGITIZED.csv --output-dir outputs/xiao_distribution_prediction_vector
```

It computes branch mean momentum disturbance from Xiao Fig. 3b and predicts Fig. 4 using the phase-mixture relation:

```text
eta_pi = (1 - V) / 2
eta_0  = (1 + V) / 2
predicted mean |p| = eta_0 * M_phi0 + eta_pi * M_phipi
```

The current run gives:

```text
status: within-paper held-out distribution prediction passes
phi=0 mean |p| from vector Fig. 3b: 0.0610 hbar/d
phi=pi mean |p| from vector Fig. 3b: 1.4112 hbar/d
vector Fig. 3 distribution no-refit RMSE on Fig. 4: 0.0133
vector Fig. 3 panel-a-scaled RMSE on Fig. 4: 0.0263
published-bound RMSE on Fig. 4: 0.0693
direct Fig. 4 linear-refit RMSE: 0.0034
no-refit / published-bound RMSE ratio: 0.193
no-refit / linear-refit RMSE ratio: 3.949
```

This is a real step forward. The bandwidth scale is no longer taken from the same six Fig. 4 points it predicts; it comes from the independently digitized Fig. 3 momentum-distribution branches. The result lands close to the direct Fig. 4 refit and beats the published lower-bound line as a point predictor.

The caution is equally important: this is still within the Xiao paper, not a third independent experiment. It strengthens the record-bandwidth target but does not validate the Lambda/Gamma/Theta product law.

## Xiao Distribution Prediction Stress Result

The robustness command is:

```bash
python src/constraint_dynamics_quantum_v3.py stress-test-xiao-distribution-prediction --momentum-input data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv --probability-input data/extracted/XIAO_2019_PROBABILITY_DIGITIZED.csv --output-dir outputs/xiao_distribution_prediction_stress --n-bootstrap 1000 --seed 20260425
python src/constraint_dynamics_quantum_v3.py stress-test-xiao-distribution-prediction --momentum-input data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv --probability-input data/extracted/XIAO_2019_PROBABILITY_VECTOR_DIGITIZED.csv --output-dir outputs/xiao_distribution_prediction_vector_stress --n-bootstrap 1000 --seed 20260425
```

The raster run gave a mixed verdict, but the vector-aware run gives:

```text
status: distribution prediction survives robustness checks
uncertainty mode: vector
observed no-refit RMSE: 0.0133
P(no-refit beats published bound): 1.000
P(no-refit RMSE < 0.025): 0.957
P(no-refit / published-bound RMSE < 0.5): 1.000
P(phi=pi branch mean > phi=0 branch mean): 1.000
no-refit RMSE 95% CI: [0.0136, 0.0256]
pairing-null P(RMSE <= observed): 0.003
branch-label-swap P(RMSE <= observed): 0.000
baseline sensitivity pass fraction: 0.750
```

This upgrades the Xiao bridge. The null controls say the observed Fig. 3-to-Fig. 4 prediction is not reproduced by random visibility/momentum pairings or by swapping the branch labels, and vector-coordinate jitter does not erase the no-refit prediction. The remaining caveat is that this is still a within-paper cross-figure prediction; it is not yet a third independent experiment.

The honest update is:

```text
Xiao now contains a robustness-grade within-paper no-refit
distribution-to-visibility bridge under vector extraction, but the
next breakthrough-grade test still requires an outside held-out dataset.
```

So the next step is not more theory freedom. It is a third experiment or author-level numerical data where the record distribution can be measured independently and used to predict visibility without refitting the bandwidth.

## Third Dataset Scout

The next source-level scout checked matter-wave decoherence experiments that can test the irreversible-record side of Theta without adding Chapman-specific model freedom.

Current ranking:

```text
1. Hackermueller 2004 thermal emission decoherence
2. Hornberger 2003 collisional decoherence
3. Durr/Nonn/Rempe 1998 complementarity
```

Hackermueller wins the next build slot because the arXiv source package includes `Figure4.eps` decoherence curves of visibility versus heating power / molecular temperature, plus `Figure3.eps` photon-emission-rate information. That is the cleanest held-out path for testing whether Theta can be operationalized as inaccessible durable environmental record load.

Hornberger is the strong backup: its arXiv source includes `fig2.eps` visibility versus gas pressure and `fig3.eps` decoherence pressure by gas species. It is excellent for falsifying overreach in standard collisional decoherence, though less likely to produce a Fourier-kernel result.

Implemented guardrail command:

```bash
python src/constraint_dynamics_quantum_v3.py scout-hornberger-collisional --source-dir outputs/tmp/third_hunt_sources/hornberger --output-dir outputs/hornberger_collisional_scout --data-dir data/extracted
```

Current Hornberger result:

```text
status: collisional record-load guardrail supports standard decoherence
Fig. 2 methane p_v: 0.807 x 10^-6 mbar
Fig. 3 CH4 p_v: 0.810 x 10^-6 mbar
gas-species pressure RMSE: 0.185 x 10^-6 mbar
gas-species theory/experiment correlation: 0.888
```

This is a strong sanity check, not a breakthrough gate. It says the irreversible environmental-record lane behaves as standard decoherence expects; it does not provide an independently measured distribution-to-visibility prediction like Xiao.

Scout artifacts:

```text
docs/third_experiment_hunt.md
outputs/third_hunt_scout/third_dataset_candidate_register.csv
outputs/third_hunt_scout/third_dataset_scout_report.md
```

Strict verdict: no breakthrough yet. The current useful result is that Chapman/Xiao/Hackermueller can be stated as one conservative operational pattern: interference is controlled by the accessible or inaccessible conjugate record made available to the environment.

## Cormann Third-Candidate Scout

The Cormann scout command is:

```bash
python src/constraint_dynamics_quantum_v3.py scout-cormann-visibility-phase --source-dir outputs/tmp/third_hunt_sources/cormann --output-dir outputs/third_hunt_scout/cormann --data-dir data/extracted
```

It extracts `VisibilityPhaseMeasurement.eps` from the arXiv source package for Cormann et al. 2016 and compares visibility against the paper's caption parameters without refitting the visibility scale.

Current result:

```text
status: cormann is viable as a phase-control scout, not a record-bandwidth win
setup 1 visibility RMSE / r: 0.0357 / 0.986
setup 2 visibility RMSE / r: 0.0655 / 0.958
setup 3 visibility RMSE: 0.2538
mean phase-sign accuracy: 0.877
```

This is a good guardrail but not the next breakthrough. Cormann can test whether the scaffold respects quantum-eraser phase/sign behavior near the weak-value transition. It does not give a new independently measured momentum-record distribution, so it cannot replace the outside held-out distribution-to-visibility test we now need.
