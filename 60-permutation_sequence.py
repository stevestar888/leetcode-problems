"""
https://leetcode.com/problems/permutation-sequence/

Brute force way with generating all possible subsets
and then taking the k-th one.

"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        p = [] #all permutations
        visited = set()
        
        def generate(subset):
            if len(subset) == n:
                p.append(subset)
            
            for i in range(1, n + 1): #possibilities: 1, 2, 3
                if i not in visited:
                    visited.add(i)
                    generate(subset + str(i))
                    visited.remove(i)
                    
        #--------------end helper function--------------
        
        generate("")
        
        #return the k-th permutation (1-based indexing)
        return p[k - 1]
    
    
#     def getPermutation(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """
#         p = [] #all permutations
#         visited = set()
#         self.count = 0
        
#         def generate(subset):
#             if len(subset) == n:
#                 p.append(subset)
#                 self.count += 1
#                 if self.count == k:
#                     return p
            
#             for i in range(1, n + 1): #possibilities: 1, 2, 3
#                 if i not in visited:
#                     visited.add(i)
#                     generate(subset + str(i))
#                     visited.remove(i)
                    
#         #--------------end helper function--------------
        
#         generate("")
        