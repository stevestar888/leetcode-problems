"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/submissions/

Runtime: O(n) — three runs, one to %, one to make dict, one to parse dict
    Runtime: 216 ms, faster than 52.59% of Python online submissions for Pairs of Songs With Total Durations Divisible by 60.
    Memory Usage: 15.7 MB, less than 10.00% of Python online submissions for Pairs of Songs With Total Durations Divisible by 60.

super clean solution: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/534027/Python-oror-O(N)-oror-Dict-oror-Clear
"""

import math

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        ans = 0
        
        #change all nums to 0 ≤ num ≤ 60
        time = [song % 60 for song in time]
        
        #store the count of each song's duration
        duration = {}
        for song in time:
            duration[song] = duration.get(song, 0) + 1
        
        #now check how many pairs we have (e.g., a 20 min song pairs with
        # a 40 min)
        # Note: you multiply the pairs for all possible combinations
        for i in range(1, 30): #iterate from song durations 1...29
            ans += duration.get(i, 0) * duration.get(60 - i, 0)
            
        #deal with the 30 min and the 60 min case
        ans += nCr(duration.get(30, 0), 2)
        ans += nCr(duration.get(0, 0), 2)
            
        return ans

    
def nCr(n, r):   
    return (factorial(n) / (factorial(r)  * factorial(n - r))) 
  
    
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)