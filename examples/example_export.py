# examples/example_export.py
from json_toolkit import JSONExporter

def export_json_to_file(json_data):
    exporter = JSONExporter(json_data)
    exporter.export_to_json('exported_data.json')
    exporter.export_to_csv('exported_data.csv')

if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]
    export_json_to_file(data)
