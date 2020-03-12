# --Link--
# https://www.lintcode.com/problem/walls-and-gates/description

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        import queue
        INF = (1 << 31) - 1
        ds = [ [1, 0], [0, -1], [-1, 0], [0, 1] ]
        q = queue.Queue()
        r, c = len(rooms), len(rooms[0])
        zeros = [(i, j, 0) for i in range(r) for j in range(c) if rooms[i][j] == 0]
        for v in zeros:
            q.put(v)
        while q.qsize() > 0:
            cur = q.get()
            for d in ds:
                ni, nj = cur[0] + d[0], cur[1] + d[1]
                if 0 <= ni < r and 0 <= nj < c and rooms[ni][nj] == INF:
                    rooms[ni][nj] = cur[2] + 1
                    q.put((ni, nj, cur[2] + 1))
        return
