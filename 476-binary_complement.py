"""
https://leetcode.com/problems/number-complement/

Strat:
    Generate the complement's binary string using num. Convert that binary string back into an int.
    
Stats:
    Runtime: 16 ms, faster than 74.90% of Python online submissions for Number Complement.
    Memory Usage: 12.7 MB, less than 14.29% of Python online submissions for Number Complement.
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #iterate & generate binary string
        flippedBin = ""
        while (num > 0):
            remainder = num % 2

            #check remainder
            if remainder == 0: #divided in whole
                flippedBin = "1" + flippedBin #if converting to binary normally would add 0
            else: #remainder is 1
                flippedBin = "0" + flippedBin

            num = num >> 1 #divide by 2


        #convert the flippedBinary into int representation
        result = 0
        index = 0
        while (flippedBin): #has char left
            bit = flippedBin[-1] #get last bit

            if bit == '1':
                result += (1 << index) # multiply by 2
            flippedBin = flippedBin[:-1] #truncate
            index += 1 #increase power of 2
        
        return result
