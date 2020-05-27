"""
https://leetcode.com/problems/first-missing-positive/

Strat: 
    A trick to do this in constant space: store extra info using the sign of each number. 
    We iterate through nums, marking nums[num] as neg if we've seen it before. However,
    before anything, we have to do some preprocessing, i.e., turn negative numbers into
    a number that cannot be the first missing positive (using N + 1, which is slightly larger
    than the size of the array) accomplishes this nicely. Now we just have to make sure 
    we ar checking between 0 < abs(num) ≤ N on each iteration.

Runtime: O(n) time, O(1) space -- we take three pass through nums + in place modification
    Runtime: 16 ms, faster than 97.75% of Python online submissions for First Missing Positive.
    Memory Usage: 12.6 MB, less than 5.88% of Python online submissions for First Missing Positive.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        
        if N == 0:
            return 1
        
        #replacing neg numbers
        nums = [num if num > 0 else N + 1 for num in nums]
        
        #mark nums[num] neg to indicate we've seen the num
        for num in nums:
            num = abs(num)
            #ensure we're within the range of nums
            if num <= N and num > 0:
                nums[num - 1] = -abs(nums[num - 1])
            
        print(nums)
        for i, num in enumerate(nums):
            if num >= 0: #there's a missing positive if the num is positive
                return i + 1
        return N + 1
    
      ### Or here's a really fast, but not guranteed O(n) method
#     def firstMissingPositive(self, nums):
#         i = 1
#         while True:
#             if i not in nums:
#                 return i
#             i += 1
        