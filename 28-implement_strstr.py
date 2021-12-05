"""
https://leetcode.com/problems/implement-strstr/

One iteration, O(n)
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hay_len = len(haystack)
        need_len = len(needle)
        
        if hay_len == 0 and need_len == 0:
            return 0
        
        for i in range(hay_len - need_len + 1):
            substring = haystack[i:i+need_len]
            if needle == substring:
                return i
        
        return -1
