# examples/example_analysis.py
from json_toolkit import JSONAnalyzer

def analyze_data(json_data):
    analyzer = JSONAnalyzer()
    stats = analyzer.analyze_numeric_data(json_data, 'age')
    print("Statistics:", stats)

if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 30}
    ]
    analyze_data(data)
