#!/usr/bin/env python3
"""
Annotating
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Sequence[Iterable]) -> List[Tuple[Iterable, int]]:
    """
    Function takes a list of iterables
    """
    return [(i, len(i)) for i in lst]
