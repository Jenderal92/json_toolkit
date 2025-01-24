# json_toolkit/json_toolkit/core/exporter.py
import json
import csv

class JSONExporter:
    def __init__(self, data):
        self.data = data

    def export_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.data, file, indent=4)
    
    def export_to_csv(self, file_path):
        keys = self.data[0].keys()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.data)
