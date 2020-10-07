"""
https://leetcode.com/problems/range-sum-of-bst/

Runtime: O(n) time
    Runtime: 284 ms, faster than 48.88% of Python online submissions for Range Sum of BST.
    Memory Usage: 29.2 MB, less than 18.86% of Python online submissions for Range Sum of BST.
    
Strat: Traverse the tree while maintaining a running sum.

Optimization: we can take advantage of the pure structure of the BST: all right children are bigger, 
    all left children are smaller. When given a node, if its value is great than R (the upper limit),
    then we don't need to check the right child anymore. The same logic can be applied to the 
    bottom limit of L. This trick is applied to iterative solution.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    #recursive (not optimized)
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        root_val = 0
        if root == None:
            return root_val
        
        if L <= root.val <= R:
            root_val = root.val
        
        left_val = self.rangeSumBST(root.left, L, R) 
        right_val = self.rangeSumBST(root.right, L, R) 
        
        return root_val + left_val + right_val
    

    #iterative with optimization 
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        result = 0
        stack = deque()
        stack.append(root)
        
        while stack:
            length = len(stack)
            
            for _ in range(length):
                item = stack.pop()
                
                if L <= item.val <= R:
                    result += item.val
                    
                #the right child of the item node will be bigger than the item
                if item.val < R and item.right: 
                    stack.append(item.right)
                
                #same logic as ^
                if item.val > L and item.left:
                    stack.append(item.left)
                
        return result
    
    """
    Easy recursive
    Runtime: 340 ms, faster than 33.78% of Python online submissions for Range Sum of BST.
    Memory Usage: 29.6 MB, less than 14.70% of Python online submissions for Range Sum of BST.
    """
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.total = 0
        def traverse(root):
            #base case
            if root == None:
                return
            
            #recursive case
            if L <= root.val <= R:
                self.total += root.val
                
            traverse(root.left)
            traverse(root.right)
        
        #--------------end helper function-------------- 
        traverse(root)
        return self.total
