#!/usr/bin/env python3
"""
A module that uses corooutine to measure the runtime of
async_comp 4 times in parrallel using gather
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel.
    """
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
