import sys
import yaml

def load_yaml(input_file):
    try:
        with open(input_file, "r") as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print("Błąd w składni pliku YAML:", str(e))
        sys.exit(1)
    except FileNotFoundError:
        print("Plik", input_file, "nie istnieje.")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == "yaml":
        data = load_yaml(input_file)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)
