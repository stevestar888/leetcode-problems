"""
https://leetcode.com/problems/same-tree/

3 recursive approaches (each progressively better) + 1 iterative approach
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    First try -- a bit messy, not super fast
    
    Runtime: 24 ms, faster than 26.25% of Python online submissions for Same Tree.
    Memory Usage: 12.8 MB, less than 40.93% of Python online submissions for Same Tree.
    """
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q: #both have values
            print(p.val, q.val)
            if p.val != q.val:
                return False
            
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            
            print(left, right)
            return left and right
        else: #either both are null or one is null
            if (p and not q) or (not p and q):
                # one is null while the other one is not
                return False
            else: 
                #both are null so they equal each other
                return True
            
            
    """
    Improved and refactored
    
    Runtime: 16 ms, faster than 84.17% of Python online submissions for Same Tree.
    Memory Usage: 13 MB, less than 7.80% of Python online submissions for Same Tree.
    """
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q:
            # one is null while the other one is not
            return False
        
        if p.val != q.val:
            return False
            
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
            
        return left and right
           
            
    """
    The best one yet
    
    Runtime: 12 ms, faster than 97.01% of Python online submissions for Same Tree.
    Memory Usage: 12.7 MB, less than 71.57% of Python online submissions for Same Tree.
    """
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: #both nodes are None
            return True
        elif not p and q: #p is None while q has a value
            return False
        elif not q and p: #q is None while p has a value
            return False
        
        return p.val == q.val and \
            self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
    
    """
    Iterative, using two stacks
    
    Runtime: 16 ms, faster than 84.17% of Python online submissions for Same Tree.
    Memory Usage: 12.6 MB, less than 99.94% of Python online submissions for Same Tree.
    """
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_stack = deque()
        q_stack = deque()
        
        p_stack.append(p)
        q_stack.append(q)

        #alternatively, do:
        # p_stack = [p]
        # q_stack = [q]
        
        while p_stack and q_stack:
            p_item = p_stack.pop()
            q_item = q_stack.pop()
            
            #both are None
            if not p_item and not q_item:
                continue
            
            #catch one is None and other is not
            if not p_item or not q_item:
                return False
            
            #values not equal
            if p_item.val != q_item.val:
                return False
            
            p_stack.append(p_item.left)
            q_stack.append(q_item.left)
            
            p_stack.append(p_item.right)
            q_stack.append(q_item.right)
        
        return True
        