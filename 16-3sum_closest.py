"""
https://leetcode.com/problems/3sum-closest/submissions/

Stats:
    Runtime: 500 ms, faster than 6.73% of Python online submissions for 3Sum Closest.
    Memory Usage: 12.7 MB, less than 64.13% of Python online submissions for 3Sum Closest.
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        def update_closest(num):
            """
            Returns how close num is to the target
            """
            #TODO - can subtract target from both sides??
            if abs(target - num) < abs(target - self.closest):
                self.closest = num
        #--------------end helper function--------------

        length = len(nums)
        self.closest = float('inf')
        
        nums = sorted(nums) #sort nums
        
        #base_num points stays at elem while other 2 pointers move;
        #while base_num is at i, do 2 pointer search on nums[i+1:length] 
        for i, base_num in enumerate(nums):
            if i > length - 2: #don't have 3 pointers anymore
                break
            
            lo = i + 1
            hi = length - 1
            
            while lo < hi:
                sum_of_ptrs = base_num + nums[lo] + nums[hi]
                
                if sum_of_ptrs == target:
                    return target #found the exact sum
                
                #update closest
                update_closest(sum_of_ptrs) #see if we can do better
                
                #close our pointers in
                if sum_of_ptrs > target:
                    hi -= 1
                else:
                    lo += 1
        
        return self.closest
