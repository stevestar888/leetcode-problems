"""
https://leetcode.com/problems/add-strings/

Strat:
    Essentially writing `return str(int(num1) + int(num2))`. Use 2 pointers that 
    start from the right side of num1 and num2. First, you'll add the ones, then
    tens, then hundreds, etc. Note: the carry logic can be tricky.
    
    
Stats: O(n) / linear time, O(n) / linear space -- n is max(len(num1), len(num2))
    Runtime: 64 ms, faster than 16.05% of Python online submissions for Add Strings.
    Memory Usage: 13.4 MB, less than 99.54% of Python online submissions for Add Strings.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        NUMS = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}

        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        result = []
        carry = False
        
        while p1 >= 0 or p2 >= 0 or carry:
            curr_sum = 0
            
            if p1 >= 0:
                curr_sum += NUMS[num1[p1]]
                p1 -= 1
                
            if p2 >= 0:
                curr_sum += NUMS[num2[p2]]
                p2 -= 1
            
            curr_sum += carry
            
            if curr_sum >= 10: 
                #carry again
                carry = True
                curr_sum -= 10
            else:
                #no carry
                carry = False
                
            result.append(str(curr_sum))
            
        #reverse result
        result = result[::-1]
        
        #join chars into string
        return "".join(result)
