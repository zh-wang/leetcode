class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) <= 2:
            return False
        self.ret = False
        self.dfs(num, [], 0)
        return self.ret

    def dfs(self, num, arr, k):
        if self.ret or k == len(num):
            if len(arr) >= 3 and arr[-3] + arr[-2] == arr[-1]:
                self.ret = True
            return
        if num[k] == '0':
            self.dfs(num, arr + [0], k + 1)
            return
        for p in range(k + 1, len(num) + 1):
            if len(arr) < 2 or arr[-2] + arr[-1] == int(num[k:p]):
                self.dfs(num, arr + [int(num[k:p])], p)
