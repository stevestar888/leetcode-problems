"""
https://leetcode.com/problems/group-anagrams/

Revisited, and sorting the word this time.

Runtime: 142 ms, faster than 58.21% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.1 MB, less than 50.57% of Python3 online submissions for Group Anagrams.

O(n * m lg m)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i, word in enumerate(strs):
            sorted_word = str(sorted(word))            
            groups[sorted_word] = groups.get(sorted_word, []) + [word]

        return groups.values()