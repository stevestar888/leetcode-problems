"""
https://leetcode.com/problems/middle-of-the-linked-list/

Strat: 
    We use the "tortoise and hare", where we have a fast and a slow pointer, with the fast one
    going at twice the speed. When the fast pointer is at the end, then the slow pointer
    will be at the middle.

Runtime: O(n) runtime, O(1) memory -- one pass through, no auxiliary data structures
    Runtime: 20 ms, faster than 37.93% of Python online submissions for Middle of the Linked List.
    Memory Usage: 12.9 MB, less than 6.25% of Python online submissions for Middle of the Linked List.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow