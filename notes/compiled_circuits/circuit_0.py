import schemdraw
import schemdraw.elements as elm
d = schemdraw.Drawing()
refs = {}
refs['Q1'] = d.add(elm.BjtNpn())
refs['Q2'] = d.add(elm.BjtNpn().right().flip().at((4, 0)))
d.add(elm.Line().to(refs['Q2'].emitter))
d.add(elm.Line().down())
refs['RE'] = d.add(elm.Resistor().down().label('$R_E$'))
refs['VEE'] = d.add(elm.Vdd().down().label('$V_{EE}$'))
refs['RC1'] = d.add(elm.Resistor().up().at(refs['Q1'].collector).label('$R_C$'))
refs['RC2'] = d.add(elm.Resistor().up().at(refs['Q2'].collector).label('$R_C$'))
d.add(elm.Line().to(refs['RC2'].end))
mid_x = (refs['RC1'].end[0] + refs['RC2'].end[0]) / 2
mid_y = refs['RC1'].end[1]
refs['VCC'] = d.add(elm.Vdd().up().at((mid_x, mid_y)))
refs['V1'] = d.add(elm.SourceSin().scale(0.6).left().at(refs['Q1'].base).label('$V_1$'))
d.add(elm.Ground())
refs['V2'] = d.add(elm.SourceSin().scale(0.6).right().flip().at(refs['Q2'].base).label('$V_2$'))
d.add(elm.Ground())
refs['out_neg'] = d.add(elm.Line().right().length(0.7).at(refs['Q1'].collector))
d.add(elm.Dot().label('-'))
refs['out_pos'] = d.add(elm.Line().left().length(0.7).at(refs['Q2'].collector))
d.add(elm.Dot().label('+'))
d.save('/home/kaoru/projects/skills/notes/compiled_circuits/circuit_0.svg')