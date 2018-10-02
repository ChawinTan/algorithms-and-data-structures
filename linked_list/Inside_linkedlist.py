class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        res, sG = 0, set(G)
        while head:
            if head.val in sG and (head.next == None or head.next.val not in sG):
                res += 1          #if reach the end of the list or the next item not in G
            head = head.next
        return res
           
