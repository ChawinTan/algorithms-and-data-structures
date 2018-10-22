class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        n = len(S)
        dp = [[0,0] for _ in range(n)]
        dp[0][0] = 0 if S[0] == '0' else 1
        dp[0][1] = 1 - dp[0][0]
        
        for i in range(1, n):
            if S[i] == '0':
                # if current is 0, former should also be zero if we don't flip
                dp[i][0] = dp[i-1][0]
                # if we set 0 to 1, add one more flip to '1' column from previous min flip, which can be 1 or zero
                dp[i][1] = min(dp[i-1]) + 1
            else:
                # if current is 1 and we flip, we must flip to make it zero 
                dp[i][0] = dp[i-1][0] + 1
                # if we chose not to flip, then select the min flips from previous results
                dp[i][1] = min(dp[i-1])
        
        return min(dp[-1])
