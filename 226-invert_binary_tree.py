# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Recursive 
    
    Stats: O(n) time, O(1) space
        Runtime: 32 ms, faster than 7.14% of Python online submissions for Invert Binary Tree.
        Memory Usage: 12.7 MB, less than 50.80% of Python online submissions for Invert Binary Tree.
    """
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ### base case
        if root == None:
            return
        
        #swap the left & right children with each other
        root.left, root.right = root.right, root.left

        #now swap for other future generations
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    
    """
    Iterative
    
    Stats: O(n) time, O(1) space
        Runtime: 20 ms, faster than 61.22% of Python online submissions for Invert Binary Tree.
        Memory Usage: 12.7 MB, less than 54.22% of Python online submissions for Invert Binary Tree.
    """
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            #swap the left & right children with each other
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return root
