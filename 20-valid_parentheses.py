"""
https://leetcode.com/problems/valid-parentheses/submissions/

Strat: We know for every opening pair, there must be a closing pair. We can use a stack
    to create a "backlog" of all the symbols we still need to find matches for (in the case
    that the symbol is an opening one). In the case we encounter a closing symbol, we look 
    at the stack to see if we can match. If we can't match, then we know we have an incompatible
    combination, e.g., (} or {] or something like that. 
    
Stats: O(n) time, O(n) space -- need to iterate through all symbols + store up to n/2 symbols in stack
    Runtime: 24 ms, faster than 46.22% of Python online submissions for Valid Parentheses.
    Memory Usage: 12.8 MB, less than 78.73% of Python online submissions for Valid Parentheses.
    
Possible  O(n) time O(1) space solution?? 
https://leetcode.com/problems/valid-parentheses/discuss/9478/No-stack-O(1)-space-complexity-O(n)-time-complexity-solution-in-C%2B%2B
"""

class Solution(object):
    def isValid(self, symbols):
        """
        :type symbols: str
        :rtype: bool
        """
        
        if len(symbols) % 2 == 1:
            return False
        
        stack = []
        for symbol in symbols:
            if symbol == "(" or symbol == "[" or symbol == "{":
                stack.append(symbol)
            else: #closing symbol -- need to match what we pop off stack
                if len(stack) == 0:
                    return False
                
                popped = stack.pop()
                if popped == "(" and symbol != ")":
                    return False
                elif popped == "[" and symbol != "]":
                    return False
                elif popped == "{" and symbol != "}":
                    return False
        
        #if stack is empty, all the pairs have been matched
        return len(stack) == 0
    
    """
    Super solution, not mine
    
    Runtime: 16 ms, faster than 90.98% of Python online submissions for Valid Parentheses.
    Memory Usage: 12.8 MB, less than 65.74% of Python online submissions for Valid Parentheses.
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = dict({'}':'{', ')':'(', ']':'['})
        stack = []
        for x in s:
            if not x in matches:
                stack.append(x)
            elif len(stack) == 0 or not matches[x] == stack.pop():
                return False
        return len(stack) == 0
