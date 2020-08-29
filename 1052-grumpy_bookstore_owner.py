"""
https://leetcode.com/problems/grumpy-bookstore-owner/

Strat:
    From a high level approach, we want to find the period of duration X 
    where there are the maximum losses, because they will be compensated 
    for later. We will use sliding window to do this.

Notes:
    Bruce thought of something interesting: we can think of the problem
    where grumpy means the number is negative, and you are trying to max
    the array.

0 = not grumpy
1 = grumpy 
"""
class Solution(object):
    """
    TODO: not sliding window code doesn't run...
    """
    def maxSatisfied(self, customers, grumpy, max_ungrumpy):  
        #changed param: X -> max_ungrumpy
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        NOT_GRUMPY = 0
        IS_GRAUMPY = 1
        
        running_sum = 0
        max_sum_so_far = float('-inf')
        max_sum_idx = -1
        for i, customer in enumerate(customers):
            #add to our window
            running_sum += customer
            
            #reduce window size (when window size is ≥ max_ungrumpy)
            if i >= max_ungrumpy:
                elem_to_subtract = customers[i - max_ungrumpy]
                running_sum -= elem_to_subtract
                     
            #best index to take will be index where running_sum is largest        
            if running_sum > max_sum_so_far:
                #tells us to be ungrumpy start at i, because
                #customers[i:i + max_ungrumpy] maximizes running_sum
                max_sum_so_far = running_sum
                max_sum_idx = i - (max_ungrumpy - 1) #-1 to deal w/ indexing
                     
        # print(max_sum_idx)
        result = 0
        for i, customer in enumerate(customers):
            #if i is within range of ungrumpy, take all elems
            if max_sum_idx <= i <= max_sum_idx + (max_ungrumpy - 1):
                result += customer
            elif grumpy[i] == NOT_GRUMPY:
                result += customer
                
        return result
