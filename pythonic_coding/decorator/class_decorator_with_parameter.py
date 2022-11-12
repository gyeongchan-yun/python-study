#!/usr/bin/python3

import time
from functools import wraps


class MeasureRuntime:

    def __init__(self, is_active):
        self.is_active = is_active

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            if not self.is_active:
                return func(*args, **kwargs)

            start = time.time()
            ret = func(*args, **kwargs)
            end = time.time()

            print("'%s' function running time: %s" % (func.__name__, end - start))
            return ret

        return wrapper


@MeasureRuntime(True)
def active_worker(delay_time):
    time.sleep(delay_time)


@MeasureRuntime(False)
def non_active_worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    non_active_worker(5)
    active_worker(5)
