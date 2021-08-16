from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        pool = defaultdict(int)
        for c in t:
            pool[c] += 1
        for c in s:
            pool[c] -= 1
            if not pool[c]:
                del pool[c]
        return pool.popitem()[0]
