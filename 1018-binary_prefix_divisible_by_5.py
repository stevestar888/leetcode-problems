"""
https://leetcode.com/problems/binary-prefix-divisible-by-5/

Strat: 
    Solution inspired by
    https://leetcode.com/problems/binary-prefix-divisible-by-5/discuss/1617173/Binary-Prefix-Divisible-By-5%3A-Combining-a-bit-shift-with-modulo

    Very clever in simple use of the bit shift--this way, you don't have to recompute the digit on every iteration


Stats: O(n) time and O(1) space if we modify nums directly
    Runtime: 308 ms, faster than 64.15% of Python online submissions for Binary Prefix Divisible By 5.
    Memory Usage: 13.9 MB, less than 100.00% of Python online submissions for Binary Prefix Divisible By 5.
"""
class Solution(object):
    def divisibleBy5(self, num):
        return num % 5 == 0
    
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum <<= 1 # left shift all digits to make room for the new digit
            running_sum += num # add the new digit on
            
            # append to a separate array or replace nums directly
            nums[i] = self.divisibleBy5(running_sum)
            
        return nums
