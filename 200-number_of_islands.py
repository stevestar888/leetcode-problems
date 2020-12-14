"""
https://leetcode.com/problems/number-of-islands/

Strat:
    BFS + Set. Apparently can also be done via union find!
    
Stats: 
    O(n * m) time, O(n * m) space, where n = len(grid) and m = len(grid[0])
    Runtime: 136 ms, faster than 36.42% of Python online submissions for Number of Islands.
    Memory Usage: 24.8 MB, less than 5.10% of Python online submissions for Number of Islands.


"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        WATER = "0"
        LAND = "1"
        
        if not grid or not grid[0]:
            return 0
        
        height = len(grid)
        length = len(grid[0])
        
        result = 0
        visited = set()
        
        def search(i, j):
            if not (0 <= i < height and 0 <= j < length):
                return
            
            if (i, j) in visited:
                return
            
            visited.add((i, j))
             
            if grid[i][j] == LAND:
                search(i + 1, j)
                search(i - 1, j)
                search(i, j + 1)
                search(i, j - 1)
                
                
        for i in range(height):
            for j in range(length):
                if (i, j) in visited:
                    continue
                    
                
                if grid[i][j] == LAND:
                    result += 1
                    search(i, j)

        return result
