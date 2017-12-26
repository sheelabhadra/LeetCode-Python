#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

#You should preserve the original relative order of the nodes in each of the two partitions.

#For example,
#Given 1->4->3->2->5->2 and x = 3,
#return 1->2->2->4->3->5.

###### SOLUTION ######

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Maintain 2 queues; queue1 stores nodes with values < x and queue2 stores nodes with values >= x
        dummy1, dummy2 = ListNode(0), ListNode(0) # heads of the 2 queues
        curr1, curr2 = dummy1, dummy2 # current tails of the 2 queues
        
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = head
            else:
                curr2.next = head
                curr2 = head
            head = head.next
        
        # Join the 2 queues
        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next

