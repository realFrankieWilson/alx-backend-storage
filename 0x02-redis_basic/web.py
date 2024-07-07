#!/usr/bin/env python3
"""
`Module web`
Provides a function to fetch web pages and cache the result
"""

import redis
import urllib.request
from functools import wraps
from typing import Callable


r = redis.Redis()


def count_cache(func: Callable[[str], str]) -> Callable[
    [
        str,
    ],
    str,
]:
    """
    A decorator that counts the number of times a url is accessd
    Then caches the result for 10 sec."""

    @wraps(func)
    def wrapper(url: str) -> str:
        """
        A Wrapper function that checks the cache,
        increaments the count, and returns the cached or
        fetched content"""
        cached_key = f"count:{url}"
        content = r.get(url)
        if content:
            r.incr(cached_key)
            return content.decode("utf-8")

        content = func(url)
        r.setex(url, 10, content.encode("utf-8"))
        r.incr(cached_key)
        return content

    return wrapper


def get_page(url: str) -> str:
    """Fetches the HTML content of a given URL using the
    urllib.request module"""
    with urllib.request.urlopen(url) as res:
        return res.read().decode("utf-8")
