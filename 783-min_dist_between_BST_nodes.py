"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/submissions/

Note: 
    This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
    
Strat: 
    We can take advantage of the pure structure of the BST to our advantage. The minimum 
    difference between 2 nodes can be found by looking at a sorted list and comparing adjacent 
    values. Using an in-order traversal, we can get all the elems in a sorted list. However, 
    we actually don't need to construct a list, because we only care about the previous element. 
    As such, we can forego the list by keep track of the previous element and the min value so far.

Runtime: O(n) runtime -- Using a modification of DFS (Pre-order, in-order and post-order traversal are all DFS variants)
    Runtime: 12 ms, faster than 97.99% of Python online submissions for Minimum Distance Between BST Nodes.
    Memory Usage: 12.9 MB, less than 14.29% of Python online submissions for Minimum Distance Between BST Nodes.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    pre = -float('inf') #previous node value
    res = float('inf')  #the minimum so far

    def minDiffInBST(self, root):
        if root == None:
            return
        
        #call left 
        self.minDiffInBST(root.left)
		# evaluate current node, then update prev node
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
		
        #call right
        self.minDiffInBST(root.right)
        return self.res
    
    ### Or with a helper function
#     def minDiffInBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         self.ans = 2**31-1
#         self.pre = None
#         def inorder(node):
#             if node.left:
#                 inorder(node.left)
                
#             if self.pre != None:
#                 self.ans = min(self.ans,node.val - self.pre)
#             self.pre = node.val
            
#             if node.right:
#                 inorder(node.right)
#         inorder(root)
#         return self.ans