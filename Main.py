import sys
import xml.etree.ElementTree as ET

def save_xml(output_file, root):
    try:
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding="utf-8", xml_declaration=True)
    except:
        print("Błąd podczas zapisu pliku XML.")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == "xml":
        root = load_xml(input_file)
        save_xml(output_file, root)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)
