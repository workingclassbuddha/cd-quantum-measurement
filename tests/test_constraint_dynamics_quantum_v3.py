import math
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from constraint_dynamics_quantum_v3 import (  # noqa: E402
    ApparatusSettings,
    build_confounded_visibility_dataset,
    build_accessibility_benchmark_dataset,
    build_joint_density,
    build_synthetic_visibility_dataset,
    chapman_complex_observables,
    chapman_default_complex_digitization_metadata,
    chapman_default_digitization_metadata,
    chapman_default_phase_grade_metadata,
    chapman_digitized_dataframe,
    chapman_mixture_amplitude,
    chapman_mixture_weights,
    chapman_phase_grade_dataframe,
    chapman_phase_quality_subset,
    chapman_phase_digitized_dataframe,
    chapman_characteristic_visibility,
    chapman_kernel_visibility,
    chapman_recoil_grid,
    chapman_sinc_first_zero,
    chapman_two_photon_amplitude,
    chapman_uniform_recoil_density,
    chapman_velocity_smearing,
    bootstrap_chapman_kernel_stress,
    cormann_theory_visibility,
    decompose_eraser_dataset,
    design_diagnostics,
    energetic_constraint,
    fit_xiao_momentum_models,
    fit_hackermueller_thermal_models,
    fit_chapman_kernel_models,
    fit_chapman_complex_kernel_models,
    fit_accessibility_hypotheses,
    fit_visibility_models,
    jitter_chapman_visibility,
    jitter_xiao_momentum,
    jitter_xiao_probability_distribution,
    main,
    make_chapman_complex_mixture_outputs,
    make_chapman_complex_kernel_outputs,
    make_chapman_phase_grade_outputs,
    make_chapman_kernel_stress_outputs,
    make_cormann_visibility_phase_scout_outputs,
    make_hackermueller_thermal_analysis_outputs,
    make_hackermueller_thermal_digitization_outputs,
    make_hackermueller_thermal_stress_outputs,
    make_xiao_momentum_analysis_outputs,
    make_xiao_momentum_digitization_outputs,
    make_xiao_momentum_stress_outputs,
    make_xiao_probability_outputs,
    make_xiao_probability_vector_outputs,
    make_xiao_distribution_prediction_outputs,
    make_xiao_distribution_prediction_stress_outputs,
    make_breakthrough_candidate_outputs,
    make_breakthrough_author_data_requests,
    make_author_outreach_queue,
    make_author_data_intake_outputs,
    make_breakthrough_gap_audit_outputs,
    make_current_goal_completion_audit_outputs,
    make_public_data_availability_outputs,
    make_no_refit_target_scout_outputs,
    make_eibenberger_recoil_scout_outputs,
    make_mir_weak_value_scout_outputs,
    make_hochrainer_momentum_correlation_scout_outputs,
    make_kokorowski_multiphoton_scout_outputs,
    make_kokorowski_multiphoton_digitization_outputs,
    make_kokorowski_multiphoton_analysis_outputs,
    make_kokorowski_multiphoton_stress_outputs,
    kokorowski_fig4_pixel_to_data,
    kokorowski_visibility_from_kappa,
    make_hornberger_collisional_scout_outputs,
    make_record_bandwidth_synthesis_outputs,
    partial_trace_marker,
    path_visibility_from_rho,
    pixel_to_data,
    predict_xiao_visibility_from_distribution,
    quantum_eraser_observables,
    hackermueller_default_metadata,
    hackermueller_digitized_dataframe,
    jitter_hackermueller_thermal,
    eibenberger_default_metadata,
    eibenberger_digitized_dataframe,
    eibenberger_recoil_reduction,
    mir_weak_value_metadata,
    mir_weak_value_scout_dataframe,
    hochrainer_momentum_correlation_metadata,
    hochrainer_momentum_correlation_scout_dataframe,
    kokorowski_multiphoton_metadata,
    kokorowski_multiphoton_scout_dataframe,
    fit_hornberger_collisional_scout,
    hornberger_default_metadata,
    hornberger_digitized_dataframe,
    xiao_default_momentum_metadata,
    xiao_default_probability_metadata,
    xiao_distribution_branch_moments,
    xiao_momentum_digitized_dataframe,
    xiao_probability_digitized_dataframe,
    summarize_xiao_probability,
    validate_author_data_manifest,
)


def test_raw_visibility_equals_marker_times_eta():
    settings = ApparatusSettings(marker_angle=0.83)
    rho, meta = build_joint_density(settings)
    raw_visibility = path_visibility_from_rho(partial_trace_marker(rho))
    marker_visibility = abs(math.cos(settings.marker_angle))
    assert np.isclose(raw_visibility, marker_visibility * meta["eta"], atol=1e-12)


def test_optimal_eraser_reaches_eta_bound():
    for alpha in [0.0, 0.3, 0.9, 1.35]:
        settings = ApparatusSettings(marker_angle=alpha)
        obs = quantum_eraser_observables(settings)
        assert np.isclose(obs["visibility_eraser_optimal_best"], obs["eta"], atol=1e-12)


def test_fixed_eraser_can_be_below_eta():
    settings = ApparatusSettings(marker_angle=1.2)
    obs = quantum_eraser_observables(settings)
    assert obs["visibility_eraser_plus"] <= obs["eta"] + 1e-12
    assert obs["visibility_eraser_minus"] <= obs["eta"] + 1e-12
    assert obs["visibility_eraser_plus"] < obs["eta"]


def test_record_accessibility_reduces_effective_theta():
    inaccessible = energetic_constraint(
        record_entropy_bits=2.0,
        record_survival_probability=1.0,
        environment_coupling=1.0,
        record_accessibility=0.0,
    )
    accessible = energetic_constraint(
        record_entropy_bits=2.0,
        record_survival_probability=1.0,
        environment_coupling=1.0,
        record_accessibility=1.0,
    )
    partial = energetic_constraint(
        record_entropy_bits=2.0,
        record_survival_probability=1.0,
        environment_coupling=1.0,
        record_accessibility=0.5,
    )
    assert inaccessible > partial > accessible
    assert np.isclose(accessible, 0.0)


def test_accessibility_benchmark_ranks_aware_product_first():
    df = build_accessibility_benchmark_dataset(noise_sd=0.0)
    summary, *_ = fit_accessibility_hypotheses(df)
    assert summary.iloc[0]["model"] == "aware_record_product"
    naive = summary[summary["model"] == "naive_record_product"].iloc[0]
    aware = summary[summary["model"] == "aware_record_product"].iloc[0]
    assert naive["aicc"] - aware["aicc"] > 10.0


def test_chapman_calibration_maps_axis_anchors():
    metadata = chapman_default_digitization_metadata()
    axis = metadata["figures"][0]["axis"]
    x_min, y_min = pixel_to_data(
        axis["x_pixel_min"][0],
        axis["y_pixel_min"][1],
        axis,
    )
    x_max, y_max = pixel_to_data(
        axis["x_pixel_max"][0],
        axis["y_pixel_max"][1],
        axis,
    )
    assert np.isclose(x_min, axis["x_min"])
    assert np.isclose(y_min, axis["y_min"])
    assert np.isclose(x_max, axis["x_max"])
    assert np.isclose(y_max, axis["y_max"])


def test_chapman_digitized_dataframe_schema_and_pairs():
    df = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    required = {
        "study_id",
        "source_figure",
        "x_name",
        "x_value",
        "visibility_obs",
        "visibility_type",
        "conditioned_on",
    }
    assert required.issubset(df.columns)
    assert len(df) == 36
    counts = df.groupby(["x_name", "x_value"])["visibility_type"].nunique()
    assert counts.min() == 2


def test_chapman_digitized_decomposition_has_recovery_window():
    df = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    decomposition = decompose_eraser_dataset(df)
    assert not decomposition.empty
    peak = decomposition.loc[decomposition["recovery_fraction"].idxmax()]
    assert 0.35 <= peak["x_value"] <= 0.65
    assert peak["recovery_fraction"] > 0.5


def test_xiao_calibration_maps_axis_anchors():
    metadata = xiao_default_momentum_metadata()
    axis = metadata["figures"][0]["axis"]
    x_min, y_min = pixel_to_data(
        axis["x_pixel_min"][0],
        axis["y_pixel_min"][1],
        axis,
    )
    x_max, y_max = pixel_to_data(
        axis["x_pixel_max"][0],
        axis["y_pixel_max"][1],
        axis,
    )
    assert np.isclose(x_min, axis["x_min"])
    assert np.isclose(y_min, axis["y_min"])
    assert np.isclose(x_max, axis["x_max"])
    assert np.isclose(y_max, axis["y_max"])


def test_xiao_digitized_dataframe_schema_and_bound():
    df = xiao_momentum_digitized_dataframe(xiao_default_momentum_metadata())
    required = {
        "study_id",
        "visibility_V",
        "visibility_loss",
        "momentum_abs_hbar_over_d",
        "published_bound_2_over_pi_loss",
        "above_bound_margin",
        "pixel_x",
        "pixel_y",
    }
    assert required.issubset(df.columns)
    assert len(df) == 6
    assert df["visibility_V"].between(0.0, 1.0).all()
    assert (df["momentum_abs_hbar_over_d"] >= 0.0).all()
    assert (df["above_bound_margin"] >= 0.0).all()


def test_xiao_momentum_analysis_finds_tight_bandwidth_relation():
    df = xiao_momentum_digitized_dataframe(xiao_default_momentum_metadata())
    summary, predictions, clean = fit_xiao_momentum_models(df)
    assert not summary.empty
    assert not predictions.empty
    assert len(clean) == 6
    linear = summary[summary["model"] == "linear_bandwidth"].iloc[0]
    bound = summary[summary["model"] == "published_bound"].iloc[0]
    assert linear["rmse_momentum"] < 0.01
    assert linear["rmse_momentum"] < bound["rmse_momentum"]


def test_xiao_momentum_outputs_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "xiao_digitize"
    analysis_dir = tmp_path / "xiao_analysis"
    cli_dir = tmp_path / "xiao_cli"

    digitized, metadata, digitization_summary = make_xiao_momentum_digitization_outputs(
        None,
        output_dir,
        data_dir,
        render_pdf=False,
    )
    assert not digitized.empty
    assert metadata["study_id"] == "XIAO_2019_MOMENTUM"
    assert not digitization_summary.empty
    assert (data_dir / "XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv").exists()
    assert (data_dir / "XIAO_2019_MOMENTUM_DIGITIZATION.json").exists()
    assert (output_dir / "xiao_digitization_report.md").exists()

    summary, predictions = make_xiao_momentum_analysis_outputs(
        data_dir / "XIAO_2019_MOMENTUM_VISIBILITY_DIGITIZED.csv",
        analysis_dir,
    )
    assert not summary.empty
    assert not predictions.empty
    assert (analysis_dir / "xiao_momentum_report.md").exists()
    assert (analysis_dir / "xiao_momentum_summary.csv").exists()
    assert (analysis_dir / "xiao_momentum_predictions.csv").exists()

    main(
        [
            "digitize-xiao-momentum",
            "--output-dir",
            str(cli_dir),
            "--data-dir",
            str(data_dir),
            "--skip-render",
        ]
    )
    assert (cli_dir / "xiao_digitization_report.md").exists()


def test_xiao_jitter_preserves_schema_and_bounds():
    df = xiao_momentum_digitized_dataframe(xiao_default_momentum_metadata())
    jittered = jitter_xiao_momentum(df, np.random.default_rng(123))
    assert list(jittered.columns) == list(df.columns)
    assert len(jittered) == len(df)
    assert jittered["visibility_V"].between(0.0, 1.0).all()
    assert (jittered["momentum_abs_hbar_over_d"] >= 0.0).all()


def test_xiao_momentum_stress_outputs_and_cli(tmp_path):
    df = xiao_momentum_digitized_dataframe(xiao_default_momentum_metadata())
    input_csv = tmp_path / "xiao.csv"
    metadata_json = tmp_path / "xiao.json"
    output_dir = tmp_path / "xiao_stress"
    cli_output_dir = tmp_path / "xiao_stress_cli"
    df.to_csv(input_csv, index=False)
    metadata_json.write_text(
        json.dumps(xiao_default_momentum_metadata()),
        encoding="utf-8",
    )

    summary, bootstrap, null_summary, null_samples = make_xiao_momentum_stress_outputs(
        input_csv,
        metadata_json,
        output_dir,
        n_bootstrap=8,
        seed=456,
    )
    assert "p_linear_beats_published_bound" in summary.columns
    assert not bootstrap.empty
    assert not null_summary.empty
    assert not null_samples.empty
    assert (output_dir / "xiao_momentum_stress_report.md").exists()
    assert (output_dir / "stress_summary.csv").exists()
    assert (output_dir / "bootstrap_samples.csv").exists()
    assert (output_dir / "null_test_summary.csv").exists()

    main(
        [
            "stress-test-xiao-momentum",
            "--input",
            str(input_csv),
            "--digitization-json",
            str(metadata_json),
            "--output-dir",
            str(cli_output_dir),
            "--n-bootstrap",
            "6",
            "--seed",
            "789",
        ]
    )
    assert (cli_output_dir / "xiao_momentum_stress_report.md").exists()


def test_xiao_probability_dataframe_has_growth_and_side_peaks():
    df = xiao_probability_digitized_dataframe(xiao_default_probability_metadata())
    assert not df.empty
    assert {"mean_abs_momentum_vs_z", "momentum_distribution"}.issubset(
        set(df["observable"])
    )
    summary = summarize_xiao_probability(df)
    growth = summary[summary["metric"] == "mean_abs_growth"].iloc[0]
    side = summary[summary["metric"] == "side_peak_abs_mean"].iloc[0]
    red_peak = summary[
        (summary["metric"] == "peak_density") & (summary["branch"] == "phi_0_far")
    ].iloc[0]
    assert growth["value"] > 0.45
    assert 1.2 <= side["value"] <= 2.0
    assert abs(red_peak["x_at_value"]) < 0.25


def test_xiao_probability_outputs_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "xiao_probability"
    cli_output_dir = tmp_path / "xiao_probability_cli"

    digitized, metadata, summary = make_xiao_probability_outputs(
        None,
        output_dir,
        data_dir,
        render_pdf=False,
    )
    assert not digitized.empty
    assert metadata["study_id"] == "XIAO_2019_MOMENTUM_PROBABILITY"
    assert not summary.empty
    assert (data_dir / "XIAO_2019_PROBABILITY_DIGITIZED.csv").exists()
    assert (data_dir / "XIAO_2019_PROBABILITY_DIGITIZATION.json").exists()
    assert (output_dir / "xiao_probability_report.md").exists()
    assert (output_dir / "xiao_probability_summary.csv").exists()

    main(
        [
            "digitize-xiao-probability",
            "--output-dir",
            str(cli_output_dir),
            "--data-dir",
            str(data_dir),
            "--skip-render",
        ]
    )
    assert (cli_output_dir / "xiao_probability_report.md").exists()


def test_xiao_probability_vector_outputs_and_cli(tmp_path):
    source_dir = Path("outputs/tmp/second_hunt_sources/xiao")
    if not (source_dir / "probability.pdf").exists():
        pytest.skip("Xiao arXiv source package is not available locally")
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "xiao_probability_vector"
    prediction_dir = tmp_path / "xiao_prediction_vector"
    cli_output_dir = tmp_path / "xiao_probability_vector_cli"

    digitized, metadata, summary, moments = make_xiao_probability_vector_outputs(
        source_dir,
        output_dir,
        data_dir,
    )
    assert not digitized.empty
    assert not summary.empty
    assert not moments.empty
    assert metadata["extraction_method"] == "vector_path_digitization_v1"
    assert (data_dir / "XIAO_2019_PROBABILITY_VECTOR_DIGITIZED.csv").exists()
    assert (data_dir / "XIAO_2019_PROBABILITY_VECTOR_DIGITIZATION.json").exists()
    assert (output_dir / "xiao_probability_vector_report.md").exists()
    dist = digitized[digitized["observable"] == "momentum_distribution"]
    assert {"phi_0_far", "phi_pi_far"}.issubset(set(dist["branch"]))
    phi0 = moments[moments["branch"] == "phi_0_far"].iloc[0]
    phipi = moments[moments["branch"] == "phi_pi_far"].iloc[0]
    assert phipi["mean_abs_momentum_hbar_over_d"] > phi0[
        "mean_abs_momentum_hbar_over_d"
    ]

    momentum = xiao_momentum_digitized_dataframe(xiao_default_momentum_metadata())
    momentum_csv = tmp_path / "xiao_momentum.csv"
    momentum.to_csv(momentum_csv, index=False)
    prediction_summary, _predictions, _moments = make_xiao_distribution_prediction_outputs(
        momentum_csv,
        data_dir / "XIAO_2019_PROBABILITY_VECTOR_DIGITIZED.csv",
        prediction_dir,
    )
    no_refit = prediction_summary[
        prediction_summary["model"] == "distribution_no_refit"
    ].iloc[0]
    bound = prediction_summary[
        prediction_summary["model"] == "published_bound"
    ].iloc[0]
    assert no_refit["rmse_momentum"] < bound["rmse_momentum"]

    main(
        [
            "digitize-xiao-probability-vector",
            "--source-dir",
            str(source_dir),
            "--output-dir",
            str(cli_output_dir),
            "--data-dir",
            str(data_dir),
        ]
    )
    assert (cli_output_dir / "xiao_probability_vector_report.md").exists()


def test_xiao_distribution_branch_moments_are_ordered():
    probability = xiao_probability_digitized_dataframe(xiao_default_probability_metadata())
    moments = xiao_distribution_branch_moments(probability)
    phi0 = moments[moments["branch"] == "phi_0_far"].iloc[0]
    phipi = moments[moments["branch"] == "phi_pi_far"].iloc[0]
    assert phi0["mean_abs_momentum_hbar_over_d"] >= 0.0
    assert phipi["mean_abs_momentum_hbar_over_d"] > phi0[
        "mean_abs_momentum_hbar_over_d"
    ]


def test_xiao_distribution_prediction_beats_published_bound():
    momentum = xiao_momentum_digitized_dataframe(xiao_default_momentum_metadata())
    probability = xiao_probability_digitized_dataframe(xiao_default_probability_metadata())
    summary, predictions, moments = predict_xiao_visibility_from_distribution(
        momentum,
        probability,
    )
    assert not predictions.empty
    assert not moments.empty
    no_refit = summary[summary["model"] == "distribution_no_refit"].iloc[0]
    bound = summary[summary["model"] == "published_bound"].iloc[0]
    assert no_refit["n_fit_params_to_fig4"] == 0
    assert no_refit["rmse_momentum"] < bound["rmse_momentum"]


def test_xiao_distribution_prediction_outputs_and_cli(tmp_path):
    momentum = xiao_momentum_digitized_dataframe(xiao_default_momentum_metadata())
    probability = xiao_probability_digitized_dataframe(xiao_default_probability_metadata())
    momentum_csv = tmp_path / "xiao_momentum.csv"
    probability_csv = tmp_path / "xiao_probability.csv"
    output_dir = tmp_path / "xiao_distribution_prediction"
    cli_output_dir = tmp_path / "xiao_distribution_prediction_cli"
    momentum.to_csv(momentum_csv, index=False)
    probability.to_csv(probability_csv, index=False)

    summary, predictions, moments = make_xiao_distribution_prediction_outputs(
        momentum_csv,
        probability_csv,
        output_dir,
    )
    assert not summary.empty
    assert not predictions.empty
    assert not moments.empty
    assert (output_dir / "xiao_distribution_prediction_report.md").exists()
    assert (output_dir / "xiao_distribution_prediction_summary.csv").exists()
    assert (output_dir / "xiao_distribution_prediction_predictions.csv").exists()
    assert (output_dir / "xiao_distribution_moments.csv").exists()

    main(
        [
            "predict-xiao-visibility-from-distribution",
            "--momentum-input",
            str(momentum_csv),
            "--probability-input",
            str(probability_csv),
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "xiao_distribution_prediction_report.md").exists()


def test_xiao_probability_jitter_preserves_schema_and_bounds():
    probability = xiao_probability_digitized_dataframe(xiao_default_probability_metadata())
    jittered = jitter_xiao_probability_distribution(
        probability,
        np.random.default_rng(123),
    )
    assert len(jittered) == len(probability)
    assert set(jittered.columns) == set(probability.columns)
    dist = jittered[jittered["observable"] == "momentum_distribution"]
    assert (dist["probability_density"] >= 0.0).all()
    assert dist["p_hbar_over_d"].between(-3.2, 3.2).all()


def test_xiao_distribution_prediction_stress_outputs_and_cli(tmp_path):
    momentum = xiao_momentum_digitized_dataframe(xiao_default_momentum_metadata())
    probability = xiao_probability_digitized_dataframe(xiao_default_probability_metadata())
    momentum_csv = tmp_path / "xiao_momentum.csv"
    probability_csv = tmp_path / "xiao_probability.csv"
    output_dir = tmp_path / "xiao_distribution_stress"
    cli_output_dir = tmp_path / "xiao_distribution_stress_cli"
    momentum.to_csv(momentum_csv, index=False)
    probability.to_csv(probability_csv, index=False)

    summary, bootstrap, null_summary, baseline = (
        make_xiao_distribution_prediction_stress_outputs(
            momentum_csv,
            probability_csv,
            output_dir,
            n_bootstrap=8,
            seed=456,
        )
    )
    assert not summary.empty
    assert not bootstrap.empty
    assert not null_summary.empty
    assert not baseline.empty
    assert "p_no_refit_beats_published_bound" in summary.columns
    assert (output_dir / "xiao_distribution_prediction_stress_report.md").exists()
    assert (output_dir / "stress_summary.csv").exists()
    assert (output_dir / "bootstrap_samples.csv").exists()
    assert (output_dir / "null_test_summary.csv").exists()
    assert (output_dir / "baseline_sensitivity.csv").exists()
    assert (output_dir / "baseline_bootstrap_summary.csv").exists()

    main(
        [
            "stress-test-xiao-distribution-prediction",
            "--momentum-input",
            str(momentum_csv),
            "--probability-input",
            str(probability_csv),
            "--output-dir",
            str(cli_output_dir),
            "--n-bootstrap",
            "8",
            "--seed",
            "789",
        ]
    )
    assert (cli_output_dir / "xiao_distribution_prediction_stress_report.md").exists()


def test_record_bandwidth_synthesis_outputs_and_cli(tmp_path):
    chapman_kernel = pd.DataFrame(
        [
            {
                "branch": "raw",
                "model": "sinc_fourier",
                "rmse_visibility": 0.026,
                "record_bandwidth_proxy": 1.96,
                "first_zero_d_over_lambda": 0.51,
            },
            {
                "branch": "raw",
                "model": "exponential",
                "rmse_visibility": 0.074,
                "record_bandwidth_proxy": np.nan,
                "first_zero_d_over_lambda": np.nan,
            },
        ]
    )
    chapman_physical = pd.DataFrame(
        [
            {
                "branch": "raw",
                "model": "uniform_recoil",
                "rmse_visibility": 0.028,
            }
        ]
    )
    xiao_momentum = pd.DataFrame(
        [
            {
                "model": "linear_bandwidth",
                "rmse_momentum": 0.0034,
                "parameters_json": json.dumps([0.043, 0.687]),
            },
            {
                "model": "published_bound",
                "rmse_momentum": 0.069,
                "parameters_json": json.dumps([]),
            },
        ]
    )
    xiao_stress = pd.DataFrame(
        [
            {
                "p_linear_beats_published_bound": 1.0,
                "pairing_null_p_pearson_ge_observed": 0.004,
            }
        ]
    )
    xiao_probability = pd.DataFrame(
        [
            {
                "metric": "side_peak_abs_mean",
                "branch": "phi_pi_far",
                "value": 1.586,
            },
            {
                "metric": "mean_abs_growth",
                "branch": "eta_half_mean_abs",
                "value": 0.568,
            },
            {
                "metric": "late_mean_abs",
                "branch": "eta_half_mean_abs",
                "value": 0.681,
            },
            {
                "metric": "central_density",
                "branch": "phi_pi_far",
                "value": 0.314,
            },
            {
                "metric": "peak_density",
                "branch": "phi_pi_far",
                "value": 1.234,
            },
        ]
    )
    hack_summary = pd.DataFrame(
        [
            {
                "panel": "combined",
                "model": "thermal_delta_T4",
                "beta": 0.016,
                "rmse_visibility": 0.077,
                "delta_aicc_panel": 0.0,
            },
            {
                "panel": "combined",
                "model": "exp_power",
                "beta": 0.20,
                "rmse_visibility": 0.092,
                "delta_aicc_panel": 11.4,
            },
        ]
    )
    hack_stress = pd.DataFrame(
        [
            {
                "p_thermal_delta_T4_beats_exp_power": 0.91,
                "p_thermal_delta_T4_best_model": 0.64,
            }
        ]
    )
    hornberger_summary = pd.DataFrame(
        [
            {
                "lane": "methane_visibility",
                "model": "exponential_pressure",
                "decoherence_pressure_pv_1e_minus_6_mbar": 0.807,
                "rmse_visibility_percent": 0.888,
            },
            {
                "lane": "gas_species_pressure",
                "model": "theory_vs_experiment",
                "fig3_rmse_pressure_1e_minus_6_mbar": 0.185,
                "fig3_theory_observed_corr": 0.888,
                "ch4_fig3_pressure_1e_minus_6_mbar": 0.810,
                "fig2_pv_minus_fig3_ch4": -0.003,
            },
        ]
    )
    paths = {}
    for name, frame in [
        ("chapman_kernel", chapman_kernel),
        ("chapman_physical", chapman_physical),
        ("xiao_momentum", xiao_momentum),
        ("xiao_stress", xiao_stress),
        ("xiao_probability", xiao_probability),
        ("hack_summary", hack_summary),
        ("hack_stress", hack_stress),
        ("hornberger_summary", hornberger_summary),
    ]:
        path = tmp_path / f"{name}.csv"
        frame.to_csv(path, index=False)
        paths[name] = path

    output_dir = tmp_path / "synthesis"
    synthesis = make_record_bandwidth_synthesis_outputs(
        paths["chapman_kernel"],
        paths["chapman_physical"],
        paths["xiao_momentum"],
        paths["xiao_stress"],
        paths["xiao_probability"],
        output_dir,
        paths["hack_summary"],
        paths["hack_stress"],
        paths["hornberger_summary"],
    )
    assert not synthesis.empty
    assert "Hackermueller 2004" in set(synthesis["experiment"])
    assert "Hornberger 2003" in set(synthesis["experiment"])
    report = output_dir / "record_bandwidth_synthesis_report.md"
    assert report.exists()
    report_text = report.read_text(encoding="utf-8")
    assert "three-experiment structure survives with Hornberger guardrail" in report_text
    assert "## Hornberger" in report_text

    cli_output_dir = tmp_path / "synthesis_cli"
    main(
        [
            "synthesize-record-bandwidth",
            "--chapman-kernel-summary",
            str(paths["chapman_kernel"]),
            "--chapman-physical-summary",
            str(paths["chapman_physical"]),
            "--xiao-momentum-summary",
            str(paths["xiao_momentum"]),
            "--xiao-stress-summary",
            str(paths["xiao_stress"]),
            "--xiao-probability-summary",
            str(paths["xiao_probability"]),
            "--hackermueller-thermal-summary",
            str(paths["hack_summary"]),
            "--hackermueller-thermal-stress-summary",
            str(paths["hack_stress"]),
            "--hornberger-collisional-summary",
            str(paths["hornberger_summary"]),
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "record_bandwidth_synthesis_report.md").exists()


def test_breakthrough_candidate_scorecard_outputs_and_cli(tmp_path):
    xiao_distribution = pd.DataFrame(
        [
            {
                "model": "linear_fig4_refit",
                "rmse_momentum": 0.0034,
            },
            {
                "model": "distribution_no_refit",
                "rmse_momentum": 0.0133,
            },
            {
                "model": "published_bound",
                "rmse_momentum": 0.0693,
            },
        ]
    )
    xiao_stress = pd.DataFrame(
        [
            {
                "p_no_refit_beats_published_bound": 1.0,
                "p_no_refit_rmse_lt_025": 0.96,
                "pairing_null_p_rmse_le_observed": 0.003,
                "branch_label_swap_p_rmse_le_observed": 0.0,
                "baseline_sensitivity_pass_fraction": 0.75,
            }
        ]
    )
    chapman_kernel = pd.DataFrame(
        [
            {
                "branch": "raw",
                "model": "sinc_fourier",
                "rmse_visibility": 0.026,
                "first_zero_d_over_lambda": 0.51,
            },
            {
                "branch": "raw",
                "model": "exponential",
                "rmse_visibility": 0.074,
                "first_zero_d_over_lambda": np.nan,
            },
        ]
    )
    chapman_mixture = pd.DataFrame(
        [
            {
                "branch": "raw",
                "model": "complex_mixture_with_smear",
                "rmse_visibility": 0.065,
                "rmse_phase_rad": 1.31,
            }
        ]
    )
    hack_stress = pd.DataFrame(
        [
            {
                "p_thermal_delta_T4_beats_exp_power": 0.994,
                "p_thermal_delta_T4_best_model": 0.701,
            }
        ]
    )
    synthesis = pd.DataFrame(
        [
            {
                "experiment": "Xiao 2019",
                "status": "survives uncertainty and pairing null",
            },
            {
                "experiment": "Hackermueller 2004",
                "status": "thermal record-load proxy supports durable environmental record lane",
            },
        ]
    )
    no_refit_scout = pd.DataFrame(
        [
            {
                "verdict": "no second no-refit distribution target yet",
                "candidate_count": 6,
                "eligible_second_distribution_targets": 0,
                "recommended_next_candidate": "EIBENBERGER_2014_RECOIL_ABSORPTION",
            }
        ]
    )
    eibenberger = pd.DataFrame(
        [
            {
                "model": "visibility_fit_sigma_abs",
                "sigma_abs_m2": 1.935e-21,
                "rmse_visibility_ratio": 0.0247,
                "status": "control_fit",
            },
            {
                "model": "paper_sigma_abs",
                "sigma_abs_m2": 1.97e-21,
                "rmse_visibility_ratio": 0.0251,
                "status": "parameter_fixed",
            },
        ]
    )
    paths = {}
    for name, frame in [
        ("xiao_distribution", xiao_distribution),
        ("xiao_stress", xiao_stress),
        ("chapman_kernel", chapman_kernel),
        ("chapman_mixture", chapman_mixture),
        ("hack_stress", hack_stress),
        ("synthesis", synthesis),
        ("no_refit_scout", no_refit_scout),
        ("eibenberger", eibenberger),
    ]:
        path = tmp_path / f"{name}.csv"
        frame.to_csv(path, index=False)
        paths[name] = path
    (tmp_path / "chapman_complex_mixture_report.md").write_text(
        "Verdict: model still fails\n",
        encoding="utf-8",
    )

    output_dir = tmp_path / "breakthrough"
    scorecard, next_steps = make_breakthrough_candidate_outputs(
        output_dir,
        paths["xiao_distribution"],
        paths["xiao_stress"],
        paths["chapman_kernel"],
        paths["chapman_mixture"],
        paths["hack_stress"],
        paths["synthesis"],
        paths["no_refit_scout"],
        paths["eibenberger"],
    )
    assert not scorecard.empty
    assert not next_steps.empty
    assert "G11" in set(scorecard["gate_id"])
    assert not bool(scorecard[scorecard["gate_id"] == "G11"]["passed"].iloc[0])
    report = output_dir / "breakthrough_candidate_report.md"
    assert report.exists()
    report_text = report.read_text(encoding="utf-8")
    assert "lead candidate found, breakthrough not yet" in report_text
    assert "Eibenberger recoil-control status: control_fit" in report_text

    cli_output_dir = tmp_path / "breakthrough_cli"
    main(
        [
            "evaluate-breakthrough-candidate",
            "--xiao-distribution-summary",
            str(paths["xiao_distribution"]),
            "--xiao-distribution-stress-summary",
            str(paths["xiao_stress"]),
            "--chapman-kernel-summary",
            str(paths["chapman_kernel"]),
            "--chapman-complex-mixture-summary",
            str(paths["chapman_mixture"]),
            "--hackermueller-stress-summary",
            str(paths["hack_stress"]),
            "--synthesis-csv",
            str(paths["synthesis"]),
            "--no-refit-target-scout-summary",
            str(paths["no_refit_scout"]),
            "--eibenberger-recoil-summary",
            str(paths["eibenberger"]),
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "breakthrough_candidate_scorecard.csv").exists()
    assert (cli_output_dir / "next_breakthrough_steps.csv").exists()


def test_current_goal_completion_audit_outputs_and_cli(tmp_path):
    scorecard = pd.DataFrame(
        [
            {"gate_id": "G10", "passed": False},
            {"gate_id": "G12", "passed": False},
        ]
    )
    g11_summary = pd.DataFrame(
        [{"eligible_second_no_refit_targets": 0}]
    )
    public_summary = pd.DataFrame(
        [{"supports_g11_without_author_contact": 0}]
    )
    author_summary = pd.DataFrame(
        [{"g11_ready_rows": 0}]
    )
    paths = {}
    for name, frame in [
        ("scorecard", scorecard),
        ("g11", g11_summary),
        ("public", public_summary),
        ("author", author_summary),
    ]:
        path = tmp_path / f"{name}.csv"
        frame.to_csv(path, index=False)
        paths[name] = path
    output_dir = tmp_path / "goal_audit"
    checklist, summary = make_current_goal_completion_audit_outputs(
        output_dir,
        paths["scorecard"],
        paths["g11"],
        paths["public"],
        paths["author"],
    )
    assert not checklist.empty
    assert not bool(summary["objective_achieved"].iloc[0])
    assert "second_independent_distribution_to_visibility_validation" in set(
        checklist["requirement"]
    )
    assert (output_dir / "current_goal_completion_audit.md").exists()

    cli_output_dir = tmp_path / "goal_audit_cli"
    # The CLI uses default repo paths; this checks parser dispatch.
    main(
        [
            "audit-current-goal-status",
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "current_goal_completion_summary.csv").exists()


def test_no_refit_target_scout_outputs_and_cli(tmp_path):
    output_dir = tmp_path / "no_refit_scout"
    register, summary = make_no_refit_target_scout_outputs(output_dir)
    assert not register.empty
    assert not summary.empty
    assert "XIAO_2019_INTERNAL_LEAD" in set(register["candidate_id"])
    assert summary["verdict"].iloc[0] == "second no-refit distribution target found"
    assert int(summary["eligible_second_distribution_targets"].iloc[0]) >= 1
    assert (
        summary["recommended_next_candidate"].iloc[0]
        == "KOKOROWSKI_2001_MULTIPHOTON_SCATTERING"
    )
    assert (
        output_dir / "second_no_refit_target_scout_report.md"
    ).exists()
    assert (
        output_dir / "no_refit_target_candidate_register.csv"
    ).exists()

    cli_output_dir = tmp_path / "no_refit_scout_cli"
    main(
        [
            "scout-no-refit-targets",
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (
        cli_output_dir / "second_no_refit_target_scout_report.md"
    ).exists()


def test_breakthrough_author_data_requests_outputs_and_cli(tmp_path):
    output_dir = tmp_path / "author_requests"
    register = make_breakthrough_author_data_requests(output_dir)
    assert not register.empty
    assert "xiao_2019_author_data" in set(register["target_id"])
    assert (output_dir / "author_data_request_register.csv").exists()
    assert (output_dir / "author_data_request_tracker.csv").exists()
    assert (output_dir / "author_contact_candidate_register.csv").exists()
    assert (output_dir / "author_data_request_packet.md").exists()
    assert (output_dir / "hochrainer_2017_independent_widths_request.md").exists()
    tracker = pd.read_csv(output_dir / "author_data_request_tracker.csv")
    assert tracker["issue_url"].str.contains("github.com").all()
    assert set(tracker["status"]) == {"draft_ready_not_sent"}
    contacts = pd.read_csv(output_dir / "author_contact_candidate_register.csv")
    assert contacts["contact_source_url"].str.startswith("https://").all()
    assert set(contacts["contact_status"]) == {
        "candidate_route_verify_before_send"
    }

    cli_output_dir = tmp_path / "author_requests_cli"
    main(
        [
            "prepare-author-data-requests",
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "author_data_request_packet.md").exists()
    assert (cli_output_dir / "author_data_request_tracker.csv").exists()
    assert (cli_output_dir / "author_contact_candidate_register.csv").exists()


def test_author_outreach_queue_outputs_and_cli(tmp_path):
    request_dir = tmp_path / "author_requests"
    intake_dir = tmp_path / "author_intake"
    validation_dir = tmp_path / "author_validation"
    output_dir = tmp_path / "author_outreach"
    make_breakthrough_author_data_requests(request_dir)
    make_author_data_intake_outputs(intake_dir)
    validation_dir.mkdir()
    pd.DataFrame([{"g11_ready_rows": 0}]).to_csv(
        validation_dir / "author_data_manifest_validation_summary.csv",
        index=False,
    )

    queue, summary = make_author_outreach_queue(
        request_dir,
        intake_dir,
        validation_dir,
        output_dir,
    )
    assert not queue.empty
    assert int(summary["possible_g11_closer_rows"].iloc[0]) >= 1
    assert set(queue["send_decision"]) == {"hold_until_contact_verified"}
    assert (output_dir / "author_outreach_queue.csv").exists()
    assert (output_dir / "author_outreach_summary.csv").exists()
    assert (output_dir / "author_outreach_queue.md").exists()

    cli_output_dir = tmp_path / "author_outreach_cli"
    main(
        [
            "prepare-author-outreach-queue",
            "--request-dir",
            str(request_dir),
            "--intake-dir",
            str(intake_dir),
            "--validation-dir",
            str(validation_dir),
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "author_outreach_queue.md").exists()


def test_author_data_intake_outputs_and_cli(tmp_path):
    output_dir = tmp_path / "author_intake"
    schema, manifest = make_author_data_intake_outputs(output_dir)
    assert not schema.empty
    assert not manifest.empty
    assert "xiao_2019_author_data" in set(schema["target_id"])
    assert bool(schema[schema["target_id"] == "xiao_2019_author_data"]["can_close_g11"].iloc[0]) is False
    assert int(schema["can_close_g11"].sum()) >= 1
    assert (output_dir / "author_data_intake_schema.csv").exists()
    assert (output_dir / "author_data_received_manifest_template.csv").exists()
    assert (output_dir / "author_data_intake_plan.md").exists()
    assert (output_dir / "mir_pwv_visibility_pairing_template.csv").exists()

    cli_output_dir = tmp_path / "author_intake_cli"
    main(
        [
            "prepare-author-data-intake",
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "author_data_intake_plan.md").exists()


def test_validate_author_data_manifest_outputs_and_cli(tmp_path):
    intake_dir = tmp_path / "author_intake"
    schema, manifest = make_author_data_intake_outputs(intake_dir)
    data_path = tmp_path / "mir_received.csv"
    pd.DataFrame(
        [
            {
                "which_way_strength_or_setting": "setting_a",
                "q_or_x": 0.0,
                "value": 0.2,
                "value_se": 0.01,
                "visibility_or_contrast": 0.7,
                "setting_note": "synthetic test row",
            }
        ]
    ).to_csv(data_path, index=False)
    manifest.loc[
        manifest["target_id"] == "mir_2007_visibility_context",
        ["received", "data_path", "supports_g11"],
    ] = [True, str(data_path), True]
    manifest_path = tmp_path / "manifest.csv"
    manifest.to_csv(manifest_path, index=False)

    output_dir = tmp_path / "validation"
    validation, summary = validate_author_data_manifest(
        manifest_path,
        intake_dir / "author_data_intake_schema.csv",
        output_dir,
    )
    assert not validation.empty
    assert int(summary["g11_ready_rows"].iloc[0]) == 1
    assert "g11_candidate_ready_for_analysis" in set(validation["status"])
    assert (output_dir / "author_data_manifest_validation_report.md").exists()

    cli_output_dir = tmp_path / "validation_cli"
    main(
        [
            "validate-author-data-manifest",
            "--manifest",
            str(manifest_path),
            "--schema",
            str(intake_dir / "author_data_intake_schema.csv"),
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "author_data_manifest_validation.csv").exists()


def test_breakthrough_gap_audit_outputs_and_cli(tmp_path):
    output_dir = tmp_path / "gap_audit"
    audit, blockers, summary = make_breakthrough_gap_audit_outputs(output_dir)
    assert not audit.empty
    assert not blockers.empty
    assert not summary.empty
    assert "XIAO_2019_INTERNAL_LEAD" in set(audit["candidate_id"])
    assert "second independent no-refit candidate found" == summary["verdict"].iloc[0]
    assert int(summary["eligible_second_no_refit_targets"].iloc[0]) >= 1
    assert "KOKOROWSKI_2001_MULTIPHOTON_SCATTERING" in set(audit["candidate_id"])
    assert "paired_visibility_curve_missing" in set(audit["blocker_class"])
    assert (output_dir / "g11_gap_audit.csv").exists()
    assert (output_dir / "g11_blocker_summary.csv").exists()
    assert (output_dir / "g11_gap_audit_report.md").exists()

    cli_output_dir = tmp_path / "gap_audit_cli"
    main(
        [
            "audit-breakthrough-gaps",
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "g11_gap_audit_report.md").exists()


def test_kokorowski_multiphoton_scout_outputs_and_cli(tmp_path):
    source_dir = tmp_path / "kokorowski_source"
    source_dir.mkdir()
    (source_dir / "decoh.tex").write_text("test source", encoding="utf-8")
    for name in ["figure2.eps", "figure3.eps", "figure4.eps"]:
        (source_dir / name).write_text("%!PS-Adobe test", encoding="utf-8")

    metadata = kokorowski_multiphoton_metadata(source_dir)
    scout_df = kokorowski_multiphoton_scout_dataframe(metadata)
    assert not scout_df.empty
    assert scout_df["visibility_curve_available"].all()
    assert int(scout_df["record_variable_independent_of_visibility_fit"].sum()) >= 2

    output_dir = tmp_path / "kokorowski"
    data_dir = tmp_path / "data"
    scout, summary, _metadata = make_kokorowski_multiphoton_scout_outputs(
        source_dir,
        output_dir,
        data_dir,
    )
    assert not scout.empty
    assert bool(summary["source_package_available"].iloc[0])
    assert not bool(summary["clears_g11_now"].iloc[0])
    assert (output_dir / "kokorowski_multiphoton_scout_report.md").exists()
    assert (data_dir / "KOKOROWSKI_2001_MULTIPHOTON_SCOUT.csv").exists()

    cli_output_dir = tmp_path / "kokorowski_cli"
    cli_data_dir = tmp_path / "kokorowski_data_cli"
    main(
        [
            "scout-kokorowski-multiphoton",
            "--source-dir",
            str(source_dir),
            "--output-dir",
            str(cli_output_dir),
            "--data-dir",
            str(cli_data_dir),
        ]
    )
    assert (cli_output_dir / "kokorowski_multiphoton_scout_summary.csv").exists()


def test_kokorowski_digitization_and_analysis_outputs_and_cli(tmp_path):
    source_dir = Path("outputs/tmp/kokorowski_source/extracted")
    if not (source_dir / "figure4.eps").exists():
        pytest.skip("Kokorowski source package not available")

    d0, v0 = kokorowski_fig4_pixel_to_data(80.50, 18.00)
    d1, v1 = kokorowski_fig4_pixel_to_data(415.00, 265.00)
    assert np.isclose(d0, 0.0)
    assert np.isclose(v0, 1.0)
    assert np.isclose(d1, 0.30)
    assert np.isclose(v1, 0.0)
    assert np.all(
        (kokorowski_visibility_from_kappa(np.array([0.0, 0.1]), 1.8) >= 0.0)
        & (kokorowski_visibility_from_kappa(np.array([0.0, 0.1]), 1.8) <= 1.0)
    )

    data_dir = tmp_path / "data"
    digitize_dir = tmp_path / "digitize"
    df, metadata = make_kokorowski_multiphoton_digitization_outputs(
        source_dir,
        digitize_dir,
        data_dir,
    )
    assert not df.empty
    assert {"open_circle", "filled_circle"} == set(df["marker"])
    assert metadata["extraction_method"] == "eps_vector_point_extraction_v1"

    analysis_dir = tmp_path / "analysis"
    summary, predictions = make_kokorowski_multiphoton_analysis_outputs(
        data_dir / "KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv",
        analysis_dir,
    )
    assert not summary.empty
    assert not predictions.empty
    calc = summary[summary["model"] == "calculated_independent_kappa"]
    assert float(calc["rmse_visibility"].max()) < 0.05
    assert (
        "independent multiphoton no-refit candidate passes"
        in summary["status"].iloc[0]
    )

    cli_data_dir = tmp_path / "cli_data"
    cli_digitize_dir = tmp_path / "cli_digitize"
    main(
        [
            "digitize-kokorowski-multiphoton",
            "--source-dir",
            str(source_dir),
            "--output-dir",
            str(cli_digitize_dir),
            "--data-dir",
            str(cli_data_dir),
        ]
    )
    cli_analysis_dir = tmp_path / "cli_analysis"
    main(
        [
            "analyze-kokorowski-multiphoton",
            "--input",
            str(cli_data_dir / "KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv"),
            "--output-dir",
            str(cli_analysis_dir),
        ]
    )
    assert (cli_analysis_dir / "kokorowski_multiphoton_report.md").exists()


def test_kokorowski_stress_outputs_and_cli(tmp_path):
    input_csv = Path("data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv")
    assert input_csv.exists()

    output_dir = tmp_path / "kokorowski_stress"
    summary, bootstrap, null_summary, calibration = make_kokorowski_multiphoton_stress_outputs(
        input_csv,
        output_dir,
        n_bootstrap=40,
        seed=7,
    )
    assert not summary.empty
    assert not bootstrap.empty
    assert not null_summary.empty
    assert not calibration.empty
    assert float(summary["bootstrap_p_rmse_lt_005"].iloc[0]) >= 0.9
    assert "standard quantum decoherence" in (
        output_dir / "kokorowski_multiphoton_stress_report.md"
    ).read_text(encoding="utf-8")
    component_summary = pd.read_csv(
        output_dir / "kokorowski_multiphoton_component_summary.csv"
    )
    assert "independent_kappa_only" in set(component_summary["component"])

    cli_output_dir = tmp_path / "kokorowski_stress_cli"
    main(
        [
            "stress-test-kokorowski-multiphoton",
            "--input",
            str(input_csv),
            "--output-dir",
            str(cli_output_dir),
            "--n-bootstrap",
            "40",
            "--seed",
            "7",
        ]
    )
    assert (cli_output_dir / "kokorowski_multiphoton_stress_summary.csv").exists()


def test_public_data_availability_outputs_and_cli(tmp_path):
    output_dir = tmp_path / "public_data"
    availability, summary = make_public_data_availability_outputs(output_dir)
    assert not availability.empty
    assert not summary.empty
    assert "XIAO_2019_INTERNAL_LEAD" in set(availability["candidate_id"])
    assert int(summary["supports_g11_without_author_contact"].iloc[0]) == 1
    assert summary["verdict"].iloc[0] == "public data closes G11"
    assert (output_dir / "public_data_availability.csv").exists()
    assert (output_dir / "public_data_availability_report.md").exists()

    cli_output_dir = tmp_path / "public_data_cli"
    main(
        [
            "audit-public-data-availability",
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "public_data_availability_report.md").exists()


def test_eibenberger_recoil_reduction_is_bounded():
    metadata = eibenberger_default_metadata()
    distances = np.linspace(0.0, 0.10, 25)
    reduction = eibenberger_recoil_reduction(
        distances,
        metadata["constants"]["paper_sigma_abs_m2"],
        metadata["constants"],
    )
    assert np.isfinite(reduction).all()
    assert (reduction >= 0.0).all()
    assert (reduction <= 1.0 + 1e-12).all()


def test_eibenberger_recoil_scout_outputs_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "eibenberger"
    cli_output_dir = tmp_path / "eibenberger_cli"
    df = eibenberger_digitized_dataframe(eibenberger_default_metadata())
    assert not df.empty
    assert {"distance_from_G1_m", "visibility_ratio"}.issubset(df.columns)

    digitized, metadata, summary, predictions = make_eibenberger_recoil_scout_outputs(
        None,
        output_dir,
        data_dir,
    )
    assert metadata["study_id"] == "EIBENBERGER_2014_RECOIL_ABSORPTION"
    assert not digitized.empty
    assert not summary.empty
    assert not predictions.empty
    assert {"paper_sigma_abs", "visibility_fit_sigma_abs"}.issubset(
        set(summary["model"])
    )
    assert (output_dir / "eibenberger_recoil_scout_report.md").exists()
    assert (
        data_dir / "EIBENBERGER_2014_RECOIL_ABSORPTION_SCOUT.csv"
    ).exists()

    main(
        [
            "scout-eibenberger-recoil-absorption",
            "--output-dir",
            str(cli_output_dir),
            "--data-dir",
            str(data_dir),
        ]
    )
    assert (cli_output_dir / "eibenberger_recoil_scout_report.md").exists()


def test_mir_weak_value_scout_outputs_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "mir"
    cli_output_dir = tmp_path / "mir_cli"
    metadata = mir_weak_value_metadata(None)
    scout_df = mir_weak_value_scout_dataframe(metadata)
    assert not scout_df.empty
    assert scout_df["momentum_distribution_available"].any()
    assert not scout_df["visibility_sweep_available"].any()

    scout, summary, metadata = make_mir_weak_value_scout_outputs(
        None,
        output_dir,
        data_dir,
    )
    assert metadata["study_id"] == "MIR_2007_WEAK_VALUE_MOMENTUM_TRANSFER"
    assert not scout.empty
    assert not summary.empty
    assert not bool(summary["clears_no_refit_gate"].iloc[0])
    assert (
        summary["verdict"].iloc[0]
        == "measured momentum-transfer distribution found, visibility sweep missing"
    )
    assert (output_dir / "mir_weak_value_scout_report.md").exists()
    assert (data_dir / "MIR_2007_WEAK_VALUE_SCOUT.csv").exists()

    main(
        [
            "scout-mir-weak-value",
            "--output-dir",
            str(cli_output_dir),
            "--data-dir",
            str(data_dir),
        ]
    )
    assert (cli_output_dir / "mir_weak_value_scout_report.md").exists()


def test_hochrainer_momentum_correlation_scout_outputs_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "hochrainer"
    cli_output_dir = tmp_path / "hochrainer_cli"
    metadata = hochrainer_momentum_correlation_metadata(None)
    scout_df = hochrainer_momentum_correlation_scout_dataframe(metadata)
    assert not scout_df.empty
    assert scout_df["visibility_curve_available"].any()
    assert scout_df["record_distribution_available"].any()
    assert scout_df["record_variable_inferred_from_visibility"].any()

    scout, summary, metadata = make_hochrainer_momentum_correlation_scout_outputs(
        None,
        output_dir,
        data_dir,
    )
    assert metadata["study_id"] == "HOCHRAINER_2017_INDUCED_COHERENCE_MOMENTUM_CORRELATION"
    assert not scout.empty
    assert not summary.empty
    assert not bool(summary["clears_no_refit_gate"].iloc[0])
    assert summary["verdict"].iloc[0] == "visibility-derived momentum-correlation near miss"
    assert (output_dir / "hochrainer_momentum_correlation_scout_report.md").exists()
    assert (data_dir / "HOCHRAINER_2017_MOMENTUM_CORRELATION_SCOUT.csv").exists()

    main(
        [
            "scout-hochrainer-momentum-correlation",
            "--output-dir",
            str(cli_output_dir),
            "--data-dir",
            str(data_dir),
        ]
    )
    assert (cli_output_dir / "hochrainer_momentum_correlation_scout_report.md").exists()


def test_hornberger_collisional_scout_outputs_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "hornberger"
    cli_output_dir = tmp_path / "hornberger_cli"
    metadata = hornberger_default_metadata()
    df = hornberger_digitized_dataframe(metadata)
    assert not df.empty
    assert {"methane_visibility", "decoherence_pressure_by_gas"}.issubset(
        set(df["panel"])
    )
    summary, predictions, fig2, fig3 = fit_hornberger_collisional_scout(df)
    assert not summary.empty
    assert not predictions.empty
    methane = summary[summary["lane"] == "methane_visibility"].iloc[0]
    species = summary[summary["lane"] == "gas_species_pressure"].iloc[0]
    assert float(methane["decoherence_pressure_pv_1e_minus_6_mbar"]) > 0.0
    assert float(species["fig3_theory_observed_corr"]) > 0.5

    digitized, metadata, summary, predictions = make_hornberger_collisional_scout_outputs(
        None,
        output_dir,
        data_dir,
    )
    assert metadata["study_id"] == "HORNBERGER_2003_COLLISIONAL"
    assert not digitized.empty
    assert not summary.empty
    assert not predictions.empty
    assert (output_dir / "hornberger_collisional_scout_report.md").exists()
    assert (data_dir / "HORNBERGER_2003_COLLISIONAL_SCOUT.csv").exists()

    main(
        [
            "scout-hornberger-collisional",
            "--output-dir",
            str(cli_output_dir),
            "--data-dir",
            str(data_dir),
        ]
    )
    assert (cli_output_dir / "hornberger_collisional_scout_report.md").exists()


def test_cormann_theory_visibility_is_bounded():
    alpha = np.linspace(-89.0, 89.0, 80)
    visibility = cormann_theory_visibility(alpha, 0.297, 0.836)
    assert np.isfinite(visibility).all()
    assert (visibility >= 0.0).all()
    assert (visibility <= 1.0).all()
    assert visibility[np.argmin(np.abs(alpha))] < 0.05


def test_cormann_visibility_phase_scout_outputs_and_cli(tmp_path):
    source_dir = Path("outputs/tmp/third_hunt_sources/cormann")
    if not (source_dir / "VisibilityPhaseMeasurement.eps").exists():
        pytest.skip("Cormann arXiv source package is not available locally")
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "cormann_scout"
    cli_output_dir = tmp_path / "cormann_scout_cli"

    scout, summary, predictions, metadata = make_cormann_visibility_phase_scout_outputs(
        source_dir,
        output_dir,
        data_dir,
    )
    assert not scout.empty
    assert not summary.empty
    assert not predictions.empty
    assert metadata["study_id"] == "CORMANN_2016_VISIBILITY_PHASE"
    assert {"visibility", "phase_sign_pi_units"}.issubset(set(scout["observable"]))
    assert (data_dir / "CORMANN_2016_VISIBILITY_PHASE_SCOUT.csv").exists()
    assert (data_dir / "CORMANN_2016_VISIBILITY_PHASE_SCOUT.json").exists()
    assert (output_dir / "cormann_visibility_phase_scout_report.md").exists()
    red = summary[
        (summary["setup"] == "setup_1") & (summary["observable"] == "visibility")
    ].iloc[0]
    assert red["rmse"] < 0.08

    main(
        [
            "scout-cormann-visibility-phase",
            "--source-dir",
            str(source_dir),
            "--output-dir",
            str(cli_output_dir),
            "--data-dir",
            str(data_dir),
        ]
    )
    assert (cli_output_dir / "cormann_visibility_phase_scout_report.md").exists()


def test_hackermueller_digitized_dataframe_schema_and_monotone_load():
    df = hackermueller_digitized_dataframe(hackermueller_default_metadata())
    required = {
        "panel",
        "laser_power_W",
        "mean_temperature_K",
        "thermal_load_delta_T4",
        "normalized_visibility",
        "visibility_se",
    }
    assert required.issubset(df.columns)
    assert not df.empty
    assert ((df["normalized_visibility"] >= 0.0) & (df["normalized_visibility"] <= 1.0)).all()
    for _panel, group in df.groupby("panel"):
        ordered = group.sort_values("laser_power_W")
        assert np.all(np.diff(ordered["thermal_load_delta_T4"]) >= -1e-12)


def test_hackermueller_thermal_fit_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "hack_digitize"
    analysis_dir = tmp_path / "hack_analysis"
    cli_digitize_dir = tmp_path / "hack_digitize_cli"
    cli_analysis_dir = tmp_path / "hack_analysis_cli"

    digitized, metadata = make_hackermueller_thermal_digitization_outputs(
        None,
        output_dir,
        data_dir,
        fetch_source=False,
    )
    assert metadata["study_id"] == "HACKERMUELLER_2004_THERMAL"
    assert (data_dir / "HACKERMUELLER_2004_THERMAL_DIGITIZED.csv").exists()
    assert (data_dir / "HACKERMUELLER_2004_THERMAL_DIGITIZATION.json").exists()
    assert (output_dir / "hackermueller_digitization_report.md").exists()

    summary, predictions, clean = fit_hackermueller_thermal_models(digitized)
    assert not summary.empty
    assert not predictions.empty
    assert not clean.empty
    assert {"exp_power", "thermal_delta_T4"}.issubset(set(summary["model"]))
    assert np.isfinite(summary["rmse_visibility"]).all()

    make_hackermueller_thermal_analysis_outputs(
        data_dir / "HACKERMUELLER_2004_THERMAL_DIGITIZED.csv",
        analysis_dir,
    )
    assert (analysis_dir / "thermal_decoherence_summary.csv").exists()
    assert (analysis_dir / "thermal_decoherence_predictions.csv").exists()
    assert (analysis_dir / "hackermueller_thermal_report.md").exists()

    main(
        [
            "digitize-hackermueller-thermal",
            "--output-dir",
            str(cli_digitize_dir),
            "--data-dir",
            str(data_dir),
            "--no-fetch-source",
        ]
    )
    main(
        [
            "analyze-thermal-decoherence",
            "--input",
            str(data_dir / "HACKERMUELLER_2004_THERMAL_DIGITIZED.csv"),
            "--output-dir",
            str(cli_analysis_dir),
        ]
    )
    assert (cli_digitize_dir / "hackermueller_digitization_report.md").exists()
    assert (cli_analysis_dir / "hackermueller_thermal_report.md").exists()


def test_hackermueller_stress_outputs_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "hack_digitize"
    stress_dir = tmp_path / "hack_stress"
    cli_stress_dir = tmp_path / "hack_stress_cli"
    digitized, _metadata = make_hackermueller_thermal_digitization_outputs(
        None,
        output_dir,
        data_dir,
        fetch_source=False,
    )
    jittered = jitter_hackermueller_thermal(digitized, np.random.default_rng(7))
    assert len(jittered) == len(digitized)
    assert ((jittered["normalized_visibility"] >= 0.0) & (jittered["normalized_visibility"] <= 1.0)).all()

    summary, bootstrap = make_hackermueller_thermal_stress_outputs(
        data_dir / "HACKERMUELLER_2004_THERMAL_DIGITIZED.csv",
        data_dir / "HACKERMUELLER_2004_THERMAL_DIGITIZATION.json",
        stress_dir,
        n_bootstrap=20,
        seed=20260430,
    )
    assert not summary.empty
    assert not bootstrap.empty
    assert "p_thermal_delta_T4_beats_exp_power" in summary.columns
    assert (stress_dir / "stress_summary.csv").exists()
    assert (stress_dir / "bootstrap_samples.csv").exists()
    assert (stress_dir / "hackermueller_thermal_stress_report.md").exists()

    main(
        [
            "stress-test-hackermueller-thermal",
            "--input",
            str(data_dir / "HACKERMUELLER_2004_THERMAL_DIGITIZED.csv"),
            "--digitization-json",
            str(data_dir / "HACKERMUELLER_2004_THERMAL_DIGITIZATION.json"),
            "--output-dir",
            str(cli_stress_dir),
            "--n-bootstrap",
            "20",
            "--seed",
            "20260430",
        ]
    )
    assert (cli_stress_dir / "hackermueller_thermal_stress_report.md").exists()


def test_chapman_sinc_first_zero_uses_normalized_sinc_width():
    assert np.isclose(chapman_sinc_first_zero(2.0), 0.5)


def test_chapman_kernel_predictors_are_bounded():
    x = np.linspace(0.0, 2.0, 25)
    for model, shape in [
        ("exponential", 2.0),
        ("sinc_fourier", 1.8),
        ("gaussian_kernel", 2.0),
    ]:
        pred = chapman_kernel_visibility(x, model, amp=1.1, floor=0.08, shape=shape)
        assert np.all(pred >= 0.0)
        assert np.all(pred <= 1.0)


def test_chapman_kernel_analysis_finds_fourier_raw_signal():
    df = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    summary, predictions, _ = fit_chapman_kernel_models(df)
    assert not summary.empty
    assert not predictions.empty
    raw = summary[summary["branch"] == "raw"]
    raw_sinc = raw[raw["model"] == "sinc_fourier"].iloc[0]
    raw_exp = raw[raw["model"] == "exponential"].iloc[0]
    case_i_sinc = summary[
        (summary["branch"] == "case_I_forward")
        & (summary["model"] == "sinc_fourier")
    ].iloc[0]
    assert raw_sinc["rmse_visibility"] < raw_exp["rmse_visibility"]
    assert raw_sinc["first_zero_d_over_lambda"] < case_i_sinc["first_zero_d_over_lambda"]
    assert raw_sinc["record_bandwidth_proxy"] > case_i_sinc["record_bandwidth_proxy"]


def test_chapman_visibility_jitter_preserves_schema_and_bounds():
    df = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    jittered = jitter_chapman_visibility(df, np.random.default_rng(123))
    assert list(jittered.columns) == list(df.columns)
    assert len(jittered) == len(df)
    assert jittered["visibility_obs"].between(0.0, 1.0).all()


def test_chapman_kernel_stress_summary_contains_core_probability():
    df = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    samples = bootstrap_chapman_kernel_stress(df, n_bootstrap=4, seed=123)
    assert not samples.empty
    assert "raw_sinc_beats_exp" in samples.columns
    probability = float(samples["raw_sinc_beats_exp"].mean())
    assert 0.0 <= probability <= 1.0


def test_chapman_kernel_stress_outputs_and_cli_write_files(tmp_path):
    df = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    input_csv = tmp_path / "chapman.csv"
    metadata_json = tmp_path / "chapman.json"
    output_dir = tmp_path / "stress"
    cli_output_dir = tmp_path / "stress_cli"
    df.to_csv(input_csv, index=False)
    metadata_json.write_text(
        json.dumps(chapman_default_digitization_metadata()),
        encoding="utf-8",
    )

    summary, bootstrap, null_summary, _ = make_chapman_kernel_stress_outputs(
        input_csv,
        metadata_json,
        output_dir,
        n_bootstrap=3,
        seed=456,
    )
    assert "p_raw_sinc_beats_exponential" in summary.columns
    assert not bootstrap.empty
    assert not null_summary.empty
    assert (output_dir / "chapman_kernel_stress_report.md").exists()
    assert (output_dir / "stress_summary.csv").exists()
    assert (output_dir / "bootstrap_samples.csv").exists()
    assert (output_dir / "null_test_summary.csv").exists()

    main(
        [
            "stress-test-chapman-kernel",
            "--input",
            str(input_csv),
            "--digitization-json",
            str(metadata_json),
            "--output-dir",
            str(cli_output_dir),
            "--n-bootstrap",
            "2",
            "--seed",
            "789",
        ]
    )
    assert (cli_output_dir / "chapman_kernel_stress_report.md").exists()


def test_chapman_recoil_distribution_normalizes():
    q = chapman_recoil_grid(401)
    density = chapman_uniform_recoil_density(q)
    assert np.isclose(np.trapezoid(density, q), 1.0, atol=1e-6)


def test_chapman_characteristic_visibility_is_bounded_and_uniform_zero():
    q = chapman_recoil_grid(801)
    density = chapman_uniform_recoil_density(q)
    x = np.array([0.0, 0.5, 1.0])
    visibility = chapman_characteristic_visibility(x, q, density)
    assert np.all(visibility >= 0.0)
    assert np.all(visibility <= 1.0)
    assert visibility[0] > 0.99
    assert visibility[1] < 0.01


def test_chapman_complex_observables_are_bounded_and_finite():
    q = chapman_recoil_grid(801)
    density = chapman_uniform_recoil_density(q)
    x = np.linspace(0.0, 0.45, 10)
    visibility, phase = chapman_complex_observables(x, q, density)
    assert np.all(visibility >= 0.0)
    assert np.all(visibility <= 1.0)
    assert np.isfinite(phase).all()
    assert visibility[0] > 0.99


def test_chapman_complex_phase_slope_tracks_narrow_q_center():
    q = chapman_recoil_grid(801)
    center = 1.65
    density = np.exp(-0.5 * ((q - center) / 0.035) ** 2)
    x = np.linspace(0.0, 0.25, 12)
    _visibility, phase = chapman_complex_observables(x, q, density)
    slope, _intercept = np.polyfit(x, phase, deg=1)
    assert np.isclose(slope / (2.0 * math.pi), center, atol=0.05)


def test_chapman_mixture_weights_are_normalized_and_nonnegative():
    weights = chapman_mixture_weights(-1.0, 2.0, 3.0)
    assert np.all(weights >= 0.0)
    assert np.isclose(weights.sum(), 1.0)


def test_chapman_two_photon_and_smearing_are_bounded():
    one = np.array([1.0 + 0.0j, 0.5 + 0.2j, -0.1 + 0.1j])
    two = chapman_two_photon_amplitude(one)
    assert np.isfinite(two).all()
    assert np.all(np.abs(two) <= np.abs(one) + 1e-12)
    x = np.linspace(0.0, 2.0, 10)
    smear = chapman_velocity_smearing(x, 0.7)
    assert np.all(smear <= 1.0)
    assert np.all(smear > 0.0)


def test_chapman_mixture_amplitude_returns_finite_observables():
    q = chapman_recoil_grid(401)
    density = chapman_uniform_recoil_density(q)
    x = np.linspace(0.0, 2.0, 20)
    amplitude = chapman_mixture_amplitude(
        x,
        q,
        density,
        chapman_mixture_weights(0.05, 0.77, 0.18),
        velocity_sigma=0.4,
    )
    assert np.isfinite(amplitude).all()
    assert np.all(np.abs(amplitude) <= 1.0 + 1e-9)


def test_chapman_phase_digitization_schema():
    phase = chapman_phase_digitized_dataframe(
        chapman_default_complex_digitization_metadata()
    )
    required = {
        "study_id",
        "source_figure",
        "x_value",
        "phase_rad",
        "phase_display_rad",
        "phase_se",
        "visibility_type",
        "conditioned_on",
    }
    assert required.issubset(phase.columns)
    assert set(phase["conditioned_on"]) >= {"", "case_I_forward", "case_III_backward"}


def test_chapman_phase_grade_schema_and_quality_subset():
    phase = chapman_phase_grade_dataframe(chapman_default_phase_grade_metadata())
    required = {
        "phase_rad",
        "phase_display_rad",
        "phase_unwrapped_rad",
        "phase_quality",
        "unwrap_group",
        "wrap_ambiguous",
        "low_contrast_ambiguous",
    }
    assert required.issubset(phase.columns)
    raw = phase[phase["visibility_type"] == "raw"]
    assert {"high", "medium", "low"}.issubset(set(raw["phase_quality"]))
    high = chapman_phase_quality_subset(phase, "high_confidence_raw")
    high_raw = high[high["visibility_type"] == "raw"]
    assert len(high_raw) < len(raw)
    assert not high_raw["wrap_ambiguous"].any()


def test_chapman_physical_kernel_analysis_outputs_ordered_centers(tmp_path):
    df = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    input_csv = tmp_path / "chapman.csv"
    metadata_json = tmp_path / "chapman.json"
    cli_output_dir = tmp_path / "physical_cli"
    df.to_csv(input_csv, index=False)
    metadata_json.write_text(
        json.dumps(chapman_default_digitization_metadata()),
        encoding="utf-8",
    )
    main(
        [
            "analyze-chapman-physical-kernel",
            "--input",
            str(input_csv),
            "--digitization-json",
            str(metadata_json),
            "--output-dir",
            str(cli_output_dir),
        ]
    )
    assert (cli_output_dir / "chapman_physical_kernel_report.md").exists()
    assert (cli_output_dir / "physical_kernel_summary.csv").exists()
    assert (cli_output_dir / "physical_kernel_predictions.csv").exists()
    summary = pd.read_csv(cli_output_dir / "physical_kernel_summary.csv")
    predictions = pd.read_csv(cli_output_dir / "physical_kernel_predictions.csv")
    assert not summary.empty
    assert not predictions.empty
    case_i = summary[
        (summary["branch"] == "case_I_forward")
        & (summary["model"] == "accepted_beta_recoil")
    ].iloc[0]
    case_iii = summary[
        (summary["branch"] == "case_III_backward")
        & (summary["model"] == "accepted_beta_recoil")
    ].iloc[0]
    assert np.isfinite(case_i["acceptance_center"])
    assert np.isfinite(case_iii["acceptance_center"])
    assert case_i["acceptance_center"] < case_iii["acceptance_center"]


def test_chapman_complex_kernel_analysis_writes_outputs(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "complex"
    data_dir.mkdir()
    visibility = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    visibility.to_csv(data_dir / "CHAPMAN_1995_SCATTER_DIGITIZED.csv", index=False)

    summary, predictions, distributions, phase, _metadata = make_chapman_complex_kernel_outputs(
        None,
        data_dir,
        output_dir,
        render_pdf=False,
    )

    assert not summary.empty
    assert not predictions.empty
    assert not distributions.empty
    assert not phase.empty
    assert (data_dir / "CHAPMAN_1995_PHASE_DIGITIZED.csv").exists()
    assert (data_dir / "CHAPMAN_1995_COMPLEX_DIGITIZATION.json").exists()
    assert (output_dir / "complex_kernel_summary.csv").exists()
    assert (output_dir / "complex_kernel_predictions.csv").exists()
    assert (output_dir / "chapman_complex_kernel_report.md").exists()
    case_i = summary[
        (summary["branch"] == "case_I_forward")
        & (summary["model"] == "accepted_beta_recoil_complex")
    ].iloc[0]
    case_iii = summary[
        (summary["branch"] == "case_III_backward")
        & (summary["model"] == "accepted_beta_recoil_complex")
    ].iloc[0]
    assert np.isfinite(case_i["acceptance_center"])
    assert np.isfinite(case_iii["acceptance_center"])
    assert case_i["acceptance_center"] < case_iii["acceptance_center"]


def test_chapman_complex_kernel_fit_returns_phase_predictions():
    visibility = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    phase = chapman_phase_digitized_dataframe(
        chapman_default_complex_digitization_metadata()
    )
    summary, predictions, _distributions = fit_chapman_complex_kernel_models(
        visibility,
        phase,
    )
    assert not summary.empty
    phase_predictions = predictions[predictions["observable"] == "phase"]
    assert not phase_predictions.empty
    assert np.isfinite(phase_predictions["pred_phase_rad"]).all()


def test_chapman_complex_mixture_outputs_and_verdict(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "mixture"
    data_dir.mkdir()
    visibility = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    visibility.to_csv(data_dir / "CHAPMAN_1995_SCATTER_DIGITIZED.csv", index=False)

    summary, predictions, distributions, phase, _metadata = (
        make_chapman_complex_mixture_outputs(
            None,
            data_dir,
            output_dir,
            render_pdf=False,
            grid_mode="test",
        )
    )

    assert not summary.empty
    assert not predictions.empty
    assert not distributions.empty
    assert not phase.empty
    assert (output_dir / "complex_mixture_summary.csv").exists()
    assert (output_dir / "complex_mixture_predictions.csv").exists()
    assert (output_dir / "complex_mixture_distributions.csv").exists()
    report_path = output_dir / "chapman_complex_mixture_report.md"
    assert report_path.exists()
    report = report_path.read_text(encoding="utf-8")
    assert any(
        verdict in report
        for verdict in ["raw phase repaired", "model still fails", "digitization-limited"]
    )
    raw_mixture = summary[
        (summary["branch"] == "raw")
        & summary["model"].isin(
            ["complex_mixture_no_smear", "complex_mixture_with_smear"]
        )
    ]
    assert not raw_mixture.empty


def test_chapman_phase_grade_outputs_and_cli(tmp_path):
    data_dir = tmp_path / "data"
    output_dir = tmp_path / "phase_grade"
    cli_output_dir = tmp_path / "phase_grade_cli"
    data_dir.mkdir()
    visibility = chapman_digitized_dataframe(chapman_default_digitization_metadata())
    visibility.to_csv(data_dir / "CHAPMAN_1995_SCATTER_DIGITIZED.csv", index=False)

    complex_summary, mixture_summary, *_ = make_chapman_phase_grade_outputs(
        None,
        data_dir,
        output_dir,
        render_pdf=False,
        grid_mode="test",
    )
    assert not complex_summary.empty
    assert not mixture_summary.empty
    assert (data_dir / "CHAPMAN_1995_PHASE_GRADED.csv").exists()
    assert (data_dir / "CHAPMAN_1995_PHASE_GRADE_DIGITIZATION.json").exists()
    assert (output_dir / "phase_grade_complex_summary.csv").exists()
    assert (output_dir / "phase_grade_mixture_summary.csv").exists()
    assert (output_dir / "chapman_phase_grade_report.md").exists()
    assert set(complex_summary["analysis_scope"]) == {
        "all_phase_points",
        "high_confidence_raw",
    }

    main(
        [
            "digitize-chapman-phase-grade",
            "--data-dir",
            str(data_dir),
            "--output-dir",
            str(cli_output_dir),
            "--grid-mode",
            "test",
            "--skip-render",
        ]
    )
    report = cli_output_dir / "chapman_phase_grade_report.md"
    assert report.exists()
    text = report.read_text(encoding="utf-8")
    assert any(
        verdict in text
        for verdict in [
            "phase-grade repairs full raw phase",
            "phase failure is wrap-limited",
            "phase still fails",
        ]
    )


def test_decompose_eraser_recovers_known_synthetic_values():
    df = pd.DataFrame(
        [
            {
                "study_id": "SYN",
                "x_name": "x",
                "x_value": 1.0,
                "visibility_type": "raw",
                "visibility_obs": 0.30,
            },
            {
                "study_id": "SYN",
                "x_name": "x",
                "x_value": 1.0,
                "visibility_type": "conditioned",
                "visibility_obs": 0.75,
                "conditioned_on": "optimal",
            },
        ]
    )
    result = decompose_eraser_dataset(df)
    row = result.iloc[0]
    assert np.isclose(row["eta_irreversible_hat"], 0.75)
    assert np.isclose(row["marker_visibility_hat"], 0.40)
    assert np.isclose(row["recoverable_loss"], 0.45)
    assert np.isclose(row["unrecoverable_loss"], 0.25)


def test_decompose_eraser_returns_empty_schema_without_pairs():
    df = pd.DataFrame(
        [
            {
                "study_id": "SYN",
                "x_name": "x",
                "x_value": 1.0,
                "visibility_type": "raw",
                "visibility_obs": 0.30,
            }
        ]
    )
    result = decompose_eraser_dataset(df)
    assert result.empty
    assert "eta_irreversible_hat" in result.columns


def test_fit_rejects_blank_constraint_columns():
    df = pd.DataFrame(
        [
            {
                "Lambda": np.nan,
                "Gamma": np.nan,
                "Theta": np.nan,
                "marker_visibility": 1.0,
                "t_meas": 1.0,
                "visibility_obs": 0.8,
            }
        ]
    )
    try:
        fit_visibility_models(df)
    except ValueError as exc:
        assert "Constraint columns contain missing values" in str(exc)
    else:
        raise AssertionError("fit_visibility_models accepted blank constraint columns")


def test_design_diagnostics_detect_confounding_ordering():
    balanced = build_synthetic_visibility_dataset()
    confounded = build_confounded_visibility_dataset()
    balanced_summary, *_ = design_diagnostics(balanced, name="balanced")
    confounded_summary, *_ = design_diagnostics(confounded, name="confounded")
    assert balanced_summary["max_abs_factor_correlation"].iloc[0] < 0.05
    assert confounded_summary["max_abs_factor_correlation"].iloc[0] > 0.7
    assert (
        confounded_summary["full_second_order_condition_number"].iloc[0]
        > balanced_summary["full_second_order_condition_number"].iloc[0]
    )
