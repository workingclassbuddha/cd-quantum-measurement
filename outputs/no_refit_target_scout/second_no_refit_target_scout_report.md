# Second No-Refit Target Scout

Verdict: second no-refit distribution target found

This scout asks a narrow question: is there a second experiment, independent of Xiao, where a measured record distribution can predict a visibility/decoherence curve without refitting the key bandwidth/load parameter?

## Result

- Candidate count: 15
- Eligible second distribution targets: 1
- Recommended next candidate: `KOKOROWSKI_2001_MULTIPHOTON_SCATTERING`
- Recommended next command: `stress-test-kokorowski-multiphoton; profile-kokorowski-kappa-uncertainty; audit-kokorowski-calibration-provenance`

The current answer is not a breakthrough closure. Kokorowski is now the first eligible public second-experiment no-refit candidate, with digitization, no-refit analysis, null controls, kappa-uncertainty profiling, and calibration-provenance extraction in the repo. It still does not close G11 because the current stress evidence leaves independent-kappa calibration uncertainty as the limiting factor.

## Candidate Register

- **Xiao et al. 2019** (`XIAO_2019_INTERNAL_LEAD`): score 0.95. Role: current lead, not independent second experiment. Blocker: within-paper cross-figure result; cannot satisfy independent second-experiment gate
- **Kokorowski et al. 2001** (`KOKOROWSKI_2001_MULTIPHOTON_SCATTERING`): score 0.84. Role: strongest public-data G11 candidate; digitized/analyzed/stress-tested but not stress-closed. Blocker: joint stress gate is below closure threshold; independent kappa calibration provenance/uncertainty is the limiting factor
- **Eibenberger et al. 2014** (`EIBENBERGER_2014_RECOIL_ABSORPTION`): score 0.70. Role: best next recoil-control scout. Blocker: visibility reduction is used to extract absorption cross section; recoil scale is known but not an independently measured distribution in the Xiao sense
- **Hackermueller/Hornberger et al. 2003** (`HORNBERGER_2003_COLLISIONAL_DECOHERENCE`): score 0.68. Role: best standard-decoherence no-adjustable-parameter control. Blocker: excellent record-load control but not an independently measured record distribution
- **Hochrainer et al. 2017** (`HOCHRAINER_2017_INDUCED_COHERENCE_MOMENTUM_CORRELATION`): score 0.60. Role: strong inverse-problem near miss. Blocker: visibility profiles are used to infer the momentum-correlation width, so the record variable is not independent of the visibility observable
- **Lahiri et al. 2017** (`LAHIRI_2017_TWIN_PHOTON_CORRELATIONS`): score 0.58. Role: theory/inverse-method near miss for momentum-correlation visibility. Blocker: visibility is used to determine the momentum correlation rather than an independently measured correlation predicting visibility
- **Mir et al. 2007** (`MIR_2007_WEAK_VALUE_MOMENTUM_TRANSFER`): score 0.52. Role: closest pre-Xiao measured momentum-transfer candidate. Blocker: directly measures a momentum-transfer distribution but does not yet provide the paired visibility curve needed for the no-refit gate
- **Ding et al. 2025** (`DING_2025_WAVE_PARTICLE_ENTANGLEMENT_TRIAD`): score 0.50. Role: modern entanglement-memory control, not record-distribution gate. Blocker: tests wave-particle-entanglement conservation, but not a measured momentum/record distribution that predicts visibility without refit
- **Chen et al. 2022** (`CHEN_2022_ASYMMETRIC_BEAM_DUALITY`): score 0.48. Role: modern duality-relation control. Blocker: measures distinguishability/visibility duality, not a measured conjugate record distribution held out from visibility
- **Yoon and Cho 2021** (`YOON_2021_QUANTITATIVE_COMPLEMENTARITY`): score 0.47. Role: source-purity complementarity control. Blocker: useful record-accessibility analogue, but the variable is source purity/entanglement rather than a measured momentum-transfer distribution
- **Kocsis et al. 2011** (`KOCSIS_2011_AVERAGE_TRAJECTORIES`): score 0.45. Role: conceptual kin, weak no-refit target. Blocker: measures momentum/trajectories but does not provide a visibility-loss curve to predict
- **Rozema et al. 2012** (`ROZEMA_2012_WEAK_MEASUREMENT_DISTURBANCE`): score 0.44. Role: measurement-disturbance control, not visibility target. Blocker: characterizes measurement disturbance with weak values but does not provide a paired interference-visibility loss curve
- **Kaneda et al. 2014** (`KANEDA_2014_ERROR_DISTURBANCE`): score 0.43. Role: measurement-strength disturbance control. Blocker: tests error-disturbance uncertainty relations rather than record-distribution prediction of visibility
- **Cormann et al. 2016** (`CORMANN_2016_MODULAR_VALUE`): score 0.42. Role: phase-control dataset, not record-distribution gate. Blocker: useful visibility-plus-phase target but no independent measured record distribution
- **Duerr/Nonn/Rempe 1998** (`DURR_1998_COMPLEMENTARITY`): score 0.35. Role: complementarity control. Blocker: distinguishability/visibility duality is not a measured record-bandwidth distribution

## Interpretation

Xiao remains the cleanest within-paper distribution-to-visibility validation. Kokorowski is the strongest public second-experiment candidate, but its status is still candidate rather than closure. Chapman, Hackermueller, Hornberger, and Eibenberger remain standard-QM-compatible controls for record bandwidth/load, not replacements for the missing stress-closed second validation.

## Next Move

Tighten Kokorowski independent-kappa provenance or find a cleaner second no-refit dataset. Keep breakthrough language blocked until the second validation stress gate, Chapman raw phase gate, and independent Lambda/Gamma/Theta product-law gate clear.
