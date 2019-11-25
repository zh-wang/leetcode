class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for k in range(len(s)-1, 0, -1):
            # [a:b:step] b is always exclusive
            # subsring 0 to k
            #            substring 0 to k, reversed
            if s[:k+1] == s[k::-1]:
                # substring k(exclusive) to end, reversed
                return s[:k:-1] + s
        return s[:0:-1] + s
