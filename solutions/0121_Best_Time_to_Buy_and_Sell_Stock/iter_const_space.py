class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        l, ret = prices[0], 0
        for i in range(1, n):
            l = min(l, prices[i])
            ret = max(ret, prices[i] - l)
        return ret
