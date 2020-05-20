"""
https://leetcode.com/problems/valid-anagram/

An anagram is a word made from another word using the same letters (assume alphanumberic lowercase)

Strat:
    1. iterate through string 1 -- put contents in a dictionary (max of 26) .... {key: letter, value: count}
    2. iterate through string 2 -- check if the i-th letter is in the dictionary.. count--; if not --> False
    3. string 2 was processed completely && OG dict is empty

Optimization: 
    Use an array of size 26 instead. Use the difference in ascii values as indicies (a=97, z=122):         
        [a - a] --> 97  - 97 = 0  (index to store 'a')
        [z - a] --> 122 - 97 = 25 (index to store 'z')
        
Runtime: O(n) time, O(1) space -- space won't exceed arr size 26 and only a few pass throughs
    Runtime: 48 ms, faster than 51.39% of Python online submissions for Valid Anagram.
    Memory Usage: 17.3 MB, less than 5.26% of Python online submissions for Valid Anagram.
"""

class Solution(object):
    
    ### Dictionary: O(n) time, O(1) space
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """      
        if len(s) != len(t):
            return False
        
        letters = {}
        
        #iterate through s (string 1)
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1 #increment by one

        #iterate through t (string 2)
        for letter in t:
            if letters.get(letter, -1) > 0: #in the dict
                letters[letter] = letters.get(letter) - 1 #decrement by one
            else: #not in dict
                return False        
        
        #now check if values are 0 for all keys
        for key, value in letters.items():
            print(key, value)
            if value != 0:
                return False
            
        return True
                

    ### Optimization: Use an array of size 26
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """      
        if len(s) != len(t):
            return False
        
        letters = [0 for i in range(26)]
        
        #iterate through s (string 1)
        for s_letter, t_letter in zip(s, t):
            letters[ord(s_letter) - ord('a')] += 1
            letters[ord(t_letter) - ord('a')] -= 1
        
        #all array entries should be 0 if we have a proper anagram
        for count in letters:
            if count != 0:
                return False
        
        #all counts match
        return True