class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue, res, counter = [root], [], 1
        
        while queue: 
            temp, path = [], []
            while queue:
                node = queue.pop(0)
                path.append(node.val)
                if node.left: 
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if counter%2 == 0:
                res.append(path[::-1])
            else:
                res.append(path)
            queue = temp
            counter += 1
        return res
