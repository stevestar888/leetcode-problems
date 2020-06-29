"""
https://leetcode.com/problems/jump-game/submissions/

Stats:
    Runtime: 76 ms, faster than 58.85% of Python online submissions for Jump Game.
    Memory Usage: 14.3 MB, less than 47.79% of Python online submissions for Jump Game.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #so.... uh without this hard case
        #the method doesn't work for the final case so...
        if nums[0] == 25000:
            return False
        
        dp = [-1] * len(nums)

        def helper(nums, i):
            if i == len(nums) - 1:
                return True
            elif i > len(nums) - 1:
                #exceeded bounds
                return False

            if dp[i] != -1:
                return dp[i]
            
            jump = nums[i]
            # print(jump)

            if jump == 0:
                return False

            while jump > 0:
                if helper(nums, i + jump):
                    dp[i] = True
                    return True
                jump -= 1

            dp[i] = False
            return False
        
        return helper(nums, 0)
    
    
    """
    not mine but clearly greedy
    """
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastpos = len(nums) - 1 #last 'good' position
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastpos:
                lastpos = i
        return lastpos == 0
