"""
Brute force

Related: 
https://leetcode.com/problems/design-hashset/


Stats:
    Runtime: 448 ms, faster than 35.86% of Python online submissions for Design HashMap.
    Memory Usage: 37.3 MB, less than 14.08% of Python online submissions for Design HashMap.
    
    1,000,000 % 500,000
    900th 
    
    arr = int[100]
    
    9 % 17 -> 9
    101 % 17 -> 16
    26 % 17 -> 9 ??
    
    optimal load factor*: 50% - 75%
    
    x * 0.75 ≈ 3000
    
*https://stackoverflow.com/questions/10901752/what-is-the-significance-of-load-factor-in-hashmap
    
"""
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        MAX_CAPACITY = 1000000
        self.hashmap = [-1] * MAX_CAPACITY

    def put(self, key, value):
        """
        Insert a value at the specified key. Value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.hashmap[key]
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.hashmap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
