"""
https://leetcode.com/problems/single-number/

Strat: 
    Run through list and map to dictionary. If a number hits the dictionary once,
    then the number is the singleton.

Runtime: O(n)
    64 ms, faster than 94.82% of Python online submissions for Single Number.
    15.2 MB, less than 5.40% of Python online submissions for Single Number.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set = {}
        for num in nums:
            if num in set:
                set[num] = 1
            else:
                set[num] = 0
        
        for num in set:
            if set[num] == 0:
                return num
