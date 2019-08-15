class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O':
                    self.bfs(board, visited, i, j, m, n)

    def bfs(self, board, visited, i, j, m, n):
        q = [(i, j)]
        di, dj = [1, 0, -1, 0], [0, -1, 0, 1]
        qi = 0
        visited[i][j] = True
        flip = True
        while qi < len(q):
            ci, cj = q[qi]
            for k in range(4):
                ni, nj = ci + di[k], cj + dj[k]
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    flip = False
                elif not visited[ni][nj] and board[ni][nj] == 'O':
                    visited[ni][nj] = True
                    q.append((ni, nj))
            qi += 1
        if flip:
            for i, j in q:
                board[i][j] = 'X'
