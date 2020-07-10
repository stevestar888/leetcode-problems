"""
https://leetcode.com/problems/ransom-note/

Runtime: 68 ms, faster than 53.97% of Python online submissions for Ransom Note.
Memory Usage: 13 MB, less than 47.96% of Python online submissions for Ransom Note.
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq = [0] * 26
        
        for char in magazine:
            freq[ord(char) - ord('a')] += 1
            
        for char in ransomNote:
            freq[ord(char) - ord('a')] -= 1
            
        return all(freq[i] >= 0 for i in range(26))
