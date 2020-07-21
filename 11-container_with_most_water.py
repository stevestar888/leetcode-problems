"""
https://leetcode.com/problems/container-with-most-water/

Strat: 
    2 pointers
    
Stats: O(n) time, O(1) space
    Runtime: 116 ms, faster than 46.73% of Python online submissions for Container With Most Water.
    Memory Usage: 14.1 MB, less than 16.90% of Python online submissions for Container With Most Water.

"""
class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(heights)
        
        if length < 2:
            return 0
        
        def calculate_vol(l, r):
            height = min(heights[l], heights[r])
            width = r - l
            return height * width
            
        #left and right index pointers
        l, r = 0, length - 1
        
        result = 0
        while l < r:
            #find vol given current l & r pointers
            result = max(result, calculate_vol(l, r))
            
            #advance either the left or right pointer    
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return result
