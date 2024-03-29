"""
https://leetcode.com/problems/find-the-duplicate-number/

Strat:
    Use the array itself to store if we've seen the num.

Stats: O(n) / linear time, O(1) / constant space 
    Runtime: 52 ms, faster than 81.82% of Python online submissions for Find the Duplicate Number.
    Memory Usage: 14.5 MB, less than 7.14% of Python online submissions for Find the Duplicate Number.

"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #iterate through nums; mark a num neg to indicate it's been seen
        for num in nums:
            num = abs(num)
            if nums[num] < 0: #if the num is already neg, found a duplicate
                return num
            else: #change to the neg version of itself
                nums[num] = -nums[num]

                

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = [0] * len(nums)
        
        for i, num in enumerate(nums):
            if store[num] == num:
                return num
            else:
                store[num] = num
