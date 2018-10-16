class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack, counter = [], 0
        for i in S:
            if i == "(":
                stack.append(i)
            elif i == ")" and len(stack) > 0:
                stack.pop()
            elif i == ")" and len(stack) == 0:
                counter += 1
            
        return len(stack) + counter
