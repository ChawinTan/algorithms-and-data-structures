''' recursively '''
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.dfs(root, val)
        return root
    
    def dfs(self, root, val):
        if root == None:
            return TreeNode(val)
        if root.val < val: 
            root.right = self.dfs(root.right, val)
        if root.val > val:
            root.left = self.dfs(root.left, val)
        return root

''' iteratively '''
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr = root
        
        while curr:
            if curr != None and curr.left == None and curr.val > val:
                curr.left = TreeNode(val)
                break
            if curr != None and curr.right == None and curr.val < val:
                curr.right = TreeNode(val)
                break
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        return root
