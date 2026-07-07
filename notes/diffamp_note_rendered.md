# Differential Amplifier

$A_v$ = voltage gain
$V_0, V_1$ = Inputs
$V_d$ = voltage differential
$R_C$ = collector resistance

takes 2 inputs, to one output

single ended


![Circuit Diagram 0](file:///home/kaoru/projects/skills/notes/compiled_circuits/circuit_0.svg)


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
