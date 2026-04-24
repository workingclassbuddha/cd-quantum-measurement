#!/usr/bin/env python3
"""Constraint Dynamics quantum-measurement test scaffold, V3.

This script is an effective research scaffold. It does not derive collapse
from first principles and it does not replace standard decoherence theory.
It asks a narrower question: whether the apparatus dependence of
measurement-induced loss of visibility is better parameterized by separable
Constraint Dynamics factors.
"""

from __future__ import annotations

import argparse
import html
import json
import math
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd


EPS = 1e-12


@dataclass(frozen=True)
class ApparatusSettings:
    """Physical knobs mapped into the effective Lambda/Gamma/Theta factors."""

    path_separation: float = 1.0
    detector_spatial_resolution: float = 0.72
    coherence_time: float = 1.0
    detector_response_time: float = 0.62
    record_entropy_bits: float = 1.25
    record_survival_probability: float = 0.72
    environment_coupling: float = 0.82
    record_accessibility: float = 0.0
    marker_angle: float = 1.20
    relative_phase: float = 0.0
    measurement_duration: float = 1.0
    record_onset_time: float = 0.24
    record_growth_time: float = 0.24
    eraser_time: float = 0.18
    eraser_phase: float = 0.0
    kappa0: float = 1.35
    background_kappa: float = 0.0


def _as_array(x):
    return np.asarray(x, dtype=float)


def clip01(x):
    return np.clip(_as_array(x), 0.0, 1.0)


def spatial_constraint(path_separation, detector_spatial_resolution):
    """Map path separation and spatial detector resolution to Lambda.

    Lambda is close to 0 when the detector point-spread function is too broad
    to distinguish the paths, and close to 1 when path separation is large
    compared with detector resolution.
    """

    d = np.maximum(_as_array(path_separation), 0.0)
    sigma = np.maximum(_as_array(detector_spatial_resolution), EPS)
    return clip01(1.0 - np.exp(-0.5 * (d / sigma) ** 2))


def temporal_constraint(coherence_time, detector_response_time):
    """Map detector response time to Gamma.

    Gamma is high when the detector responds faster than the coherence time
    of the path superposition and low when it temporally blurs path events.
    """

    tau_coh = np.maximum(_as_array(coherence_time), EPS)
    tau_det = np.maximum(_as_array(detector_response_time), EPS)
    return clip01(1.0 - np.exp(-((tau_coh / tau_det) ** 2)))


def energetic_constraint(
    record_entropy_bits,
    record_survival_probability=1.0,
    environment_coupling=1.0,
    record_accessibility=0.0,
):
    """Map irreversible record load to Theta.

    Theta is modeled as a saturating function of entropy exported into a
    durable detector/environment record that is inaccessible to later
    conditioning. Reversible or selectively accessible marker storage can make
    paths distinguishable without creating large effective Theta.
    """

    bits = np.maximum(_as_array(record_entropy_bits), 0.0)
    survival = clip01(record_survival_probability)
    coupling = clip01(environment_coupling)
    inaccessible = 1.0 - clip01(record_accessibility)
    entropy_nats = bits * math.log(2.0)
    return clip01(1.0 - np.exp(-(entropy_nats * survival * coupling * inaccessible)))


def marker_visibility_from_angle(marker_angle):
    """Reversible marker overlap contribution to raw path visibility."""

    return np.abs(np.cos(_as_array(marker_angle)))


def constraints_from_apparatus(settings: ApparatusSettings) -> dict[str, float]:
    lam = float(
        spatial_constraint(
            settings.path_separation,
            settings.detector_spatial_resolution,
        )
    )
    gam = float(
        temporal_constraint(
            settings.coherence_time,
            settings.detector_response_time,
        )
    )
    the = float(
        energetic_constraint(
            settings.record_entropy_bits,
            settings.record_survival_probability,
            settings.environment_coupling,
            settings.record_accessibility,
        )
    )
    marker = float(marker_visibility_from_angle(settings.marker_angle))
    return {
        "Lambda": lam,
        "Gamma": gam,
        "Theta": the,
        "marker_visibility": marker,
    }


def effective_kappa_cd(kappa0, Lambda, Gamma, Theta, background_kappa=0.0):
    """Product-law dephasing rate used as the V3 CD hypothesis."""

    return np.maximum(
        _as_array(background_kappa)
        + _as_array(kappa0) * _as_array(Lambda) * _as_array(Gamma) * _as_array(Theta),
        0.0,
    )


def lock_fraction(t, onset, growth_time):
    """Smooth fraction of the irreversible record that has locked in by time t."""

    elapsed = np.maximum(_as_array(t) - onset, 0.0)
    growth = max(float(growth_time), EPS)
    return clip01(1.0 - np.exp(-elapsed / growth))


def lock_integral(stop_time, onset, growth_time):
    """Integral of lock_fraction from 0 to stop_time."""

    elapsed = max(float(stop_time) - float(onset), 0.0)
    growth = max(float(growth_time), EPS)
    return elapsed - growth * (1.0 - math.exp(-elapsed / growth))


def irreversible_exposure(settings: ApparatusSettings, eraser_time: float | None = None):
    """Effective irreversible exposure time.

    If eraser_time is supplied, the eraser is assumed to prevent later
    amplification of the marker into an irreversible path record. Earlier
    irreversible exposure is not undone.
    """

    stop = settings.measurement_duration if eraser_time is None else eraser_time
    stop = max(0.0, min(float(stop), settings.measurement_duration))
    return lock_integral(
        stop,
        onset=settings.record_onset_time,
        growth_time=settings.record_growth_time,
    )


def dephasing_eta(
    settings: ApparatusSettings,
    eraser_time: float | None = None,
    overrides: dict[str, float] | None = None,
):
    constraints = constraints_from_apparatus(settings)
    if overrides:
        constraints.update(overrides)
    kappa = float(
        effective_kappa_cd(
            settings.kappa0,
            constraints["Lambda"],
            constraints["Gamma"],
            constraints["Theta"],
            settings.background_kappa,
        )
    )
    exposure = irreversible_exposure(settings, eraser_time=eraser_time)
    return float(math.exp(-2.0 * kappa * exposure)), kappa, exposure


def ket(v):
    return np.asarray(v, dtype=complex).reshape(-1, 1)


def dm_from_state(state):
    state = ket(state)
    return state @ state.conj().T


def marker_states(alpha):
    m_left = np.array([1.0, 0.0], dtype=complex)
    m_right = np.array([math.cos(alpha), math.sin(alpha)], dtype=complex)
    return m_left, m_right


def joint_state_path_marker(alpha, rel_phase=0.0):
    m_left, m_right = marker_states(alpha)
    path_left = np.array([1.0, 0.0], dtype=complex)
    path_right = np.array([0.0, 1.0], dtype=complex)
    psi = (
        np.kron(path_left, m_left)
        + np.exp(1j * rel_phase) * np.kron(path_right, m_right)
    ) / math.sqrt(2.0)
    return psi / np.linalg.norm(psi)


def apply_path_dephasing(rho, eta):
    rho = np.asarray(rho, dtype=complex).copy()
    path_labels = np.array([0, 0, 1, 1])
    mask = path_labels[:, None] != path_labels[None, :]
    rho[mask] *= eta
    return rho


def partial_trace_marker(rho_joint):
    rho_joint = np.asarray(rho_joint, dtype=complex).reshape(2, 2, 2, 2)
    return np.trace(rho_joint, axis1=1, axis2=3)


def condition_on_marker_basis(rho_joint, basis_vec):
    basis_vec = ket(basis_vec)
    projector_marker = basis_vec @ basis_vec.conj().T
    projector_joint = np.kron(np.eye(2, dtype=complex), projector_marker)
    rho_post = projector_joint @ rho_joint @ projector_joint.conj().T
    prob = float(np.real_if_close(np.trace(rho_post)))
    if prob <= EPS:
        return 0.0, np.zeros((2, 2), dtype=complex)
    return prob, partial_trace_marker(rho_post / prob)


def eraser_basis(phase=0.0):
    plus = np.array([1.0, np.exp(1j * phase)], dtype=complex) / math.sqrt(2.0)
    minus = np.array([1.0, -np.exp(1j * phase)], dtype=complex) / math.sqrt(2.0)
    return plus, minus


def optimal_eraser_basis(alpha: float):
    """Marker basis whose nonzero branches balance the two path amplitudes.

    For the two marker states used here, projecting onto the sum/difference
    marker basis erases reversible marker distinguishability. Nonzero branches
    recover path visibility up to the irreversible dephasing bound eta.
    """

    m_left, m_right = marker_states(alpha)
    raw_basis = [m_left + m_right, m_left - m_right]
    basis = []
    for vec in raw_basis:
        norm = float(np.linalg.norm(vec))
        if norm <= EPS:
            basis.append(np.array([0.0, 1.0], dtype=complex))
        else:
            basis.append(vec / norm)
    return basis[0], basis[1]


def path_visibility_from_rho(rho_path):
    rho_path = np.asarray(rho_path, dtype=complex)
    return float(np.clip(2.0 * abs(rho_path[0, 1]), 0.0, 1.0))


def screen_intensity_from_rho(x, rho_path, fringe_freq=14.0, width=0.72):
    x = np.asarray(x, dtype=float)
    rho = np.asarray(rho_path, dtype=complex)
    envelope = np.exp(-0.5 * (x / width) ** 2)
    phase = np.exp(1j * fringe_freq * x)
    base = float(np.real(rho[0, 0] + rho[1, 1]))
    cross = 2.0 * np.real(rho[0, 1] * phase)
    intensity = np.clip(envelope * (base + cross), 0.0, None)
    integrate = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    norm = float(integrate(intensity, x))
    return intensity if norm <= EPS else intensity / norm


def build_joint_density(
    settings: ApparatusSettings,
    eraser_time: float | None = None,
    theta_override: float | None = None,
):
    psi0 = joint_state_path_marker(settings.marker_angle, settings.relative_phase)
    overrides = {} if theta_override is None else {"Theta": theta_override}
    eta, kappa, exposure = dephasing_eta(settings, eraser_time, overrides)
    rho = apply_path_dephasing(dm_from_state(psi0), eta)
    return rho, {"eta": eta, "kappa_eff": kappa, "exposure": exposure}


def quantum_eraser_observables(
    settings: ApparatusSettings,
    eraser_time: float | None = None,
    theta_override: float | None = None,
):
    rho_joint, meta = build_joint_density(settings, eraser_time, theta_override)
    constraints = constraints_from_apparatus(settings)
    if theta_override is not None:
        constraints["Theta"] = float(theta_override)
    rho_path = partial_trace_marker(rho_joint)
    plus, minus = eraser_basis(settings.eraser_phase)
    p_plus, rho_plus = condition_on_marker_basis(rho_joint, plus)
    p_minus, rho_minus = condition_on_marker_basis(rho_joint, minus)
    optimal_plus, optimal_minus = optimal_eraser_basis(settings.marker_angle)
    p_opt_plus, rho_opt_plus = condition_on_marker_basis(rho_joint, optimal_plus)
    p_opt_minus, rho_opt_minus = condition_on_marker_basis(rho_joint, optimal_minus)
    v_opt_plus = path_visibility_from_rho(rho_opt_plus)
    v_opt_minus = path_visibility_from_rho(rho_opt_minus)
    optimal_visibilities = [
        visibility
        for probability, visibility in [
            (p_opt_plus, v_opt_plus),
            (p_opt_minus, v_opt_minus),
        ]
        if probability > EPS
    ]
    return {
        **meta,
        **constraints,
        "visibility_unconditioned": path_visibility_from_rho(rho_path),
        "visibility_eraser_plus": path_visibility_from_rho(rho_plus),
        "visibility_eraser_minus": path_visibility_from_rho(rho_minus),
        "visibility_eraser_optimal_plus": v_opt_plus,
        "visibility_eraser_optimal_minus": v_opt_minus,
        "visibility_eraser_optimal_best": max(optimal_visibilities, default=0.0),
        "prob_eraser_plus": p_plus,
        "prob_eraser_minus": p_minus,
        "prob_eraser_optimal_plus": p_opt_plus,
        "prob_eraser_optimal_minus": p_opt_minus,
    }


def kappa_at_time(settings: ApparatusSettings, t):
    c = constraints_from_apparatus(settings)
    base = float(
        effective_kappa_cd(
            settings.kappa0,
            c["Lambda"],
            c["Gamma"],
            c["Theta"],
            settings.background_kappa,
        )
    )
    return base * lock_fraction(t, settings.record_onset_time, settings.record_growth_time)


def simulate_phase_flip_trajectories(
    settings: ApparatusSettings,
    n_trajectories=2500,
    dt=0.004,
    sample_every=8,
    seed=23,
):
    """Stochastic phase-flip unraveling of the dephasing master equation.

    Each trajectory remains pure. Random Z flips on the path degree of freedom
    occur with a time-dependent Poisson rate kappa(t). The ensemble average
    reproduces off-diagonal decay exp[-2 integral kappa(t) dt].
    """

    rng = np.random.default_rng(seed)
    psi0 = joint_state_path_marker(settings.marker_angle, settings.relative_phase)
    states = np.repeat(psi0.reshape(1, 4), n_trajectories, axis=0)
    z_path = np.array([1.0, 1.0, -1.0, -1.0], dtype=complex)
    n_steps = int(math.ceil(settings.measurement_duration / dt))
    rows = []
    integral = 0.0

    def append_row(t_now, integral_now):
        rho_avg = states.T @ states.conj() / n_trajectories
        rho_path = partial_trace_marker(rho_avg)
        c = constraints_from_apparatus(settings)
        rows.append(
            {
                "time": t_now,
                "visibility_trajectory_mean": path_visibility_from_rho(rho_path),
                "visibility_exact": c["marker_visibility"]
                * math.exp(-2.0 * integral_now),
                "integrated_kappa": integral_now,
            }
        )

    append_row(0.0, integral)
    for step in range(1, n_steps + 1):
        t_mid = min((step - 0.5) * dt, settings.measurement_duration)
        rate = float(kappa_at_time(settings, t_mid))
        p_jump = min(rate * dt, 0.25)
        jumps = rng.random(n_trajectories) < p_jump
        states[jumps] *= z_path
        integral += rate * dt
        if step % sample_every == 0 or step == n_steps:
            append_row(min(step * dt, settings.measurement_duration), integral)

    return pd.DataFrame(rows)


def target_from_visibility(visibility, marker_visibility, t_meas):
    v = np.asarray(visibility, dtype=float)
    m = np.maximum(np.asarray(marker_visibility, dtype=float), EPS)
    t = np.maximum(np.asarray(t_meas, dtype=float), EPS)
    ratio = np.clip(v / m, 1e-9, 0.999999)
    return -np.log(ratio) / (2.0 * t)


def ensure_constraint_columns(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    required = {"Lambda", "Gamma", "Theta"}
    has_direct_constraints = required.issubset(data.columns)
    if has_direct_constraints:
        for column in sorted(required):
            data[column] = pd.to_numeric(data[column], errors="coerce")
        if not data[list(required)].isna().any().any():
            return data
    apparatus_cols = {
        "path_separation",
        "detector_spatial_resolution",
        "coherence_time",
        "detector_response_time",
        "record_entropy_bits",
        "record_survival_probability",
        "environment_coupling",
    }
    if not apparatus_cols.issubset(data.columns):
        if has_direct_constraints:
            raise ValueError(
                "Constraint columns contain missing values; provide complete "
                "Lambda/Gamma/Theta or apparatus columns."
            )
        missing = ", ".join(sorted(required - set(data.columns)))
        raise ValueError(
            f"Missing {missing}; provide Lambda/Gamma/Theta or apparatus columns."
        )
    for column in sorted(apparatus_cols):
        data[column] = pd.to_numeric(data[column], errors="coerce")
    if data[list(apparatus_cols)].isna().any().any():
        raise ValueError(
            "Constraint columns contain missing values and apparatus columns are "
            "incomplete; provide complete Lambda/Gamma/Theta or apparatus settings."
        )
    if "record_accessibility" in data.columns:
        data["record_accessibility"] = pd.to_numeric(
            data["record_accessibility"], errors="coerce"
        ).fillna(0.0)
    else:
        data["record_accessibility"] = 0.0
    data["Lambda"] = spatial_constraint(
        data["path_separation"], data["detector_spatial_resolution"]
    )
    data["Gamma"] = temporal_constraint(
        data["coherence_time"], data["detector_response_time"]
    )
    data["Theta"] = energetic_constraint(
        data["record_entropy_bits"],
        data["record_survival_probability"],
        data["environment_coupling"],
        data["record_accessibility"],
    )
    return data


def model_designs(data: pd.DataFrame) -> dict[str, tuple[np.ndarray, list[str]]]:
    L = data["Lambda"].to_numpy(dtype=float)
    G = data["Gamma"].to_numpy(dtype=float)
    T = data["Theta"].to_numpy(dtype=float)
    ones = np.ones_like(L)
    return {
        "constant": (ones[:, None], ["background"]),
        "product": ((L * G * T)[:, None], ["LGT"]),
        "product_plus_background": (
            np.column_stack([ones, L * G * T]),
            ["background", "LGT"],
        ),
        "additive": (np.column_stack([L, G, T]), ["L", "G", "T"]),
        "additive_plus_background": (
            np.column_stack([ones, L, G, T]),
            ["background", "L", "G", "T"],
        ),
        "pairwise": (
            np.column_stack([L * G, L * T, G * T]),
            ["LG", "LT", "GT"],
        ),
        "pairwise_plus_product": (
            np.column_stack([L * G, L * T, G * T, L * G * T]),
            ["LG", "LT", "GT", "LGT"],
        ),
        "full_second_order": (
            np.column_stack([L, G, T, L * G, L * T, G * T, L * G * T]),
            ["L", "G", "T", "LG", "LT", "GT", "LGT"],
        ),
    }


def weighted_lstsq(X, y, weights=None):
    if weights is None:
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        return beta
    w = np.sqrt(np.asarray(weights, dtype=float))
    beta, *_ = np.linalg.lstsq(X * w[:, None], y * w, rcond=None)
    return beta


def _aicc(n, rss, k):
    sigma2 = max(rss / max(n, 1), 1e-12)
    aic = n * math.log(sigma2) + 2 * k
    if n <= k + 1:
        return aic
    return aic + (2 * k * (k + 1)) / (n - k - 1)


def _kfold_slices(n, k=5, seed=13):
    rng = np.random.default_rng(seed)
    indices = rng.permutation(n)
    return np.array_split(indices, min(k, n))


def fit_visibility_models(
    df: pd.DataFrame,
    visibility_col="visibility_obs",
    marker_col="marker_visibility",
    time_col="t_meas",
    cv_folds=5,
    seed=13,
):
    data = ensure_constraint_columns(df)
    if marker_col not in data.columns:
        if "marker_angle" in data.columns:
            data[marker_col] = marker_visibility_from_angle(data["marker_angle"])
        else:
            data[marker_col] = 1.0
    else:
        data[marker_col] = pd.to_numeric(data[marker_col], errors="coerce").fillna(1.0)
    if time_col not in data.columns:
        data[time_col] = 1.0
    else:
        data[time_col] = pd.to_numeric(data[time_col], errors="coerce").fillna(1.0)

    y = target_from_visibility(
        data[visibility_col].to_numpy(dtype=float),
        data[marker_col].to_numpy(dtype=float),
        data[time_col].to_numpy(dtype=float),
    )
    weights = None
    if "visibility_se" in data.columns:
        se = np.maximum(data["visibility_se"].to_numpy(dtype=float), EPS)
        v = np.maximum(data[visibility_col].to_numpy(dtype=float), EPS)
        sigma_y = se / (2.0 * np.maximum(data[time_col].to_numpy(dtype=float), EPS) * v)
        weights = 1.0 / np.maximum(sigma_y, EPS) ** 2

    n = len(data)
    designs = model_designs(data)
    rows = []
    pred = pd.DataFrame({"row_id": np.arange(n)})
    if "condition_id" in data.columns:
        pred.insert(0, "condition_id", data["condition_id"].to_numpy())
    pred["target_kappa"] = y
    y_mean = float(np.average(y, weights=weights)) if weights is not None else float(np.mean(y))
    sst = float(np.sum((y - y_mean) ** 2))
    folds = _kfold_slices(n, cv_folds, seed)

    for name, (X, labels) in designs.items():
        beta = weighted_lstsq(X, y, weights)
        yhat = np.clip(X @ beta, 0.0, None)
        residual = y - yhat
        rss = float(np.sum(residual**2))
        k = X.shape[1]
        pred_vis = data[marker_col].to_numpy(dtype=float) * np.exp(
            -2.0 * yhat * data[time_col].to_numpy(dtype=float)
        )
        vis_resid = data[visibility_col].to_numpy(dtype=float) - pred_vis
        cv_target = []
        cv_vis = []
        for test_idx in folds:
            train_mask = np.ones(n, dtype=bool)
            train_mask[test_idx] = False
            train_weights = weights[train_mask] if weights is not None else None
            beta_cv = weighted_lstsq(X[train_mask], y[train_mask], train_weights)
            y_cv = np.clip(X[test_idx] @ beta_cv, 0.0, None)
            v_cv = data[marker_col].to_numpy(dtype=float)[test_idx] * np.exp(
                -2.0 * y_cv * data[time_col].to_numpy(dtype=float)[test_idx]
            )
            cv_target.append(np.mean((y[test_idx] - y_cv) ** 2))
            cv_vis.append(
                np.mean((data[visibility_col].to_numpy(dtype=float)[test_idx] - v_cv) ** 2)
            )
        rows.append(
            {
                "model": name,
                "n_params": k,
                "rmse_target": math.sqrt(rss / n),
                "mae_visibility": float(np.mean(np.abs(vis_resid))),
                "rmse_visibility": math.sqrt(float(np.mean(vis_resid**2))),
                "cv_rmse_target": math.sqrt(float(np.mean(cv_target))),
                "cv_rmse_visibility": math.sqrt(float(np.mean(cv_vis))),
                "r2_target": 1.0 - rss / sst if sst > EPS else np.nan,
                "aicc": _aicc(n, rss, k),
                "bic": n * math.log(max(rss / n, 1e-12)) + k * math.log(max(n, 2)),
                "parameter_labels_json": json.dumps(labels),
                "parameters_json": json.dumps([float(v) for v in beta]),
            }
        )
        pred[f"pred_kappa_{name}"] = yhat
        pred[f"pred_visibility_{name}"] = np.clip(pred_vis, 0.0, 1.0)

    fit = pd.DataFrame(rows).sort_values("aicc", ascending=True).reset_index(drop=True)
    fit["delta_aicc"] = fit["aicc"] - fit["aicc"].min()
    rel = np.exp(-0.5 * fit["delta_aicc"].to_numpy(dtype=float))
    fit["akaike_weight"] = rel / np.maximum(rel.sum(), EPS)
    return fit, pred, data


def build_synthetic_visibility_dataset(
    n_space=6,
    n_time=6,
    n_entropy=6,
    seed=7,
    noise_sd=0.002,
):
    rng = np.random.default_rng(seed)
    settings = ApparatusSettings()
    sigma_values = np.linspace(0.35, 2.2, n_space)
    response_values = np.linspace(0.25, 2.3, n_time)
    entropy_values = np.linspace(0.0, 3.2, n_entropy)
    rows = []
    condition_id = 0
    for sigma in sigma_values:
        for response in response_values:
            for entropy_bits in entropy_values:
                s = replace(
                    settings,
                    detector_spatial_resolution=float(sigma),
                    detector_response_time=float(response),
                    record_entropy_bits=float(entropy_bits),
                )
                c = constraints_from_apparatus(s)
                eta, kappa, exposure = dephasing_eta(s, eraser_time=None)
                visibility_true = c["marker_visibility"] * eta
                visibility_obs = float(
                    np.clip(visibility_true + rng.normal(0.0, noise_sd), 1e-4, 0.999)
                )
                rows.append(
                    {
                        "condition_id": condition_id,
                        "path_separation": s.path_separation,
                        "detector_spatial_resolution": s.detector_spatial_resolution,
                        "coherence_time": s.coherence_time,
                        "detector_response_time": s.detector_response_time,
                        "record_entropy_bits": s.record_entropy_bits,
                        "record_survival_probability": s.record_survival_probability,
                        "environment_coupling": s.environment_coupling,
                        "record_accessibility": s.record_accessibility,
                        "Lambda": c["Lambda"],
                        "Gamma": c["Gamma"],
                        "Theta": c["Theta"],
                        "marker_angle": s.marker_angle,
                        "marker_visibility": c["marker_visibility"],
                        "t_meas": exposure,
                        "kappa_eff_true": kappa,
                        "visibility_true": visibility_true,
                        "visibility_obs": visibility_obs,
                        "visibility_se": noise_sd,
                    }
                )
                condition_id += 1
    return pd.DataFrame(rows)


def build_confounded_visibility_dataset(n=216, seed=11, noise_sd=0.002):
    """Synthetic dataset where Lambda/Gamma/Theta are intentionally correlated."""

    rng = np.random.default_rng(seed)
    settings = ApparatusSettings()
    q_values = np.linspace(0.0, 1.0, n)
    rows = []
    for condition_id, q in enumerate(q_values):
        q_jitter = float(np.clip(q + rng.normal(0.0, 0.025), 0.0, 1.0))
        s = replace(
            settings,
            detector_spatial_resolution=float(2.2 - 1.85 * q_jitter),
            detector_response_time=float(2.3 - 2.05 * q_jitter),
            record_entropy_bits=float(3.2 * q_jitter),
        )
        c = constraints_from_apparatus(s)
        eta, kappa, exposure = dephasing_eta(s, eraser_time=None)
        visibility_true = c["marker_visibility"] * eta
        visibility_obs = float(
            np.clip(visibility_true + rng.normal(0.0, noise_sd), 1e-4, 0.999)
        )
        rows.append(
            {
                "condition_id": condition_id,
                "latent_detector_load": q_jitter,
                "path_separation": s.path_separation,
                "detector_spatial_resolution": s.detector_spatial_resolution,
                "coherence_time": s.coherence_time,
                "detector_response_time": s.detector_response_time,
                "record_entropy_bits": s.record_entropy_bits,
                "record_survival_probability": s.record_survival_probability,
                "environment_coupling": s.environment_coupling,
                "record_accessibility": s.record_accessibility,
                "Lambda": c["Lambda"],
                "Gamma": c["Gamma"],
                "Theta": c["Theta"],
                "marker_angle": s.marker_angle,
                "marker_visibility": c["marker_visibility"],
                "t_meas": exposure,
                "kappa_eff_true": kappa,
                "visibility_true": visibility_true,
                "visibility_obs": visibility_obs,
                "visibility_se": noise_sd,
            }
        )
    return pd.DataFrame(rows)


def build_accessibility_benchmark_dataset(
    n_space=9,
    n_access=7,
    seed=29,
    noise_sd=0.0015,
):
    """Synthetic two-axis test for inaccessible-record Theta.

    The generated data vary spatial distinguishability and record
    accessibility independently. The true visibility uses the V3
    accessibility-aware Theta, while `Theta_naive` records what Theta would
    have been if all records were treated as inaccessible.
    """

    rng = np.random.default_rng(seed)
    base = ApparatusSettings(
        marker_angle=0.0,
        detector_spatial_resolution=0.55,
        detector_response_time=0.42,
        record_entropy_bits=2.4,
        record_survival_probability=0.92,
        environment_coupling=0.9,
        kappa0=1.15,
    )
    path_values = np.linspace(0.0, 2.0, n_space)
    accessibility_values = np.linspace(0.0, 1.0, n_access)
    rows = []
    condition_id = 0
    for path in path_values:
        for accessibility in accessibility_values:
            s = replace(
                base,
                path_separation=float(path),
                record_accessibility=float(accessibility),
            )
            c = constraints_from_apparatus(s)
            theta_naive = float(
                energetic_constraint(
                    s.record_entropy_bits,
                    s.record_survival_probability,
                    s.environment_coupling,
                    record_accessibility=0.0,
                )
            )
            eta, kappa, exposure = dephasing_eta(s, eraser_time=None)
            visibility_true = c["marker_visibility"] * eta
            visibility_obs = float(
                np.clip(visibility_true + rng.normal(0.0, noise_sd), 1e-5, 0.99999)
            )
            rows.append(
                {
                    "condition_id": condition_id,
                    "path_separation": s.path_separation,
                    "detector_spatial_resolution": s.detector_spatial_resolution,
                    "coherence_time": s.coherence_time,
                    "detector_response_time": s.detector_response_time,
                    "record_entropy_bits": s.record_entropy_bits,
                    "record_survival_probability": s.record_survival_probability,
                    "environment_coupling": s.environment_coupling,
                    "record_accessibility": s.record_accessibility,
                    "inaccessible_record_fraction": 1.0 - s.record_accessibility,
                    "Lambda": c["Lambda"],
                    "Gamma": c["Gamma"],
                    "Theta": c["Theta"],
                    "Theta_naive": theta_naive,
                    "marker_angle": s.marker_angle,
                    "marker_visibility": c["marker_visibility"],
                    "t_meas": exposure,
                    "kappa_eff_true": kappa,
                    "visibility_true": visibility_true,
                    "visibility_obs": visibility_obs,
                    "visibility_se": noise_sd,
                }
            )
            condition_id += 1
    return pd.DataFrame(rows)


def _theta_naive_from_data(data: pd.DataFrame):
    if "Theta_naive" in data.columns:
        return pd.to_numeric(data["Theta_naive"], errors="coerce").to_numpy(dtype=float)
    needed = {
        "record_entropy_bits",
        "record_survival_probability",
        "environment_coupling",
    }
    if not needed.issubset(data.columns):
        return np.ones(len(data), dtype=float)
    return energetic_constraint(
        data["record_entropy_bits"],
        data["record_survival_probability"],
        data["environment_coupling"],
        record_accessibility=0.0,
    )


def fit_accessibility_hypotheses(df: pd.DataFrame):
    """Compare accessibility-aware and naive record-load hypotheses."""

    data = ensure_constraint_columns(df)
    if "marker_visibility" not in data.columns:
        data["marker_visibility"] = 1.0
    if "t_meas" not in data.columns:
        data["t_meas"] = 1.0
    y = target_from_visibility(
        data["visibility_obs"].to_numpy(dtype=float),
        data["marker_visibility"].to_numpy(dtype=float),
        data["t_meas"].to_numpy(dtype=float),
    )
    L = data["Lambda"].to_numpy(dtype=float)
    G = data["Gamma"].to_numpy(dtype=float)
    T = data["Theta"].to_numpy(dtype=float)
    T_naive = _theta_naive_from_data(data)
    if "record_accessibility" in data.columns:
        access = (
            pd.to_numeric(data["record_accessibility"], errors="coerce")
            .fillna(0.0)
            .to_numpy(dtype=float)
        )
    else:
        access = np.zeros(len(data), dtype=float)
    ones = np.ones_like(L)
    naive_product = L * G * T_naive
    aware_product = L * G * T
    designs = {
        "constant": (ones[:, None], ["background"]),
        "naive_record_product": (naive_product[:, None], ["LGT_naive"]),
        "aware_record_product": (aware_product[:, None], ["LGT_access"]),
        "naive_plus_accessibility": (
            np.column_stack([naive_product, naive_product * access]),
            ["LGT_naive", "LGT_naive_x_accessibility"],
        ),
        "naive_plus_inaccessibility": (
            np.column_stack([naive_product, naive_product * (1.0 - access)]),
            ["LGT_naive", "LGT_naive_x_inaccessible"],
        ),
    }
    rows = []
    pred = pd.DataFrame({"condition_id": data.get("condition_id", np.arange(len(data)))})
    pred["target_kappa"] = y
    for name, (X, labels) in designs.items():
        beta = weighted_lstsq(X, y)
        yhat = np.clip(X @ beta, 0.0, None)
        residual = y - yhat
        rss = float(np.sum(residual**2))
        pred_visibility = data["marker_visibility"].to_numpy(dtype=float) * np.exp(
            -2.0 * yhat * data["t_meas"].to_numpy(dtype=float)
        )
        visibility_residual = data["visibility_obs"].to_numpy(dtype=float) - pred_visibility
        rows.append(
            {
                "model": name,
                "n_params": X.shape[1],
                "rmse_target": math.sqrt(rss / len(data)),
                "rmse_visibility": math.sqrt(float(np.mean(visibility_residual**2))),
                "mae_visibility": float(np.mean(np.abs(visibility_residual))),
                "aicc": _aicc(len(data), rss, X.shape[1]),
                "bic": len(data) * math.log(max(rss / len(data), 1e-12))
                + X.shape[1] * math.log(max(len(data), 2)),
                "parameter_labels_json": json.dumps(labels),
                "parameters_json": json.dumps([float(v) for v in beta]),
            }
        )
        pred[f"pred_kappa_{name}"] = yhat
        pred[f"pred_visibility_{name}"] = np.clip(pred_visibility, 0.0, 1.0)

    summary = pd.DataFrame(rows).sort_values("aicc", ascending=True).reset_index(drop=True)
    summary["delta_aicc"] = summary["aicc"] - summary["aicc"].min()
    rel = np.exp(-0.5 * summary["delta_aicc"].to_numpy(dtype=float))
    summary["akaike_weight"] = rel / np.maximum(rel.sum(), EPS)
    return summary, pred, data


def decompose_eraser_dataset(df: pd.DataFrame):
    """Decompose paired raw/conditioned visibility into reversible and durable loss.

    This is an empirical bookkeeping utility. It treats the best conditioned
    branch at each x-value as a first-pass estimate of the irreversible
    dephasing bound, then assigns the gap between raw and conditioned
    visibility to recoverable marker/path information.
    """

    required = {"study_id", "x_name", "x_value", "visibility_type", "visibility_obs"}
    missing = sorted(required - set(df.columns))
    if missing:
        raise ValueError(
            f"Missing required eraser decomposition columns: {', '.join(missing)}"
        )

    data = df.copy()
    type_aliases = {
        "erased": "conditioned",
        "conditional": "conditioned",
        "postselected": "conditioned",
    }
    data["visibility_type"] = (
        data["visibility_type"].astype(str).str.lower().replace(type_aliases)
    )
    data["visibility_obs"] = pd.to_numeric(data["visibility_obs"], errors="coerce")
    data["x_value"] = pd.to_numeric(data["x_value"], errors="coerce")
    data = data.dropna(subset=["visibility_obs", "x_value"])
    group_cols = ["study_id", "x_name", "x_value"]
    output_columns = [
        "study_id",
        "x_name",
        "x_value",
        "raw_visibility",
        "best_conditioned_visibility",
        "eta_irreversible_hat",
        "marker_visibility_hat",
        "recoverable_loss",
        "unrecoverable_loss",
        "total_loss",
        "recovery_fraction",
        "n_raw",
        "n_conditioned",
        "best_conditioned_on",
        "source_figure",
        "extraction_method",
    ]
    rows = []

    for group_key, group in data.groupby(group_cols, dropna=False):
        raw = group[group["visibility_type"] == "raw"]
        conditioned = group[group["visibility_type"] == "conditioned"]
        if raw.empty or conditioned.empty:
            continue
        raw_visibility = float(raw["visibility_obs"].mean())
        best_idx = conditioned["visibility_obs"].idxmax()
        best = conditioned.loc[best_idx]
        best_conditioned = float(best["visibility_obs"])
        eta_hat = float(np.clip(max(raw_visibility, best_conditioned), 0.0, 1.0))
        marker_hat = float(np.clip(raw_visibility / max(eta_hat, EPS), 0.0, 1.0))
        total_loss = max(0.0, 1.0 - raw_visibility)
        recoverable_loss = max(0.0, eta_hat - raw_visibility)
        unrecoverable_loss = max(0.0, 1.0 - eta_hat)
        recovery_fraction = recoverable_loss / total_loss if total_loss > EPS else 0.0
        rows.append(
            {
                "study_id": group_key[0],
                "x_name": group_key[1],
                "x_value": float(group_key[2]),
                "raw_visibility": raw_visibility,
                "best_conditioned_visibility": best_conditioned,
                "eta_irreversible_hat": eta_hat,
                "marker_visibility_hat": marker_hat,
                "recoverable_loss": recoverable_loss,
                "unrecoverable_loss": unrecoverable_loss,
                "total_loss": total_loss,
                "recovery_fraction": float(np.clip(recovery_fraction, 0.0, 1.0)),
                "n_raw": int(len(raw)),
                "n_conditioned": int(len(conditioned)),
                "best_conditioned_on": best.get("conditioned_on", ""),
                "source_figure": best.get("source_figure", ""),
                "extraction_method": best.get("extraction_method", ""),
            }
        )

    if not rows:
        return pd.DataFrame(columns=output_columns)
    result = pd.DataFrame(rows, columns=output_columns).sort_values(
        ["study_id", "x_name", "x_value"]
    )
    return result.reset_index(drop=True)


def variance_inflation_factors(frame: pd.DataFrame, columns: list[str]):
    """Return VIF values for the requested columns."""

    rows = []
    values = frame[columns].to_numpy(dtype=float)
    for idx, name in enumerate(columns):
        y = values[:, idx]
        X = np.delete(values, idx, axis=1)
        X = np.column_stack([np.ones(len(X)), X])
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        residual = y - X @ beta
        sst = float(np.sum((y - np.mean(y)) ** 2))
        r2 = 1.0 - float(np.sum(residual**2)) / sst if sst > EPS else 0.0
        vif = 1.0 / max(1.0 - r2, EPS)
        rows.append({"factor": name, "r2_from_other_factors": r2, "vif": vif})
    return pd.DataFrame(rows)


def design_diagnostics(df: pd.DataFrame, name="dataset"):
    """Assess whether Lambda/Gamma/Theta are separable in a dataset."""

    data = ensure_constraint_columns(df)
    factors = ["Lambda", "Gamma", "Theta"]
    corr = data[factors].corr().fillna(0.0)
    off_diag = corr.to_numpy(dtype=float)[np.triu_indices(3, k=1)]
    _, full_labels = model_designs(data)["full_second_order"]
    full_X, _ = model_designs(data)["full_second_order"]
    centered = full_X - np.mean(full_X, axis=0)
    scales = np.std(centered, axis=0)
    keep = scales > EPS
    standardized = centered[:, keep] / scales[keep]
    condition = float(np.linalg.cond(standardized)) if standardized.shape[1] else np.nan
    vif = variance_inflation_factors(data, factors)
    ranges = {
        f"{factor}_range": float(data[factor].max() - data[factor].min())
        for factor in factors
    }
    summary = pd.DataFrame(
        [
            {
                "design": name,
                "n": len(data),
                "max_abs_factor_correlation": float(np.max(np.abs(off_diag))),
                "mean_abs_factor_correlation": float(np.mean(np.abs(off_diag))),
                "full_second_order_condition_number": condition,
                "max_vif": float(vif["vif"].max()),
                **ranges,
            }
        ]
    )
    corr_rows = corr.reset_index().rename(columns={"index": "factor"})
    corr_rows.insert(0, "design", name)
    vif.insert(0, "design", name)
    feature_rows = pd.DataFrame(
        {
            "design": name,
            "feature": [label for label, ok in zip(full_labels, keep) if ok],
            "standardized_scale": scales[keep],
        }
    )
    return summary, corr_rows, vif, feature_rows


def _svg_text(x, y, text, size=13, anchor="middle", color="#263238", rotate=None):
    safe = html.escape(str(text))
    transform = "" if rotate is None else f' transform="rotate({rotate} {x:.2f} {y:.2f})"'
    return (
        f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" '
        f'font-family="Arial, Helvetica, sans-serif" text-anchor="{anchor}" '
        f'fill="{color}"{transform}>{safe}</text>'
    )


def _svg_page(width, height, body):
    return "\n".join(
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
            '<rect width="100%" height="100%" fill="#ffffff"/>',
            *body,
            "</svg>",
            "",
        ]
    )


def _range_with_pad(values, pad=0.05):
    vals = np.asarray(values, dtype=float)
    low = float(np.nanmin(vals))
    high = float(np.nanmax(vals))
    if not math.isfinite(low) or not math.isfinite(high):
        low, high = 0.0, 1.0
    if abs(high - low) < EPS:
        high = low + 1.0
    span = high - low
    return low - pad * span, high + pad * span


def _scale(value, src_min, src_max, dst_min, dst_max):
    return dst_min + (np.asarray(value) - src_min) * (dst_max - dst_min) / (
        src_max - src_min + EPS
    )


def write_line_svg(
    path: Path,
    x,
    series,
    title,
    xlabel,
    ylabel,
    xlim=None,
    ylim=None,
    vlines: Iterable[tuple[float, str, str]] | None = None,
):
    width, height = 920, 520
    left, right, top, bottom = 82, 28, 54, 82
    plot_w = width - left - right
    plot_h = height - top - bottom
    x = np.asarray(x, dtype=float)
    all_y = np.concatenate([np.asarray(s["y"], dtype=float) for s in series])
    x_min, x_max = xlim if xlim else _range_with_pad(x, 0.02)
    y_min, y_max = ylim if ylim else _range_with_pad(all_y, 0.08)
    body = [
        _svg_text(width / 2, 28, title, size=20, color="#17212b"),
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#fafafa" stroke="#cfd8dc"/>',
    ]
    for tick in np.linspace(x_min, x_max, 6):
        px = float(_scale(tick, x_min, x_max, left, left + plot_w))
        body.append(f'<line x1="{px:.2f}" y1="{top}" x2="{px:.2f}" y2="{top + plot_h}" stroke="#eceff1"/>')
        body.append(_svg_text(px, top + plot_h + 24, f"{tick:.2g}", size=11))
    for tick in np.linspace(y_min, y_max, 6):
        py = float(_scale(tick, y_min, y_max, top + plot_h, top))
        body.append(f'<line x1="{left}" y1="{py:.2f}" x2="{left + plot_w}" y2="{py:.2f}" stroke="#eceff1"/>')
        body.append(_svg_text(left - 10, py + 4, f"{tick:.2g}", size=11, anchor="end"))
    if vlines:
        for xv, label, color in vlines:
            px = float(_scale(xv, x_min, x_max, left, left + plot_w))
            body.append(f'<line x1="{px:.2f}" y1="{top}" x2="{px:.2f}" y2="{top + plot_h}" stroke="{color}" stroke-width="1.8" stroke-dasharray="6 5"/>')
            body.append(_svg_text(px + 6, top + 16, label, size=11, anchor="start", color=color))
    for s in series:
        y = np.asarray(s["y"], dtype=float)
        px = _scale(x, x_min, x_max, left, left + plot_w)
        py = _scale(y, y_min, y_max, top + plot_h, top)
        points = " ".join(f"{a:.2f},{b:.2f}" for a, b in zip(px, py))
        dash = ' stroke-dasharray="7 5"' if s.get("dash") else ""
        body.append(
            f'<polyline fill="none" stroke="{s["color"]}" stroke-width="2.5"{dash} points="{points}"/>'
        )
    legend_x = left + 12
    legend_y = top + 18
    for idx, s in enumerate(series):
        y0 = legend_y + idx * 22
        dash = ' stroke-dasharray="7 5"' if s.get("dash") else ""
        body.append(f'<line x1="{legend_x}" y1="{y0}" x2="{legend_x + 28}" y2="{y0}" stroke="{s["color"]}" stroke-width="3"{dash}/>')
        body.append(_svg_text(legend_x + 36, y0 + 4, s["label"], size=12, anchor="start"))
    body.append(_svg_text(left + plot_w / 2, height - 28, xlabel, size=14))
    body.append(_svg_text(22, top + plot_h / 2, ylabel, size=14, rotate=-90))
    path.write_text(_svg_page(width, height, body), encoding="utf-8")


def write_scatter_svg(
    path: Path,
    x,
    y,
    title,
    xlabel,
    ylabel,
    color="#2962ff",
    line_x=None,
    line_y=None,
    line_label=None,
    diagonal=False,
):
    width, height = 720, 560
    left, right, top, bottom = 82, 32, 54, 82
    plot_w = width - left - right
    plot_h = height - top - bottom
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    x_min, x_max = _range_with_pad(x, 0.06)
    y_min, y_max = _range_with_pad(y, 0.06)
    if diagonal:
        low = min(x_min, y_min)
        high = max(x_max, y_max)
        x_min = y_min = low
        x_max = y_max = high
    body = [
        _svg_text(width / 2, 28, title, size=20, color="#17212b"),
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#fafafa" stroke="#cfd8dc"/>',
    ]
    for tick in np.linspace(x_min, x_max, 6):
        px = float(_scale(tick, x_min, x_max, left, left + plot_w))
        body.append(f'<line x1="{px:.2f}" y1="{top}" x2="{px:.2f}" y2="{top + plot_h}" stroke="#eceff1"/>')
        body.append(_svg_text(px, top + plot_h + 24, f"{tick:.2g}", size=11))
    for tick in np.linspace(y_min, y_max, 6):
        py = float(_scale(tick, y_min, y_max, top + plot_h, top))
        body.append(f'<line x1="{left}" y1="{py:.2f}" x2="{left + plot_w}" y2="{py:.2f}" stroke="#eceff1"/>')
        body.append(_svg_text(left - 10, py + 4, f"{tick:.2g}", size=11, anchor="end"))
    px = _scale(x, x_min, x_max, left, left + plot_w)
    py = _scale(y, y_min, y_max, top + plot_h, top)
    for a, b in zip(px, py):
        body.append(f'<circle cx="{a:.2f}" cy="{b:.2f}" r="3.4" fill="{color}" fill-opacity="0.62"/>')
    if diagonal:
        body.append(
            f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top}" stroke="#455a64" stroke-width="2"/>'
        )
    if line_x is not None and line_y is not None:
        lx = _scale(line_x, x_min, x_max, left, left + plot_w)
        ly = _scale(line_y, y_min, y_max, top + plot_h, top)
        points = " ".join(f"{a:.2f},{b:.2f}" for a, b in zip(lx, ly))
        body.append(f'<polyline fill="none" stroke="#d84315" stroke-width="2.5" points="{points}"/>')
        if line_label:
            body.append(_svg_text(left + 18, top + 20, line_label, size=12, anchor="start", color="#d84315"))
    body.append(_svg_text(left + plot_w / 2, height - 28, xlabel, size=14))
    body.append(_svg_text(22, top + plot_h / 2, ylabel, size=14, rotate=-90))
    path.write_text(_svg_page(width, height, body), encoding="utf-8")


def write_bar_svg(path: Path, labels, values, title, ylabel):
    width, height = 820, 500
    left, right, top, bottom = 86, 24, 54, 128
    plot_w = width - left - right
    plot_h = height - top - bottom
    labels = list(labels)
    values = np.asarray(values, dtype=float)
    y_min, y_max = 0.0, max(1.0, float(np.max(values)) * 1.12)
    body = [
        _svg_text(width / 2, 28, title, size=20, color="#17212b"),
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#fafafa" stroke="#cfd8dc"/>',
    ]
    for tick in np.linspace(y_min, y_max, 6):
        py = float(_scale(tick, y_min, y_max, top + plot_h, top))
        body.append(f'<line x1="{left}" y1="{py:.2f}" x2="{left + plot_w}" y2="{py:.2f}" stroke="#eceff1"/>')
        body.append(_svg_text(left - 10, py + 4, f"{tick:.2g}", size=11, anchor="end"))
    slot = plot_w / max(len(labels), 1)
    bar_w = slot * 0.64
    palette = ["#2962ff", "#00897b", "#d84315", "#6a1b9a", "#f9a825", "#455a64", "#c2185b", "#2e7d32"]
    for idx, (label, value) in enumerate(zip(labels, values)):
        x0 = left + idx * slot + (slot - bar_w) / 2
        y0 = float(_scale(value, y_min, y_max, top + plot_h, top))
        h = top + plot_h - y0
        body.append(f'<rect x="{x0:.2f}" y="{y0:.2f}" width="{bar_w:.2f}" height="{h:.2f}" fill="{palette[idx % len(palette)]}" fill-opacity="0.82"/>')
        body.append(_svg_text(x0 + bar_w / 2, top + plot_h + 18, label, size=10, rotate=-28))
    body.append(_svg_text(22, top + plot_h / 2, ylabel, size=14, rotate=-90))
    path.write_text(_svg_page(width, height, body), encoding="utf-8")


def write_matrix_heatmap_svg(path: Path, matrix_df: pd.DataFrame, title: str):
    factors = ["Lambda", "Gamma", "Theta"]
    width, height = 520, 470
    left, top = 120, 70
    cell = 86
    body = [_svg_text(width / 2, 30, title, size=20, color="#17212b")]
    for i, row_factor in enumerate(factors):
        body.append(_svg_text(left - 16, top + i * cell + cell / 2 + 5, row_factor, size=13, anchor="end"))
        body.append(_svg_text(left + i * cell + cell / 2, top - 18, row_factor, size=13))
        for j, col_factor in enumerate(factors):
            value = float(matrix_df.loc[matrix_df["factor"] == row_factor, col_factor].iloc[0])
            intensity = int(245 - 120 * abs(value))
            if value >= 0:
                color = f"rgb({intensity},{min(255, intensity + 32)},255)"
            else:
                color = f"rgb(255,{min(255, intensity + 18)},{intensity})"
            x0 = left + j * cell
            y0 = top + i * cell
            body.append(f'<rect x="{x0}" y="{y0}" width="{cell}" height="{cell}" fill="{color}" stroke="#ffffff" stroke-width="2"/>')
            body.append(_svg_text(x0 + cell / 2, y0 + cell / 2 + 5, f"{value:.2f}", size=16, color="#17212b"))
    body.append(_svg_text(width / 2, height - 42, "factor correlation matrix", size=13, color="#455a64"))
    path.write_text(_svg_page(width, height, body), encoding="utf-8")


def make_quantum_eraser_outputs(settings: ApparatusSettings, output_dir: Path):
    x = np.linspace(-1.5, 1.5, 1200)
    rho_joint, _ = build_joint_density(settings, eraser_time=None)
    rho_path = partial_trace_marker(rho_joint)
    plus, minus = eraser_basis(settings.eraser_phase)
    _, rho_plus = condition_on_marker_basis(rho_joint, plus)
    _, rho_minus = condition_on_marker_basis(rho_joint, minus)
    optimal_plus, _ = optimal_eraser_basis(settings.marker_angle)
    _, rho_opt_plus = condition_on_marker_basis(rho_joint, optimal_plus)
    raw = screen_intensity_from_rho(x, rho_path)
    erased_plus = screen_intensity_from_rho(x, rho_plus)
    erased_minus = screen_intensity_from_rho(x, rho_minus)
    erased_optimal = screen_intensity_from_rho(x, rho_opt_plus)
    write_line_svg(
        output_dir / "figures" / "figure_quantum_eraser_patterns.svg",
        x,
        [
            {"label": f"raw V={path_visibility_from_rho(rho_path):.2f}", "y": raw, "color": "#2962ff"},
            {"label": f"fixed eraser + V={path_visibility_from_rho(rho_plus):.2f}", "y": erased_plus, "color": "#00897b"},
            {"label": f"fixed eraser - V={path_visibility_from_rho(rho_minus):.2f}", "y": erased_minus, "color": "#d84315", "dash": True},
            {"label": f"optimal eraser V={path_visibility_from_rho(rho_opt_plus):.2f}", "y": erased_optimal, "color": "#6a1b9a"},
        ],
        "Raw and Conditioned Eraser Patterns",
        "screen position",
        "normalized intensity",
    )
    summary = quantum_eraser_observables(settings, eraser_time=None)
    pd.DataFrame([summary]).to_csv(output_dir / "quantum_eraser_summary.csv", index=False)


def make_timing_outputs(settings: ApparatusSettings, output_dir: Path):
    eraser_times = np.linspace(0.0, settings.measurement_duration * 1.25, 140)
    low_theta = 0.18
    high_theta = constraints_from_apparatus(settings)["Theta"]
    rows = []
    for theta in [low_theta, high_theta]:
        for t in eraser_times:
            obs = quantum_eraser_observables(settings, eraser_time=float(t), theta_override=theta)
            rows.append(
                {
                    "theta_used": theta,
                    "eraser_time": float(t),
                    **obs,
                }
            )
    timing = pd.DataFrame(rows)
    timing.to_csv(output_dir / "delayed_choice_timing_summary.csv", index=False)
    series = []
    for theta, color, label in [
        (low_theta, "#00897b", "weak irreversible record"),
        (high_theta, "#d84315", "strong irreversible record"),
    ]:
        subset = timing[timing["theta_used"] == theta]
        series.append(
            {
                "label": label,
                "y": subset["visibility_eraser_optimal_best"].to_numpy(),
                "color": color,
            }
        )
    write_line_svg(
        output_dir / "figures" / "figure_delayed_choice_timing.svg",
        eraser_times,
        series,
        "Delayed-Choice Eraser: Timing Matters Only Through Irreversibility",
        "eraser time",
        "optimal conditioned visibility",
        ylim=(0.0, 1.05),
        vlines=[
            (settings.record_onset_time, "record onset", "#455a64"),
            (settings.measurement_duration, "screen", "#6a1b9a"),
        ],
    )


def make_trajectory_outputs(settings: ApparatusSettings, output_dir: Path):
    traj = simulate_phase_flip_trajectories(settings)
    traj.to_csv(output_dir / "trajectory_summary.csv", index=False)
    write_line_svg(
        output_dir / "figures" / "figure_trajectory_convergence.svg",
        traj["time"].to_numpy(),
        [
            {
                "label": "stochastic trajectory ensemble",
                "y": traj["visibility_trajectory_mean"].to_numpy(),
                "color": "#2962ff",
            },
            {
                "label": "master-equation expectation",
                "y": traj["visibility_exact"].to_numpy(),
                "color": "#d84315",
                "dash": True,
            },
        ],
        "Quantum Trajectory Ensemble Reproduces Dephasing",
        "time",
        "raw visibility",
        ylim=(0.0, 1.05),
        vlines=[(settings.record_onset_time, "record onset", "#455a64")],
    )


def make_fit_outputs(df: pd.DataFrame, output_dir: Path, prefix="demo"):
    fit, pred, data = fit_visibility_models(df)
    summary_name = f"{prefix}_fit_summary.csv" if prefix else "fit_summary.csv"
    pred_name = f"{prefix}_fit_predictions.csv" if prefix else "fit_predictions.csv"
    fit.to_csv(output_dir / summary_name, index=False)
    pred.to_csv(output_dir / pred_name, index=False)
    best_model = str(fit.iloc[0]["model"])
    merged = data.reset_index(drop=True).join(pred.drop(columns=["condition_id"], errors="ignore"))
    write_bar_svg(
        output_dir / "figures" / "figure_model_comparison.svg",
        fit["model"].to_list(),
        fit["delta_aicc"].to_numpy(),
        "Model Comparison on Visibility Dataset",
        "delta AICc",
    )
    obs = data["visibility_obs"].to_numpy(dtype=float)
    pred_best = pred[f"pred_visibility_{best_model}"].to_numpy(dtype=float)
    write_scatter_svg(
        output_dir / "figures" / "figure_best_fit_scatter.svg",
        obs,
        pred_best,
        f"Observed vs Predicted Visibility ({best_model})",
        "observed visibility",
        "predicted visibility",
        diagonal=True,
    )
    product = (
        data["Lambda"].to_numpy(dtype=float)
        * data["Gamma"].to_numpy(dtype=float)
        * data["Theta"].to_numpy(dtype=float)
    )
    order = np.argsort(product)
    write_scatter_svg(
        output_dir / "figures" / "figure_master_curve.svg",
        product,
        obs,
        "Product-Law Master Curve",
        "Lambda * Gamma * Theta",
        "visibility",
        line_x=product[order],
        line_y=pred["pred_visibility_product"].to_numpy(dtype=float)[order],
        line_label="product fit",
    )
    return fit, pred, merged


def make_eraser_decomposition_outputs(df: pd.DataFrame, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "figures").mkdir(parents=True, exist_ok=True)
    decomposition = decompose_eraser_dataset(df)
    decomposition.to_csv(output_dir / "eraser_decomposition.csv", index=False)
    if decomposition.empty:
        (output_dir / "chapman_interpretation.md").write_text(
            "# Eraser Decomposition\n\nNo paired raw/conditioned rows were available.\n",
            encoding="utf-8",
        )
        return decomposition

    x = decomposition["x_value"].to_numpy(dtype=float)
    order = np.argsort(x)
    x_sorted = x[order]
    write_line_svg(
        output_dir / "figures" / "figure_raw_vs_conditioned_visibility.svg",
        x_sorted,
        [
            {
                "label": "raw visibility",
                "y": decomposition["raw_visibility"].to_numpy(dtype=float)[order],
                "color": "#2962ff",
            },
            {
                "label": "best conditioned visibility",
                "y": decomposition["best_conditioned_visibility"].to_numpy(dtype=float)[order],
                "color": "#00897b",
            },
            {
                "label": "eta irreversible estimate",
                "y": decomposition["eta_irreversible_hat"].to_numpy(dtype=float)[order],
                "color": "#d84315",
                "dash": True,
            },
        ],
        "Chapman First-Pass Raw vs Conditioned Visibility",
        str(decomposition["x_name"].iloc[0]),
        "relative visibility",
        ylim=(0.0, 1.05),
    )
    write_line_svg(
        output_dir / "figures" / "figure_recoverable_unrecoverable_loss.svg",
        x_sorted,
        [
            {
                "label": "recoverable loss",
                "y": decomposition["recoverable_loss"].to_numpy(dtype=float)[order],
                "color": "#00897b",
            },
            {
                "label": "unrecoverable loss",
                "y": decomposition["unrecoverable_loss"].to_numpy(dtype=float)[order],
                "color": "#d84315",
            },
        ],
        "Chapman First-Pass Loss Decomposition",
        str(decomposition["x_name"].iloc[0]),
        "visibility loss",
        ylim=(0.0, 1.05),
    )
    mean_recovery = float(decomposition["recovery_fraction"].mean())
    peak_recovery = float(decomposition["recovery_fraction"].max())
    best_row = decomposition.loc[decomposition["recovery_fraction"].idxmax()]
    status = (
        "CD-compatible exploratory signal"
        if peak_recovery >= 0.5
        else "inconclusive first-pass signal"
    )
    interpretation = f"""# Chapman First-Pass Interpretation

Status: {status}

This analysis uses first-pass visually digitized points, not publication-grade data. The best conditioned branch is treated as an empirical estimate of the irreversible dephasing bound, while the gap between raw and conditioned visibility is treated as recoverable marker/path information.

- Mean recovery fraction: {mean_recovery:.3f}
- Peak recovery fraction: {peak_recovery:.3f} at {best_row['x_name']} = {best_row['x_value']:.3f}
- Best branch at peak: {best_row['best_conditioned_on']}

Interpretation: a large conditioned/raw gap supports the scaffold's key separation between reversible which-path entanglement and durable dephasing. It does not by itself validate the Lambda/Gamma/Theta product law; it establishes the first empirical target the product law must later explain.
"""
    (output_dir / "chapman_interpretation.md").write_text(interpretation, encoding="utf-8")
    return decomposition


def make_accessibility_benchmark_outputs(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "figures").mkdir(parents=True, exist_ok=True)
    data = build_accessibility_benchmark_dataset()
    summary, pred, data = fit_accessibility_hypotheses(data)
    data.to_csv(output_dir / "accessibility_benchmark_dataset.csv", index=False)
    summary.to_csv(output_dir / "accessibility_model_comparison.csv", index=False)
    pred.to_csv(output_dir / "accessibility_model_predictions.csv", index=False)

    access_values = sorted(data["record_accessibility"].unique())
    path_values = np.sort(data["path_separation"].unique())
    series = []
    palette = ["#d84315", "#f9a825", "#00897b", "#2962ff", "#6a1b9a", "#455a64", "#c2185b"]
    for idx, access in enumerate(access_values):
        subset = data[data["record_accessibility"] == access].sort_values("path_separation")
        series.append(
            {
                "label": f"access={access:.2g}",
                "y": subset["visibility_obs"].to_numpy(dtype=float),
                "color": palette[idx % len(palette)],
                "dash": idx % 2 == 1,
            }
        )
    write_line_svg(
        output_dir / "figures" / "figure_accessibility_visibility_family.svg",
        path_values,
        series,
        "Visibility Depends on Spatial Distinguishability and Record Accessibility",
        "path separation",
        "visibility",
        ylim=(0.0, 1.05),
    )
    write_bar_svg(
        output_dir / "figures" / "figure_accessibility_model_comparison.svg",
        summary["model"].to_list(),
        summary["delta_aicc"].to_numpy(dtype=float),
        "Accessibility Benchmark Model Comparison",
        "delta AICc",
    )

    best = summary.iloc[0]
    aware = summary[summary["model"] == "aware_record_product"].iloc[0]
    naive = summary[summary["model"] == "naive_record_product"].iloc[0]
    delta_naive = float(naive["aicc"] - aware["aicc"])
    verdict = (
        "passes synthetic discrimination"
        if best["model"] == "aware_record_product" and delta_naive > 10.0
        else "does not yet discriminate cleanly"
    )
    report = f"""# Accessibility Benchmark Report

Status: {verdict}

This synthetic benchmark varies path separation and record accessibility independently. The generated data use the V3 accessibility-aware Theta definition, then compare whether a naive record-load product can recover the same visibility surface.

- Best model: {best['model']}
- Delta AICc, naive record product versus aware product: {delta_naive:.3f}
- Aware product RMSE visibility: {float(aware['rmse_visibility']):.5f}
- Naive product RMSE visibility: {float(naive['rmse_visibility']):.5f}

Interpretation: this is not empirical evidence. It is a discrimination target. If real data show this two-axis pattern, the accessibility-aware Theta parameter is doing nontrivial explanatory work. If a naive record-strength model fits equally well, the refinement is only vocabulary.
"""
    (output_dir / "accessibility_benchmark_report.md").write_text(
        report,
        encoding="utf-8",
    )
    return summary, pred, data


def make_identifiability_outputs(output_dir: Path):
    balanced = build_synthetic_visibility_dataset()
    confounded = build_confounded_visibility_dataset()
    design_frames = {"balanced_factorial": balanced, "confounded_latent_load": confounded}
    summary_frames = []
    corr_frames = []
    vif_frames = []
    feature_frames = []
    fit_frames = []

    for name, df in design_frames.items():
        summary, corr, vif, features = design_diagnostics(df, name=name)
        fit, _, _ = fit_visibility_models(df)
        summary_frames.append(summary)
        corr_frames.append(corr)
        vif_frames.append(vif)
        feature_frames.append(features)
        fit_with_name = fit.copy()
        fit_with_name.insert(0, "design", name)
        fit_frames.append(fit_with_name)

    summary = pd.concat(summary_frames, ignore_index=True)
    corr = pd.concat(corr_frames, ignore_index=True)
    vif = pd.concat(vif_frames, ignore_index=True)
    features = pd.concat(feature_frames, ignore_index=True)
    fits = pd.concat(fit_frames, ignore_index=True)
    summary.to_csv(output_dir / "identifiability_design_summary.csv", index=False)
    corr.to_csv(output_dir / "identifiability_factor_correlations.csv", index=False)
    vif.to_csv(output_dir / "identifiability_vif.csv", index=False)
    features.to_csv(output_dir / "identifiability_feature_scales.csv", index=False)
    fits.to_csv(output_dir / "identifiability_model_comparison.csv", index=False)

    product_weights = []
    labels = []
    for name in design_frames:
        row = fits[(fits["design"] == name) & (fits["model"] == "product")].iloc[0]
        product_weights.append(float(row["akaike_weight"]))
        labels.append(name.replace("_", " "))
    write_bar_svg(
        output_dir / "figures" / "figure_identifiability_product_weight.svg",
        labels,
        product_weights,
        "Product-Law Evidence Depends on Design Separability",
        "product Akaike weight",
    )
    write_bar_svg(
        output_dir / "figures" / "figure_identifiability_conditioning.svg",
        labels,
        np.log10(summary["full_second_order_condition_number"].to_numpy(dtype=float)),
        "Design Conditioning",
        "log10 condition number",
    )
    for name in design_frames:
        subset = corr[corr["design"] == name]
        write_matrix_heatmap_svg(
            output_dir / "figures" / f"figure_{name}_factor_correlation.svg",
            subset,
            f"{name.replace('_', ' ').title()} Factor Correlations",
        )


def write_template_csv(data_dir: Path):
    template = build_synthetic_visibility_dataset(n_space=2, n_time=2, n_entropy=2, noise_sd=0.0)
    cols = [
        "condition_id",
        "path_separation",
        "detector_spatial_resolution",
        "coherence_time",
        "detector_response_time",
        "record_entropy_bits",
        "record_survival_probability",
        "environment_coupling",
        "record_accessibility",
        "Lambda",
        "Gamma",
        "Theta",
        "marker_angle",
        "marker_visibility",
        "t_meas",
        "visibility_obs",
        "visibility_se",
    ]
    template[cols].to_csv(data_dir / "visibility_fit_template.csv", index=False)


def run_demo(output_dir: Path, data_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "figures").mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    settings = ApparatusSettings()
    make_quantum_eraser_outputs(settings, output_dir)
    make_timing_outputs(settings, output_dir)
    make_trajectory_outputs(settings, output_dir)
    synthetic = build_synthetic_visibility_dataset()
    synthetic.to_csv(output_dir / "synthetic_visibility_dataset.csv", index=False)
    fit, _, _ = make_fit_outputs(synthetic, output_dir, prefix="demo")
    make_identifiability_outputs(output_dir)
    write_template_csv(data_dir)
    run_summary = {
        "settings": asdict(settings),
        "constraints": constraints_from_apparatus(settings),
        "best_fit_model": str(fit.iloc[0]["model"]),
        "best_delta_aicc": float(fit.iloc[0]["delta_aicc"]),
    }
    (output_dir / "demo_run_summary.json").write_text(
        json.dumps(run_summary, indent=2),
        encoding="utf-8",
    )


def run_fit(input_csv: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "figures").mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(input_csv)
    make_fit_outputs(df, output_dir, prefix="")


def run_design(input_csv: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "figures").mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(input_csv)
    summary, corr, vif, features = design_diagnostics(df, name=input_csv.stem)
    summary.to_csv(output_dir / "design_summary.csv", index=False)
    corr.to_csv(output_dir / "design_factor_correlations.csv", index=False)
    vif.to_csv(output_dir / "design_vif.csv", index=False)
    features.to_csv(output_dir / "design_feature_scales.csv", index=False)
    write_matrix_heatmap_svg(
        output_dir / "figures" / "figure_design_factor_correlation.svg",
        corr,
        "Factor Correlations",
    )


def run_identifiability_benchmark(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "figures").mkdir(parents=True, exist_ok=True)
    make_identifiability_outputs(output_dir)


def run_decompose_eraser(input_csv: Path, output_dir: Path):
    df = pd.read_csv(input_csv)
    make_eraser_decomposition_outputs(df, output_dir)


def run_accessibility_benchmark(output_dir: Path):
    make_accessibility_benchmark_outputs(output_dir)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Constraint Dynamics quantum-measurement V3 scaffold"
    )
    sub = parser.add_subparsers(dest="command")
    demo = sub.add_parser("demo", help="generate demo data, fits, and figures")
    demo.add_argument("--output-dir", default="outputs")
    demo.add_argument("--data-dir", default="data")
    fit = sub.add_parser("fit", help="fit visibility models to a CSV")
    fit.add_argument("--input", required=True)
    fit.add_argument("--output-dir", default="outputs")
    design = sub.add_parser("design", help="diagnose factor separability for a CSV")
    design.add_argument("--input", required=True)
    design.add_argument("--output-dir", default="outputs/design_diagnostics")
    decompose = sub.add_parser(
        "decompose-eraser",
        help="decompose paired raw/conditioned eraser visibility",
    )
    decompose.add_argument("--input", required=True)
    decompose.add_argument("--output-dir", default="outputs/eraser_decomposition")
    access = sub.add_parser(
        "benchmark-accessibility",
        help="generate record-accessibility discrimination benchmark",
    )
    access.add_argument("--output-dir", default="outputs/accessibility_benchmark")
    bench = sub.add_parser("benchmark-designs", help="generate balanced vs confounded identifiability benchmark")
    bench.add_argument("--output-dir", default="outputs")
    template = sub.add_parser("template", help="write a visibility CSV template")
    template.add_argument("--data-dir", default="data")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    command = args.command or "demo"
    try:
        if command == "demo":
            output_dir = Path(getattr(args, "output_dir", "outputs"))
            data_dir = Path(getattr(args, "data_dir", "data"))
            run_demo(output_dir, data_dir)
        elif command == "fit":
            run_fit(Path(args.input), Path(args.output_dir))
        elif command == "design":
            run_design(Path(args.input), Path(args.output_dir))
        elif command == "decompose-eraser":
            run_decompose_eraser(Path(args.input), Path(args.output_dir))
        elif command == "benchmark-accessibility":
            run_accessibility_benchmark(Path(args.output_dir))
        elif command == "benchmark-designs":
            run_identifiability_benchmark(Path(args.output_dir))
        elif command == "template":
            data_dir = Path(args.data_dir)
            data_dir.mkdir(parents=True, exist_ok=True)
            write_template_csv(data_dir)
        else:
            parser.error(f"Unknown command {command}")
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
