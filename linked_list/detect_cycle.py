#iteratively
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        store = [head]
        
        if not head:
            return False
        
        while head:
            if not head.next:
                return False
            if head.next in store:
                return True
            else:
                store.append(head.next)
            head = head.next

#2 pointers
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
