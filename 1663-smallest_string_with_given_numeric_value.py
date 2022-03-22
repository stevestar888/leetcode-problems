"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

Strat:
    The hints give it away: Be greedy & if you build the string from the end to the beginning, it will always be optimal to put the highest possible character at the current index.

    And that's exactly what I did here.

Stats: O(n) / linear time & space
    Runtime: 664 ms, faster than 76.92% of Python online submissions for Smallest String With A Given Numeric Value.
    Memory Usage: 18.6 MB, less than 7.69% of Python online submissions for Smallest String With A Given Numeric Value.
"""
class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # default letter is 'a'
        letters = [1] * n
        running_total = n
        
        # iterate backward to forward
        for i in range(len(letters) - 1, -1, -1):
            if running_total == k: #achieved optimal structure
                break                
            elif running_total + 25 <= k: # switch letter to 'z'
                letters[i] += 25
                running_total += 25
            else: #switch letter to letter that comes before 'z'
                letters[i] += k - running_total
                running_total += k - running_total
                
        # alternative to ^
        #   letters[i] += min(k - running_total, 25)
        #   running_total += min(k - running_total, 25)
        
        # map numbers to letters
        return ''.join([chr(ord('a') + letter - 1) for letter in letters])

    
    
    """
    Saw in submissions; don't understand but cool.
    """
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= n
        numericValue = '_bcdefghijklmnopqrstuvwxy_'
        lexicographicallySmallestString = 'z' * (k // 25)
        if(k % 25):
            lexicographicallySmallestString = numericValue[k%25] + lexicographicallySmallestString
            
        return 'a' * (n - len(lexicographicallySmallestString)) + lexicographicallySmallestString
