class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        
        if head and (head.next == None or head.next.next == None):
            return head
        
        counter, odd, even = 1, head, head.next
        head, even_head, odd_head = head.next.next, even, odd
        
        while head:
            if counter%2 > 0:
                odd.next = head
                odd = odd.next
            if counter%2 == 0:
                even.next = head
                even = even.next
            head = head.next
            counter += 1
            
        even.next = None
        odd.next = even_head
        return odd_head
