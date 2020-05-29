"""
https://leetcode.com/problems/rotate-array/solution/

Detailed various solutions: https://leetcode.com/problems/rotate-array/discuss/390391/4-methods-in-python-%3A-index-assign-list-slicing-reversed
"""

class Solution(object):
    
    """
    List reverse method
    
    Strat: we want to get from
    1 2 3 4 5 6 --> 5 6 1 2 3 4

    1. reverse the last k elems: 
        1 2 3 4 5 6 --> 1 2 3 4 6 5

    2. reverse the first (length - k) elems:
        1 2 3 4 6 5 --> 4 3 2 1 6 5

    3. reverse the whole array:
        4 3 2 1 6 5 --> 5 6 1 2 3 4
        
    Runtime: O(n) time, O(1) space
        Runtime: 40 ms, faster than 98.29% of Python online submissions for Rotate Array.
        Memory Usage: 13 MB, less than 6.25% of Python online submissions for Rotate Array.
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        
        first_k = nums[:-k][::-1]
        last_k = nums[-k:][::-1]
        
        print(first_k, last_k)
        nums[:] = (first_k + last_k)[::-1]
            
            
    """
    List splice method
    
    Strat: take the last k elems and the first (length - k) elements and join them.
    
    Runtime: O(n) time, O(1) space
        Runtime: 44 ms, faster than 92.02% of Python online submissions for Rotate Array.
        Memory Usage: 13.1 MB, less than 6.25% of Python online submissions for Rotate Array.
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        if length > 0 and k > 0:
            k = k % length
            nums[:] = nums[-k:] + nums[:-k]

        
    """
    Find the new index method
    
    Strat: find the new index for all elements in nums (by shifting the index by k, then mod length)
    
    Runtime: O(n) time, O(1) space -- is only constant space if you use list comprehension
        Runtime: 52 ms, faster than 55.29% of Python online submissions for Rotate Array.
        Memory Usage: 13.2 MB, less than 6.25% of Python online submissions for Rotate Array.
    """ 
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[:] = [nums[(i - k) % len(nums)] for i in range(len(nums))]
        
        #Or a little more clearly:
        # length = len(nums)
        # indicies = [(i - k) % length for i in range(length)]
        # nums[:] = [nums[index] for index in indicies]
        
        
    """
    Brute force
    
    Strat: grab the elem at the end and add it to the beginning
    
    Runtime: O(n^2) time, O(1) space
        Runtime: 128 ms, faster than 13.66% of Python online submissions for Rotate Array.
        Memory Usage: 13.4 MB, less than 6.25% of Python online submissions for Rotate Array.
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            nums.insert(0,nums[-1]) #add the last elem to the front
            nums.pop(-1) #get rid of the last elem