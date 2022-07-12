"""
https://leetcode.com/problems/word-break-ii/

Seems like you don't even need to memoize or use DP to pass. Backtracking is enough.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        solutions = []
        
        def solve(index, words_used):
            # base case
            if index == len(s):
                solutions.append(words_used)
            
            # try words
            for word in wordDict:
                n = len(word)
                
                if (n + index) > len(s):
                    continue # word too large
                
                # check for if we can consume the word
                if s[index:index + n] == word:
                    solve(index + n, words_used + " " + word)

        #--------------end helper function--------------
            
        solve(0, "")
        return [solution[1:] for solution in solutions]