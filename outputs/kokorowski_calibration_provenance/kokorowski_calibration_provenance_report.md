# Kokorowski Calibration Provenance

Status: calibration provenance extracted

This artifact anchors the public-data Kokorowski G11 lead to source-text claims without turning the paper into a copied appendix. It records paraphrased claims, source line anchors, source SHA256, and the next validation question for each calibration claim.

- Source TeX: `outputs/tmp/kokorowski_source/extracted/decoh.tex`
- Source SHA256: `4f436a938adf03dfe478a0cc11f780fafb01d4975a5e61f23f617bf6c9566647`
- Output CSV: `data/extracted/KOKOROWSKI_2001_CALIBRATION_PROVENANCE.csv`
- Output JSON: `data/extracted/KOKOROWSKI_2001_CALIBRATION_PROVENANCE.json`
- Extraction method: `tex_line_anchor_provenance_v1`
- Source inventory files: 7
- Calibration-keyword files: 5
- Raw calibration table candidates found: 0

## Anchored Claims

- earlier_non_gaussian_fit_vs_beam_check: lines 248-254; fit-derived P(n) values were consistent with independent beam checks in the earlier non-Gaussian regime.
- kappa_formula_record_width: lines 301-305; kappa^2 = nbar * sigma_k^2 + sigma_n^2 * k0^2
- calculated_vs_fitted_kappa_prime: lines 380-384; calculated: 2.5(1) k0 and 1.8(1) k0; fitted: 2.39(5) k0 and 1.71(5) k0
- figure4_caption_independent_parameters: lines 393-397; lower branch nbar=4.8(2), sigma_n=1.8(1); upper branch nbar=8.1(3), sigma_n=3.5(1)
- beam_deflection_values_independent: lines 376-381; nbar and sigma_n are treated as independent inputs for the Fig. 4 calculated kappa-prime values.

## Public Source Inventory

- 00README.XXX: .xxx, 17 bytes, keyword hits=0, raw-table candidate=False
- decoh.tex: .tex, 23338 bytes, keyword hits=5, raw-table candidate=False
- figure1.eps: .eps, 239236 bytes, keyword hits=2, raw-table candidate=False
- figure2.eps: .eps, 106807 bytes, keyword hits=1, raw-table candidate=False
- figure3.eps: .eps, 167760 bytes, keyword hits=2, raw-table candidate=False
- figure4.eps: .eps, 25922 bytes, keyword hits=1, raw-table candidate=False
- resub_note: (none), 6693 bytes, keyword hits=0, raw-table candidate=False

## Interpretation

The Fig. 4 section supports the independence premise for the many-photon no-refit check, but an earlier non-Gaussian section uses fit-derived photon-number parameters and should not be conflated with the Fig. 4 claim. The public source inventory contains TeX/EPS/readme/note files and no detected raw calibration table candidate, so the kappa-uncertainty profile remains the current public-data bottleneck.

## Boundary

- This does not narrow the kappa uncertainty by itself.
- This does not clear G11.
- This does not validate the Lambda/Gamma/Theta product law.
