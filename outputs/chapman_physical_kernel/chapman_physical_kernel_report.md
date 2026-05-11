# Chapman Physical Acceptance-Kernel Report

Status: physical model improves branch interpretation

This analysis implements Chapman Eq. (3) as a characteristic function of a normalized photon transverse momentum-transfer distribution:

```text
V(d) = | integral P_eff(q) exp(i 2*pi*q*d_over_lambda) dq |
```

- Source URL: https://chapmanlabs.gatech.edu/papers/scattering_ifm_prl95.pdf
- PDF SHA256: `27c288986e414efb43a776bd7c02b79208cba51beb1598e40915ceaa3c3f5b72`
- Input CSV: `data/extracted/CHAPMAN_1995_SCATTER_DIGITIZED.csv`

## Raw Recoil Model

- Uniform recoil RMSE: 0.0285
- Fitted beta recoil RMSE: 0.0284
- Empirical raw sinc/Fourier RMSE: 0.0257

## Accepted Branch Proxies

- Case I physical RMSE: 0.0134
- Case I empirical sinc RMSE: 0.0396
- Case I accepted q center / width: 1.500 / 0.375
- Case III physical RMSE: 0.0399
- Case III empirical sinc RMSE: 0.0700
- Case III accepted q center / width: 1.950 / 0.885
- Forward/backward center ordering recovered: True
- Physical branch model beats empirical sinc on both branches: True

## Interpretation

The physical acceptance-kernel model is still standard quantum mechanics: raw loss and recovery come from averaging over, or restricting, photon momentum-transfer records. The fitted acceptance centers are inferred proxies only; they are not independent detector-geometry measurements.

## Verdict

If the physical accepted-window model beats the empirical sinc branch fits and recovers the expected forward/backward ordering, it strengthens the branch-specific accessibility interpretation. Otherwise, the robust claim remains narrower: Chapman supports a raw Fourier-kernel correction to scalar dephasing, while branch-specific Constraint Dynamics accessibility remains unvalidated.

## What This Does Not Show

- It does not solve collapse.
- It does not validate the Lambda/Gamma/Theta product law.
- It does not replace extracting the actual detector acceptance geometry.
- It does not remove the need for a second real experiment.
