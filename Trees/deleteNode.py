class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self.dfs(root, key)
    
    def dfs(self, node, key):
        if not node:
            return
        if node.val < key:
            node.right = self.dfs(node.right, key)
        elif node.val > key:
            node.left = self.dfs(node.left, key)
        else: 
            if node.left == None:
                return node.right
            else:
                temp = node.left
                while temp.right:
                    temp = temp.right
                node.val = temp.val
                
                node.left = self.dfs(node.left, temp.val)
                
        return node
