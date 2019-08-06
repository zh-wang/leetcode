class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0
        dp = [0 for _ in range(m+1)]
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(m, 0, -1): # j goes from the end
                if i < j:
                    dp[j] = 0
                else:
                    if s[i-1] == t[j-1]:
                        dp[j] = dp[j-1] + dp[j]
        return dp[m]
