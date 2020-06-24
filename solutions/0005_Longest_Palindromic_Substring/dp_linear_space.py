class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        dp00 = [True] * len(s) # length 0 strings are always True
        dp01 = [True] * len(s) # lenght 1 strings are always True
        dp02 = [False] * len(s) # working on this dp array
        dp = [dp00, dp01, dp02]
        best_len = 1 # best length of palidromic substring we found
        ret = s[0]

        p = 2
        for k in range(1, len(s)): # span from 1 to len(s) - 1
            old_p = (p + 1) % 3
            for i in range(len(s) - k): # start index i
                dp[p][i] = s[i] == s[i + k] and dp[old_p][i + 1]
                if dp[p][i] and k + 1 > best_len:
                    best_len = k + 1
                    ret = s[i : i + k + 1]
            p = (p + 1) % 3
        return ret
