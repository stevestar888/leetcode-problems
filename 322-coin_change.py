"""
Inspired by this really clean solution: 
https://leetcode.com/problems/coin-change/discuss/1679136/Python-Simplest-Recursive-Solution-with-Memoization

Strat:
    Recursive DP w/ Memoization
Stats:
    Runtime: 2674 ms, faster than 20.15% of Python3 online submissions for Coin Change.
    Memory Usage: 44.4 MB, less than 5.47% of Python3 online submissions for Coin Change.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def solve(amount_left):
            #see if solution has already been calculated
            if memo.get(amount_left):
                return memo[amount_left]
            
            #base cases
            if amount_left == 0:
                return 0
            elif amount_left < 0:
                return float('inf')
            
            #recursive cases
            best = float('inf')
            for coin in coins:
                coins_needed = 1 + solve(amount_left - coin)
                best = min(best, coins_needed)
            
            #memoize the result for future use
            memo[amount_left] = best
            return best
        #--------------end helper function-------------- 
        
        
        result = solve(amount)
        if result == float('inf'):
            return -1
        else:
            return result
