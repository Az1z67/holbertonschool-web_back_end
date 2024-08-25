#!/usr/bin/env python3
"""
All Docs
"""
import pymongo


def list_all(mongo_collection):
    """
    All Docs
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
