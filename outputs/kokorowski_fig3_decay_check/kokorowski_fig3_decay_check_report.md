# Kokorowski Fig. 3 Public-Vector Decay Check

Status: fig3 public-vector consistency check passes as supporting evidence

This check extracts Kokorowski Fig. 3 data markers and paper theory curves directly from the public EPS source. It tests whether the separate contrast-versus-mean-photon-number family is internally consistent with the paper's plotted theory curves.

- Source URL: https://arxiv.org/abs/quant-ph/0009044
- DOI: https://doi.org/10.1103/PhysRevLett.86.2191
- EPS: `outputs/tmp/kokorowski_source/extracted/figure3.eps`
- EPS SHA256: `485b2c0acad7e68ef40d3b43eb7ff20601bd1ace42a6736e109e1426008656ba`
- Extraction method: `eps_vector_marker_and_path_extraction_v1`

## Result

- Data points extracted: 28
- Theory-curve vertices extracted: 276
- Combined log10 visibility RMSE: 0.0458
- Max abs log10 visibility residual: 0.1192
- Clears G11: False

- **triangle_d_over_lambda_006** (`d/lambda=0.06`): 9 points; log10 RMSE 0.0268; max abs residual 0.0600
- **diamond_d_over_lambda_013** (`d/lambda=0.13`): 11 points; log10 RMSE 0.0550; max abs residual 0.1192
- **circle_d_over_lambda_016** (`d/lambda=0.16`): 8 points; log10 RMSE 0.0488; max abs residual 0.0867

## Interpretation

This is useful because it attacks Kokorowski from another public vector surface instead of asking authors for tables. It does not close the missing second-validation gate by itself: Fig. 3 is the same experiment as Fig. 4, and it compares digitized points to plotted paper curves rather than independently re-deriving every calibration input from raw beam-broadening data.

## Boundary

- No collapse solution.
- No beyond-standard-quantum-mechanics claim.
- No Lambda/Gamma/Theta product-law validation.
- No G11 closure from this artifact alone.
