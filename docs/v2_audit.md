# V2 Audit

## Physics Consistency

- V2 correctly separates reversible marker overlap from irreversible path dephasing in the total visibility expression.
- The joint path-plus-marker density matrix is a good starting point for raw versus conditioned eraser behavior.
- The conditioned eraser branch correctly recovers visibility limited by the irreversible dephasing factor, not by the reversible marker overlap.
- The V2 README states the right scientific posture: effective and falsifiable, not a first-principles collapse derivation.

## Main Gaps Addressed in V3

- V2 uses a direct off-diagonal damping factor but has no stochastic trajectory or master-equation interpretation.
- V2 has no timing model, so it cannot represent delayed-choice erasure or distinguish delay from irreversible record formation.
- Apparatus mappings are present but terse; V3 makes the mapping columns explicit and keeps them in the generated CSV template.
- V2 compares constant, product, additive, and pairwise models, but lacks cross-validation, BIC, Akaike weights, optional observation weights, and background/product variants.
- V2 requires matplotlib for figures. V3 writes SVG figures directly and only requires numpy and pandas.

## Coding Notes

- V2 is compact and readable, but it mixes demo generation, modeling, plotting, and fitting in one flat namespace. V3 keeps the same single-file usability while using clearer sections and dataclass-based apparatus settings.
- V2 silently assumes required fitting columns exist. V3 can compute Lambda/Gamma/Theta from apparatus columns or raise a targeted schema error.
- V2 clips observed visibility but not all predicted dephasing rates. V3 clips predicted effective rates to nonnegative values before reconstructing visibility.
