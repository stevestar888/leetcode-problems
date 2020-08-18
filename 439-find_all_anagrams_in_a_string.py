"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

(Is pretty similar to 567. Permutation in String)

Strat: 
    Sliding window. See explaination from 567.

Stats: O(s + p) time, O(1) space -- one pass in both arrays + storing up to 26 letters in each array
    Runtime: 80 ms, faster than 94.67% of Python online submissions for Find All Anagrams in a String.
    Memory Usage: 13.6 MB, less than 94.25% of Python online submissions for Find All Anagrams in a String.
"""
class Solution(object):
    def findAnagrams(self, string, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        letters_needed = [0] * 26
        for letter in p:
            letters_needed[ord(letter) - ord('a')] += 1
            
        curr_window = [0] * 26
        for i, letter in enumerate(string):
            #add to window
            curr_window[ord(letter) - ord('a')] += 1
            
            #delete from window (once curr_window is long enough)
            if i >= len(p):
                letter_to_remove = string[i - len(p)]
                curr_window[ord(letter_to_remove) - ord('a')] -= 1
            
            #compare window with target window
            if curr_window == letters_needed:
                anagram_start_idx = i + 1 - len(p) #same as i - (len(p) - 1)
                result.append(anagram_start_idx)

        return result