"""
https://leetcode.com/problems/reverse-linked-list/submissions/

Strat:
    Iterative or recursive; two ways of recursion. Use _next instead of 
    next, because next is a built-in function......
"""
class Solution(object):
    """
    Iterative
    
    Stats: O(n) time, O(1) space -- traverse through all elements + keep only vars
        Runtime: 28 ms, faster than 40.74% of Python online submissions for Reverse Linked List.
        Memory Usage: 14.7 MB, less than 25.93% of Python online submissions for Reverse Linked List.
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        
        while curr:  #while we still point to something
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
            
        #curr is None, so return prev_node
        return prev
        
        
    """
    Recursive (with helper), inspired from: https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution
    
    Alternative recursion in Leetcode solution; decent vid on it: https://www.youtube.com/watch?v=MRe3UsRadKw
    
    Stats: O(n) time, O(n) space -- traverse through all elem + stack space
        Runtime: 32 ms, faster than 38.40% of Python online submissions for Reverse Linked List.
        Memory Usage: 19.3 MB, less than 5.34% of Python online submissions for Reverse Linked List.
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._helper(head)
        
    def _helper(self, node, prev=None):
        if node == None:
            return prev
        
        _next = node.next
        node.next = prev
        return self._helper(_next, node)
