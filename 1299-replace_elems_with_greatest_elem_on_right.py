"""
Strat:
    Iterate through arr, from right to left, while keeping track 
    of the largest element we've seen. max_so_far starts out at -1, 
    because that's what the last elem's value will be. As we iterate,
    we compare to current num's value to max_so_far; update as appropiate. 

Stats: O(n) time
    Runtime: 112 ms, faster than 76.23% of Python online submissions for Replace Elements with Greatest Element on Right Side.
    Memory Usage: 14.3 MB, less than 21.28% of Python online submissions for Replace Elements with Greatest Element on Right Side.
"""
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        length = len(arr)
        max_so_far = -1
        result = [0] * length
        
        #iterate through arr, from right to left, one elem at a time
        for i in range(length - 1, -1, -1):
            #store max_so_far in results & update it
            result[i] = max_so_far
            max_so_far = max(max_so_far, arr[i])
            
        return result
