class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        r = len(triangle)
        dp = [0 for _ in range(r)]
        dp[0] = triangle[0][0]
        for i in range(1, r):
            # the order matters
            # do from end to start
            dp[i] = dp[i-1] + triangle[i][i] # the rightmost slot is always added by last row's rightmost
            for j in range(i-1,0,-1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0] # same for the leftmost slot
        return min(dp)
