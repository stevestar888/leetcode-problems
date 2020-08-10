"""
Time limit exceeded... but an attempt at top-down recursive
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}
        
        def dp_helper(amount_left, coins_used):
            #base cases
            if amount_left == 0:
                return coins_used
            elif amount_left < 0:
                return sys.maxint
            
            #see if solution has already been calculated
            if memo.get((amount_left, coins_used), -1) > 0:
                # print(memo.get((amount_left, coins_used)))
                return memo.get((amount_left, coins_used))
            
            #recursive cases
            best = sys.maxint
            for coin in coins:
                coins_needed = dp_helper(amount_left - coin, coins_used + 1)
                best = min(best, coins_needed)
            
            #memoize the result for future use
            memo[(amount_left, coins_used)] = best
            return best
        
        result = dp_helper(amount, 0)
        if result == sys.maxint:
            return -1
        else:
            return result
