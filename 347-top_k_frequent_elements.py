"""
https://leetcode.com/problems/top-k-frequent-elements/

Runtime: O(n lgn) because we need to sort the n entries after they've been put into the dict
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # put nums in dict
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        answer = []
        
        # sort dict according to *values*, from largest to smallest
        for value in sorted(counts, key=counts.get, reverse=True):
            answer.append(value)
            
            if len(answer) == k:
                return answer