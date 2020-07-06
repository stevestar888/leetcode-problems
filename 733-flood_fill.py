"""
https://leetcode.com/problems/flood-fill/submissions/

Stats: O(n) time, O(n) space
    Runtime: 72 ms, faster than 23.24% of Python online submissions for Flood Fill.
    Memory Usage: 13 MB, less than 24.83% of Python online submissions for Flood Fill.
"""
class Solution(object):
    """
    First take (uses unecessary set)
    """
    def floodFill(self, image, source_row, source_col, new_color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = set()
        self.old_color = image[source_row][source_col]
        self.image = image
        
        def fill(sr, sc):
            if (str(sr) + str(sc)) in visited:
                return
            
            visited.add(str(sr) + str(sc))
            
            length = len(self.image)
            height = len(self.image[0]) 
            
            # print(visited)
            # print(sr, sc)
            # print(self.image)
            
            if 0 <= sr < length and 0 <= sc < height: #check bounds
                if self.image[sr][sc] == self.old_color:
                    self.image[sr][sc] = new_color
                    # print("updated {} {} ".format(sr, sc))
                    # print(self.image)
                    # print("")

                    #check four sides
                    fill(sr + 1, sc)
                    fill(sr - 1, sc)
                    fill(sr, sc + 1)
                    fill(sr, sc - 1)
        
        # do our fill work
        fill(source_row, source_col)
        
        return self.image
    
    """
    Improved -- no set & uses clever bounds checking
    """
    def floodFill(self, image, source_row, source_col, new_color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[source_row][source_col] == new_color:
            return image
        
        old_color = image[source_row][source_col]
        
        def fill(sr, sc):
            if sr < 0 or sc < 0:
                return
            
            # use exception handling instead of bounds checking
            try:
                if image[sr][sc] == old_color:
                    image[sr][sc] = new_color

                    #check four sides
                    fill(sr + 1, sc)
                    fill(sr - 1, sc)
                    fill(sr, sc + 1)
                    fill(sr, sc - 1)
            except: #MUST have this otherwise error!
                return
        
        # do the dfs dirty work
        fill(source_row, source_col)
        return image
