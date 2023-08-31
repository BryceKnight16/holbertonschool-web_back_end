#!/usr/bin/env python3
"""
Module of the task_wait_n function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that uses task_wait_random n times asynchronously and returns
    the list of delays in ascending order.
    """
    delay_list = await asyncio.gather(*(task_wait_random(max_delay)
                                        for _ in range(n)))
    return sorted(delay_list)
