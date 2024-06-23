#!/usr/bin/env python3
"""
Module `10-update_topics`
Provides a function that changes all topics of a school
document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
        Args:
            mongo_collection: pymongo collection objects.
            name (String): the school name to update
            topics (List(String)): list of topics approached in
            school.
        Returns:
            None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
