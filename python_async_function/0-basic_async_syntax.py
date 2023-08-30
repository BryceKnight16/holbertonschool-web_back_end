#!/usr/bin/python3
"""
A module that has a coroutine async in it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    function that waits a random amout of time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
