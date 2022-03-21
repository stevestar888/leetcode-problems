"""
https://leetcode.com/problems/binary-tree-paths/submissions/

Recursive DFS
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        
        def traverse(node, path_so_far):
            # base case: if leaf (add the path to paths)
            if not node.left and not node.right:
                paths.append(path_so_far)
                
            # recursive case: update the path_so_far & recurse
            else:
                if node.left:
                    traverse(node.left, "{}->{}".format(path_so_far, node.left.val))
                
                if node.right:
                    traverse(node.right, "{}->{}".format(path_so_far, node.right.val))
            
        traverse(root, str(root.val))
        return paths