class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjs = collections.defaultdict(list)
        for i, e in enumerate(equations):
            adjs[e[0]] += [(e[1], values[i])]
            adjs[e[1]] += [(e[0], 1 / values[i])]
        return [self.bfs(adjs, query[0], query[1]) for query in queries]
            
    def bfs(self, adjs, s, t) -> float:
        q = collections.deque()
        visited = set()
        if s in adjs:
            q += [(s, 1)]
            visited.add(s)
        while q:
            cur = q.popleft()
            if cur[0] == t:
                return cur[1]
            for p in adjs[cur[0]]:
                if not p[0] in visited:
                    visited.add(p[0])
                    q += [(p[0], cur[1] * p[1])]
        return -1.0

