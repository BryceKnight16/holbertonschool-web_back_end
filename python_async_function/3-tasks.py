#!/usr/bin/env python3
"""
A module of the task_wait_random function
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Fucntion that returns an asyncio.Task for
    wait_random with the given max_delay.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
