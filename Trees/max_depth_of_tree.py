class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node.left == None and node.right == None:
                return 1
            return max(dfs(node.left), dfs(node.right)) + 1
        
        return dfs(root)

'''
This is to help aid me in visualizing recursive calls

suppose a tree: 1,2,3,none,none,4,5
dfs(4) = dfs(5) = 1
dfs(3) = max(dfs(4), dfs(5)) +1 = 2
dfs(2) = 1
dfs(1) = max(dfs(2), dfs(3))+1 = 3
'''
