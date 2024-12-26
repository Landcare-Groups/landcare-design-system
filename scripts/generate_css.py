import yaml

# Load YAML files
with open('styles/typography.yml', 'r') as typography_file:
    typography = yaml.safe_load(typography_file)

with open('styles/colors.yml', 'r') as colors_file:
    colors = yaml.safe_load(colors_file)

# Start building the CSS file
css = []

# Add typography styles
css.append("/* Typography Styles */")
for element, properties in typography['elements'].items():
    styles = []
    for prop, value in properties.items():
        if isinstance(value, dict):  # Handle nested properties (e.g., border)
            for sub_prop, sub_value in value.items():
                styles.append(f"{prop}-{sub_prop}: {sub_value};")
        else:
            styles.append(f"{prop}: {value};")
    css.append(f"{element} {{\n  " + "\n  ".join(styles) + "\n}}")

# Add color styles
css.append("\n/* Color Styles */")
for group, palette in colors['colors'].items():
    for color in palette:
        css.append(f".{group}-{color['name'].lower().replace(' ', '-')} {{\n  color: {color['hex']};\n}}")

# Write the CSS file
with open('assets/css/generated.css', 'w') as css_file:
    css_file.write("\n".join(css))