#!/usr/bin/env python3
"""
Module `11-schools_by_topic`
Provides a function that returns the list of school
having a specific topic
"""


def schools_by_topic(mongo_collection, topics):
    """
    A function that returns the list of school having
    with a specific topic.
        Args:
            mongo_collection: pymongo collection objects.
            topics (String): Topics searched.
        Returns:
            Lists of schools with the topic.
    """
    if isinstance(topics, str):
        topics = [topics]
    schools = mongo_collection.find({"topics": {"$in": topics}})
    return [school for school in schools]
