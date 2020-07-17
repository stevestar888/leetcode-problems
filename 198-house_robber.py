class Solution(object):
    """
    Recursive--with memoization
    
    Stats:
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
    
    
