"""
https://leetcode.com/problems/range-sum-of-bst/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
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
                print(item.val)
                if L <= item.val <= R:
                    result += item.val
                    
                if item.left:
                    stack.append(item.left)
                    
                if item.right:
                    stack.append(item.right)
                    
        return result
        
#     def rangeSumBST(self, root, L, R):
#         """
#         :type root: TreeNode
#         :type L: int
#         :type R: int
#         :rtype: int
#         """
#         result = 0
#         stack = deque()
#         stack.append(root)
        
#         while stack:
#             length = len(stack)
            
#             for _ in range(length):
#                 item = stack.pop()
                
#                 if L <= item.val <= R:
#                     result += item.val
#                 elif item.val < R and item.right: 
#                     stack.append(item.right)
#                 elif item.val > L and item.left:
#                     stack.append(item.left)
                
#                 #the right child of the item node will be bigger than the item
#                 #checking its value 
                    
#         return result