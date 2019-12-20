# STAR

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        new_s = s + '#' + rev
        f = self.kmp_lookup_table(new_s)
        print(f)
        # f[len(new_s) - 1] => where new_s's suffix matching s's prefix
        # rev[:len(s) - f[len(new_s) - 1]] => not matching part in rev
        return rev[:len(s) - f[len(new_s) - 1]] + s

    def kmp_lookup_table(self, s):
        t = 0
        f = [0] * len(s)
        for i in range(1, len(s)):
            while t > 0 and s[i] != s[t]:
                t = f[t - 1]
            if s[i] == s[t]:
                t += 1
            f[i] = t
        return f
