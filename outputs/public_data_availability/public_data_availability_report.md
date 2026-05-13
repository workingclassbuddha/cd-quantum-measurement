# Public Data Availability Audit

Verdict: public data yields candidate but does not close G11

This audit asks whether public records, source packages, or article pages already contain enough numerical data to close G11 without author contact.

## Summary

- Candidates checked: 6
- Public numerical tables found: 0
- Candidates that close G11 without author contact: 0
- Public second-candidate route found: True

## Candidate Checks

- **Xiao et al. 2019** (`XIAO_2019_INTERNAL_LEAD`): tables found = False; G11 without author contact = False. PubMed/PMC record exposes abstract, figures, and captions for Fig. 3/Fig. 4; no numerical Fig. 3 branch distributions or Fig. 4 table were found in the accessible record.
- **Hochrainer et al. 2017** (`HOCHRAINER_2017_INDUCED_COHERENCE_MOMENTUM_CORRELATION`): tables found = False; G11 without author contact = False. arXiv source package is useful, but the momentum-correlation width remains visibility-derived in the local scout.
- **Mir et al. 2007** (`MIR_2007_WEAK_VALUE_MOMENTUM_TRANSFER`): tables found = False; G11 without author contact = False. arXiv source includes the weak-valued momentum-transfer figure, but the scout did not find a paired controlled visibility-loss sweep.
- **Eibenberger et al. 2014** (`EIBENBERGER_2014_RECOIL_ABSORPTION`): tables found = False; G11 without author contact = False. arXiv source supports the recoil-control scout, but absorption cross section is extracted from visibility rather than held out.
- **Kokorowski et al. 2001** (`KOKOROWSKI_2001_MULTIPHOTON_SCATTERING`): tables found = False; G11 without author contact = False. arXiv source includes TeX and EPS figures; local vector digitization/analyze path gives a strong no-refit candidate, but stress/profile artifacts show independent-kappa uncertainty still prevents publication-grade G11 closure.
- **Ding et al. 2025** (`DING_2025_WAVE_PARTICLE_ENTANGLEMENT_TRIAD`): tables found = False; G11 without author contact = False. public article is relevant to visibility/predictability/entanglement, but not a measured momentum-record distribution target.

## Interpretation

The public record supplies a serious route toward G11, not a completed closure. Kokorowski's arXiv source package plus vector Fig. 4 digitization tests independently reported many-photon parameters against contrast loss, but the stress/profile artifacts identify independent-kappa uncertainty as the limiting factor. Author numerical tables or a reproduced calibration are still needed before treating the second validation as closed.
