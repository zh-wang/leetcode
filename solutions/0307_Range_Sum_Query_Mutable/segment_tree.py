class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self._nums = nums
        self.height = ceil(log2(len(nums))) + 1
        self.n = len(nums)
        self.max_size = 2**self.height - 1
        self.nodes = [-1 for _ in range(self.max_size)]
        self.build(nums, 0, len(nums) - 1, 0)

    def build(self, nums, l, r, i):
        # params => array, left bound, right bound, index of current node
        # print(l, r, i)
        if l == r: # If there is only one element
            self.nodes[i] = self._nums[l]
            return self.nodes[i]
        mid = (l + r) // 2
        self.nodes[i] = self.build(nums, l, mid, i * 2 + 1) + self.build(nums, mid+1, r, i * 2 + 2)
        return self.nodes[i]

    def update(self, k: int, val: int) -> None:
        l, r = 0, self.n - 1
        i = 0
        diff = val - self._nums[k]
        while l < r:
            self.nodes[i] += diff
            mid = (l + r) // 2
            if k <= mid:
                i = i * 2 + 1
                r = mid
            else:
                i = i * 2 + 2
                l = mid + 1
        self.nodes[i] += diff
        self._nums[k] = val

    def sumRange(self, i: int, j: int) -> int:
        return self._sumRange(i, j, 0, self.n - 1, 0)

    def _sumRange(self, ql, qr, l, r, i):
        if ql <= l and qr >= r:
            return self.nodes[i]
        if ql > r or qr < l:
            return 0
        mid = (l + r) // 2
        return self._sumRange(ql, qr, l, mid, i * 2 + 1) + self._sumRange(ql, qr, mid+1, r, i * 2 + 2)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
