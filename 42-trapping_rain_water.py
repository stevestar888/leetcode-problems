"""
https://leetcode.com/problems/trapping-rain-water/submissions/

Strat:
    Have a pointer that iterates through the array. For this pointer,
    if the element after it is bigger --> we'll "climb up", and
        not do anything with trapping water
    if the element after it is the same --> we'll increment the 
        pointer and keep going in our iteration
    if the element after it is smaller --> we potentially have a "hole",
        which we should find the "next max" for, meaning we need to find
        the ledge on the other side where the water will be trapped
        
    For the final case, finding where the water will be trapped requires 
    us to further iterate through the array, starting from the pointer,
    leading the overall runtime for this to be n^2, but constant space.
    
    The linear solution requries two pointers, one from the left and one
    from the right, both closing in. Here's something:
    https://github.com/bt-dot/LeetCode/blob/master/Arrays%20and%20Strings/trapRainWater.java
    
Stats: O(n^2) time, O(1) space -- iterate through the array, nested with finding the "next max"
    Runtime: 56 ms, faster than 29.90% of Python online submissions for Trapping Rain Water.
    Memory Usage: 13.2 MB, less than 64.48% of Python online submissions for Trapping Rain Water.

"""
class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(heights)
        pointer = 0
        result = 0
        
        #the min tiles required to store any water is 3 tiles
        #if we pass this check we're guranteed to have length > 2
        if length <= 2:
            return 0
        
        def find_next_max(index):
            """
            Finds the next biggest index
            """
            #try to find a tile as tall or taller than me
            pointer = index + 1
            biggest_yet = float('-inf')
            biggest_yet_index = 0

            while pointer < length:
                if heights[pointer] >= heights[index]:
                    return pointer
                else:
                    if heights[pointer] > biggest_yet:
                        biggest_yet = heights[pointer]
                        biggest_yet_index = pointer
                    pointer += 1
                    
            #since we couldn't find anything taller, return the next best alternative
            return biggest_yet_index
        
            
        def fill_water_in(max1, max2):
            """
            Given the ledges max1 and max2, update heights by filling it up to the 
            highest level of water; keep track of how much water we're filling in
            """
            # print("fill water between {} and {}".format(max1, max2))
            delta = 0
            water_level = min(heights[max1], heights[max2])
            
            #we want to look at all levels *between* max1 and max2
            #range is already inclusive
            for i in range(max1 + 1, max2):
                diff = water_level - heights[i]
                delta += diff
                heights[i] = water_level #fill in with dirt lol
            return delta
        
        
        #iterate pointer all the way through heights
        # (pointer + 1) is used because we're indexing into next elem
        # (length - 1) is used because we want to go up to the size of the arr
        while pointer + 1 < length:
            print(pointer)
            #if the next tile is the same level or a higher level, 
            #we want to advance and "climbing up", respectively
            if heights[pointer] <= heights[pointer + 1]:
                pointer += 1
                continue
            
            next_max = find_next_max(pointer)
            if next_max >= pointer:
                delta = fill_water_in(pointer, next_max)
                if delta:
                    result += delta
                else:
                    pointer = next_max #skip to next max (instead of pointer++)
                
        return result
