"""
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

Strat:
    First split on spaces to form your array of words. Iterate through all words to see 
    if any of those match the search_word.
    
Stats: O(n) / linear time, O(n) / linear space
    Iterate through ever word in the sentence + allocate array space for every word in sentence
    
    #TODO space can be improved if you don't split the array
"""
class Solution(object):
    """
    Try #1
    """
    def isPrefixOfWord(self, sentence, search_word):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        word_list = sentence.split(" ")
        search_word_len = len(search_word)
        
        for i, word in enumerate(word_list, 1): #enumerate starting at index 1
            #sure our word is long enough to contain search_word
            if len(word) < search_word_len:
                continue
            
            #check if we have a match
            if word[:search_word_len] == search_word:
                return i
        return -1
    
    
    """
    Same logic, just using startswith() so the code is a little cleaner
    
    Runtime: 16 ms, faster than 81.95% of Python online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
    Memory Usage: 12.6 MB, less than 90.00% of Python online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.

    """
    def isPrefixOfWord(self, sentence, search_word):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        word_list = sentence.split(" ")
        search_word_len = len(search_word)
        
        for i, word in enumerate(word_list, 1): #enumerate starting at index 1
            if word.startswith(search_word):
                return i
        return -1
