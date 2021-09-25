"""
https://leetcode.com/problems/n-th-tribonacci-number/
"""

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        storage = [None] * 38 # max of n is 37; so 38 to account for T_0
        storage[0] = 0
        storage[1] = 1
        storage[2] = 1
        
        for i in range(3, n + 1):
            storage[i] = storage[i - 1] + storage[i - 2] + storage[i - 3]
            
        return storage[n]
    
    
    # more readable
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        storage = [0, 1, 1]
        
        for i in range(3, n + 1):
            storage.append(storage[i - 1] + storage[i - 2] + storage[i - 3])
            
        return storage[n]
