class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 1 and num1[0] == '0':
            return '0'
        if len(num2) == 1 and num2[0] == '0':
            return '0'
        la = list(reversed(num1))
        lb = list(reversed(num2))
        ret = []
        for i in range(len(lb)):
            ret = self.list_add(ret, self.list_mul_val(la, lb[i], i))
        return ''.join(map(str, list(reversed(ret))))

    def list_mul_val(self, la, val, start_zeros):
        carry = 0
        ret = [0] * start_zeros
        for i in range(len(la)):
            m = (ord(la[i]) - 48) * (ord(val) - 48) + carry
            ret.append(m % 10)
            carry = m // 10
        if carry > 0:
            ret.append(carry)
        return ret

    def list_add(self, la, lb): # both la and lb are int array
        i = 0
        carry = 0
        ret = []
        while i < len(la) or i < len(lb):
            va = 0 if i >= len(la) else la[i]
            vb = 0 if i >= len(lb) else lb[i]
            s = va + vb + carry
            ret.append(s % 10)
            carry = s // 10
            i += 1
        if carry > 0:
            ret.append(carry)
        return ret
