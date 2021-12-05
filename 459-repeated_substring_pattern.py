"""
https://leetcode.com/problems/repeated-substring-pattern/discuss/1155561/python-one-liner

My write up:
https://leetcode.com/problems/repeated-substring-pattern/discuss/1613745/Python%3A-One-easy-to-understand-%2B-One-clever-and-super-speedy-(97-speed)
"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        divisors = []
        
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        
        for chars in divisors:
            repetitions = n / chars
            
            full_str = s[:chars] * repetitions
            
            if full_str == s:
                return True #strings match
        
        return False #never found a match

    
    """
    Stats:
        Runtime: 16 ms, faster than 97.39% of Python online submissions for Repeated Substring Pattern.
        Memory Usage: 13.7 MB, less than 87.58% of Python online submissions for Repeated Substring Pattern.
    """
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """    
        ss = (s + s)[1:-1]
        return s in ss
