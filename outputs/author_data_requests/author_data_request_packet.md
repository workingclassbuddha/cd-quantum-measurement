# Breakthrough Author Data Request Packet

Purpose: attack the missing G11 gate directly.

Current G11 blocker:

```text
Second independent candidate found, but Kokorowski stress/provenance still needs tighter independent calibration uncertainty
```

This packet prepares concise data requests for the strongest candidates and near misses. The goal is to find out whether any author-level numerical data can turn a near miss into a held-out no-refit distribution-to-visibility test.

## Targets

- **Kokorowski et al. 2001** (`kokorowski_2001_beam_calibration`): current strongest public second-experiment no-refit candidate; ask for raw beam-deflection/broadening calibration tables behind Fig. 4 kappa-prime
- **Xiao et al. 2019** (`xiao_2019_author_data`): current lead; ask for numerical Fig. 3 probability curves and Fig. 4 visibility/momentum data
- **Hochrainer et al. 2017** (`hochrainer_2017_independent_widths`): strong inverse-problem near miss; ask whether independent coincidence-based momentum widths exist
- **Mir et al. 2007** (`mir_2007_visibility_context`): closest historical measured momentum-transfer distribution; ask if paired visibility/contrast data were recorded
- **Eibenberger et al. 2014** (`eibenberger_2014_recoil_controls`): recoil-control lane; ask for raw Fig. 2 visibility ratios and independent absorption/recoil calibration details

## Tracking

- **Kokorowski et al. 2001**: draft_ready_not_sent; issue: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/7; G11 use: could close G11 if independent calibration data justify tighter kappa uncertainty
- **Xiao et al. 2019**: draft_ready_not_sent; issue: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/2; G11 use: calibrates current lead but does not close second-experiment gate
- **Hochrainer et al. 2017**: draft_ready_not_sent; issue: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/3; G11 use: possible G11 closer if independent momentum widths exist
- **Mir et al. 2007**: draft_ready_not_sent; issue: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/4; G11 use: possible weak-value no-refit control if paired visibility sweep exists
- **Eibenberger et al. 2014**: draft_ready_not_sent; issue: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/5; G11 use: possible held-out recoil/load control if sigma_abs calibration is independent

## Contact Route Register

`author_contact_candidate_register.csv` records public source pages that can be used to verify current contact routes before sending. It intentionally does not claim that requests have been sent.

## Strict Boundary

Requested data should support a standard-QM-compatible reproducibility check. Do not frame the request as a breakthrough, collapse solution, or beyond-QM claim.

## Generated Files

```text
author_data_request_register.csv
author_data_request_tracker.csv
author_contact_candidate_register.csv
kokorowski_2001_beam_calibration_request.md
xiao_2019_author_data_request.md
hochrainer_2017_independent_widths_request.md
mir_2007_visibility_context_request.md
eibenberger_2014_recoil_controls_request.md
```
