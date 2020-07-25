"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/

Strat:
    Recursively go down either the left or right branch. When we finally
    get to a point where the root.left or root.right is None, meaning
    there is no child, we make a child with a value of val. Then, all that's
    left to do is to connect root.left or root.right with the new TreeNode.

Stats:
    Runtime: 124 ms, faster than 96.53% of Python online submissions for Insert into a Binary Search Tree.
    Memory Usage: 16.8 MB, less than 65.93% of Python online submissions for Insert into a Binary Search Tree.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        
        #traverse down left or right node depending on root's value
        #if we have a node on the left or right, go there; 
        #if not, we know a TreeNode will be made recursively
        if root.val > val: #go left
            root.left = self.insertIntoBST(root.left, val)
        else: #go right
            root.right = self.insertIntoBST(root.right, val)
        
        return root
