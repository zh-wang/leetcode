class Solution:
    def integerReplacement(self, n: int) -> int:
        q = collections.deque()
        q += [(n, 0)]
        cnt = 0
        while q:
            x = q.popleft()
            if x[0] == 1:
                return x[1]
            if x[0] % 2 == 0:
                q += [(x[0] // 2, x[1] + 1)]
            else:
                q += [(x[0] - 1, x[1] + 1), (x[0] + 1, x[1] + 1)]
            cnt += 1
        return -1
