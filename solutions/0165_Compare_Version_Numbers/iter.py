class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a1, a2 = version1.split('.'), version2.split('.')
        i = 0
        while i < max(len(a1), len(a2)):
            v1 = int(a1[i]) if i < len(a1) else 0
            v2 = int(a2[i]) if i < len(a2) else 0
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i += 1
        return 0
