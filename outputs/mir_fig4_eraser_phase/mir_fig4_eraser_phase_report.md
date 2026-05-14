# Mir 2007 Fig. 4 Eraser Phase-Control Check

Status: fig4 eraser phase-control check passes as supporting evidence

This check extracts the black diamond intensity markers from the public PostScript Figure 4a/4b files. It asks only whether the two eraser settings encode a reproducible phase-control pattern on the same printed sampling grid.

- Source URL: https://arxiv.org/abs/0706.3966
- DOI: https://doi.org/10.1088/1367-2630/9/8/287
- Source directory: `outputs/tmp/second_no_refit_sources/mir/extracted`
- Extraction method: `postscript_diamond_marker_digitization_v1`
- +45 marker count: 100
- -45 marker count: 100
- Same PostScript y-grid: True
- Zero-lag intensity correlation: -0.34148697696633723
- Best positive shifted correlation: 0.8462180984453633 at shift 15
- Most negative shifted correlation: -0.7291240504752677 at shift -29

## Gate Decision

- Supports eraser phase control: True
- Clears G11 / second no-refit distribution-to-visibility gate: False
- Blocker: Figure 4 contains eraser phase/intensity patterns, not a paired controlled visibility-loss sweep.

## Interpretation

Mir Fig. 4 is now represented as a provenance-rich public-vector control instead of a prose-only near miss. The extracted markers support the paper's eraser-phase story, but they do not supply the missing independent measured-distribution-to-visibility validation.
