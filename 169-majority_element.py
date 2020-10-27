"""
https://leetcode.com/problems/majority-element/

Majority element basket:
https://leetcode.com/problems/majority-element/
https://leetcode.com/problems/majority-element-ii/
https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

Strat:
    The majority element must occur at least n / 2 times.
    Looking at index len(n) / 2 gives us the elem that 
    is in the majority.
    
Stats: O(n lgn)

Also an algo that is O(n) time O(1) space: 
https://en.wikipedia.org/wiki/File:Boyer-Moore_MJRTY.svg
    
    #TODO 
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        mid = len(nums) / 2
        
        return nums[mid]
        # or just:
        # return sorted(nums)[len(nums) / 2]

