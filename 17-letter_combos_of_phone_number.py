"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Strat:
    DFS on each digit
    
Stats: 
    (from leetcode) 3^n * 4*m, where N is the number of digits in the
    input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is the 
    number of digits in the input that maps to 4 letters (e.g. 7, 9), 
    and N+M is the total number digits in the input.
    
    Runtime: 20 ms, faster than 46.69% of Python online submissions for Letter Combinations of a Phone Number.
    Memory Usage: 13.4 MB, less than 92.64% of Python online submissions for Letter Combinations of a Phone Number.
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        LETTER_MAP = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def helper(str_so_far, idx_so_far):
            # base case
            if idx_so_far >= len(digits):
                result.append(str_so_far)
                return

            # recursive case
            digit = digits[idx_so_far]
            mapping = LETTER_MAP[digit]

            for letter in mapping:
                helper(str_so_far + letter, idx_so_far + 1)
        # --------------end helper function--------------
        
        result = []
        
        if digits == "":
            return result
        
        helper("", 0)
        return result
