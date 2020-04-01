"""
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

My approach: traverse through the tree and check if the parent node's value is the same as the children's values

Stats:
    Runtime: 16 ms, faster than 81.73% of Python online submissions for Univalued Binary Tree.
    Memory Usage: 12.7 MB, less than 8.33% of Python online submissions for Univalued Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #leaf node (no children)
        if root == None: 
            return True 
        
        #check if we have a left child. if so, compare parent & child values
        if root.left: 
            if root.val != root.left.val:
                return False
        
        #check if we have a right child. if so, compare parent & child values
        if root.right:
            if root.val != root.right.val:
                return False
        
        #send off recursive calls to children 
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        