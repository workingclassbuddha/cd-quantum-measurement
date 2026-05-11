# Theory Notes

These notes ground the test scaffold in Constraint Dynamics V17 and the companion phenomenology text, while keeping the quantum claim modest.

## Constraint Dynamics Anchor

V17 defines three observer constraints:

- Lambda: spatial constraint, the ability to locate states in a structured space.
- Gamma: temporal constraint, the ability to resolve/update events in time.
- Theta: energetic or irreversible anchoring, the cost-bearing distinction between an internal possibility and an external consequence.

The V17 quantum section is explicitly speculative. It frames the double-slit experiment as a pre-constraint regime: before measurement, path alternatives have not been forced into a single spatially located, temporally resolved, energetically consequential record. Measurement is described as Theta enforcement through energetic interaction, recruiting spatial localization and temporal path resolution.

The important boundary is also in V17: this interpretation is compatible with standard decoherence and is not currently experimentally distinguished from it. V3 therefore treats Constraint Dynamics as an effective apparatus parameterization, not as new fundamental quantum mechanics.

## Companion Phenomenology Anchor

The Geometry of Feeling gives the phenomenological side of the same triad:

- Lambda corresponds to navigable structure and orientation.
- Gamma corresponds to update rate, temporal binding, and aliasing/flicker when degraded.
- Theta corresponds to consequence, weight, and irreversible energetic grounding.

For this quantum scaffold, those terms are translated into apparatus language rather than subjective language.

## Apparatus Mapping

V3 uses these practical mappings:

- Lambda = spatial path distinguishability, computed from path separation relative to detector spatial resolution.
- Gamma = temporal distinguishability, computed from coherence time relative to detector response time or bandwidth.
- Theta = inaccessible durable record load. In Chapman-like scattering data, the more precise operational proxy is inaccessible conjugate-record bandwidth: the width and phase-carrying shape of the unresolved photon momentum-transfer record after accounting for any accessible conditioning window. Xiao-like momentum-disturbance data provide a second operational version of the same idea: an independently reconstructed momentum-record scale can be compared directly with visibility loss, and the underlying reconstructed distribution can be checked for side-peak bandwidth structure. Hackermueller-like thermal-emission data add the durable environmental-record lane: thermal photons are emitted into inaccessible modes, and the current calibrated Figure 4 pass tests whether a thermal load proxy organizes normalized visibility loss better than plain laser-power damping.
- marker_visibility = reversible marker overlap, separate from irreversible dephasing.

This separation is essential. A reversible marker can reduce raw visibility by entangling path with a marker degree of freedom. A conditioned eraser basis can recover that reversible coherence. By contrast, high Theta dephasing is a durable inaccessible record and remains unrecoverable in the conditioned branch. The Chapman kernel pass adds a caveat: some real visibility loss is not monotone exponential decay, but a Fourier transform of an unresolved record distribution with zeros, revivals, and a phase shift. The current complex-kernel test does not yet close the loop: conditioned phase ordering is promising, but raw phase still breaks or underdetermines the simple model. The mixture repair pass tests whether this is due to missing 0/1/2-photon and velocity-smearing terms. The phase-grade pass then asks whether the remaining failure is localized to raw Fig. 2 wrap/low-contrast ambiguity before adding any stronger Constraint Dynamics interpretation.

## Testable Question

The scaffold tests whether visibility data are better fit by:

```text
kappa_eff = kappa0 * Lambda * Gamma * Theta
```

than by constant, additive, or pairwise alternatives. A real experimental win would require out-of-sample apparatus datasets where the product model has better predictive accuracy and model evidence than the alternatives.

The current Chapman/Xiao/Hackermueller synthesis sharpens the empirical target but does not satisfy that standard. Chapman favors a Fourier momentum-record kernel over scalar exponential dephasing, Xiao provides an independently reconstructed momentum-disturbance bandwidth that tracks visibility loss and shows side-peak structure, and Hackermueller supports a thermal emitted-photon record-load proxy in a standard decoherence setting. This supports `record accessibility / bandwidth / load` as a useful operational variable to pursue. It is not yet a validated Constraint Dynamics law because the relevant record variables are not independently controlled across Lambda, Gamma, and Theta axes, and the strongest Xiao result remains a within-paper cross-figure prediction.

## What Would Falsify This Effective Model

- Additive or pairwise laws consistently outperform the product law on held-out apparatus configurations.
- Conditioned eraser visibility depends on marker delay even when no irreversible record is created.
- Irreversible record load fails to predict unrecoverable visibility loss once ordinary decoherence controls are included.
- Fitted Lambda, Gamma, and Theta mappings cannot be made stable across apparatus families.
