class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = [[] for _ in range(numCourses)]
        for e in prerequisites:
            edges[e[0]] += [e[1]]
        state = [0 for _ in range(numCourses)]
        order = []
        solvable = True
        for i in range(numCourses):
            solvable &= self.dfs(edges, state, i, order)
        return order if solvable else []

    def dfs(self, edges, state, i, order):
        print(i)
        if state[i] == 1:
            return False
        if state[i] > 1:
            return True
        ret = True
        state[i] = 1
        for v in edges[i]:
            ret &= self.dfs(edges, state, v, order)
        state[i] = 2
        order += [i]
        return ret
