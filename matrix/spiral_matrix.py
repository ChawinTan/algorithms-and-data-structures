class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        ans=[]
        while matrix:
            ans+=matrix.pop(0)          # pop the first row
            matrix[:]=zip(*matrix)[::-1]# transpose and inverse the matrix to make the next side at the top
            # print(matrix)
        return ans
