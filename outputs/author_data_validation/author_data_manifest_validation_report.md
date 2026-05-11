# Author Data Manifest Validation

Verdict: no author data ready for G11 analysis

This validator checks whether received author/numerical data satisfy the target schema and whether the schema allows a genuine G11 analysis.

## Summary

- Manifest rows: 4
- Received rows: 0
- Schema-passing rows: 0
- G11-ready rows: 0

## Rows

- **xiao_2019_author_data**: not_received; schema ok = False; G11 ready = False
- **hochrainer_2017_independent_widths**: not_received; schema ok = False; G11 ready = False
- **mir_2007_visibility_context**: not_received; schema ok = False; G11 ready = False
- **eibenberger_2014_recoil_controls**: not_received; schema ok = False; G11 ready = False

## Rule

Passing the CSV schema is not enough. A row is G11-ready only when the source also claims support for G11 and the target schema allows a second-experiment or held-out record-variable test.
