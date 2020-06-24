class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = collections.defaultdict(int)
        i, j = 0, 0
        best = 0
        for j in range(0, len(s)):
            if checker[s[j]] == 0:
                checker[s[j]] = 1
                best = max(best, j - i + 1)
            else:
                while i < j and s[i] != s[j]:
                    checker[s[i]] = 0
                    i += 1
                i += 1
        return best
