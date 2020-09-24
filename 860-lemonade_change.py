"""
https://leetcode.com/problems/lemonade-change/

Strat: Use a greedy algorithm: 
    when a person hands us a $20, always try to give them a $10 + $5, instead of three $5.
    `                      ` $10, can only give them a 5
    `                      ` $5, no need to make change

Runtime: O(n) time, O(1) space
    Runtime: 152 ms, faster than 24.25% of Python online submissions for Lemonade Change.
    Memory Usage: 12.9 MB, less than 33.33% of Python online submissions for Lemonade Change.
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = tens = 0
        #no need to keep track of twenties, bc that can't make change
        
        for bill in bills:
            if bill == 5:
                fives += 1
                #and don't need to make change
                
            if bill == 10: 
                tens += 1
                #now make change with fives
                if fives > 0:
                    fives -= 1
                else:
                    return False
                
            if bill == 20:
                #make change: with $5 + $5 + $5 or $10 + $5
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives > 2:
                    fives -= 3
                else: 
                    return False
            
        return True
                    
