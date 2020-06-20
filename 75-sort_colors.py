class Solution(object):
    """
    Two-pass algorithm using counting sort. First, iterate the array counting number of 0's, 1's, and 2's, 
    then overwrite array with total number of 0's, then 1's and followed by 2's.
    
    Runtime: 12 ms, faster than 99.10% of Python online submissions for Sort Colors.
    Memory Usage: 12.6 MB, less than 99.56% of Python online submissions for Sort Colors.
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        reds, whites, blues = 0, 0, 0
        for num in nums:
            if num == 0:
                reds += 1
            elif num == 1:
                whites += 1
            else:
                blues += 1
        
        pointer = 0
        while pointer < len(nums):
            if reds > 0:
                nums[pointer] = 0
                pointer += 1
                reds -= 1
            elif whites > 0:
                nums[pointer] = 1
                pointer += 1
                whites -= 1
            else:
                nums[pointer] = 2
                pointer += 1
                blues -= 1