class Solution:
    def numTrees(self, n: int) -> int:
        ret = 0
        dp = [0 for _ in range(n-1)]
        for i in range(n):
            ret += self.recur(dp, 0, i-1) * self.recur(dp, i+1, n-1)
        return ret

    def recur(self, dp, i, j):
        if i > j:
            return 1
        if dp[j-i] > 0:
            return dp[j-i]
        if i == j:
            dp[j-i] = 1
        elif i+1 == j:
            dp[j-i] = 2
        else:
            for k in range(i, j+1):
                dp[j-i] += self.recur(dp, i, k-1) * self.recur(dp, k+1, j)
        return dp[j-i]
