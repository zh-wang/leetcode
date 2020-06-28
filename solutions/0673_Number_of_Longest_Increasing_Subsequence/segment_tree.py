# count of LCS between range start and end
# we can only think about values between min[nums] and max[nums]
class Node(object):
    def __init__(self, start, end):
        self.range_left, self.range_right = start, end
        self._left = self._right = None
        self.val = 0, 1 #length, count
    @property
    def range_mid(self):
        return (self.range_left + self.range_right) // 2
    @property
    def left(self):
        self._left = self._left or Node(self.range_left, self.range_mid)
        return self._left
    @property
    def right(self):
        self._right = self._right or Node(self.range_mid + 1, self.range_right)
        return self._right

# If count of LCS in left and right are the same, take their sum
# Otherwise, take the larger one
def merge(v1, v2):
    if v1[0] == v2[0]:
        if v1[0] == 0: return (0, 1)
        return v1[0], v1[1] + v2[1]
    return max(v1, v2)

# key: num
# val: count of LCS between start(min[nums]) and key
def insert(node, key, val):
    if node.range_left == node.range_right:
        node.val = merge(val, node.val)
        return
    if key <= node.range_mid:
        insert(node.left, key, val)
    else:
        insert(node.right, key, val)
    node.val = merge(node.left.val, node.right.val)

# key: num
# return: count of LCS between start(min[nums]) and key
def query(node, key):
    if node.range_right <= key:
        return node.val
    elif node.range_left > key:
        return 0, 1
    else:
        return merge(query(node.left, key), query(node.right, key))

class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums: return 0
        root = Node(min(nums), max(nums)) # init tree
        for num in nums:
            # for each num, get length and count of LCS
            # between range min(nums) and num-1 as (L, K)
            # then length and count of LCS between range min(nums) and num
            # will be (L+1, K)
            length, count = query(root, num-1)
            # insert (L+1, K) into the segment tree
            insert(root, num, (length+1, count))
        return root.val[1]
