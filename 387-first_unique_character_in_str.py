"""
https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
"""
class Solution(object):
    
    """
    Brute force
    
    Runtime: not very good
    """
    def firstUniqChar(self, str):
        """
        :type s: str
        :rtype: int
        """
        for s in str:
            if str.count(s) == 1:
                return str.index(s)
        return -1
    
    """
    O(n) solution--using dictionary-equivalent DS
    
    Runtime: 136 ms, faster than 65.45% of Python online submissions for First Unique Character in a String.
    Memory Usage: 13 MB, less than 85.64% of Python online submissions for First Unique Character in a String.
    """
    def firstUniqChar(self, str):
        """
        :type s: str
        :rtype: int
        """
        counts = [0] * 26
        
        #find counts for each
        for s in str:
            counts[ord(s) - ord('a')] += 1
            
        for i, s in enumerate(str):
            if counts[ord(s) - ord('a')] == 1:
                return i
        return -1
