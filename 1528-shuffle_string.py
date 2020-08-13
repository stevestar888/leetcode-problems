"""
https://leetcode.com/problems/shuffle-string/

Strat: 
    Allocate result that is length of s. Use array indexing
    to put the right char in the right place.

Stats: O(n) / linear time, O(n) / linear space 

O(1) / constant space (uses swap): 
https://leetcode.com/problems/shuffle-string/discuss/755923/Used-Cyclic-Sort-with-O(1)-SPACE-and-O(N)-Time-complexity
"""
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        length = len(s)
        result = [" "] * length
        
        for i, letter in enumerate(s):
            result[indices[i]] = letter
        
        return "".join(result)