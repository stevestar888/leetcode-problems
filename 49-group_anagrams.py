"""
https://leetcode.com/problems/group-anagrams/

Strat: 
    We will use a dictionary to store groups, using each anagram group's letter occurrence as a key.
    There's not a simple way to store occurrences, but to make things simpler, we can make a list, then 
    caste that to a string. For example, "abe" becomes [a: 1, b: 1, e: 1], aka [1, 1, 0, 0, 1, 0, 0, ...],
	where index 1 is a, index 2 is b, index 3 is c, etc. At the end, the values in the dictionary are our groups. 
    
Runtime: O(n*m) time, O(n+m) space
   The actual runtimes aren't phenomenal, but it's good in terms of Big Oh. Essentially, we run through 
   every word in strs (which takes O(n) time) and we generate an occurrence list for every char (max of 
   O(m) time. All together, that is O(n*m) time.
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