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