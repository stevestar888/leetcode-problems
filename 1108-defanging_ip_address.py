"""
https://leetcode.com/problems/defanging-an-ip-address/submissions/

Strat: 
    Iterate through address & build the return string as you go.

"""
class Solution(object):
    """    
    Runtime: 8 ms, faster than 99.53% of Python online submissions for Defanging an IP Address.
    Memory Usage: 12.8 MB, less than 22.53% of Python online submissions for Defanging an IP Address.
    """
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = ""
        
        for char in address:
            if char == ".":
                result += "[.]"
            else:
                result += char
        
        return result
    
    
    """
    According to comments, doing += on a string builds a new string, which makes sense, because
    strings are immutable. So here, we connect all the chars and then join them at the end.
    
    Runtime: 12 ms, faster than 95.63% of Python online submissions for Defanging an IP Address.
    Memory Usage: 12.6 MB, less than 86.26% of Python online submissions for Defanging an IP Address.
    """
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        #Constants
        FANGED_IP = "."
        DEFANGED_IP = "[.]"
        
        result = []
        
        for char in address:
            if char == FANGED_IP:
                result.append(DEFANGED_IP)
            else:
                result.append(char)
        
        return "".join(result)
        
        
    """
    Of course you can also do this--"One liners", right?
    """
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")
