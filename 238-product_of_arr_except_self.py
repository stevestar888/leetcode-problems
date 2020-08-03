"""
Strat:
    Use a prefix and suffix array. Here's an exmaple
    1  2  3  4  (OG array)
    1  2  6  1  (starting from left, last elem is 1)
    1  24 12 4  (starting from right, first elem is 1)
    
    To calculate the result array:
    index 0:
        left[-1] * right[1]
        =      1 * 24 = 24
        
    index 1:
        left[0] * right[2]
        =     1 * 12 = 12
        
    index 3:
        left[2] * right[4%len]
        =     6 * 1 = 6
        
Stats: O(n) time, O(1) space
    Runtime: 112 ms, faster than 59.69% of Python online submissions for Product of Array Except Self.
    Memory Usage: 21.7 MB, less than 28.20% of Python online submissions for Product of Array Except Self.
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        prefixes, suffixes, result = [1] * length, [1] * length, [1] * length
        
        #populate prefixes
        running_product = 1
        for i in range(length - 1):
            running_product *= nums[i]
            prefixes[i] = running_product
        
        #populate suffixes
        running_product = 1
        for i in range(length - 1, 0, -1):
            running_product *= nums[i]
            suffixes[i] = running_product
        
        #now find result--
        #for a given i, the result is prefixes[i-1] * suffixes[i+1]
        return [prefixes[i-1] * suffixes[(i+1) % length] for i in range(length)]
    
    
    """
    TODO - Try 2, with constant space
    """
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         length = len(nums)
#         result = [1] * length
        
#         #populate result with prefixes
#         running_product = 1
#         for i in range(length):
#             running_product *= nums[i]
#             result[i] = running_product
        
#         #populate multiply suffixes to the prefixes stored in result
#         running_product = 1
#         for i in range(length - 1, 0, -1):
#             running_product *= nums[i]
#             result[i] = running_product
        
#         return result

