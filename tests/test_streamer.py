# tests/test_streamer.py
import unittest
from json_toolkit.core.streamer import JSONStreamer

class TestJSONStreamer(unittest.TestCase):
    def test_stream(self):
        streamer = JSONStreamer('test_data.json')
        data = list(streamer.stream())
        self.assertGreater(len(data), 0)  # Ensure data is streamed

if __name__ == '__main__':
    unittest.main()
