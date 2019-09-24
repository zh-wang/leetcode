# ⭐️
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        n = len(prices)
        # dp[k, i] = max(dp[k, i-1], { prices[i] - prices[j] + dp[k-1, j-1], j=[0..i-1] })
        dp = [[0 for _ in range(n)] for _ in range(3)]
        for k in range(1, 3):
            min_k_i = prices[0]
            for i in range(1, n):
                # === min_price calc can be reduced ===
                # === min_price only need to be update once when i increasing ===
                # min_price = prices[0]
                # for j in range(1, i+1):
                #     min_price = min(min_price, prices[j] - dp[k-1][j-1])
                # dp[k][i] = max(dp[k][i-1], prices[i] - min_price)
                min_k_i = min(min_k_i, prices[i] - dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i] - min_k_i)
        return dp[2][n-1]
