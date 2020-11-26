"""
https://leetcode.com/problems/leaf-similar-trees/submissions/

Strat:
    Use a traversal to find the "leaf value sequence" for each tree,
    then compare the two trees' sequences.
    
    Hacky BST iterative solution: do the normal BST and compare each
    leaf. Although the leaves we encounter won't be in the same order 
    as the "leaf value sequence", if the 2 trees have similar leaves
    then they should still have the same leaves in the same places.

Stats:
    Runtime: 24 ms, faster than 61.44% of Python online submissions for Leaf-Similar Trees.
    Memory Usage: 12.8 MB, less than 53.39% of Python online submissions for Leaf-Similar Trees.
"""
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def inorder(node, leaf_list):
            if node.left == None and node.right == None:
                #reached a leaf node
                leaf_list.append(node.val)
            
            #recursively call the left then right branches
            if node.left:
                inorder(node.left, leaf_list)
            
            if node.right:
                inorder(node.right, leaf_list)
            
        #--------------end helper function-------------- 
        
        l1, l2 = [], []
        inorder(root1, l1)
        inorder(root2, l2)
        
        return l1 == l2
    
    
    """
    From the accepted solutions, modified a bit
    
    Runtime: 20 ms, faster than 82.42% of Python online submissions for Leaf-Similar Trees.
    Memory Usage: 13.2 MB, less than 5.51% of Python online submissions for Leaf-Similar Trees.
    """
    def getLeaves(self, root, leaves):
        if root.left:
            leaves = self.getLeaves(root.left, leaves)
        if root.right:
            leaves = self.getLeaves(root.right, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)
        return leaves
        
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.getLeaves(root1, []) == self.getLeaves(root2, [])
        
