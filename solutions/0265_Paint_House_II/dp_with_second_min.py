# --Link--
# https://www.lintcode.com/problem/paint-house-ii/description

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        if not costs:
            return 0
        dp = costs[0][:]
        k = len(dp)
        if k == 1: # only has 1 color
            return dp[0]
        for i in range(1, len(costs)):
            cost = costs[i]
            # find min value and second min value, in dp array
            min_val, sec_min_val = 1 << 30, 1 << 30
            min_val_index = -1
            for j in range(k):
                if dp[j] < min_val:
                    sec_min_val = min_val
                    min_val = dp[j]
                    min_val_index = j
                elif dp[j] < sec_min_val:
                    sec_min_val = dp[j]
            print(min_val, sec_min_val)
            dp = [cost[j] + (sec_min_val if j == min_val_index else min_val) for j in range(k)]
        return min(dp)
