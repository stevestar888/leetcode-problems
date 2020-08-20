"""
https://leetcode.com/problems/find-pivot-index/

Strat:
    If we do a one pass to sum up all the contents of the array,
    and then keep track of the sum we've iterated over so far, we
    know essentially the nums left and right of the pivot at all
    times.

Stats: O(n) / linear time, O(1) / constant space 
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_right_of_pivot = sum(nums)
        
        sum_left_of_pivot = 0
        for i, num in enumerate(nums):
            sum_right_of_pivot -= num
            if sum_left_of_pivot == sum_right_of_pivot:
                return i
            sum_left_of_pivot += num
            
        return -1
