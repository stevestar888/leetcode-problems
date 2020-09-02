"""
https://leetcode.com/problems/add-binary/
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """        
        a_len, b_len = len(a), len(b)
        a_ptr, b_ptr = a_len - 1, b_len - 1
        carry = 0
        result = []
        
        for _ in range(max(a_len, b_len) + 1):
            if a_ptr >= 0:
                if a[a_ptr] == "1":
                    carry += 1
                a_ptr -= 1
                
            if b_ptr >= 0:
                if b[b_ptr] == "1":
                    carry += 1
                b_ptr -= 1
            
            print(carry)
            
            if carry == 3:
                result.append("1")
                carry -= 2
            elif carry == 2:
                result.append("0")
                carry -= 1
            elif carry == 1:
                result.append("1")
                carry -= 1
            else:
                result.append("0")
        
        #check for the leading 0
        if result[-1] == "0":
            result.pop()
        
        #reverse result
        result = result[::-1]
        
        #join chars into string
        return "".join(result)
