"""
https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

A standard binary tree traversal using BFS, aka in order traversal. 

Runtime:
    Runtime: 16 ms, faster than 97.73% of Python online submissions for Binary Tree Level Order Traversal.
    Memory Usage: 13.1 MB, less than 5.88% of Python online submissions for Binary Tree Level Order Traversal.  
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        queue.append(root)
        result = []
        
        #check for empty tree
        if root == None:
            return result
        
        while queue:
            nodes = [] #each "level"
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes.append(node.val)

                if node.left: #check for left child
                    queue.append(node.left)
 
                if node.right: #check for right child
                    queue.append(node.right)
            result.append(nodes)
        
        return result
