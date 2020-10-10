"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/

Strat:
    Look for the middle elem, then recurse on left and right. Conveniently, we want
    to return the root, so that's what we return from each of the recursive calls 
    as well. 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Try #1--uses helper but works no problem

    O(n) / linear time, O(n) / linear space

    Runtime: 72 ms, faster than 24.04% of Python online submissions for Convert Sorted Array to Binary Search Tree.
    Memory Usage: 17 MB, less than 65.96% of Python online submissions for Convert Sorted Array to Binary Search Tree.
    """
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
        
        
    """
    Try #2--code cleaned up a little more

    O(n) / linear time, O(n) / linear space

    Runtime: 64 ms, faster than 64.40% of Python online submissions for Convert Sorted Array to Binary Search Tree.
    Memory Usage: 17.7 MB, less than 20.42% of Python online submissions for Convert Sorted Array to Binary Search Tree.
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        
        mid = len(nums) // 2
        parent = TreeNode(nums[mid])
        parent.left = self.sortedArrayToBST(nums[:mid])
        parent.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return parent

    """
    Try #3: Space usage is improved because no more copying array (just using the indicies)
    
    O(n) / linear time, O(n) / linear space

    Runtime: 52 ms, faster than 99.06% of Python online submissions for Convert Sorted Array to Binary Search Tree.
    Memory Usage: 17.6 MB, less than 20.42% of Python online submissions for Convert Sorted Array to Binary Search Tree.
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            if left > right:
                return None

            half = left + (right - left) / 2

            root = TreeNode(nums[half])
            root.left = helper(left, half - 1)
            root.right = helper(half + 1, right)

            return root
        #--------------end helper function-------------- 
        
        return helper(0, len(nums) - 1)