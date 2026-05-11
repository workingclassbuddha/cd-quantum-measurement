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

## Chapman Digitization

The `digitize-chapman` command renders the Chapman 1995 PDF through `pdftoppm`, parses deterministic grayscale PGM files, and maps stored pixel picks through axis calibration anchors. The output includes a digitized CSV, JSON provenance with PDF SHA256, and a quality report comparing the first-pass and calibrated recovery windows.

## Chapman Kernel Analysis

The `analyze-chapman-kernel` command fits the calibrated Chapman raw and conditioned visibility curves with monotone exponential, Gaussian characteristic-function, and absolute sinc/Fourier-window models. This is a research diagnostic for whether a scalar dephasing picture is too blunt. In Chapman, the raw visibility zero and revival are treated as evidence that the effective record variable is an unresolved photon momentum-transfer bandwidth, not merely an entropy-like load.

The fitted sinc first-zero location is used as an operational record-bandwidth proxy. This does not validate the Constraint Dynamics product law; it only identifies the stronger empirical target that a later apparatus-parameterized model would need to predict.

## Chapman Kernel Stress Test

The `stress-test-chapman-kernel` command perturbs the calibrated visibility values within their extraction uncertainty, refits the kernel models, and runs two null controls. The pairing null shuffles conditioned visibility values across x positions before recomputing recovery alignment. The branch-label null shuffles conditioned branch identities before testing the conditioned-width ordering. These controls separate a robust raw Fourier-kernel signal from a more fragile interpretation of conditioned branch bandwidths.

## Chapman Physical Acceptance Kernel

The `analyze-chapman-physical-kernel` command implements Chapman Eq. (3) directly:

```text
V(d) = | integral P_eff(q) exp(i 2*pi*q*d/lambda) dq |
```

It compares a uniform recoil distribution, a fitted beta-family recoil distribution, and branch-specific Gaussian acceptance windows over that recoil distribution. The accepted-window parameters are inferred proxies. They can improve branch fits and recover the expected forward/backward ordering, but they are not a substitute for extracting the actual detector acceptance geometry or phase-shift data.

## Chapman Complex Kernel

The `analyze-chapman-complex-kernel` command extends the Chapman pass to the complex Eq. (3) amplitude:

```text
A(d) = integral P_eff(q) exp(i 2*pi*q*d/lambda) dq
visibility(d) = |A(d)|
phase(d) = unwrap(arg(A(d)))
```

It writes rough phase digitization provenance, a phase CSV, joint visibility/phase fit tables, inferred distributions, and diagnostic figures. The current phase extraction is intentionally marked `rough_phase_digitization_v1`; it is good enough to test whether the visibility-only interpretation survives an overconstrained check, not good enough for publication-grade phase claims.

The strict verdict is negative for now. The complex fit recovers the expected conditioned phase ordering and keeps the small-d raw slope close to the Chapman expectation, but the full raw phase RMSE is too large. That leaves the raw Fourier-kernel result intact while withholding the stronger claim that branch-specific record accessibility has been independently validated by phase.

## Chapman Complex Mixture

The `analyze-chapman-complex-mixture` command asks whether the raw phase failure is a model-incompleteness problem. It fits an effective Chapman-style mixture:

```text
A_raw(d) = w0*A0(d) + w1*A1(d) + w2*A2(d)
A2(d) ~= A1(d)^2
```

The weights are nonnegative and normalized. `A1` is a fitted beta-family one-photon recoil characteristic function, `A2` approximates independent two-photon scattering, and an optional Gaussian velocity/phase-smearing factor can damp the complex amplitude. The fitted components are proxies only; they are not independent measurements of Chapman photon counts.

The report has three possible strict verdicts. `raw phase repaired` requires full raw-phase improvement, competitive raw visibility, and preserved conditioned forward/backward ordering. `digitization-limited` means stable raw phase points look repairable but wrap-sensitive Fig. 2 points dominate the failure. `model still fails` means added mixture freedom does not rescue the raw complex phase.

In the current Chapman run, the mixture verdict is `model still fails`. The fitted mixture preserves conditioned forward/backward ordering, but the raw full-phase RMSE remains high and raw visibility worsens. This points back to the input phase extraction, especially Fig. 2 wrapping near visibility zeros, before adding more model freedom.

## Chapman Phase-Grade Digitization

The `digitize-chapman-phase-grade` command upgrades the raw Fig. 2 phase input. It stores the displayed phase, a separate unwrapped phase, the unwrap group, a quality label, and explicit ambiguity flags for wrap-adjacent and low-contrast points. It then reruns the complex and mixture checks twice: once on all phase points, and once on a high-confidence raw subset that excludes wrap-ambiguous points.

This command is a falsification hygiene step. If the high-confidence subset fits while the full set fails, the raw phase problem is likely digitization/wrap limited. If both fail, the current complex record-distribution bridge remains unsupported by Chapman phase data.

In the current focused-grid run, both all-points and high-confidence raw phase fail. That does not erase the visibility-only Fourier result or the conditioned branch ordering, but it blocks the stronger overconstrained Chapman phase claim.

## Xiao Momentum-Disturbance Pass

The `digitize-xiao-momentum` command renders Xiao et al. 2019 `visibility.pdf` from the arXiv source package using `pdftoppm`, isolates blue experimental markers by color threshold and connected components, and maps the component centers through fixed axis anchors. It writes a digitized CSV, JSON provenance with source SHA256, and a digitization report.

The `analyze-xiao-momentum` command compares total mean absolute momentum disturbance against remaining visibility. It fits constant, published-bound, scaled-loss, and linear bandwidth-style predictors:

```text
published bound: p = (2/pi) * (1 - V)
linear bandwidth: p = b0 + b1 * (1 - V)
```

The current result is `candidate cross-experiment structure`: the digitized points are monotone, all sit above the published lower-bound line, and the linear bandwidth proxy fits tightly. This is a second empirical target for the record-bandwidth language. It is not a product-law validation and does not require a Bohmian ontological commitment; the reconstructed momentum disturbance is treated as an operational proxy.

The `stress-test-xiao-momentum` command perturbs visibility and momentum values by their extraction uncertainties and reruns the momentum fits. It also shuffles the momentum values across visibility settings as a pairing null. The current stress result survives both checks: the linear bandwidth relation beats the published-bound and scaled-loss alternatives in all bootstrap samples, and the pairing null rarely matches the observed correlation or RMSE.

The `digitize-xiao-probability` command renders `probability.pdf` and extracts two supporting pieces from Fig. 3. Panel a is digitized as a binned blue curve for mean absolute momentum disturbance versus propagation distance. Panel b is digitized as red and blue far-field distribution curves after excluding the inset and legend regions. The summary checks whether the mean disturbance grows, whether `phi=0` remains centered near p=0, and whether `phi=pi` develops two side peaks near the expected momentum-transfer scale.

The `digitize-xiao-probability-vector` command targets the same figure but avoids raster color thresholding for Fig. 3b. It parses the vector PDF content streams, maps colored path samples through the same axis calibration, excludes the inset and legend windows, and writes `XIAO_2019_PROBABILITY_VECTOR_DIGITIZED.csv` plus JSON provenance. In the current run, the vector branch moments are `M_phi0 = 0.0610` and `M_phipi = 1.4112` hbar/d.

The `predict-xiao-visibility-from-distribution` command is a no-refit bridge from Xiao Fig. 3 to Fig. 4. It subtracts a small edge baseline from the digitized Fig. 3b branch distributions, computes the branch moments `M_phi0` and `M_phipi`, and predicts the Fig. 4 mean disturbance using:

```text
eta_pi = (1 - V) / 2
eta_0  = (1 + V) / 2
predicted mean |p| = eta_0 * M_phi0 + eta_pi * M_phipi
```

This keeps the bandwidth scale out of the Fig. 4 fitting loop. The direct Fig. 4 linear fit is still reported, but only as an empirical ceiling.

The `stress-test-xiao-distribution-prediction` command jitters the Fig. 3 probability curves and Fig. 4 momentum points, uses extraction-specific bootstrap baseline methods, writes a separate baseline-sensitivity table, and runs pairing and branch-label null controls. For raster extraction the result remains baseline-limited. For vector extraction the current configured run survives: `P(no-refit beats published bound) = 1.000`, `P(no-refit RMSE < 0.025) = 0.957`, and the pairing/branch-label nulls do not reproduce the observed RMSE. This is still a within-paper cross-figure check, not an independent validation.

The `scout-cormann-visibility-phase` command downloads or reuses the Cormann et al. 2016 arXiv source package, renders `VisibilityPhaseMeasurement.eps` with Ghostscript, extracts colored visibility and phase/sign markers, and compares visibility against the paper's caption parameters without fitting a new bandwidth. This is a scout-grade phase-control check. It is useful for validating eraser phase/sign behavior, but it is not a record-bandwidth dataset.

## Record-Bandwidth Synthesis

The `synthesize-record-bandwidth` command combines the already generated Chapman, Xiao, Hackermueller, and Hornberger summaries into one conservative cross-experiment report. It does not refit the experiments and does not force a Lambda/Gamma/Theta product law across incompatible apparatus axes.

The synthesis compares:

- Chapman raw Fourier-kernel width, first zero, and sinc-versus-exponential RMSE ratio.
- Xiao visibility-loss versus reconstructed momentum-disturbance slope, stress-test probabilities, and pairing-null results.
- Xiao probability-distribution side-peak scale and mean absolute disturbance growth.
- Hackermueller thermal emitted-photon record-load fits and stress-test probabilities.
- Hornberger methane collisional-decoherence pressure and gas-species theory/experiment pressure agreement.

The output label `three-experiment structure survives with Hornberger guardrail` means Chapman, Xiao, and Hackermueller each support a compatible operational record variable in their own apparatus language, while Hornberger adds a standard collisional-decoherence sanity check. It does not mean the product law is validated, and it does not repair the Chapman raw-phase failure.

## Identifiability Diagnostics

The `design` command checks whether a dataset can actually distinguish the three proposed factors. It reports factor correlations, variance inflation factors, factor ranges, and the condition number of the full second-order feature matrix. The benchmark command compares a balanced factorial synthetic design with a confounded latent-load design where Lambda, Gamma, and Theta rise together.

The intended interpretation is conservative: a product-law win in a confounded design is not strong evidence for the theory. It only becomes meaningful when the same law predicts held-out data in designs where spatial selectivity, timing resolution, and record irreversibility have been varied independently.

## Accessibility Benchmark

The `benchmark-accessibility` command varies path separation and record accessibility independently. It compares an accessibility-aware product law against a naive record-load product that treats all records as inaccessible. This is a falsification target rather than a claim of empirical success: real experiments would need to show the same two-axis visibility surface before the refined Theta variable earns its keep.

## Limitations

The model is deliberately effective. It does not derive the Born rule, does not solve the measurement problem, and does not supersede environmental decoherence. Its intended scientific use is narrower: fit apparatus-parameterized visibility data and ask whether the Constraint Dynamics product factorization is empirically useful.
