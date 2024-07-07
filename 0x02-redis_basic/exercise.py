#!/usr/bin/env python3
'''Redis data management example.
'''
import redis
import uuid
from typing import Any, Callable, Union
from functools import wraps


def track_calls(method: Callable) -> Callable:
    '''Decorator to track the number of calls to a method.
    '''
    @wraps(method)
    def wrapped(self, *args, **kwargs) -> Any:
        '''Increment call count each time the method is invoked.'''
        self._redis.incr(method.__name__)
        return method(self, *args, **kwargs)
    return wrapped


def log_history(method: Callable) -> Callable:
    '''Decorator to log the call history of a method.
    '''
    @wraps(method)
    def wrapped(self, *args, **kwargs) -> Any:
        '''Log input and output of each method call.'''
        input_key = '{}:inputs'.format(method.__name__)
        output_key = '{}:outputs'.format(method.__name__)
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapped


def show_history(func: Callable) -> None:
    '''Function to print the call history of a method.
    '''
    storage = redis.Redis()
    input_key = '{}:inputs'.format(func.__name__)
    output_key = '{}:outputs'.format(func.__name__)
    inputs = storage.lrange(input_key, 0, -1)
    outputs = storage.lrange(output_key, 0, -1)
    history = [(i.decode("utf-8"), o.decode("utf-8")) for i, o in zip(inputs, outputs)]
    print('{} was called {} times:'.format(func.__name__, len(history)))
    for inp, out in history:
        print('{}(*{}) -> {}'.format(func.__name__, inp, out))


class DataCache:
    '''Class to handle caching of data in Redis.
    '''
    def __init__(self) -> None:
        '''Initialize Redis connection and clear database.'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @log_history
    @track_calls
    def save(self, item: Union[str, bytes, int, float]) -> str:
        '''Save an item in Redis under a unique key and return the key.'''
        unique_key = str(uuid.uuid4())
        self._redis.set(unique_key, item)
        return unique_key

    def retrieve(
            self,
            key: str,
            converter: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieve and convert data from Redis.'''
        data = self._redis.get(key)
        if converter:
            data = converter(data)
        return data

    def retrieve_str(self, key: str) -> str:
        '''Convert retrieved Redis data to string.'''
        return self.retrieve(key, lambda x: x.decode('utf-8'))

    def retrieve_int(self, key: str) -> int:
        '''Convert retrieved Redis data to integer.'''
        return self.retrieve(key, lambda x: int(x))
