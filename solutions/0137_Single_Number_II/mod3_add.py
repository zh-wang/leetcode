class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b0, b1 = 0, 0
        for k in nums:
            b0 = (b0 ^ k) & ~b1
            b1 = (b1 ^ k) & ~b0
        return b0
