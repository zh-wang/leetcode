class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 0:
            return []
        self.ret = []
        t = 0
        for i in range(len(num) if num[0] != '0' else 1):
            t = t * 10 + int(num[i])
            self.dfs(num, i+1, t, t, str(t), target)
        return self.ret

    def dfs(self, num, i, total, last, s, target):
        if i >= len(num):
            if total == target:
                self.ret += [s]
            return
        t = 0
        for j in range(i, len(num) if num[i] != '0' else i+1):
            t = t * 10 + int(num[j])
            self.dfs(num, j+1, total + t, t, s + '+' + str(t), target)
            self.dfs(num, j+1, total - t, -t, s + '-' + str(t), target)
            self.dfs(num, j+1, total - last + last * t, last * t, s + '*' + str(t), target)
