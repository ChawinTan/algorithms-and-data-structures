# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        
        for i in range(n):
            fast = fast.next  ''' set this to nth node '''
        
        if not fast:
            return head.next ''' if reached the end, it means removing the first node '''
        
        while fast.next:     ''' iterate to the end of the list, with slow at the nth node from the end '''
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
