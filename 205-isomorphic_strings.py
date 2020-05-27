"""
https://leetcode.com/problems/isomorphic-strings/submissions/

Strat: 
    1. make two dictionaries: one to store s-->t mappings, and one to store t-->s mappings
    2. traverse through s & t
    3. if mapping is not there: add it; if mapping is there, check it

Example:
    paper -> title
    
    # first letter
    paper  --  s_map: {p: t}
    title  --  t_map: {t: p}
    ^
    
    # second letter
    paper  --  s_map: {p: t, a: i}
    title  --  t_map: {t: p, i: a}
     ^
     
    # third letter, note: mapping already exists, so no additions, just checks
    paper  --  s_map: {p: t, a: i}
    title  --  t_map: {t: p, i: a}
      ^
    .
    .
    .
    etc.
    
    
Runtime: Linear time O(n+m) -- but we know the two lengths are equal so just O(n) runtime
    Runtime: 40 ms, faster than 42.81% of Python online submissions for Isomorphic Strings.
    Memory Usage: 15.4 MB, less than 13.16% of Python online submissions for Isomorphic Strings.

Crazy simple one-liner here: https://leetcode.com/problems/isomorphic-strings/discuss/57838/1-line-in-Python
        
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map, t_map = {}, {}
        
        for letter_s, letter_t in zip(s, t):

            if letter_s not in s_map:
                #add the s-->t mapping
                s_map[letter_s] = letter_t
            if letter_t not in t_map:
                #add the t-->s mapping
                t_map[letter_t] = letter_s
                
            if s_map.get(letter_s) != letter_t or t_map.get(letter_t) != letter_s:
                return False
 
        return True