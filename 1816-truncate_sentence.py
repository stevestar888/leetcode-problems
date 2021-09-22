"""
https://leetcode.com/problems/truncate-sentence/

Strat:
    Split + Join

Stats: O(n) time
    Runtime: 8 ms, faster than 99.71% of Python online submissions for Truncate Sentence.
    Memory Usage: 13.4 MB, less than 65.90% of Python online submissions for Truncate Sentence.
"""

class Solution(object):
    def truncateSentence(self, sentence, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        components = sentence.split(" ")
        return " ".join(components[:k])
