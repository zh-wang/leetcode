# STAR

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) == 0:
            return 0
        if k > len(s):
            return 0
        if k <= 1:
            return len(s)

        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1

        best = 0
        maxUniqCnt = len(freq.keys())
        # for each iteration, we need to find substrings contains #curUniq unique char
        for curUniq in range(1, maxUniqCnt + 1):
            freq.clear()
            # uniq <- number of unique char in the window
            # cntAtLeastK <- number of unique char which appears k times or more in the window
            l, r, uniq, cntAtLeastK = 0, 0, 0, 0
            while r < len(s):
                if uniq <= curUniq: # expand window
                    if freq[s[r]] == 0:
                        uniq += 1
                    freq[s[r]] += 1
                    if freq[s[r]] == k:
                        cntAtLeastK += 1
                    r += 1 # expand window from right
                else: # shrink window
                    if freq[s[l]] == k:
                        cntAtLeastK -= 1
                    freq[s[l]] -= 1
                    if freq[s[l]] == 0:
                        uniq -= 1
                    l += 1 # shirink window from left
                if uniq == curUniq and cntAtLeastK == uniq:
                    best = max(best, r - l)
        return best
