class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            best = 0
            for j in range(i):
                best = max(best, \
                           dp[j],\
                           (dp[j - 2] if j > 1 else 0) + max(prices[i] - prices[j], 0))
            dp[i] = best
        return max(dp)
