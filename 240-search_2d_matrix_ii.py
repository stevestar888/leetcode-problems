"""
Strat:
    Send out two searches, both starting from the top left: 
    #1 goes right as far as possible, then starts looking down
    #2 goes down as far as possible, then starts looking right

Runtime: O(m+n) 
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        height = len(matrix) - 1
        width = len(matrix[0]) - 1
        
        
        # go right, then look down
        row = 0
        col = 0
        while col < length: #go right
            print("col: {}, row: {}".format(col, row))
            if matrix[row][col + 1] == target:
                return True
            elif matrix[row][col + 1] < target:
                col += 1
            else:
                break
                
        while row < length: #go down
            print("col: {}, row: {}".format(col, row))
            if matrix[row + 1][col] == target:
                return True
            elif matrix[row + 1][col] < target:
                row += 1
            else:
                break
                
        # go down, then right
        row = 0
        col = 0
        
        while row < length: #go down
            print("col: {}, row: {}".format(col, row))
            if matrix[row + 1][col] == target:
                return True
            elif matrix[row + 1][col] < target:
                row += 1
            else:
                break
                
                
        while col < length: #go right
            print("col: {}, row: {}".format(col, row))
            if matrix[row][col + 1] == target:
                return True
            elif matrix[row][col + 1] < target:
                col += 1
            else:
                break
                

        return False