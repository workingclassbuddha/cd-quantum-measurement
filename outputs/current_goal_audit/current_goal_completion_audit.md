# Current Goal Completion Audit

Verdict: objective not complete: breakthrough path still blocked

## Objective

Keep the public repo clean and green, continue provenance-rich analyses, and drive toward the missing second independent measured-distribution-to-visibility validation without overclaiming.

## Summary

- Objective achieved: False
- Failed requirements: 3
- Eligible second no-refit targets: 1
- Stress-closed second no-refit targets: 0
- G11 top blocker class: stress_or_calibration_uncertainty_limited
- Current public G11 path exhausted: True
- G11 closure evidence queue rows: 14
- G11 closure evidence classes: independent_record_distribution;paired_visibility_curve;raw_calibration_tables
- G11 closure evidence intake requirement rows: 14
- G11 closure evidence intake classes: independent_record_distribution;paired_visibility_curve;raw_calibration_tables
- G11 closure evidence artifact preflight passed: False
- G11 closure evidence missing artifact count: 9
- G11 closure evidence missing artifact rows: 42
- G11 closure evidence blocked classes: 3
- G11 closure evidence blocked candidates: 14
- G11 closure evidence source query rows: 42
- G11 closure evidence source query status: not_searched
- G11 closure evidence source query batches: 3
- G11 closure evidence top source query batch: raw_calibration_tables
- G11 closure evidence source routes: 42
- G11 closure evidence source route status: route_known_not_checked
- G11 closure evidence source route checklist rows: 14
- G11 closure evidence source route checklist status: not_checked
- G11 closure evidence source access plan rows: 14
- G11 closure evidence arXiv e-print access candidates: 7
- G11 closure evidence arXiv source package inventory rows: 7
- G11 closure evidence arXiv source package inventory status: not_checked
- G11 closure evidence top arXiv source package candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- G11 closure evidence arXiv package acceptance manifest rows: 21
- G11 closure evidence arXiv package acceptance manifest status: not_checked
- G11 closure evidence top arXiv package required artifact: beam_deflection_broadening_calibration.csv
- G11 closure evidence arXiv package retrieval ledger rows: 7
- G11 closure evidence arXiv package retrieval status: not_fetched
- G11 closure evidence top arXiv package expected archive: outputs/tmp/arxiv_source_packages/KOKOROWSKI_2001_MULTIPHOTON_SCATTERING/source.tar
- G11 closure evidence arXiv package inspection checklist rows: 21
- G11 closure evidence arXiv package inspection status: pending_fetch
- G11 closure evidence top arXiv package inspection pattern: beam|deflection|broadening|calibration|kappa
- G11 closure evidence arXiv package local inspection rows: 21
- G11 closure evidence arXiv package local inspection status: missing_cache
- G11 closure evidence top arXiv package local inspection matches: 0
- Top G11 closure intake priority: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING
- Top G11 closure intake class: raw_calibration_tables
- Top G11 closure intake acceptance gates: G11C;G11F;G11G
- Top G11 closure intake preflight passed: False
- Top G11 closure intake missing artifact count: 6
- Current breakthrough path exhausted without closure: True
- G11 closure contract gates: 7
- G11 closure-ready targets: 0
- Public G11 candidates scored against contract: 14
- Public G11 candidates clearing all gates: 0
- Top public G11 candidate: KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; failed gates: G11C;G11F;G11G
- Can update G11 scorecard: False
- G11 scorecard preflight failed checks: 4
- Kokorowski failed tracked G11 gates: 3
- Kokorowski failed G11 gate ids: G11C;G11F;G11G
- Kokorowski gap audit can update G11 scorecard: False
- Public G11 support without author contact: 0
- Author-data G11-ready rows: 0
- Empirical product-law-ready datasets: 0
- Partial product-law proxy candidates: 14
- Proxy-rich product-law candidates: 2
- Kokorowski joint stress probability: 0.727
- Kokorowski full reported-SE joint pass probability: 0.4166666666666667
- Kokorowski max SE scale with joint pass >= 0.80: 0.25
- Kokorowski calibration provenance status: calibration provenance extracted
- Kokorowski calibration provenance scope warning: True
- Kokorowski public raw calibration tables found: False
- Kokorowski calibration provenance blocker: raw beam-deflection/broadening calibration data are still not in the public source package
- Kokorowski detector-convolution check: detector-convolution reconstruction supports reported kappa-prime values; all within two reported SE: True; max delta: 0.0883545445616271; clears G11: False
- Chapman raw-phase blocker: G10 still blocked by raw phase; branch-optimized RMSE: 1.4753015761661024; branch gate pass: False
- Kokorowski Fig. 3 public-vector check: fig3 public-vector consistency check passes as supporting evidence; log10 RMSE: 0.0458239682635031; branch-swap pass: True; null margin: 0.247164038377803; clears G11: False
- Mir Fig. 4 eraser phase control: fig4 eraser phase-control check passes as supporting evidence; supports eraser control: True; zero-lag correlation: -0.3414869769663372; best shifted correlation: 0.8462180984453633; clears G11: False
- Kokorowski stress pass: False

## Failed Or Open Requirements

- **second_independent_distribution_to_visibility_validation**: eligible_second=1; public_support=0; stress_closed_second=0; top_blocker=stress_or_calibration_uncertainty_limited; recommended_next=tighten independent-kappa calibration provenance/uncertainty or find a cleaner second no-refit dataset; current_public_path_exhausted=True; closure_evidence_queue=14; closure_evidence_classes=independent_record_distribution;paired_visibility_curve;raw_calibration_tables; closure_evidence_intake_requirements=14; closure_evidence_intake_classes=independent_record_distribution;paired_visibility_curve;raw_calibration_tables; closure_artifact_preflight_passed=False; closure_missing_artifacts=9; closure_missing_artifact_rows=42; closure_blocked_classes=3; closure_blocked_candidates=14; closure_candidate_actions=14; closure_blocked_candidate_actions=14; closure_top_action_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_acquisition_manifest_rows=9; closure_top_acquisition_artifact=independence_provenance.md; closure_top_acquisition_candidate_count=9; closure_bundle_manifest_rows=14; closure_blocked_bundles=14; closure_top_bundle_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_source_queries=42; closure_source_query_candidates=14; closure_source_query_status=not_searched; closure_top_source_query_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_source_query_batches=3; closure_top_source_query_batch=raw_calibration_tables; closure_top_source_query_batch_status=not_searched; closure_source_routes=42; closure_source_route_status=route_known_not_checked; closure_top_source_route=https://arxiv.org/abs/quant-ph/0009044; closure_source_route_checklist=14; closure_source_route_checklist_status=not_checked; closure_top_source_route_check_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_source_access_plan=14; closure_source_access_arxiv_eprint_candidates=7; closure_top_source_access_class=arxiv_eprint_route; closure_arxiv_source_package_inventory=7; closure_arxiv_source_package_status=not_checked; closure_top_arxiv_source_package_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_arxiv_package_acceptance_manifest=21; closure_arxiv_package_acceptance_status=not_checked; closure_top_arxiv_package_acceptance_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_top_arxiv_package_required_artifact=beam_deflection_broadening_calibration.csv; closure_arxiv_package_retrieval_ledger=7; closure_arxiv_package_retrieval_status=not_fetched; closure_top_arxiv_package_retrieval_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_top_arxiv_package_expected_archive=outputs/tmp/arxiv_source_packages/KOKOROWSKI_2001_MULTIPHOTON_SCATTERING/source.tar; closure_arxiv_package_inspection_checklist=21; closure_arxiv_package_inspection_status=pending_fetch; closure_top_arxiv_package_inspection_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_top_arxiv_package_inspection_pattern=beam|deflection|broadening|calibration|kappa; closure_arxiv_package_local_inspection_rows=21; closure_arxiv_package_local_inspection_status=missing_cache; closure_top_arxiv_package_local_inspection_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; closure_top_arxiv_package_local_inspection_match_count=0; top_intake_priority=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; top_intake_class=raw_calibration_tables; top_intake_acceptance_gates=G11C;G11F;G11G; top_intake_preflight_passed=False; top_intake_missing_artifacts=6; author_ready=0; kokorowski_joint=0.727; full_reported_se_joint=0.417; max_se_scale_for_joint_gate=0.250; provenance_status=calibration provenance extracted; provenance_scope_warning=True; public_raw_tables_found=False; provenance_blocker=raw beam-deflection/broadening calibration data are still not in the public source package; detector_convolution_status=detector-convolution reconstruction supports reported kappa-prime values; detector_all_within_two_se=True; detector_max_delta=0.088; detector_clears_g11=False; fig3_status=fig3 public-vector consistency check passes as supporting evidence; fig3_log10_rmse=0.046; fig3_branch_swap_pass=True; fig3_null_margin=0.247; fig3_clears_g11=False; mir_fig4_status=fig4 eraser phase-control check passes as supporting evidence; mir_fig4_supports_eraser_control=True; mir_fig4_zero_lag_corr=-0.341; mir_fig4_best_shift_corr=0.846; mir_fig4_clears_g11=False; g11_closure_ready=0; public_candidates_scored=14; public_candidates_clearing_all_gates=0; top_public_candidate=KOKOROWSKI_2001_MULTIPHOTON_SCATTERING; top_public_failed_gates=G11C;G11F;G11G; kokorowski_failed_tracked_gates=3; kokorowski_failed_gate_ids=G11C;G11F;G11G; kokorowski_gap_can_update_scorecard=False; stress_pass=False
- **chapman_raw_phase_repaired**: G10 remains a blocker unless the scorecard says raw phase repaired; phase_verdict=G10 still blocked by raw phase; branch_optimized_rmse=1.475; branch_gate_pass=False; branch_model=complex:beta_recoil_complex.
- **product_law_independently_validated**: G12 remains a blocker unless independent Lambda/Gamma/Theta factors validate the product law; empirical_ready=0; partial_proxy_candidates=14; proxy_rich_candidates=2; named_proxy_rich_blockers=2.

## Rule

Do not mark the goal complete while any failed requirement remains. Passing CI or finding a G11 candidate cannot substitute for stress-tested second validation, Chapman phase repair, or product-law validation.
