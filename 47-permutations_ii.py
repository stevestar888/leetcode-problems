"""
https://leetcode.com/problems/permutations-ii/

Strat: Same idea as Permutations I, just use a dictionary (can't use set unfortunately)
    to make sure you don't store duplicates.

Stats: O(n!) time, O(n!) space -- we make n-1 recursive calls on every level, where 
    n is the # of digits
    Runtime: 500 ms, faster than 15.37% of Python online submissions for Permutations II.
    Memory Usage: 12.7 MB, less than 95.65% of Python online submissions for Permutations II.

"""
class Solution(object):
    result = {}
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = {}
        self.helper(nums, [])
        return self.result.keys()
        
    def helper(self, nums, result):
        if len(nums) == 0: #no more numbers to choose (therefore result is full)
            self.result[tuple(result)] = 0 #add finished permutation 
        
        # generate all possible permutations, using i as the first/next digit
        for i, num in enumerate(nums):
            #create copies
            new_list = nums[:i] + nums[i + 1:] #copy of list, excluding nums[i]
            new_result = result[:]
            
            # pick and store a number
            choosen_num = nums[i]
            new_result.append(choosen_num)
            
            self.helper(new_list, new_result)