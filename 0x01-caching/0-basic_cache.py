#!/usr/bin/env python3
""" Basic dict: inherits from BaseCaching and is a
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic cache that inherits from BaseCaching
    put- adds key/value pair
    get - gets key/value pair"""

    def put(self, key, item):
        """add key/value pair to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return value of key given from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
