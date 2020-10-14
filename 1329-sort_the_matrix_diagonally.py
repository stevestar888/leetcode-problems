"""
https://leetcode.com/problems/sort-the-matrix-diagonally/
"""
class Solution(object):
    """
    Runtime: 72 ms, faster than 71.10% of Python online submissions for Sort the Matrix Diagonally.
    Memory Usage: 13.9 MB, less than 31.56% of Python online submissions for Sort the Matrix Diagonally.
    """
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(mat)    #aligns rows
        height = len(mat[0]) #aligns cols
        
        def sort(row, col):
            nums = [] #holds all the nums of the diag
            
            #grab all nums
            r, c = row, col
            while r < length and c < height:
                nums.append(mat[r][c])
                r += 1
                c += 1
            
            #sort the nums array
            nums = sorted(nums)
            
            #update the diag with sorted nums
            i = 0 #pointer index for nums
            r, c = row, col
            while r < length and c < height:
                mat[r][c] = nums[i]
                i += 1
                r += 1
                c += 1
        #--------------end helper function-------------- 
        
        
        #sort each diag that starts from a row (as well as 0, 0)
        row = 0
        col = 0
        while row < length - 1: #len - 1 because no need to sort the corner num
            sort(row, col)
            row += 1
        
        #sort each diag that starts from a col (excluding 0,0 )
        row = 0
        col = 1
        while col < height - 1: #as rationale
            sort(row, col)
            col += 1
            
        return mat