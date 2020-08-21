"""
Brute force approach
1 4 8 6 19 8 2 1 10  -->  Look for 12
            ^ ^ ^ ^
            
 1 1 1 1 1 1 1 1 1 1 -> 8
   ^ ^ ^ ^ ^ ^ ^ ^

This is why sliding window doesn't work: negative numbers
    try doing this: 4 5 2 7 -7 2 4 1, k=7
    
    So you'd be as well of doing the bruce force
    
    
See solution for O(n) solution, or check
https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
"""
class Solution(object):
    def subarraySum(self, nums, target):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        result = 0
        
        for i in range(length):
            running_sum = 0
            for j in range(i, length):
                running_sum += nums[j]
                if running_sum == target:
                    result += 1
        
        return result
