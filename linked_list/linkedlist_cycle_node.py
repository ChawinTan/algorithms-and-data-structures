# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        store = {}
        
        while head:
            if head not in store:
                store[head] = True
            elif store[head] == True:
                return head
            head = head.next
        return None

''' no extra space '''
try:
    #need to shift fast one step ahead else fast is always == slow
    fast = head.next
    slow = head
    while fast is not slow:
        fast = fast.next.next
                slow = slow.next
except:
    # if there is an exception, we reach the end and there is no cycle
    return None

    # since fast starts at head.next, we need to move slow one step forward
    slow = slow.next
    while head is not slow:
        head = head.next
        slow = slow.next

    return head
