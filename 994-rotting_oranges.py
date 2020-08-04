"""
https://leetcode.com/problems/rotting-oranges/
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        EMPTY_CELL = 0
        FRESH_ORANGE = 1
        ROTTEN_ORANGE = 2
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        height = len(grid)    #positions rows
        length = len(grid[0]) #positions cols
        
        queue = deque()
        
        def add_oranges_to_queue(orange_freshness):
            fresh_oranges = 0
            for row in range(height):
                for col in range(length):
                    if grid[row][col] == orange_freshness:
                        queue.append((row, col))
                    if grid[row][col] == FRESH_ORANGE:
                        fresh_oranges += 1
            return fresh_oranges
        #----------------------------------------------
        
        def can_add(row, col):
            #check bounds
            if not (0 <= row <= height - 1 and 0 <= col <= length - 1):
                return False

            #check if the square can be rotted
            if grid[row][col] != FRESH_ORANGE:
                return False
            
            #passed all checks, we can visited grid[row][col]
            return True
        #----------------------------------------------
        
        if add_oranges_to_queue(ROTTEN_ORANGE) == 0:
            return 0

        time_elapsed = 0
        
        while queue:
            time_elapsed += 1
            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                #rot the orange in the cell
                if grid[row][col] == FRESH_ORANGE:
                    grid[row][col] = ROTTEN_ORANGE
                
                #do the real bfs: at this step, we've been infected; 
                #now rotting will spread to 4 adjacent squares
                for direction in DIRECTIONS:
                    dx = direction[0]
                    dy = direction[1]
                    if can_add(row + dx, col + dy): 
                        queue.append((row + dx, col + dy))
        
        #check to see if there are any fresh oranges left
        add_oranges_to_queue(FRESH_ORANGE)
        if queue:
            return -1
        else:
            return time_elapsed - 1
