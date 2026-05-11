# Two-Track Breakthrough Scout Report

## Verdict

Winner recommendation: **Xiao et al. 2019 for full implementation**.

This is not a breakthrough claim. The scout says Xiao is the cleaner second real-data target because the figure directly relates a reconstructed momentum-disturbance scale to remaining fringe visibility, while Cormann is viable but needs a dedicated calibrated digitizer before it can sharpen the Chapman raw-phase problem.

## Xiao Track

Source: https://arxiv.org/abs/1805.02059

Figure: `visibility.pdf` / Fig. 4.

Extraction method: `fast_manual_component_digitization_v0` on a fixed-DPI PPM render. Blue experimental markers were isolated by color threshold and connected components. Error bars were not separately digitized in this scout.

Scout metrics:

```text
rows: 6
monotone momentum decrease as visibility increases: True
all points above published lower-bound line: True
loss-vs-momentum Pearson r: 0.9999
linear bandwidth proxy: momentum = 0.0429 + 0.6866 * (1 - V)
linear bandwidth RMSE: 0.0034
published bound RMSE: 0.0693
```

Interpretation: the Xiao points form a tight, monotone relation between visibility loss and measured momentum-disturbance scale. They sit above the published lower-bound line, as expected. This is exactly the kind of cross-experiment structure needed to test whether the Chapman record-bandwidth language travels beyond Chapman.

## Cormann Track

Source: https://arxiv.org/abs/1508.01353

Figure: `VisibilityPhaseMeasurement.eps` / Fig. 2.

Extraction method: coarse component extraction from a Ghostscript-rendered EPS for panel-a visibility, plus sparse visual phase-sign rows for panel-b viability. This is enough to decide feasibility, not enough for a quantitative claim.

Scout metrics:

```text
visibility rows: 41
phase-sign viability rows: 18
```

Interpretation: Cormann is a credible backup for a complex visibility-plus-phase eraser test. However, the available EPS is a rendered composite with dense markers, curves, labels, and insets. A serious Cormann pass should be a dedicated calibrated digitizer, not a quick scout extraction.

## Decision

Choose Xiao for the next full implementation phase.

Next public commands should be:

```bash
python src/constraint_dynamics_quantum_v3.py digitize-xiao-momentum \
  --source-dir outputs/tmp/second_hunt_sources/xiao \
  --output-dir outputs/xiao_momentum_digitization \
  --data-dir data/extracted

python src/constraint_dynamics_quantum_v3.py analyze-xiao-momentum \
  --input data/extracted/XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv \
  --output-dir outputs/xiao_momentum
```

The target claim should remain conservative:

```text
Xiao provides a second empirical target for record-bandwidth language: measured momentum-disturbance bandwidth tracks visibility loss in a standard-QM-compatible which-way experiment.
```

## Artifacts

- `xiao_visibility_scout.csv`
- `cormann_visibility_phase_scout.csv`
- `second_hunt_scout_summary.csv`
- `figure_xiao_visibility_scout.svg`
- `figure_cormann_visibility_scout.svg`

## Caveats

- This is a fast scout, not publication-grade digitization.
- Xiao error bars are not independently digitized yet.
- Cormann phase rows are sparse sign/viability rows, not quantitative phase measurements.
- No product-law, collapse, or beyond-standard-quantum claim follows from this scout.
