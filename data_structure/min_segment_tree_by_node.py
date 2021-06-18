class Node(object):

    INIT_VAL = 1<<30

    def __init__(self, start, end):
        self.range_left, self.range_right = start, end
        self._left = self._right = None
        self.val = Node.INIT_VAL

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

    def debug(self):
        print(self.range_left, self.range_right)

class MinSegTree(object):

    def __init__(self, start, end):
        self.root = Node(start, end)

    def merge(self, v1, v2):
        return min(v1, v2)

    def insert(self, node, key, val):
        if node.range_left == node.range_right:
            node.val = self.merge(val, node.val)
            return
        if key <= node.range_mid:
            self.insert(node.left, key, val)
        else:
            self.insert(node.right, key, val)
        node.val = self.merge(node.left.val, node.right.val)

    def query(self, node, key):
        if node.range_right < key:
            return node.val
        elif node.range_left > key:
            return node.val
        else:
            return self.merge(self.query(node.left, key), self.query(node.right, key))

    def query(self, node, ql, qr):
        if qr >= node.range_right and ql <= node.range_left:
            return node.val
        elif ql > node.range_right or qr < node.range_left:
            return Node.INIT_VAL
        return self.merge(self.query(node.left, ql, qr), self.query(node.right, ql, qr))


nums = [5, 8, 2, 8, 3, 1, 2, 9, 7]
mst = MinSegTree(1, 9)
for i in range(len(nums)):
    mst.insert(mst.root, i, nums[i])
print(mst.query(mst.root, 2, 4))
print(mst.query(mst.root, 1, 6))
print(mst.query(mst.root, 6, 9))
print(mst.query(mst.root, 5, 9))
print(mst.query(mst.root, 10, 11))
