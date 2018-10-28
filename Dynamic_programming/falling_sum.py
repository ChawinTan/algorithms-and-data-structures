class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[0][i] = A[0][i]
            
        for x in range(1, n):
            for y in range(n):
                if y == 0:
                    dp[x][y] = min(dp[x-1][y] + A[x][y], dp[x-1][1] + A[x][y])
                if y > 0 and y < n-1:
                    dp[x][y] = min(dp[x-1][y] +A[x][y], dp[x-1][y-1] +A[x][y], dp[x-1][y+1] + A[x][y])
                if y == n-1:
                    dp[x][y] = min(dp[x-1][y] +A[x][y] ,dp[x-1][y-1] +A[x][y])
        
        return min(dp[len(A)-1])
