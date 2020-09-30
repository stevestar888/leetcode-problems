"""
https://leetcode.com/problems/subtree-of-another-tree/

Strat:
    Do a traversal of s (I did DFS). For every node in s, 
    see if s == t, meaning is the subtree that starts at 
    node s the same as the tree of t? 
    
Stats: 
    O(n * m) time -- At every node of s, you are potentially checking the entire tree of t
    O(n + m) space -- ?? might just be O(n)
    Runtime: 344 ms, faster than 19.93% of Python online submissions for Subtree of Another Tree.
    Memory Usage: 14.3 MB, less than 11.68% of Python online submissions for Subtree of Another Tree.
"""
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return False
        
        if self.isSameTree(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        
    def isSameTree(self, t1, t2):
        """Returns if t1 and t2 are exactly the same tree"""
        #both are empty
        if t1 == None and t2 == None:
            return True
        
        #one is empty, other is not
        if t1 == None or t2 == None:
            return False
        
        #check their val & their children's vals
        if t1.val == t2.val:
            left = self.isSameTree(t1.left, t2.left)
            right = self.isSameTree(t1.right, t2.right)
            return left and right
    
        return False
            
