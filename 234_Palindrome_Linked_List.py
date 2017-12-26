#Given a singly linked list, determine if it is a palindrome.

#Follow up:
#Could you do it in O(n) time and O(1) space?

#### SOLUTION ####

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head, l):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy # pre is a marker for the node before reversing

        for _ in range(l):
            pre = pre.next

        prev = None
        curr = pre.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        pre.next = prev

        head = dummy.next

        slow, fast = head, head
        for _ in range(l):
            fast = fast.next
        while fast:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # O(n) time and O(1) solution 
        # find length of the list
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
            
        # Reverse from middle and compare the 2 parts
        # even
        if length%2 == 0:
            return self.reverse(head, length/2)
        
        # odd 
        else:
            return self.reverse(head, (length+1)/2)
