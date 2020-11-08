"""
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

Strat:
    DFS

Stats: 
    O(n) / linear time, O(n) / linear space 
  
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        
        best = 0
        for child in root.children:
            depth = self.maxDepth(child)
            best = max(best, depth)
        
        return best + 1
