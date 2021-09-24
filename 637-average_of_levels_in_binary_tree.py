"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/

Strat:
    BFS in order, like #102.

Stats:

    Runtime: 36 ms, faster than 93.21% of Python online submissions for Average of Levels in Binary Tree.
    Memory Usage: 18 MB, less than 64.47% of Python online submissions for Average of Levels in Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def computeAvg(self, elems):
        num = float(sum(elems))
        denom = float(len(elems))
        
        return num / denom
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = deque()
        q.append(root)
        res = []
        
        while q:
            nodes = [] # stores nodes at the current level
            for _ in range(len(q)):
                node = q.popleft()
                nodes.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            res.append(self.computeAvg(nodes))
            
        return res
