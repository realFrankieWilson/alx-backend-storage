#!/usr/bin/env python3
"""
Module `8-all`
Provides a function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    Lists all collection in mongo collection
    Or return an empty lists
    """
    return mongo_collection.find()
