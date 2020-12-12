"""
https://leetcode.com/problems/backspace-string-compare/
"""
class Solution(object):
    """
    Strat:
        Build up the word using a stack. If the "#" is found, pop
        from the state.
        
    Stats: O(n + m) time, O(n + m) space
            where n = len(S) and m = len(T)
    """
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        DELETE = "#"
        def backtrack(word):
            q = []
            
            for char in word:
                if char == DELETE:
                    #only pop if the queue is not empty
                    if q:
                        q.pop()
                else:
                    q.append(char)
                    
            return "".join(q)
        
        return backtrack(S) == backtrack(T)
    
    
    """
    Strat:
        Build up the word using an array (but backwards). If the "#" is found, 
        that is reason to skip the next char. When modified, this approach can lead 
        to a constant space solution--requires using yield and itertools (check solutions).
        
    Stats: O(n + m) time, O(n + m) space
            where n = len(S) and m = len(T)
    
        Runtime: 20 ms, faster than 64.87% of Python online submissions for Backspace String Compare.
        Memory Usage: 13.6 MB, less than 32.79% of Python online submissions for Backspace String Compare.
    """
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        DELETE = "#"
        def backtrack(word):
            q = []
            skip = 0
            
            for char in word[::-1]:
                if char == DELETE:
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    q.append(char)
                    
            return "".join(q)
        
        return backtrack(S) == backtrack(T)