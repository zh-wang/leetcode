class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True
        dp = [True] * (n + 1) # win or lose when k stones left
        for i in range(4, n + 1):
            dp[i] = False if dp[i-1] and dp[i-2] and dp[i-3] else True
        return dp[n]
