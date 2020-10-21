"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/

Basket of “reverse”:
https://leetcode.com/problems/reverse-string/
https://leetcode.com/problems/reverse-string-ii/
https://leetcode.com/problems/reverse-words-in-a-string/
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Runtime: 24 ms, faster than 61.23% of Python online submissions for Largest Substring Between Two Equal Characters.
Memory Usage: 13.3 MB, less than 55.07% of Python online submissions for Largest Substring Between Two Equal Characters.
"""
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        #store the index for each letter's occurence
        first_occur = {}
        
        best = 0
        
        for i, char in enumerate(s):
            found = first_occur.get(char, None)
            print(i, found)
            if found != None: #calc current substring length
                best = max(best, i - found)
            else:
                first_occur[char] = i
            
        #subtract 1 to account for indexing
        return best - 1