class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) == 0:
            return 0
        if k > len(s):
            return 0
        if k <= 1:
            return len(s)

        self.best = 0

        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1

        self.recur(s, k)
        return self.best

    def recur(self, s, k):
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1

        if all([v >= k for v in freq.values()]):
            self.best = max(self.best, len(s))
            return

        start = 0
        for i, c in enumerate(s):
            if freq[c] < k:
                self.recur(s[start : i], k)
                start = i + 1
        self.recur(s[start:], k)
