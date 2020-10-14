"""
https://leetcode.com/problems/merge-two-binary-trees/

Strat:
    This can be done both iteratively and recursive, like most tree problems,
    but the iterative way is really straightforward. If both nodes are empty,
    then the node to return is also empty. If one node is empty, then just 
    return the other node (because it's not empty). Else, add their sums and
    recursively compute their children.

Stats: O(n) time, O(n) space*, where n is the total number of nodes that overlap
    between t1 and t2 -- traverse through every overlapping node + need stack 
    space to do recursion, which is n deep at worst in skewed tree
    
    Runtime: 80 ms, faster than 84.89% of Python online submissions for Merge Two Binary Trees.
    Memory Usage: 14.2 MB, less than 25.00% of Python online submissions for Merge Two Binary Trees.

    *Alternatively, this notation might be ok too: O(min(t1, t2))

Clean iterative: https://leetcode.com/problems/merge-two-binary-trees/discuss/360879/Python3-recursively-and-iteratively
"""
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        #base cases where one or both trees are empty
        if t1 == None and t2 == None:
            return None
        elif t1 == None:
            return t2
        elif t2 == None:
            return t1
        
        #iterative case - create a new 'merged' node
        merged_node = TreeNode(t1.val + t2.val)
        merged_node.left = self.mergeTrees(t1.left, t2.left)
        merged_node.right = self.mergeTrees(t1.right, t2.right)
        
        return merged_node
