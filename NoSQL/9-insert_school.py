#!/usr/bin/env python3
"""
Insert
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert
    """
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
