# examples/example_large_json.py
from json_toolkit import JSONStreamer

def process_large_json(file_path):
    streamer = JSONStreamer(file_path)
    for item in streamer.stream():
        print(item)

# Call the function with a large JSON file
process_large_json('large_data.json')
