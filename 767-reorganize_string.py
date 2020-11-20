"""
https://leetcode.com/problems/reorganize-string/

Same as 358. Rearrange String k Distance Apart, when k = 2

On input "aaaaaaaabcdefghji", `a` occurs every other heappop

[[-8, u'a'], [-1, u'c'], [-1, u'b'], [-1, u'e'], [-1, u'd'], [-1, u'g'], [-1, u'f'], [-1, u'i'], [-1, u'h'], [-1, u'j']]
[[-1, u'b'], [-1, u'c'], [-1, u'f'], [-1, u'e'], [-1, u'd'], [-1, u'g'], [-1, u'j'], [-1, u'i'], [-1, u'h']]
[[-7, u'a'], [-1, u'c'], [-1, u'f'], [-1, u'd'], [-1, u'h'], [-1, u'g'], [-1, u'j'], [-1, u'i'], [-1, u'e']]
[[-1, u'c'], [-1, u'd'], [-1, u'f'], [-1, u'e'], [-1, u'h'], [-1, u'g'], [-1, u'j'], [-1, u'i']]
[[-6, u'a'], [-1, u'd'], [-1, u'f'], [-1, u'e'], [-1, u'h'], [-1, u'g'], [-1, u'j'], [-1, u'i']]
[[-1, u'd'], [-1, u'e'], [-1, u'f'], [-1, u'i'], [-1, u'h'], [-1, u'g'], [-1, u'j']]
[[-5, u'a'], [-1, u'h'], [-1, u'e'], [-1, u'i'], [-1, u'j'], [-1, u'g'], [-1, u'f']]
[[-1, u'e'], [-1, u'h'], [-1, u'f'], [-1, u'i'], [-1, u'j'], [-1, u'g']]
[[-4, u'a'], [-1, u'h'], [-1, u'f'], [-1, u'i'], [-1, u'j'], [-1, u'g']]
[[-1, u'f'], [-1, u'h'], [-1, u'g'], [-1, u'i'], [-1, u'j']]
[[-3, u'a'], [-1, u'g'], [-1, u'j'], [-1, u'i'], [-1, u'h']]
[[-1, u'g'], [-1, u'h'], [-1, u'j'], [-1, u'i']]
[[-2, u'a'], [-1, u'h'], [-1, u'j'], [-1, u'i']]
[[-1, u'h'], [-1, u'i'], [-1, u'j']]
[[-1, u'a'], [-1, u'j'], [-1, u'i']]
[[-1, u'i'], [-1, u'j']]
[[-1, u'j']]

"""
class Solution(object):
    """
    Solution from https://leetcode.com/problems/reorganize-string/discuss/456020/Python-Heap-Easy-to-understand-self-explanatory-code
    """
    def reorganizeString(self, S):
        if S == "":
            return "" 
        
        # create a counter 
        d = collections.Counter(S)
        
        heap = []
        for key, value in d.items():
            heapq.heappush(heap,[-value,key])
        
        print(heap)
        res = ""
        pre = heapq.heappop(heap)
        res+= pre[1]
        
        
        while heap:
            print(heap)
            curr = heapq.heappop(heap)
            res+=curr[1]
            
            
            pre[0]+=1
            if pre[0]<0:
                heapq.heappush(heap,pre)
                
            #pre is put back into the heap on the next iteration
            pre = curr 
            
        if len(res)!=len(S):
            return ""
        else:
            return res