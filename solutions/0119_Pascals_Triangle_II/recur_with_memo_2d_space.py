class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        self.combi = [[0 for _ in range(34)] for _ in range(34)]
        return [self.combination(rowIndex, i) for i in range(rowIndex+1)]

    def combination(self, n, k):
        if self.combi[n][k]:
            return self.combi[n][k]
        if n == k or k == 0:
            self.combi[n][k] = 1
            return self.combi[n][k]
        self.combi[n][k] = self.combination(n-1, k-1) + self.combination(n-1, k)
        return self.combi[n][k]
