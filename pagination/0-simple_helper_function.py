#!/usr/bin/env python3
"""perform pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """perform pagination"""
    return ((page - 1) * page_size, page * page_size)
