"""
https://binarysearch.io/question/182

Given a list of integers nums, replace every nums[i] with the smallest integer left of i. Replace nums[0] with 0.
"""

class Solution:
    def solve(self, nums):
        prev_smallest = nums[0]
        
        for i, num in enumerate(nums):
            if i != 0:
                value = nums[i]
                nums[i] = prev_smallest
                prev_smallest = min(value, prev_smallest)
                
        nums[0] = 0
        return nums