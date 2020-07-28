"""
https://leetcode.com/problems/all-possible-full-binary-trees/
"""
class Solution(object):
    def allPossibleFBT(self, remaining_nodes):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        #basecase: we cannot have a *full* BTree if remaining_nodes is even
        if remaining_nodes % 2 == 0:
            return []
        
        #basecase: if we only have one node left, it's just the node itself
        if remaining_nodes == 1:
            return [TreeNode(0)]
            
        result = []
        #look at all combinations for left/right children
        for i in range(1, remaining_nodes, 2):
            left_nodes = self.allPossibleFBT(i)
            right_nodes = self.allPossibleFBT(remaining_nodes - i - 1)
            
            for left_tree in left_nodes:
                for right_tree in right_nodes:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    
                    result.append(root)
                    
        return result89
