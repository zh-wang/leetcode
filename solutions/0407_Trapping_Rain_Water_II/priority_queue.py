import heapq as hq

class Solution:

    def rainCnt(self, heightMap):
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        # add all bounding items into heap
        q = []
        for i in range(m):
            q += [Node(i, 0, heightMap[i][0])]
            q += [Node(i, n - 1, heightMap[i][n - 1])]
            visited[i][0], visited[i][n - 1] = True, True
        for i in range(n):
            q += [Node(0, i, heightMap[0][i])]
            q += [Node(m - 1, i, heightMap[m - 1][i])]
            visited[0][i], visited[m - 1][i] = True, True
        hq.heapify(q)
        # poll smallest height item from heap
        ret = 0
        while q:
            cur = hq.heappop(q)
            for dir in dirs:
                r, c = cur.r + dir[0], cur.c + dir[1]
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    ret += max(0, cur.v - heightMap[r][c])
                    hq.heappush(q, Node(r, c, max(cur.v, heightMap[r][c])))
                    visited[r][c] = True
        return ret

class Node(object):

    def __init__(self, r, c, v):
        self.r = r
        self.c = c
        self.v = v

    def __repr__(self):
        return f'Node: {self.r, self.c ,self.v}'

    def __lt__(self, other):
        return self.v < other.v

input = [
        [3, 3, 3, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 2, 2, 3],
        [3, 3, 3, 3, 3],
        ]
x = Solution().rainCnt(input)
print(x)
