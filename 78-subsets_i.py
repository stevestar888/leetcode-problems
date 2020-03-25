"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Stats:
    Runtime: 20 ms, faster than 70.88% of Python online submissions for Subsets.
    Memory Usage: 11.9 MB, less than 83.05% of Python online submissions for Subsets.
"""

class Solution(object):
    def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Uses bitmasks to find all lexigraphical generations of i 
        """
        powerset = []  # used to store all sets
        for i in range(1 << len(nums)):  # iterate 2^sets
            subset = []
            for j in range(len(nums)):
                # checking if the j-th bit of i is 1
                if (i & (1 << j)):
                    # if is a match, add the j-th position element to subset
                    subset.append(nums[j])
            powerset.append(subset)
        return(powerset)


    #shortened
    def subsets(nums):
        x = len(nums)
        powerset = []
        for i in range(1 << x):
            powerset.append([nums[j] for j in range(x) if (i & (1 << j))])
        return powerset


    #extreme shortened
    def subsets(nums):
        return [[nums[j] for j in range(len(nums)) if (i & (1 << j))] for i in range(1 << len(nums))]


nums = [1, 2, 3, 4]
obj = Solution.subsets(nums)
print(obj)
