import sys
import xml.etree.ElementTree as ET

def load_xml(input_file):
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print("Błąd w składni pliku XML:", str(e))
        sys.exit(1)
    except FileNotFoundError:
        print("Plik", input_file, "nie istnieje.")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == "xml":
        root = load_xml(input_file)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)
