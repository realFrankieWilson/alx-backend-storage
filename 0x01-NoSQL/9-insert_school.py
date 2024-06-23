#!/usr/bin/env python3
"""
Module `9-insert_school`
Provides a function that inserts a new documents in a collection.
Based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
        Args:
            mongo_collection -> pymongo collection objects.
            Kwargs -> The data to be inserted.
        Returns:
            The new _id
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
