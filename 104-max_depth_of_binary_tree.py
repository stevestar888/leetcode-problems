"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Strat:
    Do this problem recursively. You might think you need a helper,
    but you can do without!

Runtime: O(n) time, O(1) space -- doing a DFS traversal, where you visit every node once + no DS
    28 ms	15.6 MB	
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1

    ### Original thought:
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         return self.helper(root, 0)
        
#     def helper(self, root, max_depth):        
#         #base case
#         if root == None:
#             return max_depth

#         #found a known node, increase depth
#         max_depth += 1

#         left = self.helper(root.left, max_depth)
#         right = self.helper(root.right, max_depth)

#         return max(left, right)