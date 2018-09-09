class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [] 
        
        queue, res, final = [root], [], []
        
        while queue:
            temp = []
            while queue:
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            final.append(res)
            res = []
        return final
