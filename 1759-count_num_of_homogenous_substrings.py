"""
https://leetcode.com/problems/count-number-of-homogenous-substrings/
    
Strat:
    Break string into contiguous letter substrings. Apply the formula
    1 + 2 + 3 + ... + n = n * (n+1) / 2 to get its count. Sum all counts.
    
Stats: O(n) / linear time, O(1) space 
    Runtime: 196 ms, faster than 42.86% of Python online submissions for Count Number of Homogenous Substrings.
    Memory Usage: 17.6 MB, less than 17.86% of Python online submissions for Count Number of Homogenous Substrings.

"""

class Solution(object):
    def returnHomogenousCount(self, n):
        return n * (n+1) / 2
    
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD_CONST = 10**9 + 7
        curr_substring_len = 1
        running_sum = 0
        
        for i in range(len(s) - 1):
            curr = s[i]
            next = s[i + 1]
            
            if curr == next: # add to streak
                curr_substring_len += 1
            else: # streak of contiguous letters ended
                running_sum += self.returnHomogenousCount(curr_substring_len)
                curr_substring_len = 1 # reset back to 1
        
        running_sum += self.returnHomogenousCount(curr_substring_len)
        
        return running_sum % MOD_CONST
