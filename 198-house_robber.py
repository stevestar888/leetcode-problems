"""
https://leetcode.com/problems/house-robber/

Pretty fun problem, and definitely works the DP-mind. One really tricky thing 
is working out the bounds because you have to look at the previous, and sometimes 
the previous previous.

Strat: 
    Recursive with Memoization 
    Iterative with Memoization 
    Iterative with n variables (WIP)

Stats:
    All approaches run in linear time, and memoizing results can take you to
    linear space, too. You can even go down to constant space by using n=2
    variables to store prev & prev prev.
"""
class Solution(object):
    """
    Recursive--with memoization (from end to start)
    
    Stats: O(n) time, O(n) space 
        Runtime: 20 ms, faster than 67.86% of Python online submissions for House Robber.
        Memory Usage: 12.9 MB, less than 17.05% of Python online submissions for House Robber.
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        memo = [-1] * length
        
        def helper(i):
            if i < 0:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            rob = nums[i] + helper(i - 2)
            dont_rob = helper(i - 1)
            best = max(rob, dont_rob)
            
            memo[i] = best
            return best
        
        return helper(length - 1)
    
    
    """
    Recursive--with memoization (from start to end)
        (even though I didn't write this one first, this actually is more intuitive)
        
    Stats: O(n) time, O(n) space 
        Runtime: 24 ms, faster than 41.91% of Python online submissions for House Robber.
        Memory Usage: 12.9 MB, less than 5.72% of Python online submissions for House Robber.
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        memo = [-1] * length
        
        def helper(i):
            if i > length - 1:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            rob = nums[i] + helper(i + 2)
            dont_rob = helper(i + 1)
            best = max(rob, dont_rob)
            
            memo[i] = best
            return best
        
        return helper(0)
    
    
    """
    Iterative--with memoization
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        
        if length == 1:
            return nums[0]
        
        #initialize dp storage array
        dp = [0] * length
        
        #initialize first 2 entries so we don't have to worry 
        #about bounds checking when looping
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, length):
            take = nums[i] + dp[i - 2] #current + prev prev
            dont_take = dp[i - 1] #prev
            dp[i] = max(take, dont_take)
            
        #return last elem
        return dp[-1]
    
    
#     """
#     Doesn't work....
#
#     Iterative--with n variables
#     """
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         length = len(nums)
#         if length == 0:
#             return 0
        
#         if length == 1:
#             return nums[0]
        
#         prev_prev, prev = 0, max(nums[0], nums[1])
#         result = 0
        
#         for i in range(1, length):
#             take = nums[i] + prev_prev #same as: current + dp[i - 2]
#             dont_take = prev #same as: dp[i - 1]
#             result = max(take, dont_take) #same as: dp[i] = ...
            
#             prev_prev, prev = prev, nums[i]
#             print(result)
#         return result
