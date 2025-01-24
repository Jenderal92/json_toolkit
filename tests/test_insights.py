# tests/test_insights.py
import unittest
from json_toolkit.core.analyzer import JSONAnalyzer

class TestJSONAnalyzer(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 30}
        ]
    
    def test_analyze_numeric_data(self):
        analyzer = JSONAnalyzer()
        stats = analyzer.analyze_numeric_data(self.data, "age")
        self.assertEqual(stats['mean'], 28.33, places=2)  # Test for mean

if __name__ == '__main__':
    unittest.main()
    