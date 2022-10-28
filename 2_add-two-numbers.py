"""
https://leetcode.com/problems/add-two-numbers/

Oops, did the problem again. But in py3 noww

Stats: 
    Runtime: 128 ms, faster than 25.04% of Python3 online submissions for Add Two Numbers.
    Memory Usage: 13.9 MB, less than 43.81% of Python3 online submissions for Add Two Numbers.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        ans_head = ans
        carry = 0
        
        while l1 or l2 or carry:         
            # reset vars
            total = carry
            carry = 0
            
            if l1:
                total += l1.val
                l1 = l1.next
                
            if l2:
                total += l2.val
                l2 = l2.next
            
            if total > 9:
                carry = 1
                total -= 10
            
            # create a new node
            ans.next = ListNode(total)
            ans = ans.next
            
            
        return ans_head.next