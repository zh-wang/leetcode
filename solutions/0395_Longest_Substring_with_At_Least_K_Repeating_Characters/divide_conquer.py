class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) == 0:
            return 0
        if k > len(s):
            return 0
        if k <= 1:
            return len(s)

        return self.recur(s, k)

    def recur(self, s, k):
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1

        if all([v >= k for v in freq.values()]):
            return len(s)

        start = 0
        best = 0
        for i, c in enumerate(s):
            if freq[c] < k:
                best = max(best, self.recur(s[start : i], k))
                start = i + 1
        best = max(best, self.recur(s[start:], k))
        return best
