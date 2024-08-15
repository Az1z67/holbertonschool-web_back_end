#!/usr/bin/env python3
"""
Annotating variables and function with complex types
"""

from typing import Sequence, Union, Any, TypeVar, List

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function takes a list of any type and returns its first element
    """
    if lst:
        return lst[0]
    else:
        return None
    