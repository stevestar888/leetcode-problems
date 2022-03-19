"""
https://leetcode.com/problems/sum-of-left-leaves/submissions/

Strat:
    I found the recursive solution to be the most palatable.
"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, is_left_branch):
            if node == None:
                return 0

            #see if we are a 'leaf'
            if node.left == None and node.right == None:
                if is_left_branch: #we are at a left leaf
                    return node.val
                else: #at a right leaf
                    return 0
            else: #not at leaf, keep recursing
                left = dfs(node.left, True)
                right = dfs(node.right, False)

                return left + right
        #--------------end helper function-------------- 
        
        return dfs(root, False)
        
    
    """
    Fancy, abridged version of above.

    Runtime: 28 ms, faster than 35.47% of Python online submissions for Sum of Left Leaves.
    Memory Usage: 13.5 MB, less than 35.90% of Python online submissions for Sum of Left Leaves.
    """
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        #if I have a left child and that child doesn't have kids, aka I have a left leaf
        left_leaf_val = 0
        if root.left and root.left.left == None and root.left.right == None:
            left_leaf_val = root.left.val
        
        return left_leaf_val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
