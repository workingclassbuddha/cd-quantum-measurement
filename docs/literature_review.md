# Literature Review Notes

These notes summarize the external physics constraints that V3 should respect. They are not an argument that Constraint Dynamics replaces standard quantum theory; they define the guardrails for an honest effective model.

## Complementarity and Visibility

Englert's visibility/distinguishability inequality is the main quantitative boundary condition for any two-path model:

```text
D^2 + V^2 <= 1
```

The scaffold's marker angle is a deliberately simple version of this idea. Reversible marker overlap reduces raw visibility, but it should not be confused with irreversible environmental dephasing. The model therefore treats `marker_visibility` separately from `eta = exp(-2 integral kappa dt)`.

Primary reference:

- B.-G. Englert, "Fringe Visibility and Which-Way Information: An Inequality," Physical Review Letters 77, 2154 (1996), DOI: https://doi.org/10.1103/PhysRevLett.77.2154

## Quantum Eraser Constraints

The Scully-Druehl proposal and later delayed-choice demonstrations make a strong modeling demand: loss of raw interference due to reversible which-path marking can be recovered by conditioning on an eraser basis, but the unconditioned total distribution does not become a usable retrocausal signal.

V3 encodes this as:

```text
V_raw            = marker_visibility * eta
V_erased_optimal = eta
```

The optimal eraser branch removes the reversible marker-overlap penalty. A fixed analyzer basis can recover less, which is why V3 reports fixed and optimal conditioned branches separately. Neither branch removes the irreversible dephasing penalty.

Primary references:

- M. O. Scully and K. Druehl, "Quantum eraser: A proposed photon correlation experiment concerning observation and delayed choice in quantum mechanics," Physical Review A 25, 2208 (1982), DOI: https://doi.org/10.1103/PhysRevA.25.2208
- Y.-H. Kim, R. Yu, S. P. Kulik, Y. H. Shih, and M. O. Scully, "A Delayed Choice Quantum Eraser," Physical Review Letters 84, 1 (2000), arXiv: https://arxiv.org/abs/quant-ph/9903047
- X.-S. Ma et al., "Quantum erasure with causally disconnected choice," Proceedings of the National Academy of Sciences 110, 1221 (2013), DOI: https://doi.org/10.1073/pnas.1213201110

## Decoherence and Irreversible Records

Zurek's decoherence/einselection program is the key standard-theory reference for why a system becomes effectively classical through environmental entanglement and redundant records. V3's `Theta` factor is best understood as a candidate effective proxy for durable record formation, not as a new collapse primitive.

Primary reference:

- W. H. Zurek, "Decoherence, einselection, and the quantum origins of the classical," Reviews of Modern Physics 75, 715 (2003), DOI: https://doi.org/10.1103/RevModPhys.75.715; arXiv: https://arxiv.org/abs/quant-ph/0105127

## Quantum Trajectories

The stochastic branch in V3 is a phase-flip unraveling of a dephasing master equation. This is inspired by the Monte Carlo wave-function / quantum trajectory tradition: individual realizations remain pure, while the ensemble recovers the open-system density matrix.

Primary reference:

- J. Dalibard, Y. Castin, and K. Molmer, "Wave-function approach to dissipative processes in quantum optics," Physical Review Letters 68, 580 (1992), DOI: https://doi.org/10.1103/PhysRevLett.68.580

## Implication for Constraint Dynamics

The research stance should stay narrow:

- Good claim: Constraint Dynamics may offer a useful effective factorization of apparatus dependence.
- Risky claim: Constraint Dynamics derives collapse or supersedes decoherence.

The next decisive test is not whether V3 can generate plausible curves. It can. The decisive test is whether product-law apparatus factors predict held-out visibility data better than additive, pairwise, or standard nuisance-parameter alternatives.
