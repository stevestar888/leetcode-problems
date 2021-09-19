"""
Strat: Binary search

Stats: O(n lgn)
    Runtime: 52 ms, faster than 20.51% of Python online submissions for Search Insert Position.
    Memory Usage: 14.1 MB, less than 81.81% of Python online submissions for Search Insert Position.

"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) / 2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
        return l
