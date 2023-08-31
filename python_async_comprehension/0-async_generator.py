#!/usr/bin/env python3
"""
Module of a coroutine that takes no arguments
and generates a random number from 0 to 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    fucntion that gives a random float between 0 and 10
    asynchronously, 10 times.
    """
    for _ in range(10):
        random_num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_num
