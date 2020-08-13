"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Solution in 8 languages, using functional programming:
https://www.youtube.com/watch?v=gZLZPrgqw2A&feature=youtu.be
"""
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_count(n):
            digits = 0
            while n > 0:
                n //= 10 #floor divide by 10
                digits += 1
            
            return digits
        
        result = 0
        for num in nums:
            if digit_count(num) % 2 == 0:
                result += 1
                
        return result
    
    """
    One liner :)
    """
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(1 for num in nums if len(str(num)) % 2 == 0)