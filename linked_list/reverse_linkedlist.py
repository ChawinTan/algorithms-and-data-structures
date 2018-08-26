class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp, new_head = None, None
        
        while head:
            temp, head, temp.next, new_head = head, head.next, new_head, temp
        return new_head
    '''
    temp = head
    head = head.next
    temp.next = new_head
    new_head = temp
    '''
