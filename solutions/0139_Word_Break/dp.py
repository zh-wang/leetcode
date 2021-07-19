class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m, n = len(s), len(wordDict)
        wl = [len(wordDict[i]) for i in range(n)]
        dp = [False for _ in range(m+1)] # str[:i] can be composed by wordDict
        dp[0] = True # an empty str can be matched
        for i in range(1, m+1): # str[:i]
            for j in range(n): # check each word in wordDict
                if i >= wl[j] and dp[i-wl[j]] and s[i-wl[j]:i] == wordDict[j]:
                    dp[i] = True
        return dp[m]
