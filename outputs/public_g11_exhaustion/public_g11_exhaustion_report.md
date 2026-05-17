# Public G11 Exhaustion Audit

Verdict: current public G11 path exhausted without closure

This audit asks a narrow operational question: after the current public-data scouts, is there still a public second-experiment candidate that is cleaner than Kokorowski and could close G11 without new numerical calibration data?

## Summary

- Eligible public second no-refit candidates: 1
- Stress-closed public second no-refit candidates: 0
- Public G11 support without author/non-public data: 0
- Kokorowski raw calibration tables found in public source: False
- Cleaner public candidates than Kokorowski: 0
- Current public G11 path exhausted: True
- Closure evidence queue rows: 14
- Closure evidence classes: independent_record_distribution;paired_visibility_curve;raw_calibration_tables
- Closure evidence intake rows: 14
- Closure evidence intake classes: independent_record_distribution;paired_visibility_curve;raw_calibration_tables
- Closure evidence artifact preflight passed: False
- Closure evidence missing artifact count: 9
- Closure evidence missing artifact rows: 42
- Closure evidence blocked classes: 3
- Closure evidence blocked candidates: 14
- Closure evidence candidate actions: 14
- Closure evidence blocked candidate actions: 14
- Closure evidence top action candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Closure evidence acquisition manifest rows: 9
- Closure evidence top acquisition artifact: independence_provenance.md
- Closure evidence top acquisition candidate count: 9
- Closure evidence bundle manifest rows: 14
- Closure evidence blocked bundles: 14
- Closure evidence top bundle candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Closure evidence source query rows: 42
- Closure evidence source query candidate count: 14
- Closure evidence source query status: not_searched
- Closure evidence top source query candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Closure evidence source query batches: 3
- Closure evidence top source query batch: raw_calibration_tables
- Closure evidence top source query batch status: not_searched
- Closure evidence source routes: 42
- Closure evidence source route status: route_known_not_checked
- Closure evidence top source route: https://arxiv.org/abs/quant-ph/0009044
- Closure evidence source route checklist rows: 14
- Closure evidence source route checklist status: not_checked
- Closure evidence top source route check candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Closure evidence source access plan rows: 14
- Closure evidence arXiv e-print access candidates: 7
- Closure evidence top source access class: arxiv_eprint_route
- Closure evidence arXiv source package inventory rows: 7
- Closure evidence arXiv source package inventory status: not_checked
- Closure evidence top arXiv source package candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Closure evidence arXiv package acceptance manifest rows: 21
- Closure evidence arXiv package acceptance manifest status: not_checked
- Closure evidence top arXiv package required artifact: beam_deflection_broadening_calibration.csv
- Closure evidence arXiv package retrieval ledger rows: 7
- Closure evidence arXiv package retrieval status: not_fetched
- Closure evidence top arXiv package expected archive: outputs/tmp/arxiv_source_packages/KOKOROWSKI_2001_MULTIPHOTON_SCATTERING/source.tar
- Closure evidence arXiv package inspection checklist rows: 21
- Closure evidence arXiv package inspection status: pending_fetch
- Closure evidence top arXiv package inspection pattern: beam|deflection|broadening|calibration|kappa
- Closure evidence arXiv package local inspection rows: 21
- Closure evidence arXiv package local inspection status: missing_cache
- Closure evidence top arXiv package local inspection matches: 0
- Closure evidence arXiv package cache alias rows: 7
- Closure evidence arXiv package cache alias status: not_checked
- Closure evidence top arXiv package cache alias legacy dir: outputs/tmp/kokorowski_source/extracted
- Closure evidence arXiv package cache probe plan rows: 7
- Closure evidence arXiv package cache probe plan status: not_run
- Closure evidence top arXiv package cache probe expected min files: 1
- Top closure intake priority: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Top closure intake class: raw_calibration_tables
- Top closure intake acceptance gates: G11C;G11F;G11G
- Top closure intake preflight passed: False
- Top closure intake missing artifact count: 6

## Near Misses

- **Kokorowski et al. 2001** (`KOKOROWSKI_2001_MULTIPHOTON_SCATTERING`): stress/calibration uncertainty blocks closure; blocker: joint stress gate is below closure threshold; independent kappa calibration provenance/uncertainty is the limiting factor
- **Eibenberger et al. 2014** (`EIBENBERGER_2014_RECOIL_ABSORPTION`): record variable is visibility-derived or not an independent distribution; blocker: visibility reduction is used to extract absorption cross section; recoil scale is known but not an independently measured distribution in the Xiao sense
- **Hackermueller/Hornberger et al. 2003** (`HORNBERGER_2003_COLLISIONAL_DECOHERENCE`): record variable is visibility-derived or not an independent distribution; blocker: excellent record-load control but not an independently measured record distribution
- **Hochrainer et al. 2017** (`HOCHRAINER_2017_INDUCED_COHERENCE_MOMENTUM_CORRELATION`): record variable is visibility-derived or not an independent distribution; blocker: visibility profiles are used to infer the momentum-correlation width, so the record variable is not independent of the visibility observable
- **Lahiri et al. 2017** (`LAHIRI_2017_TWIN_PHOTON_CORRELATIONS`): record variable is visibility-derived or not an independent distribution; blocker: visibility is used to determine the momentum correlation rather than an independently measured correlation predicting visibility
- **Mir et al. 2007** (`MIR_2007_WEAK_VALUE_MOMENTUM_TRANSFER`): paired visibility curve missing; blocker: directly measures a momentum-transfer distribution but does not yet provide the paired visibility curve needed for the no-refit gate
- **Ding et al. 2025** (`DING_2025_WAVE_PARTICLE_ENTANGLEMENT_TRIAD`): record variable is visibility-derived or not an independent distribution; blocker: tests wave-particle-entanglement conservation, but not a measured momentum/record distribution that predicts visibility without refit
- **Chen et al. 2022** (`CHEN_2022_ASYMMETRIC_BEAM_DUALITY`): record variable is visibility-derived or not an independent distribution; blocker: measures distinguishability/visibility duality, not a measured conjugate record distribution held out from visibility
- **Yoon and Cho 2021** (`YOON_2021_QUANTITATIVE_COMPLEMENTARITY`): record variable is visibility-derived or not an independent distribution; blocker: useful record-accessibility analogue, but the variable is source purity/entanglement rather than a measured momentum-transfer distribution
- **Kocsis et al. 2011** (`KOCSIS_2011_AVERAGE_TRAJECTORIES`): paired visibility curve missing; blocker: measures momentum/trajectories but does not provide a visibility-loss curve to predict

## Interpretation

Kokorowski remains the only eligible public second-experiment no-refit candidate in the current register. The public source and vector digitization make it a serious route, but the stress gate remains below closure and the public source inventory does not contain raw beam-deflection/broadening calibration tables. Other public candidates either lack a paired visibility-loss curve or derive the record variable from visibility itself.

## Boundary

- This does not close G11.
- This does not claim no such dataset exists anywhere.
- This only records exhaustion of the currently implemented public-data path.
- This keeps breakthrough language blocked until a stress-closed second validation exists.
