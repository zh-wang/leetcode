class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1): # t is '', so s can always form t by NOT choosing any character
            dp[i][0] = 1 # there is only 1 way(NOT choosing any) to form t
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i < j: # s is shorter, so no substring can be formed
                    dp[i][j] = 0
                    break
                else:
                    if s[i-1] == t[j-1]:
                        # We can choose s[i-1](*), or not choose s[i-1](**)
                        # *.  last matching result is dp[i-1][j-1]
                        # **. last matching result is dp[i-1][j]
                        # Keep the sum of both
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    else:
                        # We can only not choose s[i-1]
                        # This means last matching result(i-1 <=> j) will be used
                        dp[i][j] = dp[i-1][j]
        for k in dp:
            print(k)
        return dp[n][m]

Solution().numDistinct('rabbbit','rabbit')
