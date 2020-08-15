"""
https://leetcode.com/problems/3sum/

Really smart (and fast) solution: https://leetcode.com/problems/3sum/discuss/724777/Python-or-Beats-99-or-binary-search-or-no-two-pointer
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        length = len(nums)
        if length < 3: #cannot have answer if we don't even have 3 elems
            return []
        
        result = set() #stores our answers (e.g., [x, y, z])
        seen = set() #keeps track of which #s we're using as our "base"
        
        pointer = 0 #points to our "base" number
        for i in range(length - 2):
            # nums[i] stores sum so far
            
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])

            complements = {}
            for j in range(i + 1, length):
                sum_so_far = nums[i] + nums[j]
                #complement: nums[i] + nums[j] + -sum_so_far = 0
                
                if complements.get(-sum_so_far) > -1:
                    solution_set = tuple(sorted((nums[i], nums[j], -sum_so_far)))
                    result.add(solution_set)
                else:
                    complements[nums[j]] = complements.get(sum_so_far, 0) + 1
                
        return result
