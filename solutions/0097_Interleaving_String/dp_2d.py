from collections import defaultdict
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        char_met = defaultdict(int)
        for c in s1:
            char_met[c] += 1
        for c in s2:
            char_met[c] += 1
        for c in s3:
            char_met[c] -= 1
        for v in char_met.values():
            if v:
                return False

        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        m, n = len(s1)+1, len(s2)+1
        # dp[i][j] => sub problem of matching s1[:i] and s2[:j]
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True

        for i in range(1, m): # s2 is empty, only match s1 and s3
            dp[i][0] = s1[:i-1] == s3[:i-1]
        for j in range(1, n): # s1 is empty, only match s2 and s3
            dp[0][j] = s2[:j-1] == s3[:j-1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] and s3[i+j-1] == s1[i-1] or \
                        dp[i][j-1] and s3[i+j-1] == s2[j-1]
        return dp[m-1][n-1]
