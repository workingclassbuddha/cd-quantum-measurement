# Author Outreach Queue

Verdict: author outreach prepared; current contacts still require verification

This queue is the current action surface for the missing G11 gate. It does not claim any request has been sent. Every row remains on hold until the current contact route is verified outside the repo.

## Queue Summary

- Queue rows: 5
- Ready to send now: 0
- Held for contact verification: 5
- Possible G11 closers if received and independently validated: 4
- Author-data G11-ready rows already received: 0

## Immediate Actions

- **Priority 1: Kokorowski et al. 2001** - hold_until_contact_verified; blocker: verify_current_contact_route; G11 role: possible second no-refit closer if independence is confirmed; draft: `outputs/author_data_requests/kokorowski_2001_beam_calibration_request.md`
- **Priority 2: Xiao et al. 2019** - hold_until_contact_verified; blocker: verify_current_contact_route; G11 role: calibration/control data; useful but cannot close G11 alone; draft: `outputs/author_data_requests/xiao_2019_author_data_request.md`
- **Priority 3: Hochrainer et al. 2017** - hold_until_contact_verified; blocker: verify_current_contact_route; G11 role: possible second no-refit closer if independence is confirmed; draft: `outputs/author_data_requests/hochrainer_2017_independent_widths_request.md`
- **Priority 4: Mir et al. 2007** - hold_until_contact_verified; blocker: verify_current_contact_route; G11 role: possible second no-refit closer if independence is confirmed; draft: `outputs/author_data_requests/mir_2007_visibility_context_request.md`
- **Priority 5: Eibenberger et al. 2014** - hold_until_contact_verified; blocker: verify_current_contact_route; G11 role: possible second no-refit closer if independence is confirmed; draft: `outputs/author_data_requests/eibenberger_2014_recoil_controls_request.md`

## Contact Verification Routes

- **Kokorowski et al. 2001**: verify via MIT atom interferometer group / arXiv author record / DOI publisher page. Source: https://arxiv.org/abs/quant-ph/0009044
- **Xiao et al. 2019**: verify via Griffith repository / arXiv author record / institutional pages. Source: https://research-repository.griffith.edu.au/items/18f6c166-89ac-46c5-a199-701f6c57f6b4
- **Hochrainer et al. 2017**: verify via PMC correspondence line for Hochrainer/Zeilinger. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5320961/
- **Mir et al. 2007**: verify via Lundeen Lab publication page / arXiv author record. Source: https://quantumphotonics.uottawa.ca/Publications/A-double-slit-which-way-experiment-on-the-complementarity-uncertainty-debate
- **Eibenberger et al. 2014**: verify via University of Vienna publication page / corresponding author route. Source: https://ucrisportal.univie.ac.at/en/publications/absolute-absorption-cross-sections-from-photon-recoil-in-a-matter/

## Possible G11 Closers

- **Kokorowski et al. 2001**: beam_deflection_broadening_calibration.csv; kappa_uncertainty_notes.md. Independence rule: nbar, sigma_n, or kappa_prime uncertainty must come from beam calibration independent of Fig. 4 contrast fitting
- **Hochrainer et al. 2017**: visibility_profiles.csv; independent_momentum_widths.csv. Independence rule: record width must be measured or simulated independently of the visibility FWHM being predicted
- **Mir et al. 2007**: pwv_distribution.csv; visibility_or_contrast_sweep.csv. Independence rule: P_wv(q) and visibility/contrast must be paired by controlled which-way settings
- **Eibenberger et al. 2014**: visibility_ratios.csv; independent_sigma_or_recoil_calibration.csv. Independence rule: sigma_abs or equivalent recoil/load calibration must not be inferred from the same visibility reduction

## Strict Boundary

The outreach should ask for numerical data and uncertainty/provenance notes only. It should not frame the project as a collapse solution, a product-law validation, or a beyond-standard-quantum-mechanics claim.
