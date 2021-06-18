class BIT:
    def __init__(self, nums):
        self.maxIndex = len(nums)
        self._nums = [0] * self.maxIndex
        self.tree = [0] * (self.maxIndex + 1) # index from 1, NOT 0
        for i in range(len(nums)):
            self.update(i, nums[i])
            print(self.tree)
        print(self.tree)

    def update(self, k, val):
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

bit = BIT([1,2,3,4,5,6,7])
print(bit.read(0))
print(bit.read(4))
