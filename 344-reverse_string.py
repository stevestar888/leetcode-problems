"""
https://leetcode.com/problems/reverse-string/

Strat:
    Use two pointers, and narrow in on results.
    
Stats: O(n) / linear time, O(1) / constant space 
    Runtime: 240 ms, faster than 16.60% of Python online submissions for Reverse String.
    Memory Usage: 19.6 MB, less than 66.41% of Python online submissions for Reverse String.
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