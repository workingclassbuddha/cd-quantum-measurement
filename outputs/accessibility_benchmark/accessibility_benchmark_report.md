# Accessibility Benchmark Report

Status: passes synthetic discrimination

This synthetic benchmark varies path separation and record accessibility independently. The generated data use the V3 accessibility-aware Theta definition, then compare whether a naive record-load product can recover the same visibility surface.

- Best model: aware_record_product
- Delta AICc, naive record product versus aware product: 562.779
- Aware product RMSE visibility: 0.00153
- Naive product RMSE visibility: 0.15362

Interpretation: this is not empirical evidence. It is a discrimination target. If real data show this two-axis pattern, the accessibility-aware Theta parameter is doing nontrivial explanatory work. If a naive record-strength model fits equally well, the refinement is only vocabulary.
