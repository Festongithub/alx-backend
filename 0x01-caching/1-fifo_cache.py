#!/usr/bin/env python3

"""Implement FIFO  on a dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching and
    is a caching system
    """
    def __init__(self):
        """class initialization"""
        super().__init__()

    def put(self, key, item):
        """Assign the item value to the key in self.cache_data"""
        if key is None or item is None:
            pass
        else:
            if key not in self.cache_data \
            and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """Return the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
