"""
https://leetcode.com/problems/word-break/


Strat:
    Recursive DP solution

Stats:
    Runtime: 39 ms, faster than 90.26% of Python3 online submissions for Word Break.
    Memory Usage: 14.1 MB, less than 27.61% of Python3 online submissions for Word Break.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        store = {}
        
        def solve(index):
            # check if we have memoized before
            if store.get(index) != None:
                return store.get(index)
            
            # base case
            if index == len(s):
                store[index] = True
                return True
            
            # try words
            for word in wordDict:
                n = len(word)
                
                if (n + index) > len(s):
                    continue # word too large
                
                # check for if we can consume the word
                if s[index:index + n] == word:
                    solve(index + n) # advance further along
                    store[index] = True
                    
            store[index] = False
        #--------------end helper function--------------
            
        solve(0)
        return store.get(len(s))