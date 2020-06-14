"""
https://leetcode.com/problems/jewels-and-stones/

"""
class Solution(object):
    
    """
    Strat: 
        Make a set to store occurances for each jewel. Then, iterate through each stone
        to see if it is a jewel.

    Stats: O(J + S) time, O(J) space -- iterate thru J and S + set of size J to store Jewels
        Runtime: 36 ms, faster than 6.54% of Python online submissions for Jewels and Stones.
        Memory Usage: 12.7 MB, less than 76.19% of Python online submissions for Jewels and Stones.
    """
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set()
        for jewel in J:
            jewels.add(jewel)
        
        num_jewels = 0
        for stone in S:
            if stone in jewels:
                num_jewels += 1
        
        return num_jewels
    
    """
    (it is apparently faster if you actually do a brute force and not make a dictionary)
    
    Stats: O(J * S) time, O(1) space
        Runtime: 20 ms, faster than 69.03% of Python online submissions for Jewels and Stones.
        Memory Usage: 12.8 MB, less than 36.28% of Python online submissions for Jewels and Stones.
    """
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([1 for s in S if s in list(J)])