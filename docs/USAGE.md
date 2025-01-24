# docs/USAGE.md

Detailed usage guide for the features.

# Usage Guide

## JSON Streaming
```python
from json_toolkit import JSONStreamer

streamer = JSONStreamer("large_data.json")
for item in streamer.stream():
    print(item)
```

## Filtering Data
```python
from json_toolkit import JSONFilter

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
filter_obj = JSONFilter(data)
filtered = filter_obj.filter_by_value("age", 30)
print(filtered)
```