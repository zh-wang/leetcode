class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        checker = {}
        for c1, c2 in zip(s, t):
            if c1 in checker and checker[c1] != c2:
                return False
            if c1 not in checker and c2 in checker.values():
                return False
            checker[c1] = c2
        return True
