class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans.append(tmpNode.val)
                if len(ans) > 1 and ans[len(ans)-1] <= ans[len(ans)-2]:
                    return False
                root = tmpNode.right

        return True
