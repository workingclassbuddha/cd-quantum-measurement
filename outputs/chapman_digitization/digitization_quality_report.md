# Chapman Digitization Quality Report

Status: recovery window retained

The Chapman 1995 extraction has been upgraded from first-pass visual estimates to calibrated pixel coordinates. The digitizer renders the source PDF with `pdftoppm`, parses the grayscale PGM output, and maps fixed pixel picks through stored axis anchors.

- Source URL: https://chapmanlabs.gatech.edu/papers/scattering_ifm_prl95.pdf
- PDF SHA256: `27c288986e414efb43a776bd7c02b79208cba51beb1598e40915ceaa3c3f5b72`
- Render DPI: 220
- Extracted rows: 36
- Extraction method: `calibrated_pixel_digitization_v1`

## Recovery Window

- Digitized peak recovery fraction: 0.692 at d/lambda = 0.400
- Digitized peak recoverable loss: 0.540
- Digitized raw / conditioned visibility at peak: 0.220 / 0.760
- First-pass peak recovery fraction: 0.625 at d/lambda = 0.500

## Interpretation

The calibrated pass retains a large recoverable-visibility window in Chapman, which supports the scaffold's separation between accessible entangled records and inaccessible durable records. It does not validate the Lambda/Gamma/Theta product law because detector acceptance and record accessibility have not yet been independently parameterized from the apparatus.
