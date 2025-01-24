# json_toolkit/json_toolkit/utils/validator.py
import json

class JSONValidator:
    @staticmethod
    def validate(json_data, schema):
        # Here you can integrate a schema validation library if needed
        return all(key in json_data for key in schema)
