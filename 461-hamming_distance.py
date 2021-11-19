"""
https://leetcode.com/problems/hamming-distance/

Organic solution + clever bit shift
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # find the binary rep. for x & y
        # need to chop off the '0b' part
        binary_x = bin(x)[2:]
        binary_y = bin(y)[2:]
        
        # prepend x or y with 0s if they are different lengths
        max_digits = max(len(binary_x), len(binary_y))
        min_digits = min(len(binary_x), len(binary_y))
        
        if len(binary_x) > len(binary_y):
            binary_y = "0" * (max_digits - min_digits) + binary_y
        elif len(binary_x) < len(binary_y):
            binary_x = "0" * (max_digits - min_digits) + binary_x
        #don't do anything in the same # of digits case
        
        # add up all non-matches
        return sum([1 for i in range(max_digits) if binary_x[i] != binary_y[i]])
    
    
    """
    From https://leetcode.com/problems/hamming-distance/discuss/1546370/Python-XOR-explained
    """
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # only non-matches will remain as 1
        xor = x ^ y

        # iterate through all digits and add to diffs if the digit is 1
        diffs = 0
        while xor:
            diffs += xor & 1
            xor >> 1

        return diffs
