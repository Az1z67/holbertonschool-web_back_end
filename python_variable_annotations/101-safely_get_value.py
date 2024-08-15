#!/usr/bin/env python3
"""
Annotating
"""
from typing import Union, Any, TypeVar


def safely_get_value(dct: dict, key: Any, default: Union[TypeVar('T'), None] = None) -> Union[Any, TypeVar('T')]:
    """
    Function takes a dictionary, key and default value and returns the value
    """
    if key in dct:
        return dct[key]
    else:
        return default


#!/usr/bin/env python3
'''
Module Doc
'''
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Function takes a dictionary, key and default value and returns the value
    """
    if key in dct:
        return dct[key]
    else:
        return default
