class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best, cur = 0, 0
        for v in nums:
            if v == 0:
                best, cur = max(best, cur), 0
            else:
                cur += 1
        best = max(best, cur)
        return best
