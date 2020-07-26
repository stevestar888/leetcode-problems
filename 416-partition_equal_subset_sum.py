"""
https://leetcode.com/problems/partition-equal-subset-sum/submissions/

Strat:
    Surprisingly, this is a dp problem. In fact, it's a lot like the 0-1
    knapsack problem, because for every element, you have a choice of taking
    it or not. The basecase is either you run of elements to look through, or
    you've reached your target (which is exactly 1/2 of the sum of all elems).

Stats:
    Runtime: 1972 ms, faster than 29.15% of Python online submissions for Partition Equal Subset Sum.
    Memory Usage: 13.6 MB, less than 35.30% of Python online submissions for Partition Equal Subset Sum.
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #constants
        UNSOLVED = -1
        LENGTH = len(nums)
        TOTAL = sum(nums)
        TARGET = TOTAL / 2
        
        #initial check to see if the array can be partitioned
        if TARGET * 2 != TOTAL: #the total was odd to start with
            return False
        
        #init dp table
        table = [[UNSOLVED] * (TARGET + 1)] * (LENGTH)
        
        def dp(i, remaining):
            #base case
            if remaining == 0:
                return True
            elif remaining < 0 or i > len(nums) - 1:
                return False
            
            #check if ans has been already computed
            if table[i][remaining] != UNSOLVED:
                return table[i][remaining]
            
            #choice 1: take item i from nums
            if nums[i] <= remaining:
                take = dp(i+1, remaining - nums[i])
            else: 
                take = False
                
            #choice 2: don't take item i
            dont_take = dp(i+1, remaining)
            
            #store our answer & return it
            table[i][remaining] = take or dont_take
            return take or dont_take
        
        return dp(0, TARGET)
