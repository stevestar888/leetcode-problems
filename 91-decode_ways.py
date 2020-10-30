"""
https://leetcode.com/problems/decode-ways/

Strat:
    #TODO

Stats: 

"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def form_splits(msg, idx, splits):
            """
            Given an encoded message, msg, count the number of ways it can be decoded.
            """
            #base cases
            if idx == len(msg) - 1:
                combos.add(tuple(splits))
                return
            elif idx > len(msg) - 1:
                return 

            ##We can take 1 number guranteed. We might be able to take the next 2 numbers (but have to check)

            #take the next number
            new_split = splits[:]
            new_split.append(idx + 1)
            form_splits(msg, idx + 1, new_split) #recursively call with split at idx + 1

            #see if we can take the next 2 numbers
            if idx + 2 > len(msg): #check we have 2 more letters left
                return

            next_split = msg[idx:idx+2] #check if the 2 letters left are <= 26
            if int(next_split) <= 26: #valid split
                new_split = splits[:]
                new_split.append(idx + 2)
                form_splits(msg, idx + 2, new_split) #recursively call with split at idx + 2
        
        #--------------end helper function-------------- 
    
        #stores all the possible combinations of splits 
        combos = set()

        #calculate our splits
        form_splits(s, 0, [])

        #the number of possible splits = number of possible decodes
        return len(combos)



