"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
"""
class Solution(object):
    
    """
    My one pass attempt
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        low = float('inf')
        high = float('-inf')
        
        for i, price in enumerate(prices):
            if price < low:
                low = price
            if price > high:
                high = price
                
            try:
                #only sell if the next price is smaller
                #in other words, sell if we're at the peak
                if not prices[i + 1] > prices[i]:
                    #execute a sell
                    max_profit += high - low
                    low = float('inf')
                    high = float('-inf')
            except:
                #at the end of the array 
                max_profit += high - low
                    
        return max_profit
    
    """
    Very clever solution (not mine)
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
    
    
    """
    And one liner
    
    Runtime: 40 ms, faster than 97.85% of Python online submissions for Best Time to Buy and Sell Stock II.
    Memory Usage: 13.6 MB, less than 88.11% of Python online submissions for Best Time to Buy and Sell Stock II.
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(prices[i+1] - prices[i] for i in range(len(prices)-1) if prices[i+1] > prices[i])