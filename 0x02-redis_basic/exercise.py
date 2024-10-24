#!/usr/bin/env python3
"""
This scripts create a class Cache
"""

import redis
import uuid


class Cache():
    def __init__(self) -> None:
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
