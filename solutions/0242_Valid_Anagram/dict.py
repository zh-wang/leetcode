from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        checker = defaultdict(int)
        for i in range(len(s)):
            checker[s[i]] += 1
            checker[t[i]] -= 1
        for v in checker.values():
            if v != 0:
                return False
        return True
