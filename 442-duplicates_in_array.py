"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Strat 1: make a pseudo dictionary (default value = -1) that is N long. Index into each elem at 
    arr[num - 1] increment its value. (arr[num - 1] because nums is 1-based indexing) At the end, 
    if the value is 1, then that num had 2 duplicates.
Stats: O(n) time, O(n) space -- allocated array of size N + a few pass throughs

Strat 2: use the nums array itself as a psuedo dictionary. The trick here is we can store extra
    info using the sign of each number. When we iterate through each num, we set arr[num - 1] 
    equal to its negative, meaning that it's been "found". As we keep iterating, if we find 
    arr[num - 1] is already negative, then we know it's a duplicate, so add it to the return
    list. Tricky thing here is to watch out for the indexing (lots of +1s and -1s).
Stats: O(n) time, O(1) space -- no allocated array (in place) + one pass through
"""
class Solution(object):
    """
    Strat 1 (naive) - O(n) time, O(n) space
    Runtime: 324 ms, faster than 94.16% of Python online submissions for Find All Duplicates in an Array.
    Memory Usage: 20.1 MB, less than 40.00% of Python online submissions for Find All Duplicates in an Array.
    """
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        arr = [-1 for n in nums]
        
        #if first time: -1 --> 0
        #if second time: 0 --> 1
        for n in nums:
            arr[n - 1] += 1
        
        #add to list only if value in arr reached 1
        return [i + 1 for i in range(len(arr)) if arr[i] == 1]

    """
    Strat 2 (clever space usage) - O(n) time, O(1) space
    Runtime: 332 ms, faster than 85.66% of Python online submissions for Find All Duplicates in an Array.
    Memory Usage: 19.7 MB, less than 40.00% of Python online submissions for Find All Duplicates in an Array.
    """
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            n = abs(n)
            if nums[n-1] > 0:
                nums[n-1] = -nums[n-1] #flip the sign
            else: #already neg
                ans.append(n)
                
        return ans