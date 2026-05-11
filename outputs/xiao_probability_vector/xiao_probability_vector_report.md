# Xiao Vector Probability Distribution Report

Status: vector probability extraction supports record-bandwidth target

This pass extracts Xiao et al. 2019 Fig. 3 directly from `probability.pdf` vector drawing commands. The important repair is Fig. 3b: the red and blue far-field distribution curves are read as PDF paths, with the inset and legend regions excluded before calibration. This avoids the raster color-threshold baseline that made the previous no-refit bridge fragile.

- Source URL: https://arxiv.org/abs/1805.02059
- DOI: https://doi.org/10.1126/sciadv.aav9547
- Source file: `probability.pdf`
- Source SHA256: `50ae16805cacedbf059985849f61ff186117f7168d84db89893123661f4d6c03`
- Extraction method: `vector_path_digitization_v1`
- Parsed vector paths: 348
- Extracted rows: 511
- Digitized CSV: `data/extracted/XIAO_2019_PROBABILITY_VECTOR_DIGITIZED.csv`
- Digitization JSON: `data/extracted/XIAO_2019_PROBABILITY_VECTOR_DIGITIZATION.json`

## Distribution Checks

- Mean absolute disturbance growth: 0.568
- Late mean absolute disturbance: 0.680
- `phi=0` peak location: p = -0.013
- `phi=0` baseline-subtracted mean |p|: 0.0610
- `phi=pi` baseline-subtracted mean |p|: 1.4112
- `phi=pi` mean absolute side-peak location: |p| = 1.613
- `phi=pi` central density: 0.299
- `phi=pi` peak density: 1.229

## Interpretation

The vector extraction keeps the qualitative Xiao signal: the `phi=0` branch remains centered while the `phi=pi` branch carries broad side peaks. It strengthens the provenance of the Fig. 3b branch moments, but it does not by itself prove that the Fig. 3-to-Fig. 4 bridge survives stress testing.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not solve collapse.
- It does not require Bohmian mechanics as an ontology.
- It does not replace the Xiao distribution stress test.
