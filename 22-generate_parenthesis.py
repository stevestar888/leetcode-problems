"""
https://leetcode.com/problems/generate-parentheses/

Strat:
    At any point in time, to have a "well formed parenthesis" we must have more
    open parenthesis than close ones. The open parenthesis also must come before.
    These two conditions are reflected when we see if we can add an open parenthesis:
        When can we add an open parenthesis?
            as long as we have less than n open parenthesis
        When can we add a close parenthesis?
            as long as we have more open parenthesis than closed ones
    
    Solve with backtracking. Keep track of how many open and close parenthesis we
    have remaining (called open_paren_left and closed_paren_left in code). When 
    we have depleted both, add it to the result array. Otherwise, recursively call
    generate(), modifying the argument. We are using backtracking because the actual
    values of arguments didn't get modified; the values passed into generate() are
    different, but when we're out of the if statement, the value of string, 
    open_paren_left, and closed_paren_left are unchanged. This is effectively the same
    as if we did:
        string += "("
        open_paren_left -= 1
        generate(string, open_paren_left, closed_paren_left)
        string[:-1]
        open_paren_left += 1
    
Stats:
    Runtime: 24 ms, faster than 69.98% of Python online submissions for Generate Parentheses.
    Memory Usage: 12.8 MB, less than 72.66% of Python online submissions for Generate Parentheses.
"""
class Solution(object):
    """
    Inspired from leetcode solution
    """
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
            
        def generate(string, open_paren_left, close_paren_left):
            #base case
            if open_paren_left == close_paren_left == 0:
                result.append(string)
                
            #see if we can add an open parenthesis
            if open_paren_left > 0:
                generate(string + '(', open_paren_left - 1, close_paren_left)
                
            #see if we can add a close parenthesis
            if close_paren_left > open_paren_left:
                generate(string + ')', open_paren_left, close_paren_left - 1)

        generate("", n, n)
        return result
    
    
    """
    #TODO
    Weird recursive technique double for loop that doesn't work,
    doesn't use backtracking
    """
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         result = []
#         def generate(string, open_paren_left, close_paren_left):
#             #base case: reached fully formed parentheses
#             if open_paren_left == close_paren_left == 0:
#                 result.append(string)
            
#             #have to close up to left_to_close parentheses
#             parens_to_close = close_paren_left - open_paren_left

#             if parens_to_close == 0:
#                 #just generate the open parens    
#                 for i in range(1, open_paren_left + 1): #will use i of "("
#                     string = string + "(" #sucessively add a '('
#                     print(string)
#                     generate(string, open_paren_left, close_paren_left - i)
#             else:
#                 for i in range(1, open_paren_left + 1): #can add on up to i of "("
#                     for j in range(1, parens_to_close + 1): #can add on up to j of ")"
#                         new_string = string + ")" * j + "(" * i
#                         print(new_string)
#                         generate(new_string, open_paren_left - j, close_paren_left - i)
#         generate("", n, n)
#         return result
