"""
https://leetcode.com/problems/binary-tree-preorder-traversal/

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
    Recursive
    
    Runtime: 20 ms, faster than 56.11% of Python online submissions for Binary Tree Preorder Traversal.
    Memory Usage: 12.9 MB, less than 5.72% of Python online submissions for Binary Tree Preorder Traversal.
    """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.preorder_helper(root, result)
        return result
        
    def preorder_helper(self, root, nodes_list):
        #base case
        if root == None:
            return
        
        #adding & recursing pre-order: Me Left Right
        nodes_list.append(root.val)
        
        #recursive cases
        if root.left:
            self.preorder_helper(root.left, nodes_list)
        
        if root.right:
            self.preorder_helper(root.right, nodes_list)
            
     
    """
    Iterative
    
    Runtime: 12 ms, faster than 97.77% of Python online submissions for Binary Tree Preorder Traversal.
    Memory Usage: 12.7 MB, less than 5.72% of Python online submissions for Binary Tree Preorder Traversal.
    """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        curr = root #keeps track of what node we're on currently
        
        while curr or stack:
            if curr:
                result.append(curr.val) #add "me"
                stack.append(curr) #add "me"
                curr = curr.left #go "left"
            else:
                curr = stack.pop()
                curr = curr.right #go "right"
                
        return result
        