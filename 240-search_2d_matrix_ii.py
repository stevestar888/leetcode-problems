"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

Strat: 
    (original thought)
    Send out two searches, both starting from the top left: 
    #1 goes right as far as possible, then starts looking down
    #2 goes down as far as possible, then starts looking right

    (improved)
    Just send out one search--either from top right or bottom left. Because both
    options work, this is called a twin algor. More about that here:
    https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/528263/Two-efficient-python-sol.-sharing.-90%2B-w-Diagram
    
    
Runtime: O(m+n) time, O(1) space -- we "snake" through the array a max of n + m times
    Why is there no elusive O(log(n+m))? It's because you cannot definitively know which row/col
    an element is in after doing the initial binary search. Instead, you have to do “range checking”
    on the row/col to see if it’s possible for the target element to exist. At worst, that needs O(n) 
    time--and you have to follow it with binary search, which needs O(lg(m)) time. So in the end, 
    the best you can do with binary search is O(nlog(m))... For that, you'll need https://leetcode.com/problems/search-a-2d-matrix/

    More discussion about ^: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66154/Is-there's-a-O(log(m)%2Blog(n))-solution-I-know-O(n%2Bm)-and-O(m*log(n))

    However, you can also use the "snake" pattern search, where you start from the top-right / bottom-left,
    which runs in O( m+n ) time--and is what we did here.
"""

class Solution(object):
    """
    This solution was very much inspired by: 
    https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/533148/Python-3-O(m%2Bn)
    
    Runtime: 60 ms, faster than 57.23% of Python online submissions for Search a 2D Matrix II.
    Memory Usage: 16.8 MB, less than 24.68% of Python online submissions for Search a 2D Matrix II.
    """
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
        
        #indicies of cols and rows (starting from top right)
        row = 0
        col = width
        while col >= 0 and row <= height:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1 #move down a row
            else: 
                col-=1   #move back a col
        return False
