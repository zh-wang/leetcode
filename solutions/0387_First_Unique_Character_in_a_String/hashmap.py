class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for i, c in enumerate(s):
            if c in counter:
                counter[c] = 1 << 31
            else:
                counter[c] = i
        ret = min(counter.values())
        return -1 if ret == 1 << 31 else ret
