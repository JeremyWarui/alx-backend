#!/usr/bin/env python3
""" FIFO caching: inherits from BaseCaching and is a
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache.
        Inherits all from BaseCache, only that it adds
        an entry at max capacity, and discards the latest
        entry to add the new one
        Methods:
            __init__ - initialises the class instance
            put - adds key/val pair
            get - retrieves value given the key in cache
    """

    def __init__(self):
        """initialise instance"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """add key/val pair until max capacity reached
        add new pair by removing the latest/newest entry"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print("DISCARD: {:s}".format(discard))

    def get(self, key):
        """returrn value of key in stored data"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
