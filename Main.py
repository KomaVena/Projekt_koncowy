import sys
import json

def load_json(input_file):
    try:
        with open(input_file, "r") as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print("Błąd w składni pliku JSON:", str(e))
        sys.exit(1)
    except FileNotFoundError:
        print("Plik", input_file, "nie istnieje.")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == "json":
        data = load_json(input_file)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)
