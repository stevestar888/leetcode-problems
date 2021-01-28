"""
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

Strat:
    While you can still brute force to get the Dot Product (mutliple every number from each array), 
    the algorithmically more efficient way is to iterate through one array and find out which 
    indicies have non-zero values. Given indicies with non-zero values, multiple those with 
    corresponding values in the other array.
    
    Solution 1 is brute force.
    Solution 2 is using the more efficient method described above.
"""

# class SparseVector:
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
        

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec):
#         """
#         :type vec: 'SparseVector'
#         :rtype: int
#         """
#         ret = 0
#         for i in range(len(self.nums)):
#             if self.nums[i] != 0 and vec.nums[i] != 0:
#                 ret += self.nums[i]*vec.nums[i]
#         return ret
    

class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.non_zero_dict = {}
        
        for i, num in enumerate(nums):
            if num != 0:
                self.non_zero_dict[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        result = 0
        
        for key, val in self.non_zero_dict.items():
            if vec.non_zero_dict.get(key, 0): 
                result += val * vec.non_zero_dict.get(key, 0)
            
        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
