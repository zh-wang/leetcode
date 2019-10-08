class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_size = k
        self.nums = []
        for i in range(min(k, len(nums))):
            self.nums += [nums[i]]
        if k <= len(nums):
            self.build_heap()
            for i in range(k, len(nums)):
                self.add(nums[i])

    def add(self, val: int) -> int:
        if (self.heap_size > len(self.nums)):
            self.nums += [val]
            self.build_heap()
            return self.nums[0]
        if self.nums[0] < val:
            self.nums[0] = val
            self.min_heapify(0)
            return self.nums[0]
        else:
            return self.nums[0]

    def min_heapify(self, i):
        l, r = 2*i, 2*i + 1
        largest = l if l < self.heap_size and self.nums[l] < self.nums[i] else i
        largest = r if r < self.heap_size and self.nums[r] < self.nums[largest] else largest
        if largest != i:
            self.nums[i], self.nums[largest] = self.nums[largest], self.nums[i]
            self.min_heapify(largest)

    def build_heap(self):
        for i in range(len(self.nums)//2, -1, -1):
            self.min_heapify(i)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
