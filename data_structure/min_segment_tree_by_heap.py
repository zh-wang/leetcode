from math import log2, ceil

class MinSegTree:

    NO_VALUE = 1<<31

    def __init__(self, nums):
        self.height = ceil(log2(len(nums))) + 1
        self.n = len(nums)
        self.max_size = 2**self.height - 1
        # `nodes` stores (min value, index of the min value in `nums`)
        self.nodes = [(MinSegTree.NO_VALUE, -1) for _ in range(self.max_size)]
        self.build(nums, 0, len(nums) - 1, 0)

    def build(self, nums, l, r, i):
        # params => array, left bound, right bound, index of current node
        # print(l, r, i)
        if l == r: # If there is only one element
            self.nodes[i] = (nums[l], l)
            return self.nodes[i]
        mid = (l + r) // 2
        self.nodes[i] = min(self.build(nums, l, mid, i * 2 + 1), self.build(nums, mid+1, r, i * 2 + 2))
        return self.nodes[i]

    def query_min(self, ql, qr):
        return self._min(ql, qr, 0, self.n - 1, 0)

    def _min(self, ql, qr, l, r, i):
        # print(l, r, i)
        if ql <= l and qr >= r:
            return self.nodes[i]
        if ql > r or qr < l:
            return (MinSegTree.NO_VALUE, -1)
        mid = (l + r) // 2
        return min(self._min(ql, qr, l, mid, i*2+1), self._min(ql, qr, mid+1, r, i*2+2))

st = MinSegTree([1,2,3,4,3,2,1])
print(st.nodes)
print(st.query_min(0, 6))
