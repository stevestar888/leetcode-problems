"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

Strat:
    Keep track of the prev element's value as well as the next index to insert. The
    prev value helps us keep track of if we've see the number before, and the insert_index
    tells us where to insert a new number. 
    
    So iterate through nums. If the current num is greater than one we've seen before, we 
    update nums at position insert_index.

Stats: O(n) time, O(1) space -- one pass thru nums + modifying in-place 
    Runtime: 60 ms, faster than 97.83% of Python online submissions for Remove Duplicates from Sorted Array.
    Memory Usage: 14.5 MB, less than 55.45% of Python online submissions for Remove Duplicates from Sorted Array.

Godsent solutions:
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11780/5-lines-C%2B%2BJava-nicer-loops
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = float('-inf')
        insert_index = 0
        
        for num in nums:
            if num > prev:
                #found a bigger number
                nums[insert_index] = num
                insert_index += 1
            
            prev = num
        
        return insert_index
            
