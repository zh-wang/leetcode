class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        canBuy, hold, cool = 0, float(-inf), float(-inf)
        for v in prices:
            canBuy, hold, cool = max(canBuy, cool), max(hold, canBuy - v), hold + v
        return max(canBuy, cool)
