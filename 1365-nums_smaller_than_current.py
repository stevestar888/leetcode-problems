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

"""
class Solution(object):
    #Try #1 on May23,2020
    """
    Stats: O(nlgn) time, O(n) space -- TimSort takes O(nlgn) time (see ^) + rankings dictionary
    Runtime: 36 ms, faster than 97.60% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
    Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
    """
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
    
    
    #Try #2 on sept20,2020
    """
    Regular sort
    
    Stats: O(n lgn) - normal sort
        Runtime: 36 ms, faster than 97.35% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        Memory Usage: 12.7 MB, less than 92.98% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
    """
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        
        order = {}
        
        rank = 0
        prev_num = float('-inf')
        for num in sorted_nums:
            if num != prev_num:
                order[num] = rank
                prev_num = num
            rank += 1
            
        return [order[num] for num in nums]
    
    """
    Bucket sort
    
    Stats: O(n) - bucket sort
        Runtime: 40 ms, faster than 93.66% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        Memory Usage: 12.7 MB, less than 53.93% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
    """
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #allocate bucket size of biggest num
        bucket = [0] * (max(nums) + 1)
        
        for num in nums:
            bucket[num] += 1

        rankings = {}
        rank = 0
        
        for num, count in enumerate(bucket):
            rankings[num] = rank
            rank += count
        
        return [rankings[num] for num in nums]
