# Mir 2007 Weak-Value Momentum-Transfer Scout

Verdict: measured momentum-transfer distribution found, visibility sweep missing

This scout checks whether Mir et al. 2007 can serve as the missing independent Xiao-like target. It is scientifically close because it directly measures a weak-valued momentum-transfer distribution in a double-slit which-way experiment. It does not currently clear the no-refit gate because the source does not provide a paired controlled visibility-loss sweep.

- Source URL: https://arxiv.org/abs/0706.3966
- DOI: https://doi.org/10.1088/1367-2630/9/8/287
- Source directory: `outputs/tmp/second_no_refit_sources/mir/extracted`
- TeX SHA256: `970fb0a0489b826558dca0792bc05c2dbe3fb72ce314d67a1a4c07a54e00f5c3`
- Extraction method: `source_figure_availability_scout_v1`

## Source Findings

- The paper reports direct observation of a weak-valued momentum-transfer distribution.
- Figure 3 plots P_wv(q) and a variance integral, giving a real measured distribution target.
- Figure 4 gives quantum-eraser conditional patterns, but not a controlled visibility-loss sweep.
- The current source therefore does not clear the Xiao-like no-refit gate.

## Figure Register

- **Figure 2** (`Figure2.ps`): conditional weak-valued probability P_wv(p_i | p_f). Gate role: conditional momentum-transfer structure
- **Figure 3** (`Figure3.eps`): unconditional weak-valued momentum-transfer distribution P_wv(q). Gate role: closest measured distribution analogue to Xiao
- **Figure 4a** (`Figure4a.ps`): quantum eraser conditional WVP and interference for +45 degree polarizer. Gate role: eraser phase-control evidence, not a visibility sweep
- **Figure 4b** (`Figure4b.ps`): quantum eraser conditional WVP and interference for -45 degree polarizer. Gate role: eraser phase-control evidence, not a visibility sweep

## Gate Decision

- Momentum-transfer distribution available: True
- Visibility-loss sweep available: False
- Eraser/phase structure available: True
- Clears no-refit gate: False

## Interpretation

Mir is a useful weak-value momentum-transfer control and may help interpret Xiao historically, but it is not the second independent distribution-to-visibility validation. The next breakthrough-grade target still needs both a measured record distribution and a visibility/decoherence curve whose key bandwidth/load parameter is not refit from that curve.
