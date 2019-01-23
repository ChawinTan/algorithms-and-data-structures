class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, j = [], {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in '([{':
                stack.append(i)
            if i in ')]}':
                if not stack or stack.pop() != j[i]:
                    return False
        if not stack:
            return True
        else:
            return False
