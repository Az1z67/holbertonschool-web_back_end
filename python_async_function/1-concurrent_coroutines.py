#!/usr/bin/env python3
"""
Asynchronus function
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronus function
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
