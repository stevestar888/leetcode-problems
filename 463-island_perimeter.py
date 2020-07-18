"""
Strat: 
    Finding the perimeter is nothing more than looking for tiles where their
    top, bottom, left, and/or right don't aren't bordering land. We can iterate
    through the entire grid, and look for island pieces that are touching the 
    ocean (i.e., 0). We also have to take into account the ocean could be the 
    end of the world, so in the case we extend beyond bounds of the world, then
    that particular direction from that piece is for sure part of the perimeter.
    For example, in the example given, grid[0][1] would be an edge case where the
    left, top, and right all constitute as a perimeter piece--this is because to 
    the left and right are ocean, and to the top is the edge.

Stats: O(n^2) time, O(1) space -- Iterate through every tile, no additional DS used
    Runtime: 440 ms, faster than 95.41% of Python online submissions for Island Perimeter.
    Memory Usage: 13.2 MB, less than 24.50% of Python online submissions for Island Perimeter.

Implemented using same idea, just a little cleaner:
    https://leetcode.com/problems/island-perimeter/discuss/343154/Solution-in-Python-3
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #make sure we have a map to work with
        if not grid or not grid[0]:
            return 0
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        result = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == 0:
                    continue
                    
                #now check top, down, left, right--if any of those are a 0, then 
                #we are at a perimeter tile
                
                #check top
                if j + 1 < col_len:
                    top = grid[i][j + 1]
                    if top == 0: result += 1
                else:
                    result += 1
                    
                #check bottom
                if j - 1 >= 0:
                    bottom = grid[i][j - 1]
                    if bottom == 0: result += 1
                else:
                    result += 1
                    
                #check right
                if i + 1 < row_len:
                    right = grid[i + 1][j]
                    if right == 0: result += 1
                else:
                    result += 1         
                
                #check left
                if i - 1 >= 0:
                    left = grid[i - 1][j]
                    if left == 0: result += 1
                else:
                    result += 1
        return result
