import os
import yaml

# Load typography YAML
def load_typography_yaml():
    try:
        with open("styles/typography.yml", "r") as file:
            data = yaml.safe_load(file)
            if not data:
                raise ValueError("Typography YAML is empty or invalid.")
            return data.get("typography", {})
    except FileNotFoundError:
        print("Error: typography.yml file not found.")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Generate CSS content
def generate_typography_css(typography_data):
    css = []

    # Fonts
    fonts = typography_data.get("fonts", {})
    if "primary" in fonts:
        primary = fonts["primary"]
        css.append(f"@font-face {{\n  font-family: '{primary['name']}';\n  src: local('{primary['fallback']}');\n}}")
    if "web_primary" in fonts:
        web_primary = fonts["web_primary"]
        css.append(f"@font-face {{\n  font-family: '{web_primary['name']}';\n  src: local('{web_primary['fallback']}');\n}}")

    # Headings
    sizes = typography_data.get("sizes", {})
    headings = sizes.get("headings", {})
    line_spacing = typography_data.get("line_spacing", {})
    if headings:
        for heading, size in headings.items():
            css.append(f"{heading} {{\n  font-size: {size};\n  line-height: {line_spacing.get('headings', '1.2')};\n}}")

    # Body text
    body_size = sizes.get("body", None)
    body_line_spacing = line_spacing.get("body", None)
    if body_size and body_line_spacing:
        css.append(f"body {{\n  font-size: {body_size};\n  line-height: {body_line_spacing};\n}}")

    # Lists
    list_line_spacing = line_spacing.get("lists", None)
    if list_line_spacing:
        css.append(f"ul, ol {{\n  line-height: {list_line_spacing};\n}}")
        css.append(f"li {{\n  margin-bottom: {typography_data['padding']['between_paragraphs']};\n}}")

    # Captions
    captions_size = sizes.get("captions", None)
    captions_line_spacing = line_spacing.get("captions", None)
    if captions_size and captions_line_spacing:
        css.append(f"caption {{\n  font-size: {captions_size};\n  line-height: {captions_line_spacing};\n}}")

    return "\n".join(css)

# Write CSS to file
def write_css_to_file(css_content, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(css_content)

# Main function
def main():
    typography_data = load_typography_yaml()
    if not typography_data:
        print("No typography data to process.")
        return

    # Generate CSS
    css_content = generate_typography_css(typography_data)

    # Define paths
    root_css_path = "assets/css/typography.css"
    docs_css_path = "docs/assets/css/typography.css"

    # Write CSS to both locations
    write_css_to_file(css_content, root_css_path)
    write_css_to_file(css_content, docs_css_path)

    print(f"CSS files successfully generated:\n- {root_css_path}\n- {docs_css_path}")

if __name__ == "__main__":
    main()