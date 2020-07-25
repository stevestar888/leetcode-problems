"""
https://leetcode.com/problems/lru-cache/submissions/

Strat:
    Will use an array as the DS for this, storing nested arrays of 
    [key, value, last_used_time].
    
Stats: O(n) time for get, O(n) time for put where n is capacity of cache -- every lookup 
        needs to iterate completely through the array at worst
    (really bad time but good memory usage)
    Runtime: 4352 ms, faster than 5.01% of Python online submissions for LRU Cache.
    Memory Usage: 21.8 MB, less than 93.54% of Python online submissions for LRU Cache.

"""
class LRUCache(object):
    #constants
    KEY_INDEX = 0
    VALUE_INDEX = 1
    LAST_USED_INDEX = 2
    
    #make constants global
    global KEY_INDEX
    global VALUE_INDEX
    global LAST_USED_INDEX
    
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = []
        self.space_left = capacity
        self.timer = 0
        
        
    def increment_time(self):
        """
        Helper method used to keep track of time. Every time it's called, will
        increment the timer and return the new value.
        """
        self.timer += 1
        return self.timer
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i, data in enumerate(self.cache):
            found_key = data[KEY_INDEX]
            found_value = data[VALUE_INDEX]
            if found_key == key:
                self.cache[i][LAST_USED_INDEX] = self.increment_time()
                return found_value
        
        #did not find requested key, so return -1
        return -1
        
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #check if the key already exists
        for i, data in enumerate(self.cache):
            found_key = data[KEY_INDEX]
            if found_key == key:
                self.insert(key, value, i)
                return
        
        #populate our array if it's not already full
        if self.space_left > 0:
            #decrease empty space left
            self.space_left -= 1
            
            #make our data tuple & insert into cache
            data = [0] * 3
            data[KEY_INDEX] = key
            data[VALUE_INDEX] = value
            data[LAST_USED_INDEX] = self.increment_time()
            self.cache.append(data)
            return
        
        #when our array is fully populated, find the tuple to evict
        last_used_index, last_used_timer = 0, float('inf')
        for i, data in enumerate(self.cache):
            found_timer = data[LAST_USED_INDEX]
            
            if found_timer < last_used_timer:
                last_used_index = i
                last_used_timer = found_timer
        
        #we know to invalidate the data at index last_used_index        
        self.insert(key, value, last_used_index)
        
        
    def insert(self, key, value, i):
        """
        Helper method used by put. Given the index i, will insert key, value, and time
        at that particular index.
        """
        data = [0] * 3
        data[KEY_INDEX] = key
        data[VALUE_INDEX] = value
        data[LAST_USED_INDEX] = self.increment_time()
        self.cache[i] = data
