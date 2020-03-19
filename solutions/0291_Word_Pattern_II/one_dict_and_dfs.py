# --Link--
# https://www.lintcode.com/problem/word-pattern-ii/description

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        self.dic = {}
        self.ret = False
        self.dfs(pattern, 0, str, 0)
        return self.ret

    def dfs(self, pattern, pi, s, si):
        if self.ret:
            return
        if pi >= len(pattern):
            if self.dic:
                self.ret = True
            return
        p = pattern[pi] # found pattern p in dic
        if p in self.dic and s[si:si+len(self.dic[p])-1] + '*' == self.dic[p]:
            self.dfs(pattern, pi+1, s, si+len(self.dic[p])-1)
            return
        # not found pattern p in dic
        for i in range(si, len(s) - (len(pattern) - pi) + 1):
            a, b = pattern[pi], s[si:i+1] + '*'
            if a not in self.dic and b not in self.dic:
                self.dic[a] = b
                self.dic[b] = a
                self.dfs(pattern, pi+1, s, i+1)
                del self.dic[a]
                del self.dic[b]
