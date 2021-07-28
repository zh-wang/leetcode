class BIT:
    def __init__(self, k): # init with size k
        self.maxIndex = k
        self._nums = [0] * self.maxIndex
        self.tree = [0] * (self.maxIndex + 1) # index from 1, NOT 0

    def update(self, k, val):
        diff = val - self._nums[k]
        index = k + 1
        while index <= self.maxIndex:
            self.tree[index] += diff
            index += (index & -index)
        self._nums[k] = val
        print(self.tree)

    def read(self, k):
        index = k + 1
        ret = 0
        while index > 0:
            ret += self.tree[index]
            index -= (index & -index)
        return ret

    def query_range(self, i, j):
        return self.read(j) - (0 if not i else self.read(i - 1))

# bit = BIT(8)
# for i in range(1, 9):
    # bit.update(i, 1)
# print(bit.read(1))
# print(bit.read(4))
# print(bit.query_range(1, 4))
# print(bit.query_range(2, 4))

# ======= Number of swaps in Bubble Sort =========
arr = [3, 5, 1, 2, 4, 7, 8, 6]
t = BIT(9)
# swap need for arr[i] = i - #(arr[j] < arr[i], which j < i)
#                               ^ We use BIT to count this
number_of_swaps = 0
for i, v in enumerate(arr):
    number_of_swaps += (i - t.read(v)) # t.read(v) => #(encounter of value < v)
    t.update(v, 1) # add encounter of v
    print(number_of_swaps)
