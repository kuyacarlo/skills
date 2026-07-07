#!/usr/bin/env python3
import sys
import os
import re
import subprocess

# Regular expression to find circuit code blocks
CIRCUIT_BLOCK_RE = re.compile(r'```circuit\s*(.*?)\s*```', re.DOTALL)

def compile_dsl_to_python(dsl_code, output_svg_path):
    """
    Translates the simple, human-readable circuit DSL into a Python Schemdraw script.
    """
    lines = dsl_code.split('\n')
    py_code = [
        "import schemdraw",
        "import schemdraw.elements as elm",
        "d = schemdraw.Drawing()",
        "refs = {}"
    ]
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # Parse component parameters
        parts = line.split()
        
        # Check for assignment: Name = Component ...
        var_name = None
        if len(parts) >= 3 and parts[1] == '=':
            var_name = parts[0]
            parts = parts[2:]
            
        comp_type = parts[0].lower()
        args = parts[1:]
        
        # Build Schemdraw chain
        element_str = ""
        
        if comp_type == "npn":
            element_str = "elm.BjtNpn()"
        elif comp_type == "pnp":
            element_str = "elm.BjtPnp()"
        elif comp_type == "resistor":
            element_str = "elm.Resistor()"
        elif comp_type == "capacitor":
            element_str = "elm.Capacitor()"
        elif comp_type == "inductor":
            element_str = "elm.Inductor()"
        elif comp_type == "source_sin":
            element_str = "elm.SourceSin().scale(0.6)"
        elif comp_type == "source_dc":
            element_str = "elm.SourceV().scale(0.6)"
        elif comp_type == "ground":
            element_str = "elm.Ground()"
        elif comp_type == "vdd":
            element_str = "elm.Vdd()"
        elif comp_type == "vss":
            element_str = "elm.Vdd()"  # In schemdraw Vdd can point down for Vss
        elif comp_type == "line":
            element_str = "elm.Line()"
        elif comp_type == "dot":
            element_str = "elm.Dot()"
        else:
            print(f"Warning: Unknown component type '{comp_type}'", file=sys.stderr)
            continue
            
        # Parse layout helpers
        modifiers = []
        at_pos = None
        to_pos = None
        label_val = None
        length_val = None
        flip_val = False
        
        # Iterate over arguments to extract modifiers
        i = 0
        while i < len(args):
            arg = args[i]
            if arg == "right":
                modifiers.append(".right()")
                # Check for explicit step/coordinate offset (e.g. right 4)
                if i + 1 < len(args) and re.match(r'^\d+(\.\d+)?$', args[i+1]):
                    if comp_type in ["npn", "pnp"]:
                        at_pos = f"({args[i+1]}, 0)"
                    else:
                        modifiers.append(f".length({args[i+1]})")
                    i += 1
            elif arg == "left":
                modifiers.append(".left()")
            elif arg == "up":
                modifiers.append(".up()")
            elif arg == "down":
                modifiers.append(".down()")
            elif arg == "flip":
                flip_val = True
            elif arg == "length":
                if i + 1 < len(args):
                    length_val = args[i+1]
                    modifiers.append(f".length({length_val})")
                    i += 1
            elif arg == "at":
                if i + 1 < len(args):
                    raw_pos = args[i+1]
                    # Check for mid keyword helper: at mid Q1.emitter Q2.emitter down 0.5
                    if raw_pos == "mid" and i + 3 < len(args):
                        n1 = args[i+2]
                        n2 = args[i+3]
                        py_code.append(f"mid_x = (refs['{n1.split('.')[0]}'].{n1.split('.')[1]}[0] + refs['{n2.split('.')[0]}'].{n2.split('.')[1]}[0]) / 2")
                        py_code.append(f"mid_y = refs['{n1.split('.')[0]}'].{n1.split('.')[1]}[1]")
                        at_pos = "(mid_x, mid_y)"
                        i += 3
                    else:
                        if '.' in raw_pos:
                            obj, term = raw_pos.split('.')
                            at_pos = f"refs['{obj}'].{term}"
                        else:
                            at_pos = raw_pos
                    i += 1
            elif arg == "to":
                if i + 1 < len(args):
                    raw_pos = args[i+1]
                    if '.' in raw_pos:
                        obj, term = raw_pos.split('.')
                        to_pos = f"refs['{obj}'].{term}"
                    else:
                        to_pos = raw_pos
                    i += 1
            elif arg.startswith("label="):
                label_val = arg.split('=', 1)[1]
            i += 1
            
        # Compile python command
        cmd_parts = [element_str]
        
        # Apply layout
        if modifiers:
            cmd_parts.extend(modifiers)
        if flip_val:
            cmd_parts.append(".flip()")
        if at_pos:
            cmd_parts.append(f".at({at_pos})")
        if to_pos:
            cmd_parts.append(f".to({to_pos})")
        if label_val:
            cmd_parts.append(f".label('{label_val}')")
            
        chain = "".join(cmd_parts)
        
        if var_name:
            py_code.append(f"refs['{var_name}'] = d.add({chain})")
        else:
            py_code.append(f"d.add({chain})")
            
    py_code.append(f"d.save('{output_svg_path}')")
    
    return "\n".join(py_code)

def render_markdown(input_path, output_path):
    print(f"Reading {input_path}...")
    with open(input_path, 'r') as f:
        content = f.read()
        
    output_dir = os.path.dirname(output_path) or '.'
    os.makedirs(output_dir, exist_ok=True)
    
    scratch_dir = os.path.join(output_dir, 'compiled_circuits')
    os.makedirs(scratch_dir, exist_ok=True)
    
    matches = list(re.finditer(CIRCUIT_BLOCK_RE, content))
    
    for idx, match in reversed(list(enumerate(matches))):
        dsl_code = match.group(1).strip()
        svg_filename = f"circuit_{idx}.svg"
        svg_path = os.path.join(scratch_dir, svg_filename)
        py_path = os.path.join(scratch_dir, f"circuit_{idx}.py")
        
        # Compile
        py_script = compile_dsl_to_python(dsl_code, svg_path)
        with open(py_path, 'w') as py_f:
            py_f.write(py_script)
            
        # Execute script to generate SVG
        print(f"Rendering circuit {idx} to {svg_path}...")
        res = subprocess.run([sys.executable, py_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Error compiling circuit {idx}:\n{res.stderr}", file=sys.stderr)
            continue
            
        svg_abs_path = os.path.abspath(svg_path)
        markdown_image_link = f"\n![Circuit Diagram {idx}](file://{svg_abs_path})\n"
        content = content[:match.start()] + markdown_image_link + content[match.end():]
        
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"Successfully wrote rendered note to {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: render_notes.py [input_note.md] [output_note.md]")
        sys.argv = ["render_notes.py", "/home/kaoru/projects/skills/notes/diffamp_note.md", "/home/kaoru/projects/skills/notes/diffamp_note_rendered.md"]
        
    render_markdown(sys.argv[1], sys.argv[2])
