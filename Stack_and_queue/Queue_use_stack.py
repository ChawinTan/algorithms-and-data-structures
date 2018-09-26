class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)
     
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.s1 != []:
            self.s2.append(self.s1.pop())
        poppy = self.s2.pop()
        while self.s2 != []:
            self.s1.append(self.s2.pop())
        return poppy
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.s1[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
       
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        return False
        
