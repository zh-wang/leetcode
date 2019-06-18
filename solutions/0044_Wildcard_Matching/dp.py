class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [ [False] * (len(p) + 1) for _ in range(len(s) + 1) ]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    # '*' used (0 times) OR (used once) OR (used 2 or more times)
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-2][j]
                if p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[len(s)][len(p)]
