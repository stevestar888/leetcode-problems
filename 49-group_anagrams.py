"""
https://leetcode.com/problems/group-anagrams/

Strat: 
    We will use a dictionary, using each anagram group's letter occurance as a key.
    To make things simplier, we can make a list of letter occurances, and then 
    caste that to a string. For example, "abe" becomes [a: 1, b: 1, e: 1], aka
    [1, 1, 0, 0, 1, 0, 0, ...]. At the end, the keys in the dictionary 
    
Runtime: O(n+m) time, O(n) space
    Runtime: 136 ms, faster than 41.31% of Python online submissions for Group Anagrams.
    Memory Usage: 16.7 MB, less than 14.58% of Python online submissions for Group Anagrams.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        
        for word in strs:
            group = [0] * 26 #arr of size 26
            
            #build up the group, letter by letter
            for char in word:
                group[ord(char) - ord('a')] += 1
            
            #store in dictionary         default value =👇     👇= adding our word
            groups[str(group)] = groups.get(str(group), []) + [word]
    
        return groups.values()