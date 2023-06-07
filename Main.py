import sys
import json
import yaml
import xml.etree.ElementTree as ET
from threading import Thread

def load_json_async(input_file):
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

    data = None
    thread = Thread(target=lambda: load_json(input_file))
    thread.start()
    thread.join()
    return data

def save_json_async(output_file, data):
    def save_json(output_file, data):
        try:
            with open(output_file, "w") as file:
                json.dump(data, file, indent=4)
        except:
            print("Błąd podczas zapisu pliku JSON.")
            sys.exit(1)

    thread = Thread(target=lambda: save_json(output_file, data))
    thread.start()

def load_yaml_async(input_file):
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

    data = None
    thread = Thread(target=lambda: load_yaml(input_file))
    thread.start()
    thread.join()
    return data

def save_yaml_async(output_file, data):
    def save_yaml(output_file, data):
        try:
            with open(output_file, "w") as file:
                yaml.dump(data, file, default_flow_style=False)
        except:
            print("Błąd podczas zapisu pliku YAML.")
            sys.exit(1)

    thread = Thread(target=lambda: save_yaml(output_file, data))
    thread.start()

def load_xml_async(input_file):
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

    root = None
    thread = Thread(target=lambda: load_xml(input_file))
    thread.start()
    thread.join()
    return root

def save_xml_async(output_file, root):
    def save_xml(output_file, root):
        try:
            tree = ET.ElementTree(root)
            tree.write(output_file, encoding="utf-8", xml_declaration=True)
        except:
            print("Błąd podczas zapisu pliku XML.")
            sys.exit(1)

    thread = Thread(target=lambda: save_xml(output_file, root))
    thread.start()

if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == "json":
        data = load_json_async(input_file)
    elif input_format == "yaml":
        data = load_yaml_async(input_file)
    elif input_format == "xml":
        root = load_xml_async(input_file)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)

    if output_format == "json":
        save_json_async(output_file, data)
    elif output_format == "yaml":
        save_yaml_async(output_file, data)
    elif output_format == "xml":
        save_xml_async(output_file, root)
    else:
        print("Nieobsługiwany format pliku wyjściowego.")
        sys.exit(1)

        
