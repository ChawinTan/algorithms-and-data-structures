class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, res = [root], collections.deque()
        
        while stack:
            node = stack.pop()
            res.appendleft(node.val)
            
            for child in node.children:
                stack.append(child)
        return list(res)

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        def dfs(node):
            if  not node:
                return
            for child in node.children:
                dfs(child)
            
            res.append(node.val)
            
        dfs(root)
        return res
