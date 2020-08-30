"""
https://leetcode.com/problems/add-two-numbers/

A few tricky cases:

[5]
[5]

[0]
[0]

"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        BASE = 10
        
        carry = 0
        head = ListNode(0)
        curr = head
        
        while l1 or l2 or carry:
            l1_num, l2_num = 0, 0
            if l1:
                l1_num = l1.val
                l1 = l1.next
            if l2:
                l2_num = l2.val
                l2 = l2.next
                
            digit = carry + l1_num + l2_num
            
            #if we had a 1 carry into this digit
            if carry == 1:
                carry -= 1
            
            #if we need to carry into the next digit
            if digit >= 10:
                digit %= BASE
                carry += 1
            
            # print(digit, carry)
            digit_node = ListNode(digit)
            curr.next = digit_node
            curr = curr.next
            
            
        return head.next
