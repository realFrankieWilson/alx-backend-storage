#!/usr/bin/env python3
"""
`Module exercise`
Provide a class for storing redis instance client as a
private variable.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    A class that with an __init__ method that store
    an instance of the Redis client as a private variable name
    """

    def __init__(self):
        """The init method with redis instance and flushdb"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """A method that takes in data argument and
        returns a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
