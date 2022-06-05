"""
https://leetcode.com/problems/can-place-flowers/
"""

class Solution:
    """
    Be greedy: plant at the first occasion you can; update flowerbed if planted.

    Runtime: 185 ms, faster than 70.51% of Python3 online submissions for Can Place Flowers.
    Memory Usage: 14.4 MB, less than 75.14% of Python3 online submissions for Can Place Flowers.
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed) - 1):
            #check if able to plant
            if flowerbed[i] == flowerbed[i - 1] == flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
                
                if n == 0:
                    return True
            
        return False
    
    
    
    """
    Inspired by https://leetcode.com/problems/can-place-flowers/discuss/184330/Python-easy-solution-beats-100 (some of the comments are funny)
    
    Basically, you need three 0s in a row to plant a flower.
    
    Runtime: 212 ms, faster than 52.12% of Python3 online submissions for Can Place Flowers.
    Memory Usage: 14.6 MB, less than 29.00% of Python3 online submissions for Can Place Flowers.
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        count = 1
        for flower in flowerbed:
            if flower == 0:
                count += 1
            else:
                count = 0
                
            if count == 3:
                n -= 1
                count = 1
            
            if n == 0:
                return True
        
        return False
