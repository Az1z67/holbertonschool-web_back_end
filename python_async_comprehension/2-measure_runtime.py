#!/usr/bin/env python3
"""Async Comprehension"""

import asyncio
import time
async_generator = __import__('0-async_generator').async_generator


async def measure_runtime() -> float:
    """
    Measure Runtime
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4))) # type: ignore
    end = time.time()
    return end - start
