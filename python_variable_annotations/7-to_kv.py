#!/usr/bin/env python3
"""
Annotating
"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function takes a string and an int or float and returns a tuple
    """
    return (k, v ** 2)
