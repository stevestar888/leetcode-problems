"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

Solution that bridged between my thought process and working code: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34613/A-Python-recursive-solution

A more concise version of ^ using .pop(): https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.

Probably best solution I've seen: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34602/Python-short-recursive-Low-memory-solution

Almighty Stefan's solution: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34543/Simple-O(n)-without-map

Precise one-pass iterative with stack: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/214622/Precise-one-pass-iterative-solution-O(n)
"""
class Solution(object):
    """
    Runtime: 168 ms, faster than 48.32% of Python online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    Memory Usage: 86.9 MB, less than 33.06% of Python online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder and inorder:
            #take the first node in preorder, the rest split amongst left & right children
            root_val = preorder[0]
            root = TreeNode(root_val)
            
            #find where the root_val would have existed in inorder
            inorder_root_idx = inorder.index(root_val)
            
            #find the left and right children for root
            root.left = self.buildTree(preorder[1:inorder_root_idx + 1], inorder[:inorder_root_idx])
            root.right = self.buildTree(preorder[inorder_root_idx + 1:], inorder[inorder_root_idx + 1:])
            
            return root
