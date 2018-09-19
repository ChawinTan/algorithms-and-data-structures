class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            
            res.append(node.val)
            
        dfs(root)
        return res

''' iterative '''
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res, cur = [], [], root
        
        while cur or stack!= []:
            if cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.right    #x.right == None, next iteration, goes to pop
            else:
                cur = stack.pop()  #x.left is still none, pop the one before x
                cur = cur.left
        return list(reversed(res))
