"""
https://leetcode.com/problems/largest-number/submissions/

This is actually kind of an awful problem.

Strat: the biggest leading digits have to go first; the easiest way to check for leading digits
    is the caste num elements into strings and concatenate those together. 

Some considerations:
    
Runtime: O(nlgn) time, O(n) space -- runtime would be linear, but we have to sort
    Runtime: 24 ms, faster than 86.87% of Python online submissions for Largest Number.
    Memory Usage: 12.8 MB, less than 12.50% of Python online submissions for Largest Number.
"""

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        #convert nums into strings
        nums = map(str, nums)
        
        #sort nums, according to custom compare function
        nums.sort(cmp = self.compare)
        
        #if our "biggest" elem is 0, then result is no more than 0
        if nums[0] == "0":
            return "0"
        else:
            return "".join(nums)
    
    # allow to compare
    # 54 and 5 -->
    # 554 and 545
    def compare(self, a, b):
        if a + b < b + a:
            return 1
        else:
            return -1

    ### alternatively, use the built in "less than" compare methods from 
    ### building a custom class
# class CompareKeys(str):
#     def __lt__(a, b):
#         """
#         :type a: num
#         :type b: num
#         :rtype: num 
#         """
#         return a + b > b + a
        
        
# class Solution(object):
#     def largestNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: str
#         """
#         #convert nums into strings
#         nums = map(str, nums)
        
#         #sort nums, according to custom compare function
#         nums.sort(key = CompareKeys)
        
#         print(nums)
        
#         if nums[0] == "0":
#             return "0"
#         else:
#             return "".join(nums)