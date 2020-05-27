"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

Note: 
    In order = Left Me Right
    
Runtime: O(n) -- both recursive & iterative implementations
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Recursive (with helper)
    
    Runtime: 16 ms, faster than 82.65% of Python online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Binary Tree Inorder Traversal.
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorder_helper(root, result)
        return result
        
    def inorder_helper(self, root, nodes_list):
        #base case
        if root == None:
            return

        #recursive cases
        if root.left:
            self.inorder_helper(root.left, nodes_list)

        nodes_list.append(root.val)

        if root.right:
            self.inorder_helper(root.right, nodes_list)
            
            
    """
    Iterative

    Runtime: 16 ms, faster than 82.65% of Python online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Binary Tree Inorder Traversal.
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        
        return result