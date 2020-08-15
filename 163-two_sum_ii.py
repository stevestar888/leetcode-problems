"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Strat:
    Use two pointers: one starts at the beginning, one starts at the end.
    
Stats: O(n) / linear time, O(1) / constant space 
    Runtime: 72 ms, faster than 28.94% of Python online submissions for Two Sum II - Input array is sorted.
    Memory Usage: 13.1 MB, less than 34.43% of Python online submissions for Two Sum II - Input array is sorted.

Possibly can get O(lg n) time average, O(n) time worst: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51337/binary-search-solution-idea-programmatic-performance-comparison-with-the-linear-method
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_ptr, r_ptr = 0, len(nums) - 1
        
        while l_ptr < r_ptr:
            sum = nums[l_ptr] + nums[r_ptr]
            if sum == target: #met requirements
                return [l_ptr + 1, r_ptr + 1]
            elif sum > target: #exceeded target
                #decrease sum by moving r_ptr leftwards
                r_ptr -= 1
            else: #undershot target
                #increase sum by moving l_ptr rightwards
                l_ptr += 1
                
        # we're guranteed to have a pair that adds up to target
        # so no need for return []
