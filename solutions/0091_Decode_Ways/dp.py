class Solution:
    def numDecodings(self, s: str) -> int:
        if (len(s) == 0):
            return 1
        n = len(s)
        dp = [0] * (n+1) # index 0 means empty string
        dp[0] = 1
        for i in range(1,n+1):
            dp[i] += dp[i-2] if i>=2 and 1<=int(s[i-2])<=9 and 1<=int(s[i-2:i])<=26 else 0
            dp[i] += dp[i-1] if 1<=int(s[i-1])<=9 else 0
        return dp[n]
