"""
https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/

Strat: 
    Iterate through order to build up a Data Structure that stores rank. Afterwards,
    iterate through every word in words and check if they comply, letter by letter.
    Careful of the edge case where one word has the same letters as the next but 
    is shorter in length, e.g., 'app' vs 'apple'.

Stats: 
    Runtime: 24 ms, faster than 75.56% of Python online submissions for Verifying an Alien Dictionary.
    Memory Usage: 12.9 MB, less than 31.84% of Python online submissions for Verifying an Alien Dictionary.
"""
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def get_rank(letter):
            """
            Helper func that returns the rank of a given alien letter, from 1 to 26
            """
            return alphabet[ord(letter) - ord('a')]
        
        #if we just have one word, no need to check order
        if len(words) < 2:
            return True
        
        #build the alien alphabet; will be used by get_rank()
        alphabet = [0] * len(order)
        for i, letter in enumerate(order):
            #letter has a rank of i
            #the lower the i, the earlier it appears
            alphabet[ord(letter) - ord('a')] = i
        
        #iterate through words to see if they are sorted relative to each other        
        for ptr in range(1, len(words)):
            #find corresponding words
            word1 = words[ptr - 1]
            word2 = words[ptr]
                
            greatest_common_len = min(len(word1), len(word2)) #len of the shorter word
            can_cont = False #used later for edge case where all letters match but len differs

            for i in range(greatest_common_len):
                letter1, letter2 = word1[i], word2[i] #get the letter

                #the letter than comes first should have a smaller or equal rank
                if get_rank(letter1) < get_rank(letter2):
                    can_cont = True
                    break
                #if rank is greater, then we're not in order

                elif get_rank(letter1) > get_rank(letter2):
                    return False

            #in the case where letter for letter matches (e.g., word1="apple" and word2="app"),
            #check to make sure len(word1) < len(word2)
            if not can_cont:
                if len(word1) > len(word2):
                    return False
        
        #we've checked all words, return true
        return True
    

    """
    Shortened up code a little, less comments; inspired by solution to use for/else
    
    Runtime: 24 ms, faster than 75.56% of Python online submissions for Verifying an Alien Dictionary.
    Memory Usage: 12.7 MB, less than 55.64% of Python online submissions for Verifying an Alien Dictionary.    
    """
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def get_rank(letter):
            """
            Helper func that returns the rank of a given alien letter, from 1 to 26
            """
            return alphabet[ord(letter) - ord('a')]
        
        #if we just have one word, no need to check order
        if len(words) < 2:
            return True
        
        #build the alien alphabet; will be used by get_rank()
        alphabet = [0] * len(order)
        for i, letter in enumerate(order):
            #letter has a rank of i
            #the lower the i, the earlier it appears
            alphabet[ord(letter) - ord('a')] = i
        
        #iterate through words to see if they are sorted relative to each other        
        for ptr in range(1, len(words)):
            #find corresponding words
            word1 = words[ptr - 1]
            word2 = words[ptr]
            
            for i in range(min(len(word1), len(word2))): #len of the shorter word
                letter1, letter2 = word1[i], word2[i] #get the letter

                #the letter than comes first should have a smaller or equal rank
                if get_rank(letter1) < get_rank(letter2):
                    break
                elif get_rank(letter1) > get_rank(letter2):
                    return False

            else: #will execute if we do NOT hit break
                if len(word1) > len(word2):
                    return False
        
        return True
