"""
https://leetcode.com/problems/daily-temperatures/

Strat:
    There are two good approaches, both in linear time. The stack method requires additional 
    space, while the counting backwards is constant space.

Stats:
    The best runtime is O(n) and best space is O(w), where w is the range of temperatures.
    In this case, all temperatures are within the reasonable 30 deg F and 100 deg F, so 
    O(w) <= 71. 
"""
class Solution(object):
    """
    Stack approach:
        As you iterate through the temperatures, pop the top elem off if the temperature
        is less than your current temp. Naturally, the hottest temperatures will migrate
        to the bottom. Ever time we pop, we calculate the how long the temp has been sitting
        in the stack (i.e., take the current index - the index of the temp we just popped).
    
    O(n) time, O(w) space -- iterate through all elems once + keep a stack with max height w
        Runtime: 488 ms, faster than 52.40% of Python online submissions for Daily Temperatures.
        Memory Usage: 20.9 MB, less than 6.67% of Python online submissions for Daily Temperatures.
    """
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        #a stack storing the hottest temps
        temps_stack = []
        
        #the array storing results
        result = [0] * len(T)
        
        for i, temp in enumerate(T):
            #only pop if the stack is NOT empty & our current elem is bigger than the top of the stack
            while temps_stack and temp > temps_stack[-1][0]: #[-1][0] accesses the top elem's temp
                popped_temp, popped_temp_index = temps_stack.pop()
                
                #calculate how many days we need to wait until a hotter day
                days_until_warmer = i - popped_temp_index
                
                #store days_needed_until_a_warmer_day at index_of_og_temp
                result[popped_temp_index] = days_until_warmer
            
            #regardless of if we pop, add (temp, index) to stack
            temps_stack.append((temp, i))
            
        return result
    
    """
    Counting backwards approach
    
    O(n) time, O(1) space -- iterate through all elems + keep track of nothing but vars (not counting return arr size)
        Runtime: 400 ms, faster than 99.89% of Python online submissions for Daily Temperatures.
        Memory Usage: 16.3 MB, less than 51.11% of Python online submissions for Daily Temperatures.

    From: https://leetcode.com/problems/daily-temperatures/discuss/397728/Easy-Python-O(n)-time-O(1)-space-beat-99.9
    """
    def dailyTemperatures(self, T):
        right_max = float('-inf')
        length = len(T)
        result = [0] * length
        
        for i in range(length - 1, -1, -1): #iterate from right to left
            t = T[i]
            
            #see if we can update the max so far
            if right_max <= t:
                right_max = t
            else:
                days = 1
                while T[i+days] <= t:
                    days += result[i+days]
                result[i] = days #store days
        return result
