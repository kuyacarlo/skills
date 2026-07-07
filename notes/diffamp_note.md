# Differential Amplifier

$A_v$ = voltage gain
$V_0, V_1$ = Inputs
$V_d$ = voltage differential
$R_C$ = collector resistance

takes 2 inputs, to one output

single ended

```circuit
Q1 = npn
Q2 = npn right 4 flip
line Q1.emitter to Q2.emitter
line mid Q1.emitter Q2.emitter down 0.5
RE = resistor down label=$R_E$
VEE = vss down label=$V_{EE}$
RC1 = resistor up at Q1.collector label=$R_C$
RC2 = resistor up at Q2.collector label=$R_C$
line RC1.end to RC2.end
VCC = vdd up at mid RC1.end RC2.end label=$V_{CC}$
V1 = source_sin left at Q1.base label=$V_1$
ground
V2 = source_sin right at Q2.base label=$V_2$ flip
ground
out_neg = line right at Q1.collector length 0.7
dot label=-
out_pos = line left at Q2.collector length 0.7
dot label=+
```

Non-inverting input: same phase in input signal, v1 present, no v2 aka connected to ground.
2 outputs, double ended aka diff output.

## Non-inverting, differential output
> one signal, 2 output pins: non-inverting, diff output

$V_2 = 0$
$V_0 = V_1(Av)$

## Inverting input, differential output
$V_1 = 0$
$V_0 = -V_2(A_v)$

## Inverting, single ended output
$V_1 = 0$
$V_0 = -V_2(A_v)$

# DC and AC analysis of diff ampli

**Tail Current** - current flowing through the emitter to $R_E$
*DC Circuit.

### Ideal approximation: $I=\frac{V}{R}$
$I_T=\frac{V_{EE}}{R_E}$
$I_E=\frac{I_T}{2}$
$V_C = V_{CC} - I_C R_C$

### Second Approximation
$I_T = \frac{V_{EE}-V_{BE}}{R_E}$
$V_{BE}$  = 0.7V default(silicon), 0.3V germanium

### Third Approximation

## AC Approximation
AC Emitter Resistance($re'$)
$R_{ac} = \frac{\Delta VBE}{\Delta IE}$
$R_{ac} = 25mV/I_E$
$re' = 25mV/I_E$
Voltage Gain
${R_c}/{re'}$
Input Impedance: $Z_{in} = 2\beta re'$
