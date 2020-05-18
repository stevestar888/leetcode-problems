"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Strat: We can use solve in constant space by employing a trick: store extra info using the
    sign of each number. As we iterate through each num, we set arr[num - 1] equal to its 
    negative, meaning that it's been "found". (Note: be careful not to reflip the sign if 
    we find it again.) At the end, if we find arr[num - 1] is positive, that means num+1 
    was never found. 
    
Stats: O(n) time, O(1) space -- no allocated array (in place) + 2 pass throughs
    Runtime: 344 ms, faster than 58.69% of Python online submissions for Find All Numbers Disappeared in an Array.
    Memory Usage: 20 MB, less than 38.46% of Python online submissions for Find All Numbers Disappeared in an Array.
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            n = abs(n)
            if nums[n-1] > 0:
                nums[n-1] = -nums[n-1] #flip sign to neg
            #else already neg, leave as is
    
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
        # ^functionally same as: 
        # ans = []
        # for i, n in enumerate(nums):
        #     if n > 0: #was not found (i.e., num disappeared)
        #         ans.append(i + 1)
        # return ans