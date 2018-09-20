''' N-ary tree preorder traversal '''

''' recursive '''
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            for i in node.children:
                dfs(i)
        dfs(root)
        return res
