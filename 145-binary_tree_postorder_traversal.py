"""
https://leetcode.com/problems/binary-tree-postorder-traversal/

Strat: 
    Do recursively. Iterative needs additional space or destroying the tree.
    
Post : Left Right Me

    4
  2   5
9  3 1  6
          8
          
9, 3, 2, 1, 8, 6, 5, 4
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.postorder_helper(root, result)
        return result
    
    def postorder_helper(self, root, result):
        if root == None:
            return
        
        if root.left:
            self.postorder_helper(root.left, result)
            
        if root.right:
            self.postorder_helper(root.right, result)
            
        result.append(root.val)
        
        
        #iterative is pretty hard, #TODO in the future
#     def postorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#         stack = []
#         curr = root
        
#         while stack or curr:
#             pass
