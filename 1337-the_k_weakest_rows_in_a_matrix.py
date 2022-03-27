"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
class Solution(object):
    """
    Scan of the matrix + sort dictionary
    
    runtime: O(n * m) + O(n lgn), where n = len(mat)
    
    Runtime: 96 ms, faster than 72.17% of Python online submissions for The K Weakest Rows in a Matrix.
    Memory Usage: 13.4 MB, less than 98.38% of Python online submissions for The K Weakest Rows in a Matrix.
    """
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        store = {}
        
        for i, row in enumerate(mat):
            count = sum(row)
                    
            if count in store: #edit entry
                current = store.get(count)
                store[count] = current + [i]
            else: #create entry
                store[count] = [i]
        
        ans = []
        
        for keys in sorted(store):
            for row in store[keys]:
                ans.append(row)
            
        return ans[:k]


    """
    runtime: O(nlgn) still I think, because adding elem to heap takes O(lgn) time to rebalance
    
    Runtime: 84 ms, faster than 94.82% of Python online submissions for The K Weakest Rows in a Matrix.
    Memory Usage: 13.9 MB, less than 12.95% of Python online submissions for The K Weakest Rows in a Matrix.
    """
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        min_heap = []
        
        # add all elems
        for i, row in enumerate(mat):
            count = sum(row)
            heapq.heappush(min_heap, [count, i])

        ans = []
        for _ in range(k): # pop k elems
            row = heapq.heappop(min_heap)[1]
            ans.append(row)
            
        return ans