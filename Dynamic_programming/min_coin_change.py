''' minimum coin change '''
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')]*amount
        
        for coin in coins:           
            for curr_change in range(coin, amount+1):   #curr_change is any amount between curr_coin and amount
                dp[curr_change] = min(dp[curr_change], dp[curr_change-coin]+1) #+1 because we deduct away the current coin
                
        return dp[-1] if dp[-1] != float("inf") else -1
