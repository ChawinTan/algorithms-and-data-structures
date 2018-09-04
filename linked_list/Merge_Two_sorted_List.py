class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:  #returns the one that is not null when one of the head is null
            print("here null")
            return l1 or l2
        if l1.val < l2.val:
            print("here1 " + str(l))
            l1.next = self.mergeTwoLists(l1.next, l2) #sets the next value to the smaller of the two nodes
            return l1
        else:
            print("here2")
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

'''
First recursion sets the root node, the smallest of the node

Subsequently, we recurively build the merged list through by setting the next valu to the smaller of the nodes
'''
