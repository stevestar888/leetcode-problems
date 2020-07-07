"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
class Solution(object):
    """
    O(n) runtime, one pass
    
    Runtime: 60 ms, faster than 5.33% of Python online submissions for Find Minimum in Rotated Sorted Array.
    Memory Usage: 12.9 MB, less than 71.17% of Python online submissions for Find Minimum in Rotated Sorted Array.
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] <= nums[-1]: #array is not rotated (the == is to catch arr len of 1)
            return nums[0] #smallest elem is the first elem
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        
    """
    O(lgn) runtime, achieved via binary search
    
    Runtime: 52 ms, faster than 6.01% of Python online submissions for Find Minimum in Rotated Sorted Array.
    Memory Usage: 12.9 MB, less than 80.00% of Python online submissions for Find Minimum in Rotated Sorted Array.
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] <= nums[-1]: #array is not rotated
            return nums[0] #smallest elem is the first elem
        
        #engage binary search
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + ((r - l) // 2)
            
            #check if we've found the min
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] > nums[-1]: #recurse on right side
                l = mid
            else:              #recurse on left side
                r = mid
