"""
https://leetcode.com/problems/most-common-word/

Strat:
    This is what the solution calls a "pipeline" lol. Essentially taking the 
    problem into steps: preprocess the punctuations and spaces, and then use 
    a dictionary to store the occurence of each word.
    
Stats: O(n + m) time, O(n + m) space where n is len(paragraph), m is len(banned)
        ^ have to iterate through both arrays, and both use a set or dict
    Runtime: 12 ms, faster than 99.75% of Python online submissions for Most Common Word.
    Memory Usage: 12.7 MB, less than 58.35% of Python online submissions for Most Common Word.

"""
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        #bring to lowercase
        paragraph = paragraph.lower()
        
        #preprocess to get rid of punctuation symbols (!?',;.)
        symbols = "!?',;."
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, " ")
        
        banned_words = set(banned)
        
        counts = {}
        words = paragraph.split() #luckily, gets rid of repeating 0s as well
        for word in words:
            if word not in banned_words:
                counts[word] = counts.get(word, 0) + 1
        
        ##using max instead of sort reduces runtime from nlgn to n
        # return sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][0]
        max_pair = max(counts.items(), key=lambda x: x[1])
        return max_pair[0]