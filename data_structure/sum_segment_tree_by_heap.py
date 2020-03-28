from math import log2, ceil

class SumSegmentTree:
    def __init__(self, nums):
        self._nums = nums
        self.height = ceil(log2(len(nums))) + 1
        self.n = len(nums)
        self.max_size = 2**self.height - 1
        # `nodes` stores (min value, index of the min value in `nums`)
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

    def update(self, k, val):
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

    def query_range(self, ql, qr):
        return self._query_range(ql, qr, 0, self.n - 1, 0)

    def _query_range(self, ql, qr, l, r, i):
        # print(ql, qr, l, r, i)
        if ql <= l and qr >= r:
            # print('found ', self.nodes[i])
            return self.nodes[i]
        if ql > r or qr < l:
            return 0
        mid = (l + r) // 2
        return self._query_range(ql, qr, l, mid, i * 2 + 1) + self._query_range(ql, qr, mid+1, r, i * 2 + 2)

st = SumSegmentTree([1,2,3,4,3,2,1])
print(st.nodes)
st.update(0, 3)
st.update(1, 3)
print(st.query_range(0, 5))
