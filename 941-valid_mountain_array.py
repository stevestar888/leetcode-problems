"""
https://leetcode.com/problems/valid-mountain-array/
"""
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        
        if n < 3:
            return False
        
        prev = float('-inf')
        index_of_peak = 0
        for i, num in enumerate(arr):
            if num > prev:
                prev = num
            else:
                index_of_peak = i - 1
                break
        
        if index_of_peak == 0 or index_of_peak == n:
            return False
        
        prev = arr[index_of_peak]
        for i in range(index_of_peak + 1, n):
            if arr[i] < prev:
                prev = arr[i]
            else:
                return False
        
        return True
    

