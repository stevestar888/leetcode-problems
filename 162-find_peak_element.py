"""
https://leetcode.com/problems/find-peak-element/submissions/

Runtime: O(log n) runtime, O(1) space
    Runtime: 28 ms, faster than 92.57% of Python online submissions for Find Peak Element.
    Memory Usage: 12.7 MB, less than 8.11% of Python online submissions for Find Peak Element.

"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) / 2
            
            #check if we're at local max
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            
            #binary search
            if nums[mid] < nums[mid+1]:
                left = mid + 1 #recurse on right side
            else:
                right = mid - 1 #recurse on left side

        return left
    
    
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) / 2
            
            #pick which side to recurse on--
            #choose the side with the bigger number
            if nums[mid + 1]  > nums[mid]:
                left = mid + 1 #recurse on right side
            else:
                right = mid #recurse on left side

        return left