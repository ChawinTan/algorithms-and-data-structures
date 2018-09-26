class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        
        poppy = self.q1.pop(0)
        
        while self.q2:
            self.q1.append(self.q2.pop(0))
            
        return poppy
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[len(self.q1)-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return True if len(self.q1) == 0 else False
