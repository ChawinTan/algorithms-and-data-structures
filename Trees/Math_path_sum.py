''' binary tree max path sum '''

#We can chose 3 paths, node, left or right with node, or left and right with node

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -sys.maxsize
        if root == None:
            return 0
        self.helper(root)
        return self.res
        
    def helper(self, node):
        if not node:
            return 0

        #traverse all the way to the end
        left = self.helper(node.left)
        right = self.helper(node.right)

        #sum of current node and left and right
        sum_left_right = left + right + node.val
        
        #determine left path or right path is larger
        max_left_or_right = node.val + max(left, right, 0)

        #finally, deteremine which of the 3 path is larger        
        self.res = max(sum_left_right, max_left_or_right, self.res)

        #return max of left or right to determine the value of right and left
        return max_left_or_right
