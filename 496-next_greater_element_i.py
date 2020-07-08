"""
https://leetcode.com/problems/next-greater-element-i/

Strat: Preprocess nums2 so we are able to get the index for any num in nums1 in constant time.
    (The preprocessing will take O(n) time.) Next, iterate through all nums in nums1; using 
    the preprocessed dictionary, we can look up the index of the num we need to find the 
    next greatest value for in constant time. Once found, iterate through the rest of nums2
    to find the next greatest value.
    
Stats: O(n^2) time??
    Runtime: 68 ms, faster than 30.73% of Python online submissions for Next Greater Element I.
    Memory Usage: 12.9 MB, less than 64.20% of Python online submissions for Next Greater Element I.

Good solutions:
    https://leetcode.com/problems/next-greater-element-i/discuss/563496/2-solutions-or-Easy-to-Understand-or-Faster-than-99.5-or-Simple-or-Python-Solution
    OR
    https://github.com/bt-dot/LeetCode/blob/master/Stack%20and%20Queue/nextGreaterValueI.js
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        #preprocess nums2 so we know the index for any given element
        positions = {}
        for i, num in enumerate(nums2):
            positions[num] = i
        
        #now identify the next greatest elem for all nums in nums1
        result = []
        for num in nums1:
            num2_pos = positions[num]
            
            next_greatest = -1
            for i in range(num2_pos, len(nums2)):
                if nums2[i] > num:
                    next_greatest = nums2[i]
                    break
            result.append(next_greatest)
            
        return result
