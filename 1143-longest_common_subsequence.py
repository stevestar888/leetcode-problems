"""
https://leetcode.com/problems/longest-common-subsequence/solution/

Applications: 
    "Finding the longest common subsequence between two strings is useful for 
    checking the difference between two files (diffing). Git needs to do this 
    when merging branches. It's also used in genetic analysis (combined with 
    other algorithms) as a measure of similarity between two genetic codes."
    
Note:
    Should be able to use the built-in cache instead of memoing
    (only works in python3 ???). import supposed to be:
    # from functools import lru_cache
    
    then
    
    @lru_cache(maxsize=None)
    # def lcs(idx1, idx2):
        ....
    ^doesn't work, check https://stackoverflow.com/questions/45819563/python-importerror-name-lru-cache
    
"""    
class Solution(object):
    """
    Recursive top-down attempt (dict to memoize)
    
    Stats: O(len(text1) * len(text2)) aka O(n * m) time
        Runtime: 2436 ms, faster than 5.16% of Python online submissions for Longest Common Subsequence.
        Memory Usage: 151.2 MB, less than 5.04% of Python online submissions for Longest Common Subsequence.
    """
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1 = len(text1)
        len2 = len(text2)
        def lcs(idx1, idx2):
            """
            :type word1: str
            :type word2: str
            :rtype: int
            """
            #base cases (empty string)
            if idx1 == len1 or idx2 == len2:
                return 0
            
            if memo.get((idx1, idx2)) > -1:
                return memo[(idx1, idx2)]

            #recursive cases
            answer = 0
            if text1[idx1] == text2[idx2]:
                #if the char matches
                answer = 1 + lcs(idx1 + 1, idx2 + 1)
            else: 
                #if the chars don't match
                call1 = lcs(idx1 + 1, idx2)
                call2 = lcs(idx1, idx2 + 1)
                answer = max(call1, call2)
            
            #memoize the answer
            memo[(idx1, idx2)] = answer
            return answer
        
        #--------------end helper function-------------- 
        
        #don't know why 2d arrays to store answers don't work:
        # memo = [[-1] * len(text2)] * len(text1)
        # memo = [[-1] for _ in range(len2) for _ in range(len1)]
        #use a dictionary for now, which works just as well
        memo = {} 
        return lcs(0, 0)
    
    
    """
    Bottom-up tabulation with 2d array
    
    Stats: O(n * m) time, O(n * m) space
        Runtime: 356 ms, faster than 66.86% of Python online submissions for Longest Common Subsequence.
        Memory Usage: 21.5 MB, less than 26.95% of Python online submissions for Longest Common Subsequence.
    """
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1 = len(text1) + 1
        len2 = len(text2) + 1
        memo = [[0 for i in range(len2)] for j in range(len1)]
        # memo = [[0] * (len2)] * (len1)
        #for some reason, ^ doesn't work for some cases...

        for i in range(1, len1):
            for j in range(1, len2):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i][j - 1], memo[i - 1][j])
        
        return memo[-1][-1]
    
    
    """
    Bottom-up tabulation with 1d array
    
    Inspired by: https://leetcode.com/problems/longest-common-subsequence/discuss/473089/Python-DP-with-T(n)-O(nm)-and-S(n)-O(m)
    
    Stats: O(n * m) time, O()
        Runtime: 300 ms, faster than 92.66% of Python online submissions for Longest Common Subsequence.
        Memory Usage: 12.7 MB, less than 97.13% of Python online submissions for Longest Common Subsequence.
    """
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #puts the shorter text in text2
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        len1 = len(text1) + 1
        len2 = len(text2) + 1
        memo = [0] * len2
        
        for i in range(1, len1):
            prev_diagonal = 0

            for j in range(1, len2):
                curr = memo[j]
                
                if text1[i - 1] == text2[j - 1]:
                    memo[j] = prev_diagonal + 1
                else:
                    memo[j] = max(memo[j - 1], memo[j])
            
                prev_diagonal = curr
            # print(memo)
            
        return memo[-1]
    