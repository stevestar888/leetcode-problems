"""
https://leetcode.com/problems/last-stone-weight/submissions/

Strat: 
    Using a Priority Queue (with heap implementation). Since the default python
    heap is a min heap, but we want a max heap, we need to use a trick: reverse
    the sign of all the elements in the stones list, and when you take it out, 
    reverse the sign again.
    
    So try to take out the first stone, and try to take out the second stone.
    If we have both stones, smash then and add the different (if there is one).
    If there is not a second stone, return the first stone.
    If there are no stones left, return 0.
    Boom.

Stats: O(nlgn) runtime, O(n) space
    Runtime: 16 ms, faster than 92.45% of Python online submissions for Last Stone Weight.
    Memory Usage: 12.7 MB, less than 56.16% of Python online submissions for Last Stone Weight.

"""
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #make all stone values negative
        stones = [-stone for stone in stones]
        
        #turn stones list into a heap
        heapq.heapify(stones)
        
        #ensure we have values in the heap
        while stones:
            stone1 = heapq.heappop(stones)
            
            #try to get the second stone
            if stones:
                stone2 = heapq.heappop(stones)
                diff = abs(stone2 - stone1)
                if diff:
                    heapq.heappush(stones, -diff)
                    
            #only 1 stone is left
            else:
                return -stone1
            
        #no stones are left, so return 0
        return 0
