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
            # find min value for next dp[i], base on each value except dp[i]
            min_val = min(dp)
            min_index_arr = [i for i in range(k) if dp[i] == min_val]
            if len(min_index_arr) == 1: # min_val appear only once, we need to find a second min value
                j = min_index_arr[0]
                second_min_val = min(dp[:j] + dp[j+1:])
                dp = [cost[p] + (second_min_val if p == j else min_val) for p in range(k)]
            else: # min_val appears more than 2 times
                dp = [cost[p] + min_val for p in range(k)]
        return min(dp)
