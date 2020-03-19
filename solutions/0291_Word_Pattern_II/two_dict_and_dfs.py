class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        self.p1 = {}
        self.p2 = {}
        self.ret = False
        self.dfs(pattern, 0, str, 0)
        return self.ret

    def dfs(self, pattern, pi, s, si):
        if self.ret:
            return
        if pi >= len(pattern):
            if self.p1:
                self.ret = True
            return
        p = pattern[pi] # found pattern p in p1
        if p in self.p1 and s[si:si+len(self.p1[p])] == self.p1[p]:
            self.dfs(pattern, pi+1, s, si+len(self.p1[p]))
            return
        # not found pattern p in p1
        for i in range(si, len(s) - (len(pattern) - pi) + 1):
            a, b = pattern[pi], s[si:i+1]
            if a not in self.p1 and b not in self.p2:
                self.p1[a] = b
                self.p2[b] = a
                self.dfs(pattern, pi+1, s, i+1)
                del self.p1[a]
                del self.p2[b]
