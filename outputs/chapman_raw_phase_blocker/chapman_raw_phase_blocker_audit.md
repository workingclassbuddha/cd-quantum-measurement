# Chapman Raw Phase Blocker Audit

Verdict: G10 still blocked by raw phase

This audit does not add model freedom. It summarizes why G10 remains blocked after the calibrated phase-grade pass and names the minimum data needed to repair or falsify the raw-phase overconstraint.

## Inputs

- Phase CSV: `data/extracted/CHAPMAN_1995_PHASE_GRADED.csv`
- Complex summary: `outputs/chapman_phase_grade/phase_grade_complex_summary.csv`
- Mixture summary: `outputs/chapman_phase_grade/phase_grade_mixture_summary.csv`
- Complex predictions: `outputs/chapman_phase_grade/phase_grade_complex_predictions.csv`
- Mixture predictions: `outputs/chapman_phase_grade/phase_grade_mixture_predictions.csv`

## Current G10 State

- Raw phase rows: 21
- Raw phase quality counts: high=9, medium=7, low=5
- Wrap-ambiguous raw rows: 5
- Low-contrast ambiguous raw rows: 8
- All-points best phase RMSE: 1.4753 rad
- All-points excess over 0.75 rad gate: 0.7253 rad
- High-confidence best phase RMSE: 1.6207 rad
- High-confidence excess over 0.75 rad gate: 0.8707 rad
- All-points phase gate pass: False
- High-confidence phase gate pass: False

## Interpretation

The visibility-kernel story is not the failing part of G10. The failure is the raw complex phase: neither the all-points fit nor the high-confidence masked fit reaches the 0.75 rad phase gate while preserving the visibility gate. Because the remaining input phase picks are still manual plotted-point extractions, the next valid move is numerical source data or publication-grade redigitization, not a looser model.

## Needed Data

1. `fig2_raw_phase_trace.csv` with numerical fringe-fit phase, uncertainty, displayed phase, unwrap group, and paired visibility.
2. `fig2_phase_wrap_notes.md` explaining phase branch choices near contrast zeros.
3. `paired_raw_visibility_table.csv` from the same underlying fits, so phase and visibility stay paired.

## Boundary

- This does not repair G10.
- This does not affect G11.
- This does not validate the Lambda/Gamma/Theta product law.
- This preserves the current no-overclaiming boundary.
