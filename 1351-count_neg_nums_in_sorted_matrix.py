"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
"""
class Solution(object):
    """
    Just the brute force, O(m * n)
    """
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid) #positions rows
        height = len(grid[0]) #positions cols
        
        counter = 0
        
        for row in range(length):
            for col in range(height):
                if grid[row][col] < 0:
                    counter += 1
        
        return counter
    
    """
    "Snaking" method, where you start in the bottom left corner
    and zig zag your way up to the top right
    
    With implementation help from: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/510249/JavaPython-3-2-similar-O(m-%2B-n)-codes-w-brief-explanation-and-analysis.
    
    O(n + m) / linear time, where n = height, m = length
    
    Runtime: 88 ms, faster than 99.73% of Python online submissions for Count Negative Numbers in a Sorted Matrix.
    Memory Usage: 14.6 MB, less than 9.57% of Python online submissions for Count Negative Numbers in a Sorted Matrix.
    """
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid) #positions rows
        height = len(grid[0]) #positions cols
        
        row, col = 0, height - 1
        result = 0
        
        while row < length and col >= 0:
            if grid[row][col] < 0:
                result += length - row
                col -= 1
            else:
                row += 1
        return result