"""
https://leetcode.com/problems/word-subsets/submissions/

Strat: make a dictionary of all the different letters we have to have in each word ("subset").
    Although B may have many required letters, as long as we fulfill the most demanding 
    requirement, we won't need to worry about the other cases. 
    
    For example, given B = ["ec","oc","ceo","oo"], our subset would need to have the following:
    {e: 1, c: 1, o: 2}
    
    While there's a 'c' in nearly all elements of B, as long as we have one, we are set. Similarly,
    we need two 'o's.
    
    Now that the subset of all required letters has been built, we can compare all a in A against
    the subset. If the word has all the required letters, then it is a universal word which we can
    add to the return list.
    

Runtime: I don't 100% agree with the runtime analysis in the "solution". Personally, I feel
    O(BbAa) time, where B and A are array lengths, and b and a are word lengths
            Why? We have to iterate through every char in every word of both A and B
         O(1) space
            Why? When we make subset, there will be a total of 26 entries--max. Since 26 is a 
            constant number, we can ignore it. We also don't need to count the return array
            as additional space (I think this is precedent in other leetcode probs, too).
         
    Runtime: 524 ms, faster than 92.92% of Python online submissions for Word Subsets.
    Memory Usage: 17.3 MB, less than 33.33% of Python online submissions for Word Subsets.
"""

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        #construct the unique subset for B
        subset = {} #could do [0] * 26 instead of a dict
        
        for b in B:
            for char in b: #see if current count of char or previous count of char has more
                subset[char] = max(b.count(char), subset.get(char, 0))
                
        # Old way of writing it
#         for b in B:
#             for char in b:
#                 char_count = b.count(char)
#                 prev_count = subset.get(char, 0)
                
#                 #update count in B_subset if we'ven't seen the char
#                 #OR we have more occurences of a letter now
#                 if prev_count == 0 or char_count > prev_count:
#                     subset[char] = char_count
                    
        #now see if any words satisfy the letters in the subset
        ans = []
        for a in A:
            #look through all the entries in the dictionary (its keys)
            #if the count in 'a' is enough to cancel out for all keys, we're golden
            if all(a.count(char) >= subset[char] for char in subset.keys()):
                ans.append(a)
                
        return ans
    
    
    # shortened version, because I want to make it unreadable
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        subset = {}
        for b in B:
            for char in b:
                subset[char] = max(b.count(char), subset.get(char, 0))
        
        return [a for a in A if all(a.count(char) >= subset[char] for char in subset.keys())]