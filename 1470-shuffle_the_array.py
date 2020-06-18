"""
https://leetcode.com/problems/shuffle-the-array/submissions/

old: 2,5,1,3,4,7
new: 2,3,5,4,1,7
"""
class Solution(object):
    """
    O(n) time, O(n) space
    
    Runtime: 48 ms, faster than 81.20% of Python online submissions for Shuffle the Array.
    Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Shuffle the Array.
    """
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n + i])
        
        return result
    
    """
    O(n) time, O(1) space
    "jumping" and multiplying by -1 to detect cycles

    Strat: There also faster ways to do this, but asymptotically this code is still O(n). 
        For every element except the first and last (because those always stay in the same 
        place), we find its "intended" location:
        • if the index is in range (0, n/2 -1) --> index ends up on even indicies (2 * i)
        • if the index is in range (n/2, n) --> ends up on odd indicies (1 + 2*(i-n))

        Before we evict the num at the intended index, we save it. That num will now be
        our new target to find a home for. We repeat evictions for length - 2 times.
        
        The caveat is you might hit a cycle when evicting numbers and jumping to their 
        indicies. A fix for this is to mark each index that has been "completed" with -1. 
        Mulitplying by -1 at the very end will revert it back to its original value. (This 
        idea is also used for many other problems where you have to design a solution in-place.)
        
    Other ways to get O(1) space:
        • swaps: https://leetcode.com/problems/shuffle-the-array/discuss/684649/O(n)-Time-O(1)-Space-No-bitwise-cheating-beats-99.7-time-and-beats-100-space
        OR https://leetcode.com/problems/shuffle-the-array/discuss/675007/Python-O(1)-space-detailed-explanation
        • bitwise operations: https://leetcode.com/problems/shuffle-the-array/discuss/674947/O(1)-space-O(n)-time-detailed-explanation
    
    Stats:
        Runtime: 48 ms, faster than 81.20% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Shuffle the Array.
    """
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        length = 2 * n
        count = 0 #ensure we do the right # of replaces
        pointer = 0 #keep track of the next index to look if we've entered a cycle
        
        prev_index, prev_val = 1, nums[1] #start in index 1
        new_index, new_val = 0, 0
        while (count < length - 2): #don't replace 1st and last
            #find new index
            if prev_index < n:
                new_index = prev_index * 2
            else: 
                new_index = 1 + 2 * (prev_index - n)
                    
            #make sure we're not in a cycle
            if nums[new_index] < 0:
                #increase our pointer to keep inching forward & update index/value
                pointer += 1
                prev_index, prev_val = pointer, nums[pointer]
                continue
            
            #update and replace
            new_val = prev_val
            prev_val = nums[new_index] 
            nums[new_index] = -new_val
            prev_index = new_index

            count += 1
        
        #now we've visited every element (except first & last), reverse signs
        for i in range(1, length - 1):
            nums[i] = -nums[i]
            
        #can also do:
        # nums = map(lambda x: abs(x), nums)
        
        return nums