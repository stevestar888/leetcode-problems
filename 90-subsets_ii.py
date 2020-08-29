"""
https://leetcode.com/problems/subsets-ii/

Strat:
    Apply the strat from Subset I and use a set.

Stats:
    Runtime: 28 ms, faster than 38.61% of Python online submissions for Subsets II.
    Memory Usage: 11.9 MB, less than 30.77% of Python online submissions for Subsets II.
"""

def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    powerset = []  # used to store all sets
    for i in range(1 << len(nums)):  # iterate 2^sets
        subset = []
        for j in range(len(nums)):
            # checking if the j-th bit of i is 1
            if (i & (1 << j)):
                # if is a match, add the j-th position element to subset
                subset.append(nums[j])

        subset = sorted(subset)
        if subset not in powerset:
            powerset.append(subset)

    return(powerset)
