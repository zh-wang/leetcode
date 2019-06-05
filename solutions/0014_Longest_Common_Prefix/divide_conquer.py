class Solution(object):
    def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            if len(strs) == 0: return ""
            return self.recur(strs, 0, len(strs) - 1)

    def recur(self, strs, l, r) -> str:
        if l == r: return strs[l]
        m = (l + r) // 2
        print(l, m , r)
        lstr = self.recur(strs, l, m)
        rstr = self.recur(strs, m + 1, r)
        i = 0
        while i < len(lstr) and i < len(rstr) and lstr[i] == rstr[i]:
            i += 1
        return lstr[:i]
