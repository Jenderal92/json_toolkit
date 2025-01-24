# json_toolkit/json_toolkit/core/filter.py
class JSONFilter:
    def __init__(self, data):
        self.data = data

    def filter_by_key(self, key):
        return [item for item in self.data if key in item]
    
    def filter_by_value(self, key, value):
        return [item for item in self.data if item.get(key) == value]
