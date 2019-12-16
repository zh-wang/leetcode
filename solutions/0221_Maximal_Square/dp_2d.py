class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        best = 0

        # first row
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            best = max(best, dp[0][j])
        # first column
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            best = max(best, dp[i][0])
        # dp from [1,m] & [1,n]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = 0 if matrix[i][j] == '0' else min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                best = max(best, dp[i][j])
        return best*best
