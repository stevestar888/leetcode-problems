"""
https://leetcode.com/problems/merge-two-sorted-lists/

Both Iterative and Recursive Solutions are possible, though the recursive one is really elegant.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    """
    Iterative Solution
    
    Runtime: 
        Runtime: 20 ms, faster than 95.09% of Python online submissions for Merge Two Sorted Lists.
        Memory Usage: 12.7 MB, less than 5.75% of Python online submissions for Merge Two Sorted Lists.
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(None)
        pointer = new_head 
        
        while True:
            #check empty node cases
            if l1 == None and l2 == None:
                break
            elif l1 == None:
                pointer.next = l2 #rest of the linked list is l2 (because l1 is empty)
                break
            elif l2 == None: 
                pointer.next = l1 #rest of the linked list is l1 (because l2 is empty)
                break
                
            #both nodes have values - choose the smaller node and attach it
            else:
                if l1.val < l2.val:
                    pointer.next = l1
                    l1 = l1.next #advance l1
                else:
                    pointer.next = l2
                    l2 = l2.next #advance l2
                
                #we've advanced l1 or l2, now advance the pointer
                pointer = pointer.next
        
        #out of the loop -- return beginning of linked list
        return new_head.next
    
    
    """
    Recursive Solution
    
    Runtime: 
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #base cases
        if l1 == None: #since l1 is empty, the rest of the linked list is l2
            return l2  #note: it's ok if l2 is also empty
        if l2 == None: 
            return l1  #same logic as ^
        
        #choose the smaller node, return *that*.next
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2