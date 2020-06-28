import heapq

"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

Strat: Use a heap. Building it with the built-in library (documentation:
    https://docs.python.org/2/library/heapq.html#heapq.heapify). After it's
    built, just remove (nums - k) numbers from it. The last number you 
    remove will be the k-th largest number.

Can also use QuickSelect, with average runtime of O(n), but it's not guranteed
    https://en.wikipedia.org/wiki/Quickselect
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums) #turn nums from a list into a min heap
        
        for _ in range(len(nums) + 1 - k):
            elem = heapq.heappop(nums)
        
        return elem
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums) 
        
        k_largest = heapq.nlargest(k, nums) #grab the list of k largest nums
        return k_largest[-1] #last elem of nlargest
    
    
"""
A nice quick select I found
"""
# from random import randint

# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         def partition(p, r):
#             x = nums[r]
#             i = p-1
#             for j in range(p,r):
#                 if nums[j] < x:
#                     i += 1
#                     nums[i], nums[j] = nums[j], nums[i]
#             nums[i+1],nums[r] = nums[r], nums[i+1]    
#             return i+1
        
#         def random_partition(p,r):
#             ri = randint(p,r)
#             nums[ri], nums[r] = nums[r], nums[ri]
#             return partition(p, r) 
            
#         def select(p, r, k):
#             if p == r:
#                 return nums[p]
#             q = random_partition(p, r)
#             i = q-p+1
#             if i == k:
#                 return nums[q]
#             elif k < i:
#                 return select(p, q-1, k)
#             else:
#                 return select(q+1, r, k-i)

#         return select(0, len(nums)-1, len(nums)-k+1)   



sol = Solution().findKthLargest([1,4,6,3,2], 2)
print(sol)