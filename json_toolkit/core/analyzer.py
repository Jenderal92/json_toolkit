# json_toolkit/json_toolkit/core/analyzer.py
import statistics

class JSONAnalyzer:
    @staticmethod
    def analyze_numeric_data(json_data, key):
        values = [item[key] for item in json_data if isinstance(item[key], (int, float))]
        return {
            'mean': statistics.mean(values),
            'median': statistics.median(values),
            'stdev': statistics.stdev(values)
        }
        