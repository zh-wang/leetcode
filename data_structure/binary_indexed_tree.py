class BIT:
    def __init__(self, k): # init with size k
        self.maxIndex = k
        self._nums = [0] * self.maxIndex
        # index from 1, NOT 0
        self.tree = [0] * (self.maxIndex + 1)

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
        # return self.read(j) - (0 if not i else self.read(i - 1))
        return self.read(j) - self.read(i)

bit = BIT(8)
# for i in range(8):
    # bit.update(i, 1)
bit.update(7, 1)

print('read 0 : ', bit.read(0))
print('read 1 : ', bit.read(1))
print('read 4 : ', bit.read(4))
print('read 7 : ', bit.read(7))
print('query 0 ~ 4 : ', bit.query_range(0, 4))
print('query 1 ~ 4 : ', bit.query_range(1, 4))
print('query 2 ~ 4 : ', bit.query_range(2, 4))
print('query 0 ~ 2 : ', bit.query_range(0, 2))
bit.update(3, 1) # add 1 in range [3, 4]
bit.update(5, -1)
print('query 0 ~ 2 : ', bit.query_range(0, 2))
print('query 0 ~ 3 : ', bit.query_range(0, 3))
print('query 0 ~ 4 : ', bit.query_range(0, 4))
print('query 0 ~ 5 : ', bit.query_range(0, 5))

# ======= Number of swaps in Bubble Sort =========
# arr = [3, 5, 1, 2, 4, 7, 8, 6]
# t = BIT(9)
# # swap need for arr[i] = i - #(arr[j] < arr[i], which j < i)
# #                               ^ We use BIT to count this
# number_of_swaps = 0
# for i, v in enumerate(arr):
    # number_of_swaps += (i - t.read(v)) # t.read(v) => #(encounter of value < v)
    # t.update(v, 1) # add encounter of v
    # print(number_of_swaps)
