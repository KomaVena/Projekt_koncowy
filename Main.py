import sys
import yaml

def save_yaml(output_file, data):
    try:
        with open(output_file, "w") as file:
            yaml.dump(data, file, default_flow_style=False)
    except:
        print("Błąd podczas zapisu pliku YAML.")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == "yaml":
        data = load_yaml(input_file)
        save_yaml(output_file, data)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)
