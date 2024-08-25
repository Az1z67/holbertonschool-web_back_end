#!/usr/bin/env python3
""" List documents """
import pymongo


def list_all(mongo_collection) -> list:
    """ List documents
    """
    documents: list = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
