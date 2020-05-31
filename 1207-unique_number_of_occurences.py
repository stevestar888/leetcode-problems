"""
https://leetcode.com/problems/unique-number-of-occurrences/

Strat: First we make a count of how frequently each number occurs


Runtime: O(n) time, O(n) space -- one pass thru array & one pass thru dict + construct two dicts
    Runtime: 20 ms, faster than 92.90% of Python online submissions for Unique Number of Occurrences.
    Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Unique Number of Occurrences.
"""
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #count how frequently each num occurs
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
    
    #count the occurence. if the occurence is already considered, we do not
        #have a unique number of occurences
        occurences = {}
        for value in counts.values():
            if occurences.get(value, 0) == 0: #seen for first time
                occurences[value] = True
            else:
                return False
            
        return True
        
#         #or...
#         occurences = counts.values()
#         unique_occurences = set(occurences)
        
#         return len(occurences) == len(unique_occurences)
        