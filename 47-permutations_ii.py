"""
https://leetcode.com/problems/permutations-ii/

Strat: Same idea as Permutations I, just use a dictionary (can't use set unfortunately)
    to make sure you don't store duplicates.

Stats: O(n!) time*, O(n!) space -- we make n-1 recursive calls on every level, where 
    n is the # of digits
    Runtime: 500 ms, faster than 15.37% of Python online submissions for Permutations II.
    Memory Usage: 12.7 MB, less than 95.65% of Python online submissions for Permutations II.

*A note on runtime:
    The number of recursive calls cannot equal the number of permutations, since a permutation is 
    produced only when the recursion hits the base case. Notice that you have 24 = 4! calls of size 1, 
    i.e. 4! calls where you hit a base case and a permutation is completed/generated. However, the 
    growth *rate* of the number of recursive calls (remember, asymptotic analysis is all about growth) is O(n!):

    list of size 1 generates 1 call = 1 call
    list of size 2 generates 1 call + 2 calls on lists of size 1 = 1 + 2(1) = 3 (about 2 times as many as size 1)
    list of size 3 generates 1 call + 3 calls on lists of size 2 = 1 + 3(3) = 10 (about 3 times as many as size 2)
    list of size 4 generates 1 call + 4 calls on lists of size 3 = 1 + 4(10) = 41 (about 4 times as many as size 3)
    list of size 5 generates 1 call + 5 calls on lists of size 4 = 1 + 5(41) = 206 (about 5 times as many as size 4)
    list of size 6 generates 1 call + 6 calls on lists of size 5 = 1 + 6(206) = 1237 (about 6 times as many as size 5)
    etc.

    So, the number of calls, although not exactly n!, is growing at a factorial rate.
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