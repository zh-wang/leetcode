class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip().replace(' ', '')
        if len(s) == 0:
            return 0
        scanned = []
        v = 0
        for c in s:
            if '0' <= c <= '9':
                v = v * 10 + int(c)
            else:
                scanned += [v]
                scanned += [c]
                v = 0
        scanned += [v]

        if len(scanned) == 0:
            return 0

        stack = [scanned[0]]
        for i in range(1, len(scanned), 2):
            if scanned[i] == '*':
                stack += [stack.pop() * scanned[i+1]]
            elif scanned[i] == '/':
                stack += [int(float(stack.pop()) // scanned[i+1])]
            else:
                stack += [scanned[i]]
                stack += [scanned[i+1]]

        if stack:
            ret = stack[0]
            for i in range(1, len(stack), 2):
                if stack[i] == '+':
                    ret += stack[i+1]
                else:
                    ret -= stack[i+1]
        return ret
