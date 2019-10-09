class Heap:

    def __init__(self, nums):
        self.heap_size = len(nums)

    def max_heapify(self, nums, i):
        l, r = 2*i, 2*i + 1
        largest = l if l < self.heap_size and nums[l] > nums[i] else i
        largest = r if r < self.heap_size and nums[r] > nums[largest] else largest
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.max_heapify(nums, largest)

    def build_max_heap(self, nums):
        for i in range(len(nums)//2, -1, -1):
            self.max_heapify(nums, i)

    def heap_sort(self, nums):
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heap_size -= 1
            self.max_heapify(nums, 0)

x = [4,6,8,1,2,3,5,9,7]
heap = Heap(x)
heap.build_max_heap(x)
print(x)
heap.heap_sort(x)
print(x)
