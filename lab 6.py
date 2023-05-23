import sys
import json
import yaml
import xml.etree.ElementTree as ET

# Task1
arguments = sys.argv[1:]
print("Parsowane argumenty:", arguments) 

# Task2:
json_file = "file.json"
try:
    with open(json_file, "r") as file:
        data = json.load(file)
    print("Wczytano plik JSON:", data)
except Exception as e:
    print("Nie udało się wczytać pliku:", e)

# Task3: 
output_file = "output.json"
try:
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    print("Plik JSON zapisany", output_file)
except Exception as e:
    print("Nie udało się zapisać pliku:", e)
    
# Task4:
yml_file = "file.yml"
try:
    with open(yml_file, "r") as file:
        data = yaml.safe_load(file)
    print("Wczytano plik YAML:", data)
except Exception as e:
    print("Nie udało się wczytać pliku:", e)

# Task5: 
output_file = "output.yml"
try:
    with open(output_file, "w") as file:
        yaml.dump(data, file)
    print("Plik YAML zapisany", output_file)
except Exception as e:
    print("Nie udało się zapisać pliku:", e)

# Task6: 
xml_file = "file.xml"
try:
    tree = xml_file.parse(xml_file)
    root = tree.getroot()
    print("Wczytano plik XML:")
    for child in root:
        print(child.tag, child.text)
except Exception as e:
    print("Nie udało się wczytać pliku:", e)