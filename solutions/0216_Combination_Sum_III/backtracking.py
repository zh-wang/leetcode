class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ret = []
        self.dfs(k, n, 1, [])
        return self.ret

    def dfs(self, k, n, start, l):
        if k == 0:
            if n == 0:
                self.ret += [l]
            return
        for v in range(start, 10):
            if n >= v:
                self.dfs(k - 1, n - v, v + 1, l + [v])
