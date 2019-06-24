class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        ret = []
        m, n = len(matrix), len(matrix[0])
        visited = [[c==0 or c==n+1 or r==0 or r==m+1 for c in range(n+2)] \
                   for r in range(m+2)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        i, j = 1, 1
        d = 0
        while visited[i][j] == 0:
            visited[i][j] = 1
            ret.append(matrix[i-1][j-1])
            next_i = i + dr[d]
            next_j = j + dc[d]
            if visited[next_i][next_j]:
                d = (d + 1) % 4
                next_i = i + dr[d]
                next_j = j + dc[d]
            i, j = next_i, next_j
        return ret
