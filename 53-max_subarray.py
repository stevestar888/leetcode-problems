"""
https://leetcode.com/problems/maximum-subarray/

Strat: 
    Use DP:
    [-2,1,-3,4,-1,2,1,-5,4] <-- nums
    [-2,1,-2,4, 3,5,6, 1,5] <-- stores the max subarray ending at index i
    
Stats:
    O(n) time, O(n) space, but space can go to O(1) using DP with n vars
    
Very clear Divide & Conquer: https://leetcode.com/problems/maximum-subarray/discuss/578388/Divide-and-Conquer.
"""
class Solution(object):
    """
    O(n) time, O(n) space -- one pass thru nums and one pass thru dp + store the dp results in an array

    This becomes clear when you see an example:
    input: [-2,1,-3,4,-1,2,1,-5,4]

    output:
    [-2, 0, 0, 0, 0, 0, 0, 0, 0]
    [-2, 1, 0, 0, 0, 0, 0, 0, 0]
    [-2, 1, -2, 0, 0, 0, 0, 0, 0]
    [-2, 1, -2, 4, 0, 0, 0, 0, 0]
    [-2, 1, -2, 4, 3, 0, 0, 0, 0]
    [-2, 1, -2, 4, 3, 5, 0, 0, 0]
    [-2, 1, -2, 4, 3, 5, 6, 0, 0]
    [-2, 1, -2, 4, 3, 5, 6, 1, 0]
    [-2, 1, -2, 4, 3, 5, 6, 1, 5]

    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        
        dp = [0] * length 
        dp[0] = nums[0] 
        
        for i in range(1, length):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            
        return max(dp)
    
    """
    O(n) time, O(1) space -- no storing the dp results in an array, just keeping track of the prev
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        prev = nums[0]
        result = nums[0] #initally, the best we can do is 0 (don't take anything)
        
        for i in range(1, length):
            #compute
            best = max(prev + nums[i], nums[i])
            
            #update
            result = max(best, result)
            prev = best
         
        return result
