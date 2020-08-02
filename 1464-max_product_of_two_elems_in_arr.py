"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/

Strat:
    The largest product can be found be finding the two biggest numbers, which we will
    dub as max1 and max2. Iterate through the array to find them and then return their
    product at the end.

Stats: O(n) time, O(1) space -- iterate through all elems + keep track of only a few vars
"""
class Solution(object):
    """
    2 pass
    
    Runtime: 64 ms, faster than 29.46% of Python online submissions for Maximum Product of Two Elements in an Array.
    Memory Usage: 12.9 MB, less than 18.18% of Python online submissions for Maximum Product of Two Elements in an Array.
    """
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find the first max then erase it from the array
        max1 = max(nums)
        nums[nums.index(max1)] = 0
        
        #find the second max
        max2 = max(nums)
        
        return (max1 - 1) * (max2 - 1)
    
    
    """
    1 pass
    
    Runtime: 48 ms, faster than 46.47% of Python online submissions for Maximum Product of Two Elements in an Array.
    Memory Usage: 12.7 MB, less than 59.94% of Python online submissions for Maximum Product of Two Elements in an Array.
    """
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we can think of max1 as being greater than max2
        max1 = max2 = float('-inf')
        for num in nums:
            #first try to update max1 (if sucessful, update max2 to max1's prev value)
            #(if not sucessful, see if max2 can be updated)
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
                
        return (max1 - 1) * (max2 - 1)
