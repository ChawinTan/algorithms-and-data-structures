#forward solution
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        col, row = len(obstacleGrid[0]), len(obstacleGrid)
        
        if (len(obstacleGrid[0]) == 1 and obstacleGrid[0][0] == 1) or obstacleGrid[-1][-1] == 1:
            return 0
        
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = "x"
        
        for i in range(col):
            if obstacleGrid[0][i] == "x":
                break
            else:
                obstacleGrid[0][i] = 1
        
        for i in range(row):
            if obstacleGrid[i][0] == "x":
                break
            else:
                obstacleGrid[i][0] = 1
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == "x":
                    continue
                elif obstacleGrid[i][j-1] == "x" and obstacleGrid[i-1][j] != "x":
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                elif obstacleGrid[i-1][j] == "x" and obstacleGrid[i][j-1] != "x":
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif obstacleGrid[i-1][j] != "x" and obstacleGrid[i][j-1] != "x":
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
 
        return obstacleGrid[-1][-1]

#backwards solution
'''
This solution is more effecient since we know straight away which route
is not possible as we traverse backwards
'''

def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        # initialize memo array
        rows,cols = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0] * cols for i in range(rows)]
                
        # go through each row, m-1 --> 0
        for r in range(rows-1, -1, -1):
            # go through each col, n-1 --> 0
            for c in range(cols-1, -1, -1):
                # if it's not an obstacle
                if obstacleGrid[r][c] == 0:
                    # base case -> at the end
                    if r == rows-1 and c == cols-1:
                        memo[r][c] = 1
                    # can go down
                    if r+1 < rows:
                        memo[r][c] += memo[r+1][c]
                    # can go right
                    if c+1 < cols:
                        memo[r][c] += memo[r][c+1]
                   
        # solve original problem --> starting point = (0,0)
        return memo[0][0]
