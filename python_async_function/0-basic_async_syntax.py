#!/usr/bin/env python3
"""
Asynchronus function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async function
    """
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
