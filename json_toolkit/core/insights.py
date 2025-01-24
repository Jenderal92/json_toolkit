import statistics

class JSONInsights:

    def __init__(self, json_data):

        self.json_data = json_data

    def calculate_mean(self, key):
        
        values = [obj.get(key) for obj in self.json_data if isinstance(obj.get(key), (int, float))]
        return statistics.mean(values) if values else None

    def calculate_median(self, key):
        
        values = [obj.get(key) for obj in self.json_data if isinstance(obj.get(key), (int, float))]
        return statistics.median(values) if values else None

    def calculate_mode(self, key):
        
        values = [obj.get(key) for obj in self.json_data if isinstance(obj.get(key), (int, float))]
        return statistics.multimode(values) if values else []
