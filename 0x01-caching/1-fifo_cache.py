#!/usr/bin/python3

'''
FIFO caching
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    Class FIFOCache that inherits from BaseCaching and is a caching system
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        Dictionary with the item self.cache_data and key key
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''
        Returns value in self.cache_data linked to key.
        '''
        return self.cache_data.get(key, None)
