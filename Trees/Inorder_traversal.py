''' recursive '''
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res

''' iterative '''
def inorderTraversal(root):
    s, res = []
    cur = root

    while cur:
        if cur:
            s.append(cur)
            cur = cur.left
        else:
            temp = s.pop()   #pop when left side or every time child is None
            res.append(root.val)
            cur = cur.right
    return res
