// ⭐️
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        m, n = len(s), len(wordDict)
        wl = [len(wordDict[i]) for i in range(n)]
        dp = [False for _ in range(m+1)]
        dp[0] = True # an empty str can be matched
        for i in range(1, m+1):
            for j in range(n):
                if i >= wl[j] and dp[i-wl[j]] and s[i-wl[j]:i] == wordDict[j]:
                    dp[i] = True
        if not dp[-1]:
            return []
        self.ret = []
        self.dfs(s, 0, dp, wordDict, '')
        return self.ret

    # s => str, k => index working on
    def dfs(self, s, k, dp, d, ans):
        if k > len(s) or not dp[k]:
            return
        if k == len(s):
            self.ret += [ans[1:]]
            return
        for i in range(k+1, len(s)+1):
            if s[k:i] in d:
                self.dfs(s, i, dp, d, ans+' '+s[k:i])
