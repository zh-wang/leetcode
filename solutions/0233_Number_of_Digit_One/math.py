class Solution:
    def countDigitOne(self, n: int) -> int:
        # e.g. 123 => 0-99 contains 20. 100-123 contains 24. remove 100, remain 23. [44]
        #       23 => two 0-9 and 10-19 contains 10.  remove 20, remain 3. [2 + 10]
        #        3 => contains 1
        k = n
        digitLen = 0
        while k > 0:
            digitLen += 1
            k //= 10
        self.dp = {}
        ret = 0
        for i in range(digitLen - 1, -1, -1):
            scale = 10 ** i # 100
            num = n // scale # number on the third digit
            ret += self.count(i) * num # how many 0-99
            if num > 1: # how many 1's appears above 100. If n >= 200, then we have 100-199 contains 100
                ret += scale
            elif num == 1: # Otherwise, 123 can be treated 100-123, contains 24
                ret += (n - scale + 1)
            n -= scale * num
        return ret

    # each 0-9 contains only 1
    # each 0-99 contains 0-9 on the lowest digit ten times.
    #           and 1 on the second digit ten times (10-19). So 1 * 10 + 10 = 20
    # each 0-999 contains 0-99, ten times.
    #           and 1 on the third digit ten times (100-199). So 20 * 10 + 100 = 300
    def count(self, digitLen):
        if digitLen == 0:
            return 0
        if digitLen == 1:
            return 1
        if digitLen in self.dp:
            return self.dp[digitLen]
        ret = self.count(digitLen - 1) * 10 + 10 ** (digitLen - 1)
        self.dp[digitLen] = ret
        return ret
