class Solution:
    def calculate(self, s: str) -> int:
        stack, vSum = [], 0
        s = s.replace(' ', '')
        for v in s:
            if v == ')':
                ps = len(stack) - 1
                while stack[ps] != '(':
                    ps -= 1
                temp = self.calc(stack, ps)
                stack = stack[:ps]
                stack += [temp]
            else:
                stack += [v]
        if len(stack) > 0:
            vSum += self.calc(stack, 0)
        return vSum

    def calc(self, stack, ps):
        if stack[ps] == '(':
            ps += 1 # index ps+1 is '('
        vSum, vCur, isAdd = 0, 0, True
        if stack[ps] == '-':
            isAdd = False
            ps += 1
        while ps < len(stack):
            if stack[ps] == '-':
                vSum += vCur if isAdd else -vCur
                isAdd, vCur = False, 0
            elif stack[ps] == '+':
                vSum += vCur if isAdd else -vCur
                isAdd, vCur = True, 0
            else:
                vCur = (vCur) * 10 + int(stack[ps])
            ps += 1
        vSum += vCur if isAdd else -vCur
        return vSum
