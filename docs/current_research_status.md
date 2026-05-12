# Current Research Status

Last updated: 2026-05-12

## Active Objective

Keep the Constraint Dynamics quantum-measurement scaffold public, clean, reproducible, and conservative while pursuing the missing second independent measured-distribution-to-visibility validation.

## Artifact Checklist

| Requirement | Evidence | Status |
| --- | --- | --- |
| Public repo exists and is usable | `https://github.com/workingclassbuddha/cd-quantum-measurement` | Pass |
| Main branch remains green | Latest GitHub Actions run passed after `add author outreach queue` | Pass |
| Chapman Fourier/record-bandwidth lane implemented | `outputs/chapman_kernel/chapman_kernel_report.md`; `outputs/chapman_kernel_stress/chapman_kernel_stress_report.md` | Pass |
| Chapman complex phase overconstraint tested | `outputs/chapman_complex_kernel/`; `outputs/chapman_complex_mixture/`; `outputs/chapman_phase_grade/` | Pass, but raw phase still fails |
| Xiao distribution-to-visibility bridge implemented | `outputs/xiao_distribution_prediction_vector/`; `outputs/xiao_distribution_prediction_vector_stress/` | Pass |
| Xiao result kept conservative | `outputs/breakthrough_candidate/breakthrough_candidate_report.md` | Pass |
| Hackermueller thermal durable-record lane implemented | `outputs/hackermueller_thermal/`; `outputs/hackermueller_thermal_stress/` | Pass |
| Hornberger collisional guardrail implemented | `outputs/hornberger_collisional_scout/` | Pass |
| Second no-refit target scout implemented | `outputs/no_refit_target_scout/` | Pass, Kokorowski is now the first eligible public second target |
| Kokorowski multiphoton public-data scout implemented | `outputs/kokorowski_multiphoton_scout/` | Pass |
| Kokorowski Fig. 4 vector digitization implemented | `data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv`; `outputs/kokorowski_multiphoton_digitization/` | Pass |
| Kokorowski independent-parameter no-refit analysis implemented | `outputs/kokorowski_multiphoton/kokorowski_multiphoton_report.md` | Pass, combined independent-kappa RMSE 0.0240 |
| Kokorowski uncertainty/null stress test implemented | `outputs/kokorowski_multiphoton_stress/` | Mixed: clean nulls; component sensitivity points to independent-kappa uncertainty as the weak link |
| Kokorowski kappa-uncertainty profile implemented | `outputs/kokorowski_kappa_uncertainty_profile/` | Pass, full reported SE gives joint pass 0.417; 0.25x reported SE gives 0.975 |
| Kokorowski calibration provenance extracted | `data/extracted/KOKOROWSKI_2001_CALIBRATION_PROVENANCE.csv`; `outputs/kokorowski_calibration_provenance/` | Pass, 4 paraphrased source claims with line anchors |
| G11 gap audit implemented | `outputs/breakthrough_gap_audit/` | Pass |
| Public records checked for immediate G11 data | `outputs/public_data_availability/` | Pass, but public data does not close G11 |
| Author-data request packet prepared | `outputs/author_data_requests/` | Pass |
| Author-data request tracker prepared | `outputs/author_data_requests/author_data_request_tracker.csv`; issues #2-#5 | Pass, drafts ready but not sent |
| Author contact route candidates recorded | `outputs/author_data_requests/author_contact_candidate_register.csv` | Pass, verify before sending |
| Author outreach queue prepared | `outputs/author_outreach_queue/` | Pass, 4 rows held until contact verification |
| Author-data intake schemas prepared | `outputs/author_data_intake/` | Pass |
| Author-data manifest validator prepared | `outputs/author_data_validation/` | Pass, no rows ready for G11 yet |
| GitHub coordination created | Issues #1-#5 | Pass |
| Current goal completion audit prepared | `outputs/current_goal_audit/` | Pass, objective not complete |
| Second independent measured-distribution-to-visibility validation found | `outputs/current_goal_audit/current_goal_completion_audit.md`; `outputs/kokorowski_multiphoton_stress/` | Not yet: Kokorowski is the first eligible candidate, but stress joint probability is 0.727 |
| Lambda/Gamma/Theta product law independently validated | `outputs/breakthrough_candidate/breakthrough_candidate_scorecard.csv` gate G12 | Fail |
| Beyond-QM or collapse claim made | README, theory notes, and reports reject this claim | Correctly not claimed |

## Current Verdict

```text
lead candidate found, breakthrough not yet
```

The strongest empirical structure is now Xiao plus Kokorowski: Xiao gives the cleanest within-paper no-refit momentum-distribution prediction, and Kokorowski gives a second-experiment public no-refit decoherence prediction from independently reported many-photon parameters.

This is still not enough for a breakthrough claim because Chapman raw complex phase remains unrepaired and the Lambda/Gamma/Theta product law is not independently validated. Kokorowski has now been stress-tested: the null controls are clean, point/visibility uncertainty alone is stable, but independent-kappa uncertainty is not strong enough to treat it as publication-grade.

The kappa-uncertainty profile makes the next provenance question numerical: full reported kappa SE gives joint stress pass probability 0.417; half reported SE gives 0.783; quarter reported SE gives 0.975. The next useful G11 move is to verify whether the beam-deflection/broadening calibration justifies a tighter effective uncertainty, preferably from source text, author tables, or a reproduced calibration.

The calibration-provenance extractor now anchors the independence premise to the arXiv TeX source by source SHA and line windows. It supports the public-data rationale but also records the remaining gap: raw beam-deflection/broadening calibration tables are not present in the public source package.

## Open Gates

- **G10:** Chapman raw complex phase remains unrepaired.
- **G11:** second independent public no-refit candidate found in Kokorowski; first stress test is mixed and calls for tighter provenance/uncertainty work.
- **G12:** Lambda/Gamma/Theta product law remains provisional.

## Live Coordination

- Parent G11 tracker: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/1
- Xiao author data: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/2
- Hochrainer author data: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/3
- Mir author data: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/4
- Eibenberger author data: https://github.com/workingclassbuddha/cd-quantum-measurement/issues/5

## Next Decision

Do not add more model freedom until either:

1. author-level numerical data create a second held-out no-refit test; or
2. Kokorowski survives a stricter robustness pass as a second independent no-refit validation.

Immediate public-data next step:

```bash
python src/constraint_dynamics_quantum_v3.py digitize-kokorowski-multiphoton \
  --source-dir outputs/tmp/kokorowski_source/extracted \
  --output-dir outputs/kokorowski_multiphoton_digitization \
  --data-dir data/extracted

python src/constraint_dynamics_quantum_v3.py analyze-kokorowski-multiphoton \
  --input data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv \
  --output-dir outputs/kokorowski_multiphoton

python src/constraint_dynamics_quantum_v3.py stress-test-kokorowski-multiphoton \
  --input data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv \
  --output-dir outputs/kokorowski_multiphoton_stress \
  --n-bootstrap 1000 \
  --seed 28044
```

If neither path produces a second validation, the honest conclusion is that the current breakthrough path has found a strong empirical target but not a breakthrough.
