"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Strat: 
    Iterate list and store the index of occurance in dictionary. If the num's complement exists in 
    dictionary, retreive its index! (Continue iterating if not)

Stats:
    Runtime: 40 ms, faster than 61.01% of Python online submissions for Two Sum.
    Memory Usage: 14.1 MB, less than 5.13% of Python online submissions for Two Sum.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            
            if nums_dict.get(complement) > -1: #found counterpart
                return [i, nums_dict.get(complement)]
            else: #store our num in the dict
                nums_dict[num] = i
                
        return None