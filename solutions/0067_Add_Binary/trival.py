class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0 and len(b) == 0:
            return 0
        ret = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            x = a[i] if i >= 0 else 0
            y = b[j] if j >= 0 else 0
            t = carry + int(x) + int(y)
            carry = 1 if t >= 2 else 0
            ret.append(str(t % 2))
            i, j = i-1, j-1
        if carry > 0:
            ret.append(str(carry))
        return ''.join(reversed(ret))
