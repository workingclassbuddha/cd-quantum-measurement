# Xiao Probability Distribution Report

Status: probability distribution supports record-bandwidth target

This pass digitizes Xiao et al. 2019 Fig. 3 from `probability.pdf`. Panel a tracks the growth of total mean absolute momentum disturbance with propagation distance. Panel b tracks the far-field momentum-disturbance distributions for `phi=0` and `phi=pi`.

- Source URL: https://arxiv.org/abs/1805.02059
- DOI: https://doi.org/10.1126/sciadv.aav9547
- Source file: `probability.pdf`
- Source SHA256: `50ae16805cacedbf059985849f61ff186117f7168d84db89893123661f4d6c03`
- Render DPI: 250
- Extracted rows: 365
- Extraction method: `calibrated_curve_digitization_v1`

## Distribution Checks

- Mean absolute disturbance growth: 0.568
- Late mean absolute disturbance: 0.681
- `phi=0` peak location: p = -0.022
- `phi=pi` mean absolute side-peak location: |p| = 1.586
- `phi=pi` central density: 0.314
- `phi=pi` peak density: 1.234

## Interpretation

The useful signal is distributional rather than just scalar. The `phi=pi` far-field branch develops two side peaks near the expected momentum-transfer scale, while the `phi=0` branch remains centered near p=0. Panel a shows that the mean absolute disturbance grows during propagation. Together with the Fig. 4 stress result, this makes Xiao a stronger second empirical target for record-bandwidth language.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not solve collapse.
- It does not require Bohmian mechanics as an ontology.
- It does not repair the Chapman raw-phase failure.
