class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.maxIndex = len(nums)
        self._nums = [0] * self.maxIndex
        self.tree = [0] * (self.maxIndex + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, k: int, val: int) -> None:
        diff = val - self._nums[k]
        index = k + 1
        while index <= self.maxIndex:
            self.tree[index] += diff
            index += (index & -index)
        self._nums[k] = val

    def read(self, k):
        index = k + 1
        ret = 0
        while index > 0:
            ret += self.tree[index]
            index -= (index & -index)
        return ret

    def sumRange(self, i: int, j: int) -> int:
        return self.read(j) - (self.read(i - 1) if i > 0 else 0)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
