class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        digits = []
        isNeg = False
        if num < 0:
            num = -num
            isNeg = True
        while num:
            digits += [num % 16]
            num = num // 16
        if isNeg: # for negative number, convert it to its complement number
            digits = [15 - d for d in digits] # 16's complement
            carry = 1 # plus 1
            i = 0
            while i < len(digits):
                k = digits[i] + carry
                if k == 16:
                    digits[i] = 0
                    i += 1
                else:
                    digits[i] = k
                    break
        chars = [self.octoToHex(d) for d in digits]
        if isNeg:
            return 'f' * (8 - len(chars)) + ''.join(list(reversed(chars)))
        else:
            return ''.join(list(reversed(chars)))

    def octoToHex(self, d):
        return chr(ord('0') + d) if d < 10 else chr(ord('a') + d - 10)
