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


def call_history(method: Callable) -> Callable:
    """A decorator that stores the history of inputs and outputs for a function"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A method that returns a Callable"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output

    return wrapper


class Cache:
    """
    A class that with an __init__ method that store
    an instance of the Redis client as a private variable name
    """

    def __init__(self) -> None:
        """The init method with redis instance and flushdb"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """A method that takes in data argument and
        returns a string.
        """
        key = str(uuid.uuid4())
        if isinstance(data, str):
            self._redis.set(key, data.encode("utf-8"))
        else:
            self._redis.set(key, str(data).encode("utf-8"))
        return key

    def get(self, key: str) -> Optional[bytes]:
        """A method that convert data back to desired format"""

        return self._redis.get(key)

