"""
Write a function to find the longest common prefix string amongst an array of strings.

Strat:
    Iterate through the array once to find the shortest word; this is the most letters 
    we'll need to iterate. Then loop through array to see if the common prefix
    holds for all array elements. Return once there's a violation.

Stats:
    Runtime: 8 ms, faster than 99.97% of Python online submissions for Longest Common Prefix.
    Memory Usage: 12.8 MB, less than 6.25% of Python online submissions for Longest Common Prefix.

Runtime:
    O(n*s), where n is the number of elements in the array & s is the length of the shortest word in the array

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        
        if len(strs) == 0:
            return common_prefix
        
        #find the length of the shortest word
        #this lets us know the max number of times we have to iterate over the rest of the words
        prefix_count = 9999999
        for word in strs:
            if len(word) < prefix_count:
                prefix_count = len(word)
                
        for i in range(prefix_count):
            char_in_consideration = strs[0][i]
            
            for word in strs:
                if (word[i] != char_in_consideration): #is not a common prefix
                    return common_prefix
            
            common_prefix += char_in_consideration
        
        return common_prefix