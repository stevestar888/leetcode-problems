"""
https://leetcode.com/problems/running-sum-of-1d-array/submissions/

Runtime: 36 ms, faster than 100.00% of Python online submissions for Running Sum of 1d Array.
Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Running Sum of 1d Array.  
"""
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sum_so_far = 0
        for num in nums:
            sum_so_far += num
            result.append(sum_so_far)
            
        return result