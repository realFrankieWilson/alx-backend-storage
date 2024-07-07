#!/usr/bin/env python3
"""
`Module exercise`
Provide a class for storing redis instance client as a
private variable.
"""

import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """A count call method that defines a decorator"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A method that returns a Callable"""
        key = f"{self.__class__.__qualname__}.{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    A class that with an __init__ method that store
    an instance of the Redis client as a private variable name
    """

    def __init__(self):
        """The init method with redis instance and flushdb"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """A method that takes in data argument and
        returns a string.
        """
        key = str(uuid.uuid4())
        if isinstance(data, str):
            self._redis.set(key, data.encode("utf-8"))
        else:
            self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable
                                         [[bytes], any]] = None) -> any:
        """A method that convert data back to desired format"""

        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> str:
        """Automatically parametrize Cache.get"""

        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Automatically parametrize Cache.get"""
        return self.get(key, int)
