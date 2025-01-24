# json_toolkit/json_toolkit/core/converter.py
import csv
import xml.etree.ElementTree as ET

class JSONConverter:
    @staticmethod
    def json_to_csv(json_data, output_file):
        keys = json_data[0].keys()
        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(json_data)
    
    @staticmethod
    def json_to_xml(json_data, root_tag):
        root = ET.Element(root_tag)
        for item in json_data:
            item_element = ET.SubElement(root, "item")
            for key, value in item.items():
                sub_element = ET.SubElement(item_element, key)
                sub_element.text = str(value)
        return ET.tostring(root, encoding='utf-8')
