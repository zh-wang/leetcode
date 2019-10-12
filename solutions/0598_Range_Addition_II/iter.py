class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        r, l = 1<<32, 1<<32
        if len(ops) == 0:
            return m * n
        for op in ops:
            r = min(r, op[0])
            l = min(l, op[1])
        return r * l
