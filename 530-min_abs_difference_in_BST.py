"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Note:
    This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
    See more details at 783-,,,.py
    
Runtime: O(n) runtime -- Using a modification of DFS (Pre-order, in-order and post-order traversal are all DFS variants)
    Runtime: 48 ms, faster than 71.22% of Python online submissions for Minimum Absolute Difference in BST.
    Memory Usage: 16.8 MB, less than 25.00% of Python online submissions for Minimum Absolute Difference in BST.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    pre = -float('inf')
    res = float('inf')
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #base case
        if root == None:
            return
        
        #recursive cases
        self.getMinimumDifference(root.left)
        
        #see if our min improved
        self.res = min(self.res, root.val - self.pre)
        
        #update prev node
        self.pre = root.val
        
        self.getMinimumDifference(root.right)
        
        return self.res