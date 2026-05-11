# Kokorowski 2001 Multiphoton Decoherence Scout

Verdict: high-priority public no-refit candidate, digitization required

This scout checks whether Kokorowski et al. 2001 can become the missing second independent measured-record-to-visibility validation. It is especially relevant because the paper explicitly formulates decoherence as the Fourier transform of photon momentum-transfer distributions and reports independent beam-deflection/broadening measurements for the many-photon parameters used in Fig. 4.

- Source URL: https://arxiv.org/abs/quant-ph/0009044
- arXiv source URL: https://arxiv.org/e-print/quant-ph/0009044
- DOI: https://doi.org/10.1103/PhysRevLett.86.2191
- Source directory: `outputs/tmp/kokorowski_source/extracted`
- TeX SHA256: `4f436a938adf03dfe478a0cc11f780fafb01d4975a5e61f23f617bf6c9566647`
- Extraction method: `source_text_and_eps_manifest_scout_v1`

## Source Findings

- Eq. beta(d) is written as the Fourier transform of photon momentum-transfer distribution P(Delta k).
- The total decoherence function sums beta(d)^n over a photon-number distribution P(n).
- Figure 2 nbar/sigma_n values were extracted from best-fit visibility curves, so Fig. 2 is not a strict no-refit result.
- The text says Fig. 4 nbar and sigma_n were independently determined from beam-deflection and broadening measurements.
- Figure 4 therefore looks like a public-data route to the missing second no-refit gate, pending calibrated digitization and model comparison.

## Figure Register

- **Figure 2** (`figure2.eps`): normalized contrast/decoherence function versus path separation for several mean photon numbers. Role: few-photon Fourier-kernel control; reported nbar/sigma_n values are extracted from best-fit visibility curves
- **Figure 3** (`figure3.eps`): contrast loss versus mean photons scattered at fixed path separations. Role: possible no-refit decay check using beam-broadening photon-number calibration and measured phase product
- **Figure 4** (`figure4.eps`): many-photon contrast loss versus path separation for two laser intensities. Role: strongest next candidate: caption reports theory curves generated from independently measured nbar and sigma_n

## Gate Decision

- Source package available: True
- No-refit-like figures found: 2
- Clears G11 now: False

Kokorowski does not clear G11 yet because this scout has not digitized the visibility curves or reproduced the no-refit prediction numerically. It is now the best public-data candidate to implement next.

## Exact Next CLI Proposal

```bash
python src/constraint_dynamics_quantum_v3.py digitize-kokorowski-multiphoton \
  --source-dir outputs/tmp/kokorowski_source/extracted \
  --output-dir outputs/kokorowski_multiphoton_digitization \
  --data-dir data/extracted

python src/constraint_dynamics_quantum_v3.py analyze-kokorowski-multiphoton \
  --input data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv \
  --output-dir outputs/kokorowski_multiphoton
```

## Strict Boundary

This is a standard quantum-decoherence candidate, not a collapse solution and not product-law validation. The only possible breakthrough relevance is whether independently measured recoil/photon-number parameters predict visibility without refitting the record bandwidth/load variable.
