# tests/test_utils.py
import unittest
from json_toolkit.utils.validator import JSONValidator
from json_toolkit.utils.timer import JSONTimer

class TestJSONUtils(unittest.TestCase):
    def test_validate(self):
        validator = JSONValidator()
        valid = validator.validate({"name": "Alice", "age": 30}, ["name", "age"])
        self.assertTrue(valid)  # Should be valid
        
    def test_timer(self):
        def dummy_func():
            pass
        timer = JSONTimer()
        duration = timer.time_function(dummy_func)
        self.assertLess(duration, 1)  # Ensure the dummy function runs in less than 1 second

if __name__ == '__main__':
    unittest.main()
