"""
https://leetcode.com/problems/minimum-absolute-difference/submissions/

Strat:
    Sort array so it's easy to find the distance between any two elements.
    As you iterate through, save the min_diff between any two elements. Afterwards,
    do one more pass, and save the pairs that have min_diff.
    
Stats: O(n*lgn) time, O(n) space -- Sort + return list can be up to n long
    Runtime: 360 ms, faster than 48.40% of Python online submissions for Minimum Absolute Difference.
    Memory Usage: 23.7 MB, less than 39.03% of Python online submissions for Minimum Absolute Difference.

Java solution: https://github.com/jlin-orange/Leetcode/blob/master/minAbsVal.java
"""

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr[:] = sorted(arr)
        length = len(arr)
        min_diff = arr[1] - arr[0]
        
        for i in range(1, length):
            min_diff = min(min_diff, arr[i] - arr[i - 1])
        print(min_diff)
        
        result = []
        for i in range(1, length):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
                
        return result