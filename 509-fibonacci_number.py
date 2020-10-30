"""
https://leetcode.com/problems/fibonacci-number/submissions/

Strat:
    This is the "Iterative Top-Down" approach. However, you can do better
    with some math tricks.
    
Stats: O(n) / linear time, O(1) / constant space 
    Runtime: 12 ms, faster than 96.05% of Python online submissions for Fibonacci Number.
    Memory Usage: 13.5 MB, less than 12.17% of Python online submissions for Fibonacci Number.
"""
class Solution(object):
    def fib(self, n):
        """
        :type N: int
        :rtype: int
        """
        #basecases
        if n == 0:
            return 0
        elif n == 1:
            return 1

        #two vars to keep track of the sequence
        num0 = 0
        num1 = 1

        #keep tracks of what iteration we're on
        i = 0

        while i < n - 1:
            #generate the next num in the sequence:
            #num0 -> num1
            #num1 -> num0 + num1
            num0, num1 = num1, num0 + num1
            i += 1

        return num1
