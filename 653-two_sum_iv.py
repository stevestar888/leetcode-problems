"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""
class Solution(object):
    """
    Strat: 
        Use BFS to traverse through the BST, and use a dictionary to store complements.
    
    Stats: O(n) / linear time, O(n) / linear space 
        Runtime: 72 ms, faster than 81.20% of Python online submissions for Two Sum IV - Input is a BST.
        Memory Usage: 17.5 MB, less than 16.81% of Python online submissions for Two Sum IV - Input is a BST.
    """
    def findTarget(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        seen = set()
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.pop()
            complement = target - node.val
            if complement in seen:
                return True
            else:
                seen.add(node.val)
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False
