import sys
import json

def save_json(output_file, data):
    try:
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
    except:
        print("Błąd podczas zapisu pliku JSON.")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == "json":
        data = load_json(input_file)
        save_json(output_file, data)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)

