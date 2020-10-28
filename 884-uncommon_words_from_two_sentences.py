"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""
class Solution(object):
    """
    Strat:
        Use Dict
    
    Stats: O(n + m) time, O(n + m) space

    """
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_words = {}
        B_words = {}
        
        #populate A_words
        for word_a in A.split():
            A_words[word_a] = A_words.get(word_a, 0) + 1
            
        #populate B_words
        for word_b in B.split():
            B_words[word_b] = B_words.get(word_b, 0) + 1
        
        uncommon = []
        for word in A_words.keys():
            if A_words.get(word, 0) == 1 and B_words.get(word, 0) == 0:
                uncommon.append(word)
        
        for word in B_words.keys():
            if B_words.get(word, 0) == 1 and A_words.get(word, 0) == 0:
                uncommon.append(word)
        
        return uncommon

    
    """
    Much cleaner, inspired by:
    https://leetcode.com/problems/uncommon-words-from-two-sentences/discuss/158967/C%2B%2BJavaPython-Easy-Solution-with-Explanation
    
    Stats: Stats: O(n + m) time, O(n + m) space
        Runtime: 24 ms, faster than 36.07% of Python online submissions for Uncommon Words from Two Sentences.
        Memory Usage: 13.5 MB, less than 27.27% of Python online submissions for Uncommon Words from Two Sentences.
    """
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = {}
        
        for word in (A + " " + B).split():
            count[word] = count.get(word, 0) + 1
        
        result = []
        for word in count.keys():
            if count.get(word) == 1:
                result.append(word)
                
        return result
