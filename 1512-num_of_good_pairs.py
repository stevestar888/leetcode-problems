"""
https://leetcode.com/problems/number-of-good-pairs/submissions/

Strat:
    Since we only have to calculate the # of good pairs (instead of find all
    the good pairs themselves), we can employ a trick: given [1, 1, 1, 1], the 
    number of good pairs for the first 1 is 3 (all the 1s preceding it). The 
    number of good pairs for the second 1 is 2 (all the 1s preceding it).
    Apply this trick for the rest of the 1s, and the pattern of 
    1 + 2 + 3 + ... + n = (n)(n-1)/2 emerges.
    
    So use a dictionary to count the number of occurances for each #. Iterate through
    all the counts, and apply the above series.
    
Stats:
    Runtime: 16 ms, faster than 98.00% of Python online submissions for Number of Good Pairs.
    Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Number of Good Pairs.
"""
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counts = {}
        
        for num in nums:
            nums_counts[num] = nums_counts.get(num, 0) + 1 
        
        result = 0
        for count in nums_counts.values():
            result += self.count_good_pairs(count)
        
        return result
    
    
    def count_good_pairs(self, count):
        return count * (count - 1) / 2
        