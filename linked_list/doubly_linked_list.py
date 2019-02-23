''' Doubly linked list '''
class Node(self, Next=None, Prev=None, data=None):
    self.Next = Next
    self.Prev = Prev
    self.data = data

'''
Inserting:
1. At the front
2. After the node
3. End of the list
4. Before the node
'''
class DoublyLinkedList():
    def frontOfList(self, new_data):
        node = Node(data = new_data)

        node.next = self.head
        node.prev = None

        if self.head is not None:
            self.head.prev = node

        self.head = node

    def afterTheNode(self, prev_node, new_data):
        node = Node(data = new_data)

        node.next = prev_node.next

        prev_node.next = node
        node.prev = prev_node

        ''' check if newnode.next is not none '''
        ''' if true, then assign the prev of new-next-node to newnode '''
        if node.next is not None:
            node.next.prev = node

    def endOfList(self, new_data):
        node = Node(data = new_data)

        node.next = None

        ''' make node the head if head is none '''
        if self.head is None:
            node.prev = None
            self.head = node
            return node

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = node
        node.prev = last

    def beforeNode(self, next_node, new_data):
        node = Node(data = new_data)

        node.next = next_node
        node.prev = next_node.prev
        next_node.prev = node

        if node.prev is not None:
            node.prev.next = node
            
        
