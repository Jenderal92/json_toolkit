# tests/test_converter.py
import unittest
import tempfile
from json_toolkit.core.converter import JSONConverter

class TestJSONConverter(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]
    
    def test_json_to_csv(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            JSONConverter.json_to_csv(self.data, tmpfile.name)
            tmpfile.seek(0)
            content = tmpfile.read().decode()
            self.assertIn("name,age", content)  # Check if CSV contains header
    
    def test_json_to_xml(self):
        xml_data = JSONConverter.json_to_xml(self.data, "people")
        self.assertIn(b"<name>Alice</name>", xml_data)  # Check if XML contains the name Alice

if __name__ == '__main__':
    unittest.main()
