"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Naive approach: Two pointer (O(n))
    One starts at the begn and looks right -->
    Other one starts at the end and looks left <--

Better approach: Binary Search (O(lgn))
    Look for left_index & right_index:
    [1, 3, 4, 5, 8, 8, 8, 9]
                 ^     ^   
    Left index: 
    < -- recurse on right side
    > -- recurse on left side
    = -- check elem on left (else recurse on left side)

    Right index: [left_index:]
    < -- recurse on right side
    > -- recurse on left side
    = -- check elem on right (else recurse on right side)
    
Runtime: O(lgn) time, O(1) space -- two binary searches + no additional DSs
    Runtime: 1600 ms, faster than 5.01% of Python online submissions for Find First and Last Position of Element in Sorted Array.
    Memory Usage: 100.1 MB, less than 5.88% of Python online submissions for Find First and Last Position of Element in Sorted Array.
    
    Note: The actual Runtime in ms is much better if you do binary search iteratively. Then check if left_index == -1
    before looking for right_index
"""

class Solution(object):
    LEFT = 0
    RIGHT = 1
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        left_index = self.helper(nums, 0, len(nums) - 1, target, self.LEFT)
        right_index = self.helper(nums, left_index, len(nums) - 1, target, self.RIGHT)
        
        return [left_index, right_index]
    
    
    def helper(self, nums, l, r, target, side):
        mid = l + (r - l) // 2
        
        #base case
        if l == r:
            if nums[l] != target:
                return -1
        
        #recursive cases
        if nums[mid] < target:
            return self.helper(nums, mid + 1, r, target, side)
        if nums[mid] > target:
            return self.helper(nums, l, mid, target, side)
        if nums[mid] == target:
            try: #use an exception block to catch possible error from nums[mid-1] or nums[mid+1]
                if side == self.LEFT:
                    if nums[mid - 1] < target: #found our target
                        return mid 
                    else:
                        return self.helper(nums, l, mid, target, side)
                if side == self.RIGHT:
                    if nums[mid + 1] > target:
                        return mid #found our target
                    else: #not the correct index... keep searching
                        return self.helper(nums, mid + 1, r, target, side)
            except: #found our target
                return mid