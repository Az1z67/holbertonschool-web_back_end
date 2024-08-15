#!/usr/bin/env python3
'''
Module Doc
'''
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Function takes a dictionary, key and default value and returns the value
    """
    if key in dct:
        return dct[key]
    else:
        return default
