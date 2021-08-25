import collections

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        n, m = len(mat), len(mat[0])
        ret = [[-1 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    ret[i][j] = 0

        while q:
            cur = q.popleft()
            r, c, v = cur[0], cur[1], cur[2]
            for i, j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= i < n and 0 <= j < m and ret[i][j] == -1:
                    ret[i][j] = v + 1
                    q.append((i, j, v + 1))

        return ret
