#brute forece recursion
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        end_row, end_column, path_sum = len(grid[0])-1, len(grid)-1, []
        
        def dfs(row_index, column_index, temp):
            temp += grid[column_index][row_index]

            if row_index == end_row and column_index == end_column:
                if not path_sum:
                    path_sum.append(temp)
                else:
                    if path_sum[0] > temp:
                        path_sum[0] = temp
                return
            elif row_index == end_row and column_index != end_column:
                dfs(row_index, column_index+1, temp)
            elif row_index != end_row and column_index == end_column:
                dfs(row_index+1, column_index, temp)
            else:
                dfs(row_index, column_index+1, temp)
                dfs(row_index+1, column_index, temp)
        dfs(0, 0, 0)
        return path_sum[0]

#dynamic programming
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, column = len(grid[0]), len(grid)
        
        for i in range(1, row):                   #record the consecutive sum of the first element of row 1
            grid[i][0] = grid[i-1][0] + grid[i][0]
        print(grid)
       
        for j in range(1, column):                #record the consecutive sum of the element of column 1
            grid[0][j] = grid[0][j-1] + grid[0][j]
        print(grid)
        for i in range(1, row):
            for j in range(1, column):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        print(grid)
        #memoize the consecutive mimimum sums of each the previous top and left elemements at each point 
        return grid[-1][-1]

'''

'''
