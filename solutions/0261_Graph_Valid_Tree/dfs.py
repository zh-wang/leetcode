# --Link--
# https://www.lintcode.com/problem/graph-valid-tree/description

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        adjs = collections.defaultdict(lambda: [])
        for e in edges:
            adjs[e[0]] += [e[1]]
            adjs[e[1]] += [e[0]]
        visited = [False] * n
        isTree = self.check(0, -1, adjs, visited)
        return isTree and all(visited)

    def check(self, node, pnode, adjs, visited):
        if visited[node]:
            return False
        visited[node] = True
        ret = True
        for k in adjs[node]:
            if k != pnode:
                ret &= self.check(k, node, adjs, visited)
        return ret
