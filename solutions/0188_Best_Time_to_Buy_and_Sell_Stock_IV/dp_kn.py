# ⭐️
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if (len(prices) <= 1):
            return 0

        n = len(prices)
        if k > n // 2:
            return self.unlimitedK(prices)

        min_k = [prices[0] for _ in range(k+1)]
        dp = [0 for _ in range(k+1)]
        for i in range(1, n):
            for j in range(1, k+1):
                min_k[j] = min(min_k[j], prices[i] - dp[j-1])
                dp[j] = max(dp[j], prices[i] - min_k[j])
        return dp[k]


    def unlimitedK(self, prices):
        ret = 0
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            ret += diff if diff > 0 else 0
        return ret
