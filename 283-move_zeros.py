"""
https://leetcode.com/problems/move-zeroes/

Strat: look for non-zero digits in the array. Once you found one, move it to start
    of the array. Repeat until you've iterated through the entire array, where
    you fill in zeros for the rest of the elements.
    
Stats: 
    Runtime: 32 ms, faster than 93.26% of Python online submissions for Move Zeroes.
    Memory Usage: 13.7 MB, less than 5.06% of Python online submissions for Move Zeroes.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        
        finger = 0
        
        #look for non-zero digits in the array
        for num in nums:
            if num != 0:
                nums[finger] = num
                finger += 1
                
        #looked through all non-zero digits; replace the rest with 0s
        while finger < len(nums):
            nums[finger] = 0
            finger += 1
