"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Strat:
    Swap each individual word component of the given string. 

Stats: O(n) / linear time, O(n) / linear space

"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #make sure our string is not empty
        if not s:
            return ""
        
        s = list(s)
        
        word_index = 0 #keeps track of the start of a word
        ptr1, ptr2, = 0, 0
        while ptr2 < len(s):
            #advance the pointers to the correct locations
            if word_index < len(s):
                ptr1 = ptr2 = word_index
                while ptr2 + 1 < len(s) and s[ptr2 + 1] != " ":
                    ptr2 += 1
            else:
                break
            
            #store where the next word begins (ptr2 points at the last char, so go
            #2 chars after ptr2)
            word_index = ptr2 + 2
            
            #begin swapping and close in
            while ptr1 < ptr2:
                s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
                ptr1 += 1
                ptr2 -= 1
            
            # print("".join(s))
        return "".join(s)