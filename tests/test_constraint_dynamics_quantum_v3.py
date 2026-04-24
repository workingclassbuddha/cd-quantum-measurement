import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from constraint_dynamics_quantum_v3 import (  # noqa: E402
    ApparatusSettings,
    build_confounded_visibility_dataset,
    build_joint_density,
    build_synthetic_visibility_dataset,
    decompose_eraser_dataset,
    design_diagnostics,
    energetic_constraint,
    fit_visibility_models,
    partial_trace_marker,
    path_visibility_from_rho,
    quantum_eraser_observables,
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
