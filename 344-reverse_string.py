"""
https://leetcode.com/problems/reverse-string/submissions/

Strat:
    Use two pointers, and narrow in on results.
    
Stats:
    Runtime: 240 ms, faster than 16.60% of Python online submissions for Reverse String.
    Memory Usage: 19.6 MB, less than 66.41% of Python online submissions for Reverse String.

Cool resource linked: http://pythontutor.com/live.html#mode=edit
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """    
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s