class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, temp = -1 << 31, 0
        for v in nums:
            temp += v
            best = max(best, temp)
            if temp < 0:
                temp = 0
        return best
