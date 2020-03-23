class NumArray:

    def __init__(self, nums: List[int]):
        self.addup = []
        if not nums:
            return
        for v in nums:
            self.addup += [(0 if len(self.addup) == 0 else self.addup[-1]) + v]

    def sumRange(self, i: int, j: int) -> int:
        if i > j:
            return -1 << 32
        return self.addup[j] - (self.addup[i - 1] if i >= 1 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
