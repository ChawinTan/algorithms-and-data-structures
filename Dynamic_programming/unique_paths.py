#ineffecient dfs solution
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        counter = []
        def dfs(m, n, counter):
            if m == 0 and n == 0:
                counter.append(1)
                return
            elif m == 1 and n == 1:
                dfs(m-1, n-1, counter+1)
            elif m == 1 and n > 1:
                dfs(m, n-1, counter)
            elif n == 1 and m > 1:
                dfs(m-1, n, counter)
            else:
                dfs(m-1, n, counter)
                dfs(m, n-1, counter)
        dfs(m, n, counter)
        return sum(counter)

#dynamic programming approach
'''
Since robot can only arrive at each spot from the top or the left, there are
only 2 possible ways the robt can arrive at each spot.

Hence, the number of ways robot can reach that spot is the addition of number
of ways the robot takes to reach each of its previous 2 spots.
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        board = [[0 for y in range(m)] for x in range(n)]
       
        for i in range(m):
            board[0][i] = 1
            
        for j in range(n):
            board[j][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                board[i][j] = board[i-1][j] + board[i][j-1]
        
        return board[-1][-1]
