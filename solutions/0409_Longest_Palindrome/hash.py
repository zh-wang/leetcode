from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        cnts = defaultdict(int)
        for c in s:
            cnts[c] += 1
        ret, has_odd = 0, False
        for c in cnts.values():
            if c % 2 == 0:
                ret += c
            else:
                has_odd = True
                ret += (c - 1)
        return ret + (1 if has_odd else 0)
