class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1 << 31] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            best = 1 << 31
            for c in coins:
                if i >= c:
                    best = min(best, dp[i - c] + 1)
            dp[i] = best
        return -1 if dp[amount] == 1 << 31 else dp[amount]
