
class Node:

    def __init__(self, r1, c1, r2, c2, lt = None, lb = None, rt = None, rb = None):
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2
        self.lt = lt
        self.lb = lb
        self.rt = rt
        self.rb = rb
        self.v = (lt.v if lt else 0) \
                + (lb.v if lb else 0) \
                + (rt.v if rt else 0) \
                + (rb.v if rb else 0)

    def contains(self, r, c):
        return self.r1 <= r <= self.r2 and self.c1 <= c <= self.c2

    def __str__(self):
        return f'{self.r1} {self.c1} {self.r2} {self.c2} v {self.v}'

class Solution:

    def rangeSum(self, matrix, operations):
        self._matrix = matrix
        m, n = len(matrix), len(matrix[0])
        root = self.buildTree(0, 0, m - 1, n - 1)
        for op in operations:
            if op[0] == 'query':
                v = self.query(op[1], op[2], op[3], op[4], root)
                print(v)
            if op[0] == 'update':
                r, c = op[1], op[2]
                diff = op[3] - self._matrix[r][c]
                self.update(r, c, diff, root)

    def buildTree(self, r1, c1, r2, c2) -> Node:
        if r1 > r2 or c1 > c2:
            return None
        if r1 == r2 and c1 == c2:
            node = Node(r1, c1, r2, c2)
            node.v = self._matrix[r1][c1]
            return node
        r_mid, c_mid = (r1 + r2) // 2, (c1 + c2) // 2
        return Node(r1, c1, r2, c2, \
                self.buildTree(r1, c1, r_mid, c_mid), \
                self.buildTree(r_mid + 1, c1, r2, c_mid), \
                self.buildTree(r1, c_mid + 1, r_mid, c2), \
                self.buildTree(r_mid + 1, c_mid + 1, r2, c2))

    def query(self, r1, c1, r2, c2, node):
        if r1 > r2 or c1 > c2:
            return 0
        if not node:
            return 0
        if r1 == node.r1 and c1 == node.c1 and r2 == node.r2 and c2 == node.c2:
            return node.v
        r_mid, c_mid = (node.r1 + node.r2) // 2, (node.c1 + node.c2) // 2
        return self.query(r1, c1, r_mid, c_mid, node.lt) \
                + self.query(r_mid + 1, c1, r2, c_mid, node.lb) \
                + self.query(r1, c_mid + 1, r_mid, c2, node.rt) \
                + self.query(r_mid + 1, c_mid + 1, r2, c2, node.rb)

    def update(self, r, c, diff, node):
        if not node:
            return
        if not node.contains(r, c):
            return
        node.v += diff
        r_mid, c_mid = (node.r1 + node.r2) // 2, (node.c1 + node.c2) // 2
        self.update(r, c, diff, node.lt)
        self.update(r, c, diff, node.lb)
        self.update(r, c, diff, node.rt)
        self.update(r, c, diff, node.rb)

    def traverse(self, node):
        if not node:
            return
        print(node)
        self.traverse(node.lt)
        self.traverse(node.lb)
        self.traverse(node.rt)
        self.traverse(node.rb)

inputs = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
        ]
operations = [
        ['query', 2, 1, 4, 3],
        ['query', 0, 0, 4, 4],
        ['update', 0, 0, 100],
        ['query', 0, 0, 4, 4]
        ]
Solution().rangeSum(inputs, operations)
