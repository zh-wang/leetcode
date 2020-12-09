class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjs = collections.defaultdict(list)
        for i, e in enumerate(equations):
            adjs[e[0]] += [(e[1], values[i])]
            adjs[e[1]] += [(e[0], 1 / values[i])]
        ret = []
        for query in queries:
            if query[0] not in adjs:
                ret += [-1.0]
            else:
                self.dfs_ans = None
                self.dfs(adjs, set(), query[0], query[1], 1.0)
                ret += [self.dfs_ans if self.dfs_ans else -1.0]
        return ret

    def dfs(self, adjs, visited, s, t, v):
        if self.dfs_ans:
            return
        if s == t:
            self.dfs_ans = v
            return
        visited.add(s)
        for p in adjs[s]:
            if p[0] not in visited:
                self.dfs(adjs, visited, p[0], t, v * p[1])


