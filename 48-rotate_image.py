"""
https://leetcode.com/problems/rotate-image/

Strat: 
    Since we have to do this problem in-place, we are going to do a bunch of swaps. 
    The general idea is to mirror across an imaginary line from the top-left to bottom-right
    (y=-x). Afterwards, mirror the columns, which we can do with a left and right pointer, 
    first swapping columns, then continuously moving them inward. This strat work, 
    but it's hard to explain. Visualizing it out on paper makes things easier.

Optimization: 
    Turns out, we can swap rows, then mirror across the diagonals. 

Runtime: O(n^2)
"""

class Solution(object):
    """
    Original strat
    
    Runtime: 56 ms, faster than 6.55% of Python online submissions for Rotate Image.
    Memory Usage: 12.7 MB, less than 5.41% of Python online submissions for Rotate Image.
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        
        #do a mirror along the top-left/bottom-right line--swap matrix[i][j] with matrix[j][i]
        col_cutoff = 0
        for i in range(length):
            for j in range(length):
                if j < col_cutoff: 
                    #swap matrix[i][j] with matrix[j][i]
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            col_cutoff += 1

        #mirror columns using 2 pointers
        l_ptr = 0
        r_ptr = length - 1
        while r_ptr > l_ptr:
            for col in range(length):
                print(col, l_ptr, r_ptr)
                matrix[col][r_ptr], matrix[col][l_ptr] = matrix[col][l_ptr], matrix[col][r_ptr]
            r_ptr -= 1
            l_ptr += 1
            
    """
    Optimized strat
    
    Runtime: 16 ms, faster than 97.24% of Python online submissions for Rotate Image.
    Memory Usage: 12.7 MB, less than 5.41% of Python online submissions for Rotate Image.   
    """
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        
        #swap rows using the built in reverse method
        matrix.reverse()
        
        #mirror by swapping matrix[i][j] with matrix[j][i]
        #note: don't need a cutoff var; inner loop can go from j...i instead
        for i in range(length):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]