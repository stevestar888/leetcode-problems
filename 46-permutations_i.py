"""
https://leetcode.com/problems/permutations/

Strat:
    We generate by looking at all the digits we can still use. When we start off, it's 
    all the digits, and we'll add our choosen digit as the first elem in the permutation. 
    Then, one by one, we add the rest of the "choosen" digits to result array.

    When we don't have anymore digits to choose from, then we've finished generating
    that particular permutation.
    (iterative: https://leetcode.com/problems/permutations/discuss/431726/Beats-99-in-O(n-*-n!)-with-an-iterative-approach-in-Python)
    
Stats:
    Runtime: 32 ms, faster than 43.85% of Python online submissions for Permutations.
    Memory Usage: 12.7 MB, less than 75.51% of Python online submissions for Permutations.
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
        
    def helper(self, nums_remaining, curr_permutation):
        if len(nums_remaining) == 0: #no more numbers to choose (therefore result is full)
            self.result.append(curr_permutation) #add finished permutation 
        
        # generate all possible permutations, using i as the chosen digit
        for i, num in enumerate(nums_remaining):
            #create copies
            new_list = nums_remaining[:i] + nums_remaining[i + 1:]
            new_permutation = curr_permutation[:]
            
            # pick and store a number
            chosen_num = nums_remaining[i]
            new_permutation.append(chosen_num)
            
            self.helper(new_list, new_permutation)
        