# STAR

class Solution:
    def minCut(self, s: str) -> int:

        def both_size_of_palindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                yield i, j
                i, j = i - 1, j + 1
            yield i + 1, j - 1

        n = len(s)
        is_palindrome = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            # expand from char at i
            for l, r in both_size_of_palindrome(i, i):
                is_palindrome[l][r] = True
            # expand from char at i and i + 1
            if i == n - 1:
                break
            for l, r in both_size_of_palindrome(i, i + 1):
                is_palindrome[l][r] = True

        dp = [n for _ in range(n)]
        dp[0] = 0
        for i in range(1, n):
            if is_palindrome[0][i]:
                dp[i] = 0
                continue
            for j in range(i):
                if dp[j] < n and is_palindrome[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]
