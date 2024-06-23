#!/usr/bin/env python3
"""
Module `101-students`
Provides a function that returns all students sorted by
average score
"""


def top_students(mongo_collection):
    """
    A function that returns all students soreted by
    Average score.
        Args:
            mongo_collection: pymongo collection objects.
        Returns:
            A sorted list of students
    """
    pipeline = [
        {"$project": {"name": 1, "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}},
    ]
    return list(mongo_collection.aggregate(pipeline))
