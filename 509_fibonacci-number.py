"""
https://leetcode.com/problems/fibonacci-number/

Recursive DP solution w/ Memoization
"""
class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def solve(i):
            if memo.get(i):
                return memo[i]
            
            if i == 0: return 0
            if i == 1: return 1
            
            res = solve(i-1) + solve(i-2)
            memo[i] = res
            return res
        #--------------end helper function--------------
        
        return solve(n)