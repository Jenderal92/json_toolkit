# json_toolkit/json_toolkit/core/streamer.py
import json

class JSONStreamer:
    def __init__(self, file_path):
        self.file_path = file_path

    def stream(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                yield json.loads(line)
