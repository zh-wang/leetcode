import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjs = [[] for _ in range(numCourses)]
        for e in prerequisites:
            adjs[e[0]] += [e[1]]
        # state 0 => not opened.
        # state 1 => opening. A cycle is found when an opening vertex is visisted.
        # state 2 => closed.
        state = [0 for _ in range(numCourses)]
        ret = True
        for v in range(numCourses):
            ret = ret & self.dfs(adjs, state, v)
        return ret

    def dfs(self, adjs, state, index) -> bool:
        if state[index] == 1:
            return False
        if state[index] > 1:
            return True
        state[index] = 1
        ret = True
        for v in adjs[index]:
            ret = ret & self.dfs(adjs, state, v)
        state[index] = 2
        return ret
