"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Inspired by this really clean solution: 
https://leetcode.com/problems/longest-palindromic-subsequence/discuss/445783/Python-Recursive-DP-Solution-with-Explanation

Strat: Recursive DP w/ Memoization
    Starting from the ends. If the letters match, great! If not, advance one of the pointers inward. 
Stats:
    Runtime: 2385 ms, faster than 48.09% of Python3 online submissions for Longest Palindromic Subsequence.
    Memory Usage: 249.9 MB, less than 12.43% of Python3 online submissions for Longest Palindromic Subsequence.
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        
        def solve(l, r):
            if memo.get((l, r)):
                return memo[(l, r)]
            
            if l > r:
                return 0
            if l == r: #on same letter
                return 1
            
            best = 0
            if s[l] == s[r]:
                best = 2 + solve(l + 1, r - 1)
            else:
                advance_l = solve(l + 1, r)
                advance_r = solve(l, r - 1)
                
                best = max(advance_l, advance_r)
                
            memo[(l, r)] = best
            return best
        #--------------end helper function-------------- 
        
        return solve(0, len(s) - 1)