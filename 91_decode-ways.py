"""
https://leetcode.com/problems/decode-ways/

DP
"""
class Solution:
# inspired by: https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-+-DFS)/1336893
#     def numDecodings(self, s: str) -> int:
#         n=len(s)
#         store = {}
        
#         def dp(i):
#             if store.get(i):
#                 return store[i]
            
#             if i==n: return 1
#             if s[i]=='0': return 0
#             if i==n-1: return 1

#             if int(s[i:i+2])<=26:
#                 result = dp(i+1)+dp(i+2)
#                 store[i] = result
#                 return result
#             else:
#                 result = dp(i+1)
#                 store[i] = result
#                 return result
            
#         return dp(0)

    def numDecodings(self, s: str) -> int:        
        store = {}
        
        def solve(index):
            #check if we've computed this before
            if store.get(index):
                return store[index]
            
            if index == len(s):
                return 1
            
            if s[index] == '0': #deals with case like "10", where there the answer is 1
                return 0
            
            # consume last number
            if (index + 1) == len(s):
                return 1
            
            consumed = 0
            if 1 <= int(s[index:index+2]) <= 26: # can we consume 2 nums?
                consumed = solve(index + 1) + solve(index + 2) #yes
            else: 
                consumed = solve(index + 1) #no
            
            #memoize
            store[index] = consumed
            return consumed
        #--------------end helper function-------------- 
        
        return solve(0)
      
    
    
    """
    Inspired from https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
    
    Ex: s = 12321
    
    [1, 1, 0, 0, 0, 0] 2 12
    [1, 1, 1, 0, 0, 0]
    [1, 1, 2, 0, 0, 0]

    [1, 1, 2, 0, 0, 0] 3 23
    [1, 1, 2, 2, 0, 0]
    [1, 1, 2, 3, 0, 0]

    [1, 1, 2, 3, 0, 0] 2 32
    [1, 1, 2, 3, 3, 0]
    [1, 1, 2, 3, 3, 0]

    [1, 1, 2, 3, 3, 0] 1 21
    [1, 1, 2, 3, 3, 3]
    [1, 1, 2, 3, 3, 6]

    """
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        
        store = [0] * (len(s) + 1)
        
        store[0] = 1
        store[1] = 1
        
        for i in range(2, len(s) + 1):
            #consume 1 or 2 nums? try both
            if 0 < int(s[i-1 : i]) <= 9:
                store[i] += store[i-1]
            if 10 <= int(s[i-2 : i]) <= 26:
                store[i] += store[i-2]

        return store[-1]
