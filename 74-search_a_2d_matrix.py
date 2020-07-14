"""
https://leetcode.com/problems/search-a-2d-matrix/submissions/
"""
class Solution(object):    
    """
    Strat: 
        All the values in a row of the matrix will "pick up" in the next row.
        If you chain all the rows of the matrix together, you will essentially
        be getting one long, sorted array--and you can use generic binary search
        to find a target number. This is what 
    
    Stats: O(log(n*m)) time
        Runtime: 60 ms, faster than 34.74% of Python online submissions for Search a 2D Matrix.
        Memory Usage: 14.5 MB, less than 69.76% of Python online submissions for Search a 2D Matrix.
    """
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #check for empty matricies
        if not matrix or not matrix[0]:
            return False
        
        height = len(matrix)
        length = len(matrix[0])
        
        #begin binary search
        lo = 0
        hi = height * length - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            row = mid / length
            col = mid % length

            found = matrix[row][col]
            if target == found:
                return True
            elif target > found: #look right
                lo = mid + 1
            else: #look left
                hi = mid - 1
                
        return False
    
#     """
#     **Not working
#     First find the correct row--via Binary Search in log(n) time,
#     then find the correct column--via Binary Search in log(m) time.
    
#     Runtime: O(lgn + lgm) = O(log(n*m)) time
#     """
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         #check for empty matricies
#         if not matrix or not matrix[0]:
#             return False
        
#         height = len(matrix)
#         length = len(matrix[0])
        
#         #find the correct col index
#         lo = 0
#         hi = length - 1
        
#         while lo <= hi:
#             mid = lo + (hi - lo) / 2
#             print(lo, mid, hi)
            
#             if target < matrix[mid][0]: 
#                 hi = mid - 1
#             if target > matrix[mid][0]: 
#                 lo = mid + 1
#             else:
#                 return True
        
#         col = hi
#         #find the correct row index
#         lo = 0
#         hi = height - 1
        
#         while lo <= hi:
#             mid = lo + (hi - lo) / 2
            
#             if target < matrix[col][mid]: 
#                 hi = mid - 1
#             if target > matrix[col][mid]: 
#                 lo = mid + 1
#             else:
#                 return True
#         return False
