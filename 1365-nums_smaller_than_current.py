"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Strat: The easiest way to do this problem is using sort*. After you sort nums, 
    then iterate through every element and assign it a ranking (note: you only
    have to assign a num one ranking, regardless of how many times that num appears).
    The tricky thing here is you have to check what your previous element was. 
    Lastly, go through the original nums, and find its corresponding ranking.

    *Python's built-in sort is TimSort, which is O(nlgn) at worst; however, using an 
    implementation of Counting Sort, Radix Sort, Bucket Sort, or any other linear sort 
    would allow you to do this problem in O(n) time. On an amortized basis though, 
    Timsort will have comparable runtimes.

Runtime: O(nlgn) time, O(n) space -- TimSort takes O(nlgn) time (see ^) + rankings dictionary
    Runtime: 36 ms, faster than 97.60% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
    Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        rankings = {}
        
        #iterate through every element and assign it a ranking
        prev_elem = -1
        ranking = -1
        for i, num in enumerate(sorted_nums):
            if num > prev_elem: #moved on to a new num
                prev_elem = num
                ranking = i
            rankings[num] = ranking
    
        #For some reason, this runs slower than ^
#         prev_num = -1
#         for i, num in enumerate(sorted_nums):
#             if num > prev_num: #moved on to a new num
#                 rankings[num] = i
#             prev_num = num
        
        #now that we've assigned rankings, iterate through the
        #unsorted nums, and find its corresponding ranking
        return [rankings[num] for num in nums]