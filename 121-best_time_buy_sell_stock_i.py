"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

This is an NOT application of the Maximum Subarray Problem (MPS) unfortunately
"""
class Solution(object):
    """
    First try at one-pass
    best_buy is the index of the lowest stock price
    
    Runtime: 44 ms, faster than 92.94% of Python online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 13.8 MB, less than 31.05% of Python online submissions for Best Time to Buy and Sell Stock.

    O(n) time, O(1) space
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_buy = 0
        max_prof = 0
        
        for i in range(1,len(prices)):
            curr_prof = prices[i] - prices[best_buy]
            max_prof = max(max_prof, curr_prof)
            
            if (prices[i] < prices[best_buy]):
                best_buy = i
                
        return max_prof
    
    """
    One-pass attempt #2
    Runtime: 48 ms, faster than 79.29% of Python online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 13.6 MB, less than 99.43% of Python online submissions for Best Time to Buy and Sell Stock.
    
    O(n) time, O(1) space
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < lowest_price:
                lowest_price = price
                
            if (price - lowest_price) > max_profit:
                max_profit = price - lowest_price
        
        return max_profit

