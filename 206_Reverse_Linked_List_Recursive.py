"""PROBLEM:
Reverse a singly linked list.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        def helper(curr, prev):
            if not curr:
                return prev
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            return helper(curr, prev)
        
        return helper(head, None)
        
