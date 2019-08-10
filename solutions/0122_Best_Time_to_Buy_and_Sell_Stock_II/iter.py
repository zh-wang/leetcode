class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        ret = 0
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            ret += diff if diff > 0 else 0
        return ret
