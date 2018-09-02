class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        def dfs(node):
            temp = None
            temp, node.right, node.left = node.right, node.left, node.right
            
            if not node.left and not node.right:
                return
            elif not node.right:
                dfs(node.left)
            elif not node.left:
                dfs(node.right)
            else:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return root
