import heapq as hq
from collections import defaultdict

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        # dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        m, n = len(grid), len(grid[0])
        b, p, t = None, None, None
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'B':
                    b = (r, c)
                    grid[r][c] = '.'
                if grid[r][c] == 'S':
                    p = (r, c)
                    grid[r][c] = '.'
                if grid[r][c] == 'T':
                    t = (r, c)
                    grid[r][c] = '.'

        def h(a, b):
            # manhattan distance of a & b
            return sum(abs(x - y) for x, y in zip(a, b))

        def adjs(p, box_pos=[]):
            x, y = p
            for r, c in [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]:
                if 0 <= r < m and 0 <= c < n and grid[r][c] == '.' \
                and (r, c) not in box_pos:
                    yield r, c

        def pushable(p):
            x, y = p
            blocks = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
            for i in range(len(blocks)):
                r, c = blocks[i][0], blocks[i][1] # player position
                r2, c2 = blocks[(i + 2) % 4][0], blocks[(i + 2) % 4][1] # box position after pushing
                if 0 <= r < m and 0 <= r2 < m \
                    and 0 <= c < n and 0 <= c2 < n \
                    and grid[r][c] == '.' and grid[r2][c2] == '.':
                    yield (r, c), (r2, c2)

        def reachable(pos, target, box_pos=[]):
            # Can character move from pos to target?
            costs = defaultdict(lambda: m * n) # postion => cost, maximum is m*n
            costs[pos] = 0
            q = [(h(pos, target), pos)]
            while q:
                _, cur_pos = hq.heappop(q)
                if cur_pos == target:
                    return True
                else:
                    for next_pos in adjs(cur_pos, box_pos=box_pos):
                        next_cost = costs[cur_pos] + 1
                        if next_cost < costs[next_pos]:
                            costs[next_pos] = next_cost
                            hq.heappush(q, (next_cost + h(next_pos, target), next_pos))
            return False

        costs = defaultdict(lambda: m * n) # (box_pos, next_box_pos) => cost(number of pushes)
        q = [(h(b, t), 0, b, p)] # heuristic, cost(step), box position, player position
        while q:
            _, cost, box_pos, player_pos = hq.heappop(q)
            if t == box_pos:
                return cost
            else:
                for next_player_pos, next_box_pos in pushable(box_pos):
                    if reachable(player_pos, next_player_pos, box_pos=[box_pos]):
                        next_cost = cost + 1
                        if next_cost < costs[box_pos + next_box_pos]:
                            costs[box_pos + next_box_pos] = next_cost
                            hq.heappush(q, (next_cost + h(next_box_pos, t), next_cost, next_box_pos, box_pos))
        return -1
