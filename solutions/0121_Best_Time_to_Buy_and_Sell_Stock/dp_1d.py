class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        l = [0] * n # min value from 0...k, 0<=k<n
        l[0] = prices[0]
        ret = 0
        for i in range(1, n):
            l[i] = min(l[i-1], prices[i])
            ret = max(ret, prices[i] - l[i])
        return ret
