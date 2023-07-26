#!/usr/bin/env python3
""" LRU caching: inherits from BaseCaching and is a
caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache.
        Inherits all from BaseCache, only that it adds
        an entry at max capacity, and discards the least used entry
        to and a new one
        Methods:
            __init__ - initialises the class instance
            put - adds key/val pair
            get - retrieves value given the key in cache
    """

    def __init__(self):
        """initialise class instance"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """add key/val pair
        if at max capacity, discard least recentry used entry"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                disc = self.keys.pop(0)
                del self.cache_data[disc]
                print("DISCARD: {:s}".format(disc))

    def get(self, key):
        """return value stored in key of cache_data"""
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
