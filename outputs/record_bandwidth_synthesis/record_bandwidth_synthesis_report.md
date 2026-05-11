# Record-Bandwidth Cross-Experiment Synthesis

Status: three-experiment structure survives with Hornberger guardrail

This synthesis compares the strongest Chapman and Xiao outputs without forcing them into a shared product-law fit. The question is narrower: do independent experiments support treating the relevant measurement record as a conjugate momentum-transfer bandwidth rather than a scalar dephasing load?

## Chapman

- Raw sinc/Fourier width: 1.961
- Raw first zero: d/lambda = 0.510
- Raw sinc RMSE: 0.0257
- Raw exponential RMSE: 0.0738
- Exponential/sinc RMSE ratio: 2.87
- Uniform physical recoil RMSE: 0.0285

## Xiao

- Linear bandwidth slope: 0.6866
- Linear bandwidth intercept: 0.0429
- Linear RMSE: 0.0034
- Published-bound RMSE: 0.0693
- Published-bound/linear RMSE ratio: 20.51
- Stress P(linear beats bound): 1.000
- Pairing-null P(Pearson r >= observed): 0.004
- Far-field phi=pi side-peak |p| scale: 1.586
- Mean absolute disturbance growth: 0.568
- Late mean absolute disturbance: 0.681

## Cross-Experiment Reading

Chapman and Xiao are not the same apparatus and should not be numerically merged as if their axes were identical. The useful agreement is structural: Chapman raw visibility behaves like a Fourier transform of an unresolved momentum-transfer record, while Xiao independently reconstructs a momentum-disturbance distribution whose bandwidth grows and whose scalar magnitude tracks visibility loss.

## Hackermueller

- Thermal delta-T4 RMSE: 0.0767
- Simple exp(power) RMSE: 0.0923
- Exp(power)/thermal RMSE ratio: 1.20

- Stress P(thermal delta-T4 beats exp power): 0.994
- Stress P(thermal delta-T4 is best): 0.701

Hackermueller tests a different lane from Chapman and Xiao: durable environmental records emitted as thermal photons. It should be read as standard decoherence-compatible support for a record-load variable, not as a Fourier-revival result.


## Hornberger

- Methane fitted decoherence pressure p_v: 0.807 x 10^-6 mbar
- Methane visibility RMSE: 0.888 percentage points
- Fig. 3 CH4 decoherence pressure: 0.810 x 10^-6 mbar
- Fig. 2 p_v minus Fig. 3 CH4 pressure: -0.003 x 10^-6 mbar
- Gas-species theory/experiment pressure RMSE: 0.185 x 10^-6 mbar
- Gas-species theory/experiment correlation: 0.888

Hornberger is the standard-decoherence guardrail. It supports the environmental-record-load reading by showing that collision records give internally consistent monotone decoherence, while also reminding us not to overgeneralize Fourier-kernel revival language to every irreversible record.


The scale comparison is suggestive but not decisive:

```text
Xiao phi=pi side-peak scale / Chapman raw sinc width = 0.809
```

## What Would Make This Breakthrough-Grade

- A second dataset with both visibility and independently measured momentum/acceptance distributions.
- A held-out prediction where a measured distribution predicts the visibility curve without refitting nuisance bandwidth.
- Independent detector-acceptance geometry for Chapman conditioned branches.
- A product-law test where Lambda, Gamma, and Theta vary independently rather than being inferred post hoc.

## What This Does Not Show

- It does not validate the Lambda/Gamma/Theta product law.
- It does not solve collapse.
- It does not show physics beyond standard quantum mechanics.
- It does not require Bohmian mechanics as an ontology.
- It does not repair the Chapman raw-phase failure.
