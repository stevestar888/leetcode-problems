"""
https://leetcode.com/problems/deepest-leaves-sum/

We need to do BFS, which will get us the deepest layer's elements. Add of all those up and
that's our answer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        node = root
        children = [root]
        
        while children:
            # print(children)
            sum_of_level = 0
            elems_on_level = len(children)
            
            for _ in range(elems_on_level):
                child = children.pop(0)
                
                sum_of_level += child.val
                
                if child.left:
                    children.append(child.left)
                    
                if child.right:
                    children.append(child.right)
                    
        return sum_of_level
