"""
https://leetcode.com/problems/pascals-triangle/

Strat:
    Look at the previous row.

Stats:
    Runtime: 12 ms, faster than 93.27% of Python online submissions for Pascal's Triangle.
    Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Pascal's Triangle.
"""

import pprint

class Solution(object):
    def generate(self, num_rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        #if row == 0 return because triangle is nonexistent
        #check if 0 rows, else give us the basic row to start off
        if num_rows == 0:
            return result
        else:
            result.append([1])

        #num_rows - 1 because we only start summing when rows ≥ 2
        for i in range(num_rows - 1):
            prev_row = result[i]
            new_row = [1] #the leading [1]

            #len(prev_row) - 1 because we look at prev_row[j + 1]
            for j in range(len(prev_row) - 1):
                sum = prev_row[j] + prev_row[j + 1]
                new_row.append(sum)

            new_row.append(1) #the trailing [1]
            result.append(new_row)

        return result



obj = Solution.generate(None, 12)
pprint.pprint(obj)
