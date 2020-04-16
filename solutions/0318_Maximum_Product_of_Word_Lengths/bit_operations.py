from functools import reduce

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask = [reduce(lambda x, y: x | (1 << (ord(y) - ord('a'))), w, 0) \
                   for w in words]
        n = len(words)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bitmask[i] & bitmask[j] == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret<Paste>
