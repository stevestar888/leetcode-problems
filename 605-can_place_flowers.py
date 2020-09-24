"""
#TODO solve later

Best solution: https://leetcode.com/problems/can-place-flowers/discuss/466172/Python-*Very*-Straightforward-Solution-90
"""
class Solution(object):
    """
    doesn't work right now
    """
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        curr_empty = 0
        for i, slot in enumerate(flowerbed):
            #need one less because we're at the begn or end
            if i == 0 and slot == 0:
                curr_empty += 1
                
            if i == len(flowerbed) - 1 and slot == 0:
                curr_empty += 1
            
            if slot == 0:
                curr_empty += 1
            else: # slot == 1:
                curr_empty = 0
                
            if curr_empty == 3:
                n -= 1
                curr_empty = 1
                    
        return n <= 0
