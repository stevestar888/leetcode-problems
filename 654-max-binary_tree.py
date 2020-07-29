"""
https://leetcode.com/problems/maximum-binary-tree/

Strat:
    Recursive solution is pretty straightforward, but is O(n^2).
    Iterative solution is mindblogging, but is linear.

Note: 
    Turns out that this "max btree" is actually a Cartesian Tree https://en.wikipedia.org/wiki/Cartesian_tree 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Recursive solution
    
    Stats: O(n^2) runtime -- need to find max for every single num in worse case
    """
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #basecase
        if nums == []:
            return 
        
        #recursive cases: compute left & right
        root_val = max(nums)
        root_idx = nums.index(root_val)
        root = TreeNode(root_val)
        
        root.left = self.constructMaximumBinaryTree(nums[:root_idx])
        root.right = self.constructMaximumBinaryTree(nums[root_idx + 1:])
        
        return root
    
    
    """
    Iterative (not mine)
    
    Stats: O(n) runtime (explaination: https://leetcode.com/problems/maximum-binary-tree/discuss/316286/Python-O(n)-Solution-with-explanation)
    """
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        stack = []
        for num in nums:
            node = TreeNode(num)
            while len(stack) > 0 and stack[-1].val < num:
                node.left = stack.pop()
            
            if len(stack) > 0 and stack[-1].val > num:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
