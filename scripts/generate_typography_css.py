import yaml

# Load the typography.yml file
with open("styles/typography.yml", "r") as file:
    typography = yaml.safe_load(file)

# Prepare the CSS content for typography
css_typography = []

# Generate font styles
if "fonts" in typography["typography"]:
    fonts = typography["typography"]["fonts"]
    primary_font = fonts.get("primary", {})
    web_font = fonts.get("web_primary", {})

    if primary_font:
        css_typography.append(f"@font-face {{\n  font-family: '{primary_font['name']}';\n  src: local('{primary_font['fallback']}');\n}}")

    if web_font:
        css_typography.append(f"@font-face {{\n  font-family: '{web_font['name']}';\n  src: local('{web_font['fallback']}');\n}}")

# Generate styles for font sizes and headings
if "sizes" in typography["typography"]:
    sizes = typography["typography"]["sizes"]
    headings = sizes.get("headings", {})

    for heading, size in headings.items():
        css_typography.append(f"h{heading[-1]} {{\n  font-size: {size};\n}}")

    body_size = sizes.get("body", None)
    if body_size:
        css_typography.append(f"body {{\n  font-size: {body_size};\n}}")

# Generate line-spacing
if "line_spacing" in typography["typography"]:
    line_spacing = typography["typography"]["line_spacing"]
    for element, spacing in line_spacing.items():
        css_typography.append(f"{element} {{\n  line-height: {spacing};\n}}")

# Write to typography.css
with open("assets/css/typography.css", "w") as file:
    file.write("\n".join(css_typography))

print("Typography CSS successfully generated.")