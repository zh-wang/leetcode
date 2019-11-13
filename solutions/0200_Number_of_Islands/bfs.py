import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = 0 if not grid[0] else len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.bfs(grid, visited, i, j, m, n)
                    ret += 1
        return ret

    def bfs(self, grid, visited, oi, oj, m, n):
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = collections.deque()
        q.append((oi, oj))
        while q:
            i, j = q.pop()
            visited[i][j] = True
            for k in range(4):
                ni, nj = i + d[k][0], j + d[k][1]
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] == '1':
                    q.append((ni, nj))

