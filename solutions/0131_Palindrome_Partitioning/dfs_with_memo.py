class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 0:
            return [[]]
        self.ret = []
        memo = [[False for _ in range(n)] for _ in range(n)]
        self.dfs(s, memo, 0, [])
        return self.ret

    def dfs(self, s, memo, i, par):
        if i >= len(s):
            self.ret += [par[:]]
            return
        for j in range(len(s)-1, i-1, -1):
            l, r = i, j
            ok = True
            while l <= r:
                if memo[l][r]:
                    break
                if s[l] != s[r]:
                    ok = False
                    break
                l, r = l+1, r-1
            if ok:
                memo[i][j] = True
                self.dfs(s, memo, j+1, par+[s[i:j+1]])
