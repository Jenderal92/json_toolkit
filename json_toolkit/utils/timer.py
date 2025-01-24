# json_toolkit/json_toolkit/utils/timer.py
import time

class JSONTimer:
    @staticmethod
    def time_function(func):
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time
