#!/usr/bin/env python3
"""
Annotating
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function takes a float multiplier
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
