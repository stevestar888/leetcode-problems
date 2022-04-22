"""
https://leetcode.com/problems/sum-of-even-numbers-after-queries/

O(n) / linear time — iteration over queries; all other operations are constant

Runtime: 507 ms, faster than 98.92% of Python3 online submissions for Sum of Even Numbers After Queries.
Memory Usage: 20.5 MB, less than 76.90% of Python3 online submissions for Sum of Even Numbers After Queries.
"""
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        running_even_sum = sum(num for num in nums if num % 2 == 0)
        res = list()
        
        # perform query operations
        for query in queries:
            value, idx = query
            
            if nums[idx] % 2 == 0:
                running_even_sum -= nums[idx]
            
            nums[idx] += value
            
            if nums[idx] % 2 == 0:
                running_even_sum += nums[idx]
            
            res.append(running_even_sum)
            
        return res
