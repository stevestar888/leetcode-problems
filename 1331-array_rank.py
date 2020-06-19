"""
https://leetcode.com/problems/rank-transform-of-an-array/

Strat: First sort, then store rank in a dict, where the key is the value & rank is key.
    Make sure to watch out for duplicates (keep a `prev` variable for this).

Stats: O(n*lgn) time, O(n) space -- one loop to find rank, and another loop assign rank, but both are 
    overshadowed by the sort procedure + use a dict (or set + dict) as auxiliary DS
    
Optimization: 
    I don't think there is a linear solution because sort is the easiest way to find rank. Otherwise, 
    you would have to take linear time to find the right rank for an element--and do that n times. 
"""

class Solution(object):
    """
    OG solution
    
    Runtime: 352 ms, faster than 60.35% of Python online submissions for Rank Transform of an Array.
    Memory Usage: 30.7 MB, less than 96.67% of Python online submissions for Rank Transform of an Array.
    """
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # sort results
        sorted_arr = sorted(arr[:])
        
        # store appearance in dict
        order = {}
        prev = float('-inf')
        rank = 0
        
        for num in sorted_arr:
            if num != prev:
                rank += 1
            
            order[num] = rank
            prev = num
            
        # replace the OG num w/ its rank
        for i, num in enumerate(arr):
            arr[i] = order.get(num)
        
        return arr
    
    
    """
    Slight optimization to get of duplicates by using set()
    
    Runtime: 332 ms, faster than 88.99% of Python online submissions for Rank Transform of an Array.
    Memory Usage: 31.1 MB, less than 94.44% of Python online submissions for Rank Transform of an Array.
    """
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nums = sorted(set(arr))
        order = {}
        rank = 1
        
        for num in nums:
            order[num] = rank
            rank += 1
        
        for i, num in enumerate(arr):
            arr[i] = order.get(num)
        
        return arr
        # OR instead of loop + return:
        # return map(order.get, arr)