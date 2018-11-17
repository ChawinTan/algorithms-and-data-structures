''' binary tree pruning '''
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0: 
            return None
        #just need to check if bottom is zero.
        #once we set it to none, same logic applies as we traverse upwards
        #if there is a one, entire subtree would be kept
        return root
