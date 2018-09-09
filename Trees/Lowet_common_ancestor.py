class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root or not p or not q:
            return None
        
        if root.val < p.val and root.val < q.val:              #if root is too small, go to bigger node
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:            #if root is too big, go to smaller node
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root 
