class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #base cases
        if text1 == "":
            return 0
        if text2 == "":
            return 0

        #recursive cases
        if text1[0] == text2[0]: 
            #if the char matches
            return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        else: 
            #if the chars don't match
            call1 = self.longestCommonSubsequence(text1[1:], text2)
            call2 = self.longestCommonSubsequence(text1, text2[1:])
            return max(call1, call2)        
        