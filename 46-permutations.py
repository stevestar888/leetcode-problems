"""
https://leetcode.com/problems/permutations/

Strat: 
    We generate by looking at all the digits we can still use. When we start off, it's 
    all the digits, and we'll add our choosen digit as the first elem in the permutation. 
    Then, one by one, we add the rest of the "choosen" digits to result array.

    When we don't have anymore digits to choose from, then we've finished generating
    that particular permutation.

Stats:
    Runtime: 28 ms, faster than 69.90% of Python online submissions for Permutations.
    Memory Usage: 12.7 MB, less than 84.51% of Python online submissions for Permutations.
"""

class Solution(object):
    result = []
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = [] #clear array on every iteration
        self.helper(nums, [])
        return self.result
        
    def helper(self, nums, result):
        if len(nums) == 0: #no more numbers to choose (therefore result is full)
            self.result.append(result) #add finished permutation 
        
        # generate all possible permutations, using i as the first/next digit
        for i, num in enumerate(nums):
            #create copies
            new_list = nums[:] 
            new_result = result[:]
            
            # pick and store a number
            choosen_num = new_list.pop(i) 
            new_result.append(choosen_num)
            
            self.helper(new_list, new_result)