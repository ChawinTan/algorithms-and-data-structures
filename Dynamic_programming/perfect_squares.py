''' dynamic programming, 1d array with static variable '''
class Solution:
    _memo = [0,1,2,3]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4: return self._memo[n]
        # we already know the solution upto k
        # from previous test cases
        k = len(self._memo)                  # k is existing len
        for i in range(k,n+1):               # i is current sum
            j, minval = 1, float('inf')      # j is square tracker
            while i-(j*j) >= 0:
                minval = min(minval, self._memo[i-(j*j)]+1)    #look back to the difference between sum and latest n*j-square and add 1 more of the current j-square value, eg: 7 = lookback(7-4)=3 + 1 more 4, 12 equals lookback(12-4)=2 + 1 more 4
                j+=1
            self._memo.extend([minval])
        return self._memo[n]
  
 ''' dynamic programming 2d array '''
            
        board = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for curr_sum in range(n+1):
            for number in range(n+1):
                if curr_sum == 0 or number > curr_sum:
                    board[curr_sum][number] = 0
                    
                elif number == 1:
                    board[curr_sum][number] = curr_sum
                    
                elif curr_sum == number and (curr_sum**0.5).is_integer() and (number**0.5).is_integer():
                    board[curr_sum][number] = 1
                    
                elif not (number**0.5).is_integer() and number > 1:
                    board[curr_sum][number] = board[curr_sum][number-1]
                    
                elif (number**0.5).is_integer() and number > 1:
                    board[curr_sum][number] = min(board[number][number] + board[curr_sum - number][curr_sum - number], board[curr_sum][number-1])
                    
        return board[-1][-1]
