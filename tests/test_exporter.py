# tests/test_exporter.py
import unittest
import tempfile
import json
from json_toolkit.core.exporter import JSONExporter

class TestJSONExporter(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25}
        ]
    
    def test_export_to_json(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            exporter = JSONExporter(self.data)
            exporter.export_to_json(tmpfile.name)
            tmpfile.seek(0)
            content = json.load(tmpfile)
            self.assertEqual(len(content), 2)  # Check if 2 records were exported
    
    def test_export_to_csv(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            exporter = JSONExporter(self.data)
            exporter.export_to_csv(tmpfile.name)
            tmpfile.seek(0)
            content = tmpfile.read().decode()
            self.assertIn("name,age", content)  # Check if CSV contains header

if __name__ == '__main__':
    unittest.main()
