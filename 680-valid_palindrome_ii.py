"""
https://leetcode.com/problems/valid-palindrome-ii/
"""
class Solution(object):
    """
    Recursive - O(n) time, even though 3x iterations may be required at worst
    
    Runtime: 592 ms, faster than 5.19% of Python online submissions for Valid Palindrome II.
    Memory Usage: 39.6 MB, less than 5.02% of Python online submissions for Valid Palindrome II.
    """
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(left, right, skip_available):
            if right - left <= 0:
                return True
            
            # print(left, right)
            if s[left] == s[right]: #match
                return helper(left + 1, right - 1, skip_available)
            
            
            # didn't match -- we have a chance at redemption (can go skip either letter on left or letter on right)
            if skip_available:
                return helper(left + 1, right, False) or helper(left, right - 1, False)

        
        return helper(0, len(s) - 1, True)
    
    
    """
    Super speedy solution, inspired by submissions page
    May not be so good on memory since [::-1] on strings requries creating new string
    
    Runtime: 80 ms, faster than 96.88% of Python online submissions for Valid Palindrome II.
    Memory Usage: 14.4 MB, less than 38.67% of Python online submissions for Valid Palindrome II.
    """
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        
        # iterate until error found
        l = 0
        r = len(s) - 1
        
        while s[l] == s[r]:
            l += 1
            r -= 1
            
        # remove letter on left / right
        left_letter_removed = s[l+1:r+1]
        right_letter_removed = s[l:r]
        
        return left_letter_removed == left_letter_removed[::-1] or right_letter_removed == right_letter_removed[::-1]
