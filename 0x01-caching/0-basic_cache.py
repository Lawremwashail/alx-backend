#!/usr/bin/python3

'''
Task 0: Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    A class that inherits from BaseCaching
    and is a caching system
    '''

    def put(self, key, item):
        '''
        Assigns an item to the dictionary`
        '''
        if key is None and item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Retrieves an item linked to `key`
        '''

        return self.cache_data.get(key, None)
