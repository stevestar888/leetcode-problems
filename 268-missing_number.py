"""
https://leetcode.com/problems/missing-number/

use math: find 1 + 2 + 3 + 4 + ⋯
    total_sum = len(nums) * (len(nums) + 1) / 2

Runtime: O(n) time, O(1) space
    Runtime: 108 ms, faster than 96.70% of Python online submissions for Missing Number.
    Memory Usage: 13.7 MB, less than 5.26% of Python online submissions for Missing Number.

More interesting solution: https://leetcode.com/problems/missing-number/discuss/69891/1-line-Python-Solution
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) * (len(nums) + 1) / 2) - sum(nums)
    
        ##long version:
#         array_sum = 0 
#         for num in nums:
#             array_sum += num
        
#         return total_sum - array_sum
    