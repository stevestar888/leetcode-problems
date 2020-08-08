"""
https://leetcode.com/problems/palindrome-linked-list/

Pretty fun problem (conceptually), but implementing it with the reversing is really tough,
esp. if you need to restore the nodes at the end. 

Strat:
    Brute force strategy is to convert into an arr, and then iterate through the array. 
    To get O(1) / constant space though, you need to reverse half of the Linked List, 
    and then compare the unreversed half to the reversed half. More details below!
    
Stats: O(n) / linear time, O(1) / constant space is most optimal

As always, Stefan killed it here: https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space

PhDs and not PhDs bickering about read-only, constant space, etc.: https://leetcode.com/problems/palindrome-linked-list/discuss/64493/Reversing-a-list-is-not-considered-%22O(1)-space%22
"""
class Solution(object):
    """
    Brute force, O(n) / linear time, O(n) / linear space
    
    Runtime: 76 ms, faster than 67.40% of Python online submissions for Palindrome Linked List.
    Memory Usage: 31.7 MB, less than 90.69% of Python online submissions for Palindrome Linked List.
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        elems = []
        while head:
            elems.append(head.val)
            head = head.next
        
        #see our elems makes a palindrome
        start = 0
        end = len(elems) - 1
        while start < end:
            if elems[start] != elems[end]:
                return False
            start += 1
            end -= 1
        return True
        
        #alternatively, see if elems == elems reversed:
        #elems == elems[::-1]
    
    
    """
    Now the real O(1) space way: reversing the second half of the linked list
    Code based on Solution, actually implementation is insanely tricky
    """
    def isPalindrome(self, head):
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.find_mid_node(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    
    def find_mid_node(self, head):
        """
        Uses the "tortoise and hare", where we have a fast and a slow pointer,
        to find the node that's at the beginning of the second half.
        """
        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    
    def reverse_list(self, head):
        """
        Given the start of a linked list (head), reverse all nodes starting
        from the head until end of linked list.
        """
        prev = None
        curr = head

        while curr:
            _nxt = curr.next
            curr.next = prev
            prev = curr
            curr = _nxt

        return prev
