"""
Reverse a singly linked list.

Runtime: 28 ms, faster than 40.74% of Python online submissions for Reverse Linked List.
Memory Usage: 14.7 MB, less than 25.93% of Python online submissions for Reverse Linked List.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        prev_node = None
        curr_node = head
        
        while curr_node: #while our head points to something
            next_node = curr_node.next
            curr_node.next = prev_node
            
            #advance to next node
            prev_node = curr_node
            curr_node = next_node
            
        #curr_node is None, so return prev_node
        return prev_node