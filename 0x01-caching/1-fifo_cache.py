#!/usr/bin/env python3
""" FIFO caching: inherits from BaseCaching and is a
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache.
    Inherits from BaseCaching but add an entry to cache when
    its max capacity is specified by MAX_ITEMS. Discards the
    oldest entry to accomodate the new
    Has _init__ - to instanciate the class
    put - to add the key/val pair
    get - get the key/value pair
    """

    def __init__(self):
        """initialise class instance"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """add key/value to cache
        if at max capacity, remove oldest/first entry
        and add new entry"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {:s}".format(discard))

    def get(self, key):
        """return value stored in key of cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
