#!/usr/bin/env python3
"""
A module that  measures time of wait function
"""
import time
import asyncio
from typing import Callable


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total time for wait_n(n, max_delay) and returns
    total_time divived by n.
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time_per_execution = total_time / n
    return average_time_per_execution
