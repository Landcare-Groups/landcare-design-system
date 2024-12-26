import yaml

def validate_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
            print(f"{file_path} is valid YAML!")
    except yaml.YAMLError as exc:
        print(f"Error in {file_path}: {exc}")

# Specify the file(s) to validate
files_to_validate = [
    "styles/typography.yml",
    "styles/colors.yml"
]

for file in files_to_validate:
    validate_yaml(file)