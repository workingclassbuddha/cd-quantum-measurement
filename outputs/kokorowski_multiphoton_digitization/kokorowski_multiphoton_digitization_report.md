# Kokorowski 2001 Multiphoton Digitization

Status: vector Fig. 4 digitization complete

- Source URL: https://arxiv.org/abs/quant-ph/0009044
- DOI: https://doi.org/10.1103/PhysRevLett.86.2191
- EPS: `outputs/tmp/kokorowski_source/extracted/figure4.eps`
- EPS SHA256: `a85b2073c180fbd505206c109711386449cc4c7702c7f5c9ec7f7cf5f7b3161d`
- Extraction method: `eps_vector_point_extraction_v1`
- Output CSV: `data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZED.csv`
- Output JSON: `data/extracted/KOKOROWSKI_2001_MULTIPHOTON_DIGITIZATION.json`

## Branch Counts

- **bullet_lower_intensity**: 13 points
- **circle_high_intensity**: 10 points

## Calibration

- x-axis: path separation `d/lambda` from 0.00 to 0.30
- y-axis: relative contrast from 1.0 to 0.0
- point source: EPS `arc` commands with `StrokePath` for open circles and `FillPath` for bullets

## Boundary

This digitization is stronger than raster picking because it reads vector point centers, but it still uses figure coordinates from the publication rather than author tables.
