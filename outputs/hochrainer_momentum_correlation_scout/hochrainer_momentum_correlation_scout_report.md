# Hochrainer 2017 Momentum-Correlation Scout

Verdict: visibility-derived momentum-correlation near miss

This scout checks whether induced-coherence visibility profiles can provide the missing independent distribution-to-visibility validation. The paper is highly relevant because it explicitly links visibility to the conditional transverse momentum probability density. It does not clear the strict no-refit gate because the reported momentum-correlation width is computed from the measured visibility FWHM.

- Source URL: https://arxiv.org/abs/1610.05529
- DOI: https://doi.org/10.1073/pnas.1615874114
- Source directory: `outputs/tmp/second_no_refit_sources/hochrainer/extracted`
- TeX SHA256: `3e0e2e3fddc6c3f147b884e611b42a2727005f08c1135189b36e26dc5b61a2bb`
- Extraction method: `source_figure_visibility_correlation_scout_v1`

## Source Findings

- The paper states visibility depends on conditional momentum probability density P(q_i|q_s).
- Visibility profiles are measured by scanning interferometric phase.
- The FWHM of the visibility profile is used to numerically compute the momentum-correlation variance.
- This is a strong operational record-width lane, but it is an inverse problem rather than an independent no-refit validation.

## Figure Register

- **Figure 2** (`visibilityfigure.pdf`): visibility profiles and FWHM versus pump waist. Role: visibility-to-momentum-correlation inverse problem
- **Figure 3** (`correlationWidths.pdf`): experimentally determined transverse momentum-correlation variance versus pump waist. Role: derived momentum-correlation width, not independent held-out record

## Gate Decision

- Visibility curve available: True
- Record distribution/width available: True
- Record variable inferred from visibility: True
- Clears no-refit gate: False

## Interpretation

Hochrainer is a strong record-width control and may be useful for a future inverse-problem section. It is not the second independent no-refit validation unless author-level or supplementary data provide an independently measured momentum-correlation width that can be held out from the visibility fit.
