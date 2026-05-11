# Second No-Refit Target Scout

Verdict: no second no-refit distribution target yet

This scout asks a narrow question: is there a second experiment, independent of Xiao, where a measured record distribution can predict a visibility/decoherence curve without refitting the key bandwidth/load parameter?

## Result

- Candidate count: 8
- Eligible second distribution targets: 0
- Recommended next candidate: `EIBENBERGER_2014_RECOIL_ABSORPTION`
- Recommended next command: `scout-eibenberger-recoil-absorption`

The answer is currently negative for the strict Xiao-like gate. The best next practical target is Eibenberger 2014 because it has a clean photon-recoil mechanism and visibility reduction in a matter-wave interferometer. But it is a recoil-control scout, not yet the missing independent measured-distribution prediction.

## Candidate Register

- **Xiao et al. 2019** (`XIAO_2019_INTERNAL_LEAD`): score 0.95. Role: current lead, not independent second experiment. Blocker: within-paper cross-figure result; cannot satisfy independent second-experiment gate
- **Eibenberger et al. 2014** (`EIBENBERGER_2014_RECOIL_ABSORPTION`): score 0.70. Role: best next recoil-control scout. Blocker: visibility reduction is used to extract absorption cross section; recoil scale is known but not an independently measured distribution in the Xiao sense
- **Hackermueller/Hornberger et al. 2003** (`HORNBERGER_2003_COLLISIONAL_DECOHERENCE`): score 0.68. Role: best standard-decoherence no-adjustable-parameter control. Blocker: excellent record-load control but not an independently measured record distribution
- **Hochrainer et al. 2017** (`HOCHRAINER_2017_INDUCED_COHERENCE_MOMENTUM_CORRELATION`): score 0.60. Role: strong inverse-problem near miss. Blocker: visibility profiles are used to infer the momentum-correlation width, so the record variable is not independent of the visibility observable
- **Mir et al. 2007** (`MIR_2007_WEAK_VALUE_MOMENTUM_TRANSFER`): score 0.52. Role: closest pre-Xiao measured momentum-transfer candidate. Blocker: directly measures a momentum-transfer distribution but does not yet provide the paired visibility curve needed for the no-refit gate
- **Kocsis et al. 2011** (`KOCSIS_2011_AVERAGE_TRAJECTORIES`): score 0.45. Role: conceptual kin, weak no-refit target. Blocker: measures momentum/trajectories but does not provide a visibility-loss curve to predict
- **Cormann et al. 2016** (`CORMANN_2016_MODULAR_VALUE`): score 0.42. Role: phase-control dataset, not record-distribution gate. Blocker: useful visibility-plus-phase target but no independent measured record distribution
- **Duerr/Nonn/Rempe 1998** (`DURR_1998_COMPLEMENTARITY`): score 0.35. Role: complementarity control. Blocker: distinguishability/visibility duality is not a measured record-bandwidth distribution

## Interpretation

Xiao remains the lead because it uniquely combines an experimentally reconstructed momentum-disturbance distribution with a visibility-loss curve in a way that supports a no-refit cross-figure prediction. Chapman, Hackermueller, Hornberger, and Eibenberger are strong standard-QM-compatible controls for record bandwidth/load, but they do not presently clear the second independent distribution-to-visibility gate.

## Next Move

Build `scout-eibenberger-recoil-absorption` only as a recoil-control lane, while continuing the literature search for a true second measured-distribution dataset.
