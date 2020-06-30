"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/

Strat: Look for the middle elem, then recurse on left and right.

Stats:
    Runtime: 72 ms, faster than 24.04% of Python online submissions for Convert Sorted Array to Binary Search Tree.
    Memory Usage: 17 MB, less than 65.96% of Python online submissions for Convert Sorted Array to Binary Search Tree.

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            mid = len(nums) // 2
            return self.helper(nums[:mid], nums[mid], nums[mid + 1:])
        else:
            return None
        
    def helper(self, left, mid, right):
        # print(left, mid, right)
        parent = TreeNode(mid)
        
        #work out left node
        if left:
            mid = len(left) // 2
            parent.left = self.helper(left[:mid], left[mid], left[mid + 1:])
        
        #work out right node
        if right:
            mid = len(right) // 2
            parent.right = self.helper(right[:mid], right[mid], right[mid + 1:])
        
        return parent
        
