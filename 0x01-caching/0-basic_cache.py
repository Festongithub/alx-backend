#!/usr/bin/env python3

"""class BasicCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache"""
    def __init__(self):
        """super init"""
        super().__init__()

    def put(self, key, item):
        """Assign the item value to the key in self.cache_data"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to the key in self.cache_data"""
        if key is None not in self.cache_data.keys():
            return None
        return self.cache_data.get(key, None)
