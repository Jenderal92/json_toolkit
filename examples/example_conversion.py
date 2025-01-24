# examples/example_conversion.py
from json_toolkit import JSONConverter

def convert_json_to_csv(json_data, output_file):
    JSONConverter.json_to_csv(json_data, output_file)

def convert_json_to_xml(json_data, root_tag):
    xml_data = JSONConverter.json_to_xml(json_data, root_tag)
    print(xml_data)

# Sample JSON data
json_data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

convert_json_to_csv(json_data, 'output.csv')
convert_json_to_xml(json_data, 'people')
