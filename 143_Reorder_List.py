#Given a singly linked list L: L0→L1→…→Ln-1→Ln,
#reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

#You must do this in-place without altering the nodes' values.

#For example,
#Given {1,2,3,4}, reorder it to {1,4,2,3}.

#### SOLUTION ####

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        # 3 steps
        # Step 1: Find the middle of the list
        p1, p2 = head, head
    
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        
        # Step 2: Reverse the half after middle
        # 1->2->3->4->5->6 to 1->2->3->6->5->4
        pre = p1
        prev = None
        curr = p1.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        pre.next = prev
        
        # Step 3: Start reorder one by one
        # 1->2->3->6->5->4 to 1->6->2->5->3->4
        p1 = head
        p2 = pre.next
        while p1 != pre:
            pre.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = pre.next
