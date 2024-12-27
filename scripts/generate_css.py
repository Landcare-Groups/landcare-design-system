import yaml

# Load YAML files
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Generate CSS
def generate_css():
    # Load typography and colors
    typography = load_yaml('styles/typography.yml')
    colors = load_yaml('styles/colors.yml')

    css = []

    # Add typography styles
    css.append("/* Typography Styles */")
    css.append("/* Print documents, Word templates, InDesign templates */")
    css.append("@font-face {")
    css.append("  font-family: 'Sari';")
    css.append("  src: local('Sari'), local('Open Sans, Arial, sans-serif');")
    css.append("}")
    css.append("/* Websites, digital platforms */")
    css.append("@font-face {")
    css.append("  font-family: 'Open Sans';")
    css.append("  src: local('Open Sans'), local('Arial, sans-serif');")
    css.append("}")

    # Add font sizes for headings, body, and other text
    sizes = typography['typography']['sizes']
    for heading, size in sizes['headings'].items():
        css.append(f"{heading} {{ font-size: {size}; }}")
    css.append(f"body {{ font-size: {sizes['body']}; }}")
    css.append(f".small_text {{ font-size: {sizes['small_text']}; }}")
    css.append(f".list_text {{ font-size: {sizes['list_text']}; }}")
    css.append(f".captions {{ font-size: {sizes['captions']}; }}")
    css.append(f".footnotes {{ font-size: {sizes['footnotes']}; }}")

    # Add typography elements
    elements = typography['typography']['elements']
    css.append("\n/* Typography Elements */")
    css.append("hr {")
    css.append(f"  border-top: {elements['horizontal_rule']['thickness']} {elements['horizontal_rule']['style']} {elements['horizontal_rule']['color']};")
    css.append(f"  margin-top: {elements['horizontal_rule']['margin_top']};")
    css.append(f"  margin-bottom: {elements['horizontal_rule']['margin_bottom']};")
    css.append("}")
    css.append("blockquote {")
    css.append(f"  font-size: {elements['block_quotes']['font_size']};")
    css.append(f"  font-style: {elements['block_quotes']['font_style']};")
    css.append(f"  margin-left: {elements['block_quotes']['indentation']};")
    css.append(f"  border-left: {elements['block_quotes']['border_left']['thickness']} solid {elements['block_quotes']['border_left']['color']};")
    css.append("}")
    css.append("ul { list-style-type: disc; margin-left: 1.5rem; }")
    css.append("ol { list-style-type: decimal; margin-left: 1.5rem; }")

    # Add alignment styles
    css.append("\n/* Alignment Styles */")
    alignment = typography['typography']['alignment']
    css.append(f"body {{ text-align: {alignment['body']}; }}")
    css.append(f"h1, h2, h3, h4, h5, h6 {{ text-align: {alignment['headings']}; }}")
    css.append(f"ul, ol {{ text-align: {alignment['lists']}; }}")
    css.append(f"blockquote {{ text-align: {alignment['quotes']}; }}")

    # Add grid styles
    css.append("\n/* Grid Styles */")
    grid = typography['typography']['grid']
    css.append(".grid {")
    css.append("  display: grid;")
    css.append(f"  grid-template-columns: repeat({grid['columns']}, 1fr);")
    css.append(f"  gap: {grid['gutter']};")
    css.append("}")
    css.append(f".grid-margin-web {{ margin: {grid['margins']['web']}; }}")
    css.append(f".grid-margin-print {{ margin: {grid['margins']['print']}; }}")

    # Add colors
    css.append("\n/* Color Styles */")
    for group, palettes in colors['colors'].items():
        for palette_type, color_list in palettes.items():
            for color in color_list:
                css.append(f".{group}-{palette_type}-{color['name'].lower().replace(' ', '-')} {{")
                css.append(f"  color: {color['hex']};")
                css.append("}")

    # Write the CSS file
    with open('assets/css/generated.css', 'w') as css_file:
        css_file.write("\n".join(css))

# Run the script
if __name__ == "__main__":
    generate_css()