"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

My approach: 
    In 118-pascal_triangle_i, it made sense to genereate every row. Here, since we only care about
    the k-th row, we can use a clever trick with binomial coefficient: https://en.wikipedia.org/wiki/Binomial_coefficient.
    Essentially, Pascal's triangle is the same as the binomial coefficient, which can also be 
    represented with combinations: nCr = n! / (r! * (n - r)!)
                                       = n! / r! / (n - r)!
                                       
Best Stats:
Runtime: 16 ms, faster than 82.35% of Python online submissions for Pascal's Triangle II.
Memory Usage: 11.8 MB, less than 34.61% of Python online submissions for Pascal's Triangle II.
"""

from math import factorial as f

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        result = []
        for r in range(n + 1):
            coeff = f(n) / f(r) / f(n-r)
            result.append(int(coeff))
        return result

    #one liner
    def getRow(self, n):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return([f(n) / f(r) / f(n-r) for r in range(n + 1)])
    

obj = Solution.getRow(None, 3)
print(obj)