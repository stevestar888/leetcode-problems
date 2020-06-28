"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

#Starter code for generalizing to un-sorted list
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def solve(self, node):
#         head = node
#         seen = set()
#         seen.add(None)
        
#         while node and node.next:
#             print(node.val)
#             if node.next.val in seen:
#                 node.next = node.next.next
#             else:
#                 seen.add(node.val)
#                 # prev = node
#                 node = node.next
            
#         if node.next in seen:
#             node = None
    
#         return head